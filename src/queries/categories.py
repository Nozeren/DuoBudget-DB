from src.queries.base import BaseQuery
import pandas as pd
import asyncpg

INITIAL_DATA =  {"name": ["House", "Family", "Transport", "Extra", "Income"]} 

class Categories(BaseQuery):
    def __init__(self, pool):
        super().__init__(pool)
    
    async def load_initial_data(self):
        if not await self.check_data():
           dataframe = pd.DataFrame(data=INITIAL_DATA) 
           await self.load_dataframe_to_database(df=dataframe)
    
    async def get_id(self,  category_name:str): 
        query = f"""SELECT id FROM {self.table_name} WHERE name= '{category_name}'"""
        return await self.pool.fetchrow(query)
