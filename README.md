# menari-cli

Menari is a program and ongoing project to train your mental arithmentic skills. Another part is to have a private project to getting used to github actions and CI implementation of software. 

## Status
[![Menari](https://github.com/FelixLueth/menari-cli/actions/workflows/menari_default.yml/badge.svg)](https://github.com/FelixLueth/menari-cli/actions/workflows/menari_default.yml)

## Setup

### Get project and install requirements

```bash
git clone git@github.com:FelixLueth/menari-cli.git
cd menari-cli
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
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
