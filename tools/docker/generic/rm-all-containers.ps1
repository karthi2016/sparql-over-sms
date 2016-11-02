$containers = docker ps -qa

if ($containers -ne $null) {
    $containers.Split("\n") | ForEach-Object {
        Write-Host -NoNewline "Killed container: "
        docker kill $_
        Write-Host -NoNewline "Removed container: "
        docker rm $_
    }
} else {
    Write-Host "No docker containers to remove."
}