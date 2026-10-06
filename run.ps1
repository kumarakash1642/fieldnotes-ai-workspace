param([switch]$CheckOnly)

$ErrorActionPreference = 'Stop'
$workspacePath = $PSScriptRoot
$pageUrl = 'http://127.0.0.1:5050/'

function Test-WorkspaceReady {
    try {
        $response = Invoke-RestMethod -Uri ($pageUrl + 'api/bootstrap') -TimeoutSec 2
        return ($null -ne $response.state.answers -and $null -ne $response.questions)
    } catch {
        return $false
    }
}

try {
    $ready = Test-WorkspaceReady
    if ($CheckOnly) {
        if ($ready) { Write-Output 'The SIP workspace is ready.'; exit 0 }
        Write-Output 'The SIP workspace is not running.'
        exit 1
    }

    if (-not $ready) {
        $pythonPath = Join-Path $workspacePath '.venv\Scripts\python.exe'
        if (-not (Test-Path -LiteralPath $pythonPath)) {
            throw 'Run run.bat to set up the Python environment first.'
        }
        $logDirectory = Join-Path $workspacePath 'data'
        New-Item -ItemType Directory -Path $logDirectory -Force | Out-Null
        $logTag = Get-Date -Format 'yyyyMMdd-HHmmss-fff'
        $outputLog = Join-Path $logDirectory ("server-$logTag.log")
        $errorLog = Join-Path $logDirectory ("server-$logTag-error.log")
        Write-Output 'Starting your SIP workspace...'
        $server = Start-Process -FilePath $pythonPath -ArgumentList 'app.py' `
            -WorkingDirectory $workspacePath -WindowStyle Hidden -PassThru `
            -RedirectStandardOutput $outputLog -RedirectStandardError $errorLog

        $deadline = (Get-Date).AddSeconds(30)
        do {
            $ready = Test-WorkspaceReady
            if ($ready) { break }
            if ($server.HasExited) {
                throw "The app could not start. Another program may be using port 5050. Details: $errorLog"
            }
            Start-Sleep -Milliseconds 300
        } while ((Get-Date) -lt $deadline)

        if (-not $ready) {
            throw "The app did not become ready within 30 seconds. Details: $errorLog"
        }
    }

    Start-Process -FilePath $pageUrl
    Write-Output 'Opened your SIP workspace. The app runs in the background until Windows shuts down or its Python process is stopped.'
} catch {
    Write-Host ('Could not open the SIP workspace: ' + $_.Exception.Message) -ForegroundColor Red
    exit 1
}
