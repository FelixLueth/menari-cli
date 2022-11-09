# menari-cli

Menari is a program and ongoing project to train your mental arithmentic skills. Another part is to have a private project to getting used to github actions and CI implementation of software. 

## Setup

### Get project and install requirements

```bash
git clone git@github.com:FelixLueth/menari-cli.git
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run Menari

```bash
source venv/bin/activate
python main.py
```

### Run Tests

```bash
source venv/bin/activate
pytest */*Test.py
```

### Deactivate Environment 
```bash
deactivate
```
