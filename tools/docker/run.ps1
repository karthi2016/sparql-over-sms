#::::::::::::::::::::::::::#
# SPARQL over SMS - Docker #
#::::::::::::::::::::::::::#

$setup = Get-Content "setup.json" | ConvertFrom-Json | Select templates, instances

foreach ($template In $setup.templates) 
{    
    $templateInstances = $setup.instances | Where-Object { $_.template -eq $template.name }
    $sharedTriplestore = $template.persistence.triplestore.shared
    $sharedTaskQueue = $template.processing.taskqueue.shared
    
    if ($templateInstances.Count -eq 0)
    {
        continue
    }

    # Create network for this template
    $tpNetworkId = docker network create --driver bridge ("sos-{0}-network" -f $template.name)

    Write-Host ("Setting up instance(s) for template '{1}':" -f $templateInstances.Count, $template.name)
    Write-Host ("|")
    if ($sharedTriplestore -eq $true)
    {
        $tsType = $template.persistence.triplestore.type
        $tsHostname = "sos-triplestore"
        $tsContainerId = docker run -P -d --hostname $tsHostname --name $tsHostname --network $tpNetworkId onnovalkering/cliopatria:latest

        Write-Host ("├── Created shared triplestore: `t`t`t`t {0}" -f $tsHostname)
    }
    if ($sharedTaskQueue -eq $true)
    {
        $tqType = $template.processing.taskqueue.type
        $tqHostname = "sos-taskqueue"
        $tqContainerId = docker run -P -d --hostname $tqHostname --name $tqHostname --network $tpNetworkId redis:latest

        Write-Host ("├── Created shared task queue: `t`t`t`t`t {0}" -f $tqHostname)

        $wkHostname = "{0}-worker" -f $tqHostname
        $wkContainerId = docker run -d --hostname $wkHostname --name $wkHostname --network $tpNetworkId sos-service "./run-worker.sh"

        Write-Host ("|   └── Created {0} shared task worker(s): `t`t sos-default-worker[1-n]" -f $template.processing.workers.count)
    }

    Write-Host ("|")
    foreach ($instance In $templateInstances) 
    {
        if ($sharedTriplestore -eq $true -and $sharedTaskQueue -eq $true) 
        {
            $inHostname = "sos-{0}" -f $instance.name
            $inContainerId = docker run -P -d --hostname $inHostname --name $inHostname --network $tpNetworkId sos-service

            Write-Host ("├── Created service: `t`t`t`t`t`t`t {0}" -f $instance.name)
            Write-Host ("|   ├── Linked to shared triplestore: `t`t`t {0}" -f $tsHostname)
            Write-Host ("|   └── Linked to shared task queue: `t`t`t {0}" -f $tqHostname)

        }
        else
        {
            Write-Host ("Dedicated triplestore and/or task queue is not yet supported.")
        }
    }
}

