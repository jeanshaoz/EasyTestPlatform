	# run_ci.ps1 (English Version - No Encoding Issues)
	Write-Host "========== [Stage 1] Environment Check ==========" -ForegroundColor Cyan
	Write-Host "Current Python Version:" -NoNewline
	python --version
	Write-Host "`n========== [Stage 2] Starting Service ==========" -ForegroundColor Cyan
	# Kill existing python processes to clean environment
	Stop-Process -Name python -Force -ErrorAction SilentlyContinue
	# Start app.py in background
	Start-Process python -ArgumentList "app.py" -WindowStyle Hidden
	Write-Host "Service is starting..." -ForegroundColor Yellow
	Start-Sleep -Seconds 3
	Write-Host "`n========== [Stage 3] Running Tests ==========" -ForegroundColor Cyan
	# Run pytest
	pytest test_framework/test_cases/ -v --alluredir=reports
	# Check result
	if ($LASTEXITCODE -eq 0) {
	    Write-Host "`n========== [Stage 4] Pipeline Success ==========" -ForegroundColor Green
	    Write-Host ">>> Tests Passed! Deployment Allowed." -ForegroundColor Green
	} else {
	    Write-Host "`n========== [Stage 4] Pipeline Failed ==========" -ForegroundColor Red
	    Write-Host ">>> Tests Failed! Deployment Blocked." -ForegroundColor Red
	}
	Write-Host "`nCleaning up background service..." -ForegroundColor Gray
	Stop-Process -Name python -Force -ErrorAction SilentlyContinue
	Write-Host "Done."