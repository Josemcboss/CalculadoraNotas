# Makefile for CalculadoraNotas project

.PHONY: help install test lint format run-tkinter run-streamlit clean

help:
	@echo "Available commands:"
	@echo "  install      Install dependencies"
	@echo "  test         Run tests"
	@echo "  lint         Run linting (flake8)"
	@echo "  format       Format code (black)"
	@echo "  run-tkinter  Run tkinter app"
	@echo "  run-streamlit Run Streamlit app"
	@echo "  clean        Clean cache files"

install:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

test:
	python -m unittest test_utils.py -v

lint:
	flake8 *.py

format:
	black *.py

run-tkinter:
	python calculadora_notas.py

run-streamlit:
	streamlit run app.py

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -name "*.pyc" -delete