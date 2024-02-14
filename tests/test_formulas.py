import formulas
import json
import sys
from os.path import join, dirname
from os import pardir
import pathlib
import random

sys.path.append(join(dirname(__file__), pardir))

FIXTURES_DIR = join(pathlib.Path(__file__).parent.absolute(), "fixtures")

with open(join(FIXTURES_DIR, "finance_details.json"), "r") as mock:
    bfo_data = json.load(mock)


class TestFormulas:
    def test_calculate_revenue_growth_yoy(self):
        current_year = 117
        previous_year = 100
        result = formulas.calculate_revenue_growth_yoy(current_year, previous_year)
        assert result == 17

    def test_calculate_revenue_growth_yoy_negative(self):
        current_year = random.randint(0, 10)
        previous_year = 0 if current_year > 0 else random.randint(0, 10)
        result = formulas.calculate_revenue_growth_yoy(current_year, previous_year)
        assert result == None

    def test_calculate_revenue_growth_yoy_zero(self):
        current_year = 0
        previous_year = 0
        result = formulas.calculate_revenue_growth_yoy(current_year, previous_year)
        assert result == None

    def test_calculate_profit_margin(self):
        net_income = 1691611
        revenue = 35432270
        result = formulas.calculate_profit_margin(net_income, revenue)
        assert result == 4.8

    def test_calculate_profit_margin_negative(self):
        net_income = random.randint(0, 10)
        revenue = 0 if net_income > 0 else random.randint(0, 10)
        result = formulas.calculate_profit_margin(net_income, revenue)
        assert result == None

    def test_calculate_profit_margin_zero(self):
        net_income = 0
        revenue = 0
        result = formulas.calculate_profit_margin(net_income, revenue)
        assert result == None

    def test_calculate_ebit_margin(self):
        income_before_taxes = 2275033
        revenue = 35432270
        result = formulas.calculate_ebit_margin(income_before_taxes, revenue)
        assert result == 6.4

    def test_calculate_ebit_margin_negative(self):
        income_before_taxes = random.randint(0, 10)
        revenue = 0 if income_before_taxes > 0 else random.randint(0, 10)
        result = formulas.calculate_ebit_margin(income_before_taxes, revenue)
        assert result == None

    def test_calculate_ebit_margin_zero(self):
        income_before_taxes = 0
        revenue = 0
        result = formulas.calculate_ebit_margin(income_before_taxes, revenue)
        assert result == None

    def test_calculate_sales_margin(self):
        profit_on_sales = 6989431
        revenue = 35432270
        result = formulas.calculate_sales_margin(profit_on_sales, revenue)
        assert result == 19.7

    def test_calculate_sales_margin_negative(self):
        profit_on_sales = random.randint(0, 10)
        revenue = 0 if profit_on_sales > 0 else random.randint(0, 10)
        result = formulas.calculate_ebit_margin(profit_on_sales, revenue)
        assert result == None

    def test_calculate_sales_margin_zero(self):
        profit_on_sales = 0
        revenue = 0
        result = formulas.calculate_ebit_margin(profit_on_sales, revenue)
        assert result == None

    def test_calculate_gross_margin(self):
        gross_profit = 22662543
        revenue = 35432270
        result = formulas.calculate_sales_margin(gross_profit, revenue)
        assert result == 64.0

    def test_calculate_gross_margin_negative(self):
        gross_profit = random.randint(0, 10)
        revenue = 0 if gross_profit > 0 else random.randint(0, 10)
        result = formulas.calculate_ebit_margin(gross_profit, revenue)
        assert result == None

    def test_calculate_gross_margin_zero(self):
        gross_profit = 0
        revenue = 0
        result = formulas.calculate_ebit_margin(gross_profit, revenue)
        assert result == None

    def test_calculate_roe(self):
        total_assets = 31314200
        total_assets_previous_year = 29622589
        net_income = 1691611
        result = formulas.calculate_roe(
            net_income, total_assets, total_assets_previous_year
        )
        assert result == 5.4

    def test_calculate_roe_negative(self):
        total_assets = random.randint(0, 10)
        total_assets_previous_year = 0
        net_income = 0 if total_assets > 0 else random.randint(0, 10)
        result = formulas.calculate_roe(
            net_income, total_assets, total_assets_previous_year
        )
        assert result == None

    def test_calculate_roe_zero(self):
        total_assets = 0
        total_assets_previous_year = 0
        net_income = 0
        result = formulas.calculate_roe(
            net_income, total_assets, total_assets_previous_year
        )
        assert result == None
