---
name: aks-deployment-skill
description: >
  Deploy and operate workloads on Azure Kubernetes Service (AKS) the safe way. Use for
  provisioning an AKS cluster, wiring it to Azure Container Registry, applying Kubernetes
  manifests or Helm charts, configuring ingress and autoscaling, and troubleshooting rollouts.
  USE FOR: "deploy to AKS", "create an AKS cluster", "set up ingress on AKS", "scale my AKS
  workload", "why is my pod CrashLoopBackOff on AKS". DO NOT USE FOR: non-Kubernetes Azure
  compute (App Service, Container Apps, Functions) or generic kubectl questions with no Azure
  context.
---

# AKS Deployment Skill

Provision, deploy, and operate workloads on **Azure Kubernetes Service**. This skill favors
repeatable, idempotent steps over one-off portal clicks, so the same commands run in a demo and
in a pipeline.

## When to use

- Standing up a new AKS cluster for a demo, lab, or non-production workload.
- Pushing an image to **Azure Container Registry (ACR)** and rolling it out to the cluster.
- Adding **ingress**, **horizontal pod autoscaling**, or **cluster autoscaling**.
- Diagnosing a failed rollout (`ImagePullBackOff`, `CrashLoopBackOff`, pending pods).

## Prerequisites

- Azure CLI 2.60+ with the `aks-preview` extension only if a preview feature is needed.
- `kubectl` on PATH (`az aks install-cli` installs a matching version).
- An Azure subscription and a resource group you own.

## Core workflow

1. **Provision the cluster.** Create a resource group, then an AKS cluster with managed identity,
   a system node pool, and monitoring add-on enabled.

   ```bash
   az group create --name rg-aks-lab --location eastus2
   az aks create \
     --resource-group rg-aks-lab \
     --name aks-lab \
     --node-count 2 \
     --enable-managed-identity \
     --enable-addons monitoring \
     --generate-ssh-keys
   ```

2. **Get credentials.** Merge the cluster context into your kubeconfig.

   ```bash
   az aks get-credentials --resource-group rg-aks-lab --name aks-lab
   kubectl get nodes
   ```

3. **Attach ACR (if pulling private images).** Grant the cluster's managed identity pull rights so
   deployments don't carry image-pull secrets.

   ```bash
   az aks update --resource-group rg-aks-lab --name aks-lab --attach-acr <acrName>
   ```

4. **Deploy the workload.** Apply manifests or a Helm chart. Always confirm the rollout before
   moving on.

   ```bash
   kubectl apply -f k8s/
   kubectl rollout status deployment/<name>
   ```

5. **Expose and scale.** Add an ingress controller (NGINX or the AKS-managed application routing
   add-on) for HTTP traffic, then set autoscaling targets.

   ```bash
   kubectl autoscale deployment/<name> --cpu-percent=70 --min=2 --max=10
   ```

## Guardrails

- **Right-size node pools.** Start small (2 nodes) for labs; enable the cluster autoscaler rather
  than over-provisioning.
- **Never hardcode secrets in manifests.** Pull them from Azure Key Vault via the Secrets Store
  CSI driver, or use Kubernetes secrets sourced from environment variables in CI.
- **Clean up.** Non-production clusters cost money while idle. Delete the resource group when the
  lab ends: `az group delete --name rg-aks-lab --yes --no-wait`.

## Troubleshooting quick reference

| Symptom | First check |
|---------|-------------|
| `ImagePullBackOff` | ACR attached? Image tag correct? `kubectl describe pod <name>` |
| `CrashLoopBackOff` | Container logs: `kubectl logs <pod> --previous` |
| Pods stuck `Pending` | Node capacity or resource requests too high; check `kubectl get events` |
| Ingress returns 404 | Ingress controller running? Host and path rules match the request? |
