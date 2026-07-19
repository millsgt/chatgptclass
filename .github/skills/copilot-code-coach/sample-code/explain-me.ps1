<#
.SYNOPSIS
    Azure resource inventory reporter — teaching-grade PowerShell demo.

.DESCRIPTION
    Pulls a list of Azure resource groups and their resource counts,
    then produces a formatted summary table.

    Intentionally contains several beginner mistakes for use with the
    copilot-code-coach skill (Modes 3 and 5):

        Issue 1  — alias use (gci instead of Get-ChildItem equivalent; here
                   "select" instead of Select-Object)
        Issue 2  — no param block; hard-coded subscription ID
        Issue 3  — Write-Host instead of Write-Output (breaks pipeline)
        Issue 4  — no error handling around Az calls
        Issue 5  — variable named $data (too generic)
        Issue 6  — missing comment-based help on inner function
        Issue 7  — Connect-AzAccount called unconditionally (re-authenticates
                   on every run even if already connected)

    Exercise: Use copilot-code-coach Mode 3 to annotate every issue,
              then Mode 5 to produce a clean version.

.NOTES
    Requires: Az PowerShell module (Install-Module Az -Scope CurrentUser)
    Author  : Tim Warner (teaching artifact — not production code)
#>

# Issue 7: unconditional Connect-AzAccount
Connect-AzAccount | Out-Null

# Issue 2: hardcoded subscription — change this on your machine
$subscriptionId = "00000000-0000-0000-0000-000000000000"
Set-AzContext -SubscriptionId $subscriptionId | Out-Null

function Get-ResourceSummary {
    # Issue 6: no comment-based help

    # Issue 5: generic name
    $data = Get-AzResourceGroup

    $results = @()

    foreach ($rg in $data) {
        # Issue 4: no error handling — if Get-AzResource throws, loop crashes
        $count = (Get-AzResource -ResourceGroupName $rg.ResourceGroupName).Count

        # Issue 1: "select" alias instead of Select-Object
        $results += [PSCustomObject]@{
            ResourceGroup = $rg.ResourceGroupName
            Location      = $rg.Location
            ResourceCount = $count
        } | select ResourceGroup, Location, ResourceCount
    }

    return $results
}

$summary = Get-ResourceSummary

# Issue 3: Write-Host breaks pipeline — output cannot be captured by caller
Write-Host "`n=== Azure Resource Inventory ===" -ForegroundColor Cyan
Write-Host "Subscription: $subscriptionId"
Write-Host "Generated   : $(Get-Date -Format 'yyyy-MM-dd HH:mm')`n"

$summary | Format-Table -AutoSize
