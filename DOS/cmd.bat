echo 

:: 显示命令

@echo %cd%
:: @ 不显示当前命令
cd /d C:\Users\1744\Desktop     
:: /d 进入不同磁盘必须有，%cd% 显示当前路径
@echo %cd%               

if exist ui.py python ui.py
if not exist ui python ui.py
pause