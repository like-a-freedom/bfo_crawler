import pandas as pd
import warnings
from typing import List

YEARS: List = [2021, 2020]


class FinStatements:
    balance = None
    pnl = None
    capital_change = None
    funds_movement = None

    def __init__(self, excel_file: bytes):
        with warnings.catch_warnings(record=True):
            warnings.simplefilter("always")
            excel = pd.ExcelFile(excel_file, engine="openpyxl")

        self.balance = pd.read_excel(excel, "Balance")
        self.pnl = pd.read_excel(excel, "Financial Result")

        # TODO: Implement additional calculations
        #
        # try:
        #     self.capital_change = pd.read_excel(self.excel, "Capital Change")
        # except ValueError:
        #     self.capital_change = None
        # try:
        #     self.funds_movement = pd.read_excel(self.excel, "Funds Movement")
        # except ValueError:
        #     self.funds_movement = None

    def locate_column_index(self, df: pd.DataFrame, value: str) -> int:
        try:
            self.column_name = df.isin([value]).any()
            self.column_name = self.column_name.index[self.column_name == True].values[
                0
            ]
            self.column_idx = df.columns.get_loc(self.column_name)
            return self.column_idx
        except Exception as e:
            raise Exception(e)

    def find_in(self, string_code: int, year: int) -> int:
        """
        It is quite tricky to parse excel files,
        because the names of the required columns
        may be different, the position of the
        columns is different also.

        I used codes 3, 4 and 5 - it's unreliable,
        but it seems to work so far.

        For better parsing quality, it would be nice
        to do the following: look for the name of the row,
        if it matches, then look in the cell below for the
        appropriate code (3, 4 or 5), if it is found, then
        return column index.

        Examples of values:

        labels = [
            "За 2021 г.",
            "За 2020 г.",
            "На 31 декабря 2021 года.",
            "На 31 декабря 2020 года.",
            "На 31 декабря 2021 года",
        ]
        """

        if string_code // 1000 == 1:
            df: pd.DataFrame | None = self.balance
            years = {
                YEARS[0]: self.locate_column_index(df, "4"),
                YEARS[1]: self.locate_column_index(df, "5"),
            }
            # print(df.iloc[:, self.locate_column_index("4")])
        elif string_code // 1000 == 2:
            df = self.pnl
            years = {
                YEARS[0]: self.locate_column_index(df, "4"),
                YEARS[1]: self.locate_column_index(df, "5"),
            }
        else:
            raise Exception(
                f"String code `{string_code}` calculation is not implemented yet"
            )

        n = df.iloc[:, self.locate_column_index(df, "3")]

        try:
            year_column = years[year]
        except KeyError:
            raise Exception("Year not found...")
        try:
            index = n.index[list(n).index(str(string_code))]
        except ValueError:
            return 0

        value = df.iloc[index, year_column]

        negative = -1 if value == "(" or value == "-" else 1
        try:
            value = int("".join([x for x in value if x.isdigit()]))
        except:
            value = 0
        return negative * value
