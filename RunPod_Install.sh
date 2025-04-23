pip install requests
pip install tqdm
apt update
git lfs install
apt install ffmpeg --yes
apt update --yes

git clone https://github.com/FurkanGozukara/FramePack

cd FramePack

git pull

python -m venv venv

source ./venv/bin/activate

pip install --pre torch==2.7.0.dev20250311 torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu128

pip install deepspeed

pip install triton

pip install wheel

pip install torchao

pip install ninja

pip install https://huggingface.co/MonsterMMORPG/SECourses_Premium_Flash_Attention/resolve/main/flash_attn-2.7.4.post1-cp310-cp310-linux_x86_64.whl

pip install https://huggingface.co/MonsterMMORPG/SECourses_Premium_Flash_Attention/resolve/main/sageattention-2.1.1-cp310-cp310-linux_x86_64.whl

pip install -r requirements.txt

pip install huggingface_hub ipywidgets hf_transfer

pip install easydict

pip install moviepy

pip install -r requirements.txt

git clone https://github.com/FurkanGozukara/Practical-RIFE
cd Practical-RIFE 
git pull
pip install -r requirements.txt

cd ..
cd ..

python Download_RIFE.py

echo "Virtual environment made and installed properly"

read -p "Press [Enter] key to continue..."
