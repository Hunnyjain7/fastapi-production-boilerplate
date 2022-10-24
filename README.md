## FastAPI Boilerplate for Production Development with MySql and Alembic Migrations

<p align="center">
  <a href="https://fastapi.tiangolo.com"><img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI"></a>
</p>
<p align="center">
    <em>FastAPI framework, high performance, easy to learn, fast to code, ready for production</em>
</p>
---

## Technology Stack:
* Python version 3.7 or above
* FastAPI
* Uvicorn (server)
* Sqlalchemy
* MySql
* Alembic (database migrations)


## How to start the project ?
```
git clone https://github.com/Hunnyjain7/fastapi-production-boilerplate.git
cd fastapi-production-boilerplate
python -m venv env                  #create a virtual environment
.\env\Scripts\activate              #activate your virtual environment
pip install -r requirements.txt
update your database connection string in .env
uvicorn application:app --reload    #start server use --host for host if required
visit Welcome screen at 127.0.0.1:8000 
visit Swagger UI docs screen at 127.0.0.1:8000/docs  # here all api routing and request can be triggered...

```

## Guide towards the Alembic Migrations for SqlAlchemy in FastAPI
```
* Install alembic
pip install alembic

step 1: cd project then alembic init alembic

step 2: mention your mysql connection string inside sqlalchemy.url

step 3: in env.py file inside alembic dir mention all models inside target_metadata this way
target_metadata = [usr_user.Base.metadata, cli_client.Base.metadata]

step 4: alembic revision --autogenerate -m "message to identify migration"

step 5: now below command will migrate all changes to the database
alembic upgrade head

step 6: whenever you make changes into the models then create the revision and upgrade it, even if you remove fields from the models upgrade command will be used
alembic revision --autogenerate -m "second migration message"
followed by alembic upgrade first three or four initials of your recent version created in my case command was
alembic upgrade 2a43 

to downgrade the recent migration simply alembic downgrade first three or four initials of your recent version created in my case command was
alembic downgrade 2a43
```
