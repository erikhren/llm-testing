# llm-testing

## Requirements
1. Install requirements (poetry or pip)
`pip install -r requirements.txt`

2. Install Ollama CLI & Server

🐧 Linux (Debian/Ubuntu)
`curl -fsSL https://ollama.com/install.sh | sh`

If ollama does not detect GPU's during installation:
`apt install -y lspci lshw`

Sets it up to run as a background service:
`ollama serve`

`ollama run llama3`

# Update python to match the requirements version
## Update and install prerequisites
apt update
apt install -y software-properties-common

## Add the deadsnakes PPA (provides newer Python versions)
add-apt-repository ppa:deadsnakes/ppa
apt update

## Install Python 3.11
apt install -y python3.11 python3.11-venv python3.11-dev

## Now you should be able to create the venv
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

## If want to run in jupyter
Then, add your `.venv` as a jupyter kernel:
`python -m ipykernel install --user --name=llm-testing --display-name "Python (llm-testing)"`

### Requirements for RAG
`apt install -y poppler-utils`

`apt install -y tesseract-ocr`

Xet Storage is enabled for this repo, but the 'hf_xet' package is not installed. Falling back to regular HTTP download. For better performance, install the package with: `pip install huggingface_hub[hf_xet]` or `pip install hf_xet`