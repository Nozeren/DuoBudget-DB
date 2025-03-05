import asyncpg
import dotenv
import logging
import os
from src.queries.categories import Categories 
from src.queries.subcategories import Subcategories 

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

# Environment Variables
dotenv.load_dotenv()
user = os.getenv("PSQL_USER")
password = os.getenv("PSQL_PASSWORD")
host = os.getenv("PSQL_HOST")
port = os.getenv("PSQL_PORT")
database = os.getenv("PSQL_DB")

async def create_db() -> asyncpg.Pool:
    try:
        logging.info('Creating a pool.')
        con = await asyncpg.create_pool(
            user=user,
            password=password,
            host=host,
            port=port,
            database=database
        )
    except asyncpg.InvalidCatalogNameError:
        logging.info('Pool creation: FAILED. Database does not exist.')
        logging.info('Creating DB')
        sys_con = await asyncpg.connect(database="template1", user=user, password=password)
        await sys_con.execute(f'CREATE DATABASE "{database}" OWNER "{user}"')
        logging.info('Database Creation: SUCCESSFUL')
        logging.info('Creating a pool.')
        con = await asyncpg.create_pool(user=user, database=database, password=password)
    logging.info('Pool creation: SUCCESSFUL')
        
    return con

async def create_tables(pool: asyncpg.Pool) -> None:
    logging.info('Creating Tables')  
    async with pool.acquire()  as con:
        with open("src/schemas/tables.sql", "r") as sql:
            await con.execute(sql.read())
    logging.info('Tables Creation: SUCCESSFUL')

async def load_initial_data(pool: asyncpg.Pool) -> None:
    await Categories(pool=pool).load_initial_data()
    await Subcategories(pool=pool).load_initial_data()