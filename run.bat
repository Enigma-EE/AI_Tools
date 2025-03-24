@echo off


:: 检查是否在项目根目录
if not exist "app.py" (
    echo [X] 错误：请在项目根目录（包含app.py的文件夹）运行此脚本
    pause
    exit /b
)

:: 检查并激活虚拟环境
if exist "venv\Scripts\activate.bat" (
    echo [✓] 检测到虚拟环境
    call "venv\Scripts\activate.bat"
    if %errorlevel% neq 0 (
        echo [X] 激活失败！尝试修复...
        :: 修复可能的路径空格问题
        set "VENV_PATH=%~dp0venv\Scripts\activate.bat"
        call "%VENV_PATH%"
        if %errorlevel% neq 0 (
            echo [X] 仍然失败，请手动检查：
            echo     - 确保 venv\Scripts\activate.bat 文件存在
            echo     - 尝试手动运行：call venv\Scripts\activate
            pause
            exit /b
        )
    )
) else (
    echo [!] 未检测到虚拟环境，正在创建...
    python -m venv venv
    if %errorlevel% neq 0 (
        echo [X] 创建失败！请检查Python安装
        pause
        exit /b
    )
    call "venv\Scripts\activate.bat"
)

:: 安装依赖
pip install flask --quiet

:: 启动应用
start "" "http://127.0.0.1:5000"
python app.py

if %errorlevel% neq 0 (
    echo [X] 启动失败！尝试解决方案：
    echo     1. 关闭其他占用5000端口的程序
    echo     2. 检查app.py是否有语法错误
    pause
)