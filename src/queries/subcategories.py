from src.queries.base import BaseQuery
from src.queries.categories import Categories
import pandas as pd

INITIAL_DATA = {"House": [
    "Rent",
    "Water",
    "Electricity",
    "Internet",
    "SIM-Card",
    "Condominium",
],
    "Family": [
    "Groceries",
    "Healthcare",
    "Gym",
    "Education",
    "Presents",
    "Clothes",
    "Shared-expenses"
],
    "Transport": ["Tickets"],
    "Extra": [
    "Restaurants",
    "Fast-food",
    "Entertainment",
    "Repair",
    "Vacations",
    "Household-Items",
    "Transactions",
],
    "Income": [
    "Salary",
    "Savings"
]
}


class Subcategories(BaseQuery):
    def __init__(self, pool):
        super().__init__(pool)

    async def load_initial_data(self):
        if not await self.check_data():
            data = []
            for category in INITIAL_DATA:
                category_data = await Categories(self.pool).get_id(category_name=category)
                category_id = category_data["id"]
                for subcategory in INITIAL_DATA[category]:
                    data.append((subcategory, category_id))
            dataframe = pd.DataFrame(
                data=data, columns=("name", "category_id"))
            await self.load_dataframe_to_database(df=dataframe)
