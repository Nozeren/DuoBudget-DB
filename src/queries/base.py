import asyncpg
import logging
import pandas
class BaseQuery:
    def __init__(self, pool: asyncpg.Pool) -> None:
        self.pool = pool
        self.table_name:str = str(type(self).__name__).lower()
        
    async def check_data(self) -> bool:
        """Returns 1 if the table has data else 0"""
        return await self.pool.fetchval(f"SELECT CASE WHEN EXISTS(SELECT * FROM {self.table_name} LIMIT 1) THEN 1 ELSE 0 END")
    
    async def load_dataframe_to_database(self, df: pandas.DataFrame) -> None:
        data = [tuple(row) for row in df.values]
        await self.pool.copy_records_to_table(self.table_name, records=data, columns=list(df.columns))
        logging.info(f'Initial data loaded: {self.table_name} table')