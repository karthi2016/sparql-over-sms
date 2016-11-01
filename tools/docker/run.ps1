#::::::::::::::::::::::::::#
# SPARQL over SMS - Docker #
#::::::::::::::::::::::::::#

$setup = Get-Content "setup.json" | ConvertFrom-Json | Select templates, instances

foreach ($template In $setup.templates) 
{    
    $templateInstances = $setup.instances | Where-Object { $_.template -eq $template.name }
    $sharedTriplestore = $template.persistence.triplestore.shared
    $sharedTaskQueue = $template.processing.taskqueue.shared
    
    Write-Host ("Setting up instance(s) for template '{1}':" -f $templateInstances.Count, $template.name)
    Write-Host ("|")
    if ($sharedTriplestore -eq $true)
    {
        $tsType = $template.persistence.triplestore.type
        $tsHostname = "sos-" + $template.name + "-" + $template.persistence.triplestore.type
        $tsContainerId = docker run -P -d --hostname $tsHostname --name $tsHostname onnovalkering/cliopatria:latest

        Write-Host ("├── Created shared triplestore: `t`t`t`t {0}" -f $tsHostname)
    }
    if ($sharedTaskQueue -eq $true)
    {
        $tqType = $template.processing.taskqueue.type
        $tqHostname = "sos-" + $template.name + "-" + $tqType
        $tqContainerId = docker run -P -d --hostname $tqHostname --name $tqHostname redis:latest

        Write-Host ("├── Created shared task queue: `t`t`t`t`t {0}" -f $tqHostname)
        Write-Host ("|   └── Created {0} shared task worker(s): `t`t sos-default-worker[1-n]" -f $template.processing.workers.count)
    }

    Write-Host ("|")
    foreach ($instance In $templateInstances) 
    {
        Write-Host ("├── Created service: `t`t`t`t`t`t`t {0}" -f $instance.name)
        Write-Host ("|   ├── Linked to shared triplestore: `t`t`t {0}" -f $tsHostname)
        Write-Host ("|   └── Linked to shared task queue: `t`t`t {0}" -f $tqHostname)
        # docker run -P -d --link sos-rabbitmq:sos-rabbitmq sos-service
    }
}

