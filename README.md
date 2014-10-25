Human
=====

The digital api of your life

CONFIGURATION
=============
- Create a new virtualenv
```
cd Human/
virtualenv venv
```
- Add the requirements
```
pip install -r requirements.txt
```
- Add environmental variable for the data source. Accepted values JSON
```
export HUMAN_DATA_SOURCE_TYPE=JSON
```
- Change the json file for your data source
```
cd Human/human/core/api/sources/data
vim me.json
```

RUN
=======
```
cd Human/
python app.py
```

TESTING
=======
Use nosetests for running your unit tests or whatever you prefer ;)
```
cd Human/
nosetests
```

