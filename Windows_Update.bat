@echo off

cd FramePack

git remote set-url origin https://github.com/FurkanGozukara/FramePack

git pull

py --version >nul 2>&1
if "%ERRORLEVEL%" == "0" (
    echo Python launcher is available. Generating Python 3.10 VENV
    py -3.10 -m venv venv
) else (
    echo Python launcher is not available, generating VENV with default Python. Make sure that it is 3.10
    python -m venv venv
)

call .\venv\Scripts\activate.bat

python -m pip install --upgrade pip

pip install --pre torch==2.7.0.dev20250311 torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu128

pip install https://huggingface.co/MonsterMMORPG/SECourses_Premium_Flash_Attention/resolve/main/flash_attn-2.7.4.post1-cp310-cp310-win_amd64.whl

pip install https://files.pythonhosted.org/packages/3d/65/1a6394f5d6dee851e9ea59e385f6d6428e3bfe36f83c06e0336e14dcfd11/deepspeed-0.16.4-cp310-cp310-win_amd64.whl

pip install https://github.com/woct0rdho/SageAttention/releases/download/v2.1.1-windows/sageattention-2.1.1+cu128torch2.7.0-cp310-cp310-win_amd64.whl

pip install -U --pre triton-windows

pip install torchao

pip install -r requirements.txt

pip install huggingface_hub ipywidgets hf_transfer

cd ..

REM python Download_Models.py

REM Show completion message
echo FramePack installed check out all messages and save them before close to verify any errors or not later

REM Pause to keep the command prompt open
pause