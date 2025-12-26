python --version
python -m venv env
pip install "fastapi[standard]"
pip install "uvicorn[standard]"
python -m uvicorn src.main:app --reload --host 127.0.0.1 --port 8000