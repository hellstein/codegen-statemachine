# Deployment 

### Create test environment
```
pip3 install smgen
mkdir testapp
```
### Create configuration
```
cd testapp
mkdir conf
cd conf
vim states.json
vim init.json
```
* `states.json` has the format as
```json
{ 
    "INIT": {
        "description": "",
        "definition": {},
        "transitions": {
            "backup": "PREPARED"
        }
    },
    "PREPARED": {
        "description": "",
        "definition": {},
        "transitions": {
            "config": "CONFED",
            "restore": "INIT"
        }
    },
    "CONFED": {
        "description": "",
        "definition": {},
        "transitions": {
            "config": "CONFED",
            "restore": "INIT",
            "start": "RUNNING"
        }
    },
    "RUNNING": {
        "description": "",
        "definition": {},
        "transitions": {
            "stop": "CONFED",
            "config": "RECONFED",
            "restart": "RUNNING"
        }
    },
    "RECONFED": {
        "description": "",
        "definition": {},
        "transitions": {
            "config": "RECONFED",
            "restart": "RUNNING"
        }
    }     
}
```

* `init.json` has the format as
```json
{
    "state": "INIT",
    "action": "backup"
}
```

### Create application
```
cd testapp
python3 -m smgen.app --states conf/states.json --init conf/init.json --app app
```

### Test application
```
cd testapp/app
python3 context.py
```

