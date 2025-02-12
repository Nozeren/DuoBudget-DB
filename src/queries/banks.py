from src.queries.base import BaseQuery
import pandas as pd

INITIAL_DATA = {"name": ["Alpha", "Eurobank", "Piraeus", "Revolut", "Santander"]} 

class Banks(BaseQuery):
    def __init__(self, pool):
        super().__init__(pool)
    
    async def load_initial_data(self):
        if not await self.check_data():
            df = pd.DataFrame(data=INITIAL_DATA)
            await self.load_dataframe_to_database(df=df)  