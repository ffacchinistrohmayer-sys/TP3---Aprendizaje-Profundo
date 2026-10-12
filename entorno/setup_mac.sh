#!/usr/bin/env bash
# Prepara el entorno del TP3 en tu Mac. Correlo vos desde la Terminal:
#   cd <carpeta TP3/entorno> && bash setup_mac.sh
set -e
cd "$(dirname "$0")"

PY=$(command -v python3.12 || command -v python3.11 || command -v python3.10 || command -v python3 || true)
if [ -z "$PY" ]; then
  echo "No encontré Python 3. Instalalo con: brew install python@3.11  (o desde python.org)"; exit 1
fi
echo ">> Usando $($PY --version) en $PY"

$PY -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt

# Registra el kernel para que VS Code lo liste como "TP3 Aprendizaje Profundo"
python -m ipykernel install --user --name tp3-ap --display-name "TP3 Aprendizaje Profundo"

echo ">> Verificando instalación..."
python check_entorno.py
echo ">> Listo. En VS Code: abrí el .ipynb > 'Select Kernel' > 'TP3 Aprendizaje Profundo' (o .venv)."
