import asyncio
from src import creator


async def main():
    pool = await creator.create_db()
    await creator.create_tables(pool=pool)
    await creator.load_initial_data(pool=pool)


asyncio.run(main())