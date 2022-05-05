from glob import glob
from os import getcwd, path
from typing import List

from pandas.core.frame import DataFrame
from bfo_crawler.excel_parser import YEARS, FinStatements
from bfo_crawler.functions import *
from bfo_crawler.excel_parser import FinStatements

FIXTURES_PATH: str = "bfo_crawler/tests/fixtures"


def get_fixtures(path: str) -> List[str]:
    return glob(f"{path}/*.xlsx")


def get_file(filepath: str):
    with open(
        path.join(getcwd(), filepath),
        "rb",
    ) as file:
        return file.read()


YEARS: List[int] = [2020, 2021]


class TestExcelParse:
    def test_excel_fin_statements_parse(self):
        for filepath in get_fixtures(FIXTURES_PATH):
            excel_file = get_file(filepath)

            fin = FinStatements(excel_file)
            assert isinstance(fin.balance, DataFrame)
            assert isinstance(fin.pnl, DataFrame)
            # assert isinstance(fin.capital_change, DataFrame | None)
            # assert isinstance(fin.funds_movement, DataFrame | None)

    def test_locate_column(self):
        column_values = [
            [13, 22, 29],
            [7, 11, 15],
            [8, 12, 15],
            [7, 11, 15],
            [8, 12, 15],
            [7, 11, 15],
            [13, 22, 29],
            [13, 22, 29],
        ]

        for idx, filepath in enumerate(get_fixtures(FIXTURES_PATH)):
            excel_file = get_file(filepath)
            fin = FinStatements(excel_file)

            assert fin.locate_column_index(fin.balance, "3") == column_values[idx][0]
            assert fin.locate_column_index(fin.pnl, "4") == column_values[idx][1]
            assert fin.locate_column_index(fin.pnl, "5") == column_values[idx][2]

    def test_parse(self):
        fin_values = [
            [  # 2020
                [1229783, 6180988, 48738913, 859617, 363190, 281815],
                [0, 0, 135567, 0, 0, 14538],
                [4680731, 4996782, 16501452, 3061498, 2904086, 2269340],
                [0, 0, 6783, 0, 0, 982],
                [54528, 5622, 8721, 11326, 13721, 13721],
                [0, 0, 34807, 0, 0, 27212],
                [616073, 955005, 4749017, 534962, 601972, 470283],
                [1229783, 6180988, 48738913, 859617, 363190, 281815],
            ],
            [  # 2021
                [1363309, 6664340, 51718041, 804797, 182837, 133526],
                [94213, 0, 126886, 0, 0, 25504],
                [6744308, 13874089, 18144918, 3137553, 2589282, 2395696],
                [2362, 0, 5355, 0, 0, 517],
                [72656, 4973, 9044, 16702, 17087, 17087],
                [1607, 0, 44880, 0, 0, 34685],
                [563945, 937218, 4394378, 312372, 317147, 250221],
                [1363309, 6664340, 51718041, 804797, 182837, 133526],
            ],
        ]

        for idx, filepath in enumerate(get_fixtures(FIXTURES_PATH)):
            excel_file = get_file(filepath)
            fin = FinStatements(excel_file)

            for year_idx, year in enumerate(YEARS):
                assert fin.find_in(1300, year) == fin_values[year_idx][idx][0]
                assert fin.find_in(2100, year) == fin_values[year_idx][idx][1]
                assert fin.find_in(2110, year) == fin_values[year_idx][idx][2]
                assert fin.find_in(2200, year) == fin_values[year_idx][idx][3]
                assert fin.find_in(2300, year) == fin_values[year_idx][idx][4]
                assert fin.find_in(2400, year) == fin_values[year_idx][idx][5]
