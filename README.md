A FastApi Boilerplate for Production Development

## Technology Stack:
* FastAPI
* Uvicorn (server)
* Sqlalchemy
* MySql


## How to start the project ?
```
git clone https://github.com/Hunnyjain7/fastapi-production-boilerplate.git
cd fastapi-production-boilerplate
python -m venv env                  #create a virtual environment
.\env\Scripts\activate              #activate your virtual environment
pip install -r requirements.txt
cd project/database/database.py     #make sure you change the db connection string in DATABASE_URL variable
uvicorn application:app --reload    #start server
visit  127.0.0.1:8000/
```
