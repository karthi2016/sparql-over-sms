$containers = docker ps -q

if ($containers -ne $null) {
    $containers.Split("\n") | ForEach-Object {
        Write-Host -NoNewline "Killed container: "
        docker kill $_
    }
} else {
    Write-Host "No docker containers to kill."
}