+++
title= "Windows 上切换 Jetbrains IDE 的 terminal 为 PowerShell 或 cmder"
draft = false
date= "2017-03-31 11:02:00"
+++

### 替换为 PowerShell

首先用管理员权限打开 PowerShell ，并运行以下命令：

```
Set-ExecutionPolicy Unrestricted
```

然后记住一定要打开 64 位的 IDE ，如 `phpstorm64.exe`，否则 PowerShell 会报 `Cannot load PSReadLine module. Console is running without PSReadLine.`。

在 `File > Settings > Tools > Terminal` 面板修改 `Shell Path` 为 `powershell.exe` 即可。

### 替换为 cmder

安装完成 cmder 后，需要设置环境变量 `CMDER_ROOT`，变量值为 cmder 安装目录。

然后在 `Terminal` 面板修改 `Shell Path` 为 `"cmd.exe" /k ""%CMDER_ROOT%\vendor\init.bat""`。