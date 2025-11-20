param(
    [string]$NgrokURL = ""
)

if ($NgrokURL -eq "") {
    Write-Host "ERROR: No ngrok URL provided."
    Write-Host "Run this script like:"
    Write-Host "  .\test_ngrok.ps1 -NgrokURL 'https://xxxx-xxxx.ngrok-free.app'"
    exit
}

$headers = @{ 'ngrok-skip-browser-warning' = 'true' }

Write-Host "Testing ONI backend through ngrok..."
Write-Host "URL: $NgrokURL"
Write-Host ""

# Test 1: /health
Write-Host "TEST 1: /health"
try {
    $health = Invoke-RestMethod "$NgrokURL/health" -Headers $headers
    Write-Host "PASS:" $health
} catch {
    Write-Host "FAIL: /health did not respond."
}

# Test 2: /test/ping
Write-Host ""
Write-Host "TEST 2: /test/ping"
try {
    $ping = Invoke-RestMethod "$NgrokURL/test/ping" -Headers $headers
    Write-Host "PASS:" $ping
} catch {
    Write-Host "FAIL: /test/ping not reachable."
}

# Test 3: /pipeline/run
Write-Host ""
Write-Host "TEST 3: /pipeline/run"
try {
    $body = '{"text":"oni online"}'
    $pipeline = Invoke-RestMethod -Method Post -Uri "$NgrokURL/pipeline/run" -Body $body -ContentType "application/json" -Headers $headers
    Write-Host "PASS:" $pipeline
} catch {
    Write-Host "FAIL: /pipeline/run failed."
}

# Test 4: /openapi.json
Write-Host ""
Write-Host "TEST 4: /openapi.json"
try {
    $openapi = Invoke-RestMethod "$NgrokURL/openapi.json" -Headers $headers
    Write-Host "PASS: OpenAPI received."
} catch {
    Write-Host "FAIL: Could not load /openapi.json"
}

Write-Host ""
Write-Host "DONE."
