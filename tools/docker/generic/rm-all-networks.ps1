$networks = docker network ls -q

if ($networks -ne $null) {
    $networks.Split("\n") | ForEach-Object {
        Write-Host -NoNewline "Removed network: "
        docker network rm $_
    }
} else {
    Write-Host "No docker networks to remove."
}