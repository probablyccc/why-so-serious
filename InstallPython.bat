@echo off
setlocal enabledelayedexpansion
for /f "tokens=2 delims==" %%a in ('wmic os get caption /value 2^>nul') do (
    set "os_name=%%a"
)
for /f "tokens=*" %%i in ("%os_name%") do set "os_name=%%i"

set "arch=%PROCESSOR_ARCHITECTURE%"
echo "!os_name!" | find /i "Windows" >nul
if !errorlevel! equ 0 (
    if "%arch%"=="AMD64" (
        if "%PROCESSOR_ARCHITEW6432%"=="ARM64" (
            set "url=https://www.python.org/ftp/python/3.13.0/python-3.13.0-arm64.exe"
        ) else (
            set "url=https://www.python.org/ftp/python/3.13.0/python-3.13.0-amd64.exe"
        )
    ) else (
        set "url=https://www.python.org/ftp/python/3.13.0/python-3.13.0.exe"
    )
    echo Download URL: !url!
    if defined url (
        set "tmp_exe=%TEMP%\python-installer-%RANDOM%.exe"
        echo Temp EXE path: !tmp_exe!
        powershell -Command "(New-Object Net.WebClient).DownloadFile('!url!', '!tmp_exe!')"
        if exist "!tmp_exe!" (
            start "" "!tmp_exe!"
            echo Python installer has been executed: !tmp_exe!
        ) else (
            echo Failed to download Python installer.
        )
	timeout 5
    ) else (
        echo Failed to set download URL.
    )
) else (
    echo Unsupported operating system: !os_name!
)

endlocal
