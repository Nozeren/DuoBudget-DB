from src.queries.base import BaseQuery
import pandas as pd


class Banks(BaseQuery):
    def __init__(self, pool):
        super().__init__(pool)
    