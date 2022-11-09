# menari-cli

Menari is a program and ongoing project to train your mental arithmentic skills. Another part is to have a private project to getting used to github actions and CI implementation of software. 

## Status
![main](.github/workflows/menari_default.yml/badge.svg)

## Setup

### Get project and install requirements

```bash
git clone git@github.com:FelixLueth/menari-cli.git
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate
```

### Run Menari
For easier use copy and enter all commands at once.
```bash
source venv/bin/activate
python main.py
deactivate
```

### Run Tests

```bash
source venv/bin/activate
pytest */*Test.py
deactivate
```

### Deactivate Environment 
```bash
deactivate
```
