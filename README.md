# DuoBudget-DB
Automatically Generate Database and populates with initial data for the [DuoBudget](https://github.com/Nozeren/DuoBudget)

# Requirements
PostgreSQL connection or installed on your local machine.
### Postgresql & PGAdmin4 with docker-compose
Change credentials on docker-compose.yml and run the command bellow:
`docker-compose up -d`

Open pgadmin4: http://localhost:8888/browser/
Click on add server and add the DB credentials.

# Install
Create virtual environment:
`python -m venv /path/to/new/virtual/environment`

Activate virtual environment:
`/path/to/new/virtual/environment/Scripts/activate`

Install Requirements:
`pip install -r requirements.txt`

# Execution
Create enviroment variables for Posgresql credentials
```PSQL_USER
PSQL_PASSWORD
PSQL_HOST
PSQL_PORT 
PSQL_DB
```

Execute main.py
`python main.py`
