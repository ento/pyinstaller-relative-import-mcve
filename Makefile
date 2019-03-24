.PHONY: debug
debug: main.py
	python3 main.py

.PHONY: run
run: dist/main/main
	dist/main/main

dist/main/main: venv/bin/pyinstaller main.py
	venv/bin/pyinstaller main.py -y

venv/bin/pyinstaller: requirements.txt venv/bin/pip
	venv/bin/pip install -r requirements.txt

venv/bin/pip:
	python3.5 -m venv venv

.PHONY: clean
clean:
	rm -rf dist build venv
