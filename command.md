python --version
python -m venv env
pip install "fastapi[standard]"
pip install "uvicorn[standard]"
uvicorn src.__init__:app --reload  # to run project
pip install alembic
almebic --help
alembic init -t async migration
alembic revision --autogenerate -m "message"
 alembic upgrade head     #to apply in database
 pip install passlib    # passward hash and verify
 