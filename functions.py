represent = lambda number: str(round(100 * number, 1)) + "%"
calculate_profit_margin = (
    lambda self, year: represent(self.find_in(2400, year) / self.find_in(2110, year))
    if ((self.find_in(2400, year) > 0) and (self.find_in(2110, year) > 0))
    else None
)

calculate_ebit_margin = (
    lambda self, year: represent(self.find_in(2300, year) / self.find_in(2110, year))
    if ((self.find_in(2300, year) > 0) and (self.find_in(2110, year) > 0))
    else None
)

calculate_sales_margin = (
    lambda self, year: represent(self.find_in(2200, year) / self.find_in(2110, year))
    if ((self.find_in(2200, year) > 0) and (self.find_in(2110, year) > 0))
    else None
)

calculate_gross_margin = (
    lambda self, year: represent(self.find_in(2100, year) / self.find_in(2110, year))
    if ((self.find_in(2100, year) > 0) and (self.find_in(2110, year)))
    else None
)

calculate_roe = (
    lambda self, year: represent(
        self.find_in(2400, year)
        / (self.find_in(1300, year) + self.find_in(1300, year - 1))
    )
    if (
        (self.find_in(2400, year) > 0)
        and ((self.find_in(1300, year) > 0) and (self.find_in(1300, year - 1) > 0))
    )
    else None
)

calculate_revenue = (
    lambda self, year: int(self.find_in(2110, year)) * 1000
    if (self.find_in(2110, year) > 0)
    else None
)

calculate_income = (
    lambda self, year: (self.find_in(2400, year)) * 1000
    if (self.find_in(2400, year) > 0)
    else None
)

calculate_revenue_growth_yoy = (
    lambda self, year: str(
        round(
            int(self.find_in(2110, year) / self.find_in(2110, year - 1) * 100 - 100),
            1,
        )
    )
    + "%"
    if ((self.find_in(2110, year) > 0) and (self.find_in(2110, year - 1) > 0))
    else None
)
