@echo off

cd FramePack

echo Edit this file and set set HF_HUB_ENABLE_HF_TRANSFER=0 if you get model download errors of HF_TRANSFER

call .\venv\Scripts\activate.bat || exit /b
REM SET CUDA_VISIBLE_DEVICES=0  - this is used to set certain CUDA device visible only used
set PYTHONWARNINGS=ignore
REM SET CUDA_VISIBLE_DEVICES=1
set HF_HUB_ENABLE_HF_TRANSFER=1

set TEMP=temp
set TMP=tmp

set TRANSFORMERS_CACHE=%~dp0FramePack\models
set HF_HOME=%~dp0FramePack\models
set HF_DATASETS_CACHE=%~dp0FramePack\models
echo Hugging Face cache folders set to: %TRANSFORMERS_CACHE%

python app.py

pause