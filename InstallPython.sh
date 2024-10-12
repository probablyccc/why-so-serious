ma_os=$(uname)
arch=$(uname -m)
if [ "$ma_os" = "Darwin" ]; then
    url="https://www.python.org/ftp/python/3.13.0/python-3.13.0-macos11.pkg"
    tmp_pkg=$(mktemp /tmp/python-installer.XXXXXX.pkg)
    curl -o "$tmp_pkg" "$url"
    if [ $? -eq 0 ]; then
        open "$tmp_pkg"
        echo "Python installer has been executed: $tmp_pkg"
    else
        echo "Failed to download Python installer."
    fi
elif [[ "$ma_os" == *"MINGW"* || "$ma_os" == *"CYGWIN"* || "$ma_os" == *"MSYS"* ]]; then
    if [ "$arch" = "x86_64" ]; then
        if [[ "$PROCESSOR_ARCHITECTURE" == "ARM64" || "$PROCESSOR_ARCHITEW6432" == "ARM64" ]]; then
            url="https://www.python.org/ftp/python/3.13.0/python-3.13.0-arm64.exe"
        else
            url="https://www.python.org/ftp/python/3.13.0/python-3.13.0-amd64.exe"
        fi
    else
        url="https://www.python.org/ftp/python/3.13.0/python-3.13.0.exe"
    fi
    tmp_exe=$(mktemp /tmp/python-installer.XXXXXX.exe)
    curl -o "$tmp_exe" "$url"
    if [ $? -eq 0 ]; then
        "$tmp_exe"
        echo "Python installer has been executed: $tmp_exe"
    else
        echo "Failed to download Python installer."
    fi
else
    echo "Unsupported operating system."
fi