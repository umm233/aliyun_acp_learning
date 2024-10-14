conda update --all 
conda init

conda create -n learnacp python=3.9.12 -y
conda activate learnacp

pip install ipykernel
python -m ipykernel install --user --name learnacp --display-name "py39(learnacp)"






pip install torch==2.2.1 torchvision==0.17.1 torchaudio==2.2.1 --index-url https://download.pytorch.org/whl/cu118
pip install auto-gptq
# git clone https://github.com/PanQiWei/AutoGPTQ
# cd AutoGPTQ
# pip install .


pip install bitsandbytes --no-cache-dir
pip install "git+https://github.com/PanQiWei/AutoGPTQ.git@v0.4.2"

nvidia-smi
nvcc --version


pip install ipywidgets
# jupyter nbextension enable --py widgetsnbextension


python -u reverie.py>20240401-02.log 2>&1


# https://dsw-gateway.alibaba-inc.com/dsw76233/proxy/8000/demo/debug_1713053266416/2400/3/#