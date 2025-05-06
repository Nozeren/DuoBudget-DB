from src.queries.base import BaseQuery
import pandas as pd
import asyncpg

INITIAL_DATA = {"name":['debit', 'savings'],"in_budget": [True, False]}

class Accounts_Type(BaseQuery):
    def __init__(self, pool):
        super().__init__(pool)
    
    async def load_initial_data(self):
        if not await self.check_data():
           dataframe = pd.DataFrame(data=INITIAL_DATA) 
           await self.load_dataframe_to_database(df=dataframe)
    
