"""
Норма чистой прибыли (profit margin) = Чистая прибыль (стр. 2400 ф. 0710002) / Выручка (стр. 2110 ф. 0710002) х 100
Рентабельность продаж (sales margin) = Прибыль от продаж (стр. 2200 ф. 0710002) / Выручка (стр. 2110 ф. 0710002)
Рентабельность основной деятельности = Чистая прибыль (стр. 2400 ф. 0710002) / Себестоимость продаж (стр. 2120 ф. 0710002)

Рентабельность собственного капитала (ROE) = Чистая прибыль (стр. 2400 ф. 0710002) / Собственный капитал (стр. 1300 ф. 0710001)
Формула ROE для расчета за период, отличный от года:
Рентабельность собственного капитала = Чистая прибыль х (365/ Количество дней в периоде): [(Собственный капитал на начало периода + Собственный капитал на конец периода)/2]
"""


def represent(number: int | float) -> int | float:
    return round(100 * number, 1)


def calculate_revenue_growth_yoy(current_year: int, previous_year: int) -> float | None:
    return (
        round(
            int(current_year) / int(previous_year) * 100 - 100,
        )
        if ((current_year > 0) and (previous_year > 0))
        else None
    )


def calculate_profit_margin(net_income: int, revenue: int) -> float | None:
    """
    net_income == "2400" code
    revenue == "2110" code
    """
    return represent(net_income / revenue) if (net_income > 0 and revenue > 0) else None


def calculate_ebit_margin(income_before_taxes: int, revenue: int) -> float | None:
    """
    income_before_taxes == "2300" code
    revenue == "2110" code
    """
    return (
        represent(income_before_taxes / revenue)
        if (income_before_taxes > 0 and revenue > 0)
        else None
    )


def calculate_sales_margin(profit_on_sales: int, revenue: int) -> float | None:
    """
    profit_on_sales == "2200" code
    revenue == "2110" code
    """
    return (
        represent(profit_on_sales / revenue)
        if (profit_on_sales > 0 and revenue > 0)
        else None
    )


def calculate_gross_margin(gross_profit: int, revenue: int) -> float | None:
    """
    gross_profit == "2100" code
    revenue == "2110" code
    """
    return (
        represent(gross_profit / revenue)
        if (gross_profit > 0 and revenue > 0)
        else None
    )


def calculate_roe(
    net_income: int,
    total_assets: int,
    total_assets_previous_year: int,
) -> float | None:
    """
    net_income == "2400" code
    total_assets == "1300" code
    """
    return (
        represent(net_income / total_assets)
        if (net_income > 0 and total_assets > 0 and total_assets_previous_year > 0)
        else None
    )
