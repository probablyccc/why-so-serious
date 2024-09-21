#!/bin/bash
ma_os=$(uname)
if [ "$ma_os" = "Darwin" ]; then
    url="https://www.python.org/ftp/python/3.12.5/python-3.12.5-macos11.pkg"
    tmp_pkg=$(mktemp /tmp/python-installer.XXXXXX.pkg)
    curl -o "$tmp_pkg" "$url"
    if [ $? -eq 0 ]; then
        open "$tmp_pkg"
        echo "Python installer has been executed: $tmp_pkg"
    else
        echo "Failed to download Python installer."
    fi
elif [[ "$ma_os" == *"MINGW"* || "$ma_os" == *"CYGWIN"* || "$ma_os" == *"MSYS"* ]]; then
    url="https://www.python.org/ftp/python/3.12.5/python-3.12.5.exe"
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