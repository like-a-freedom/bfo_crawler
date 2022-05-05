# What is it?

This tool is intended to collect and calculate the financial indicators of Russian companies based on public accounting data from the portal bo.nalog.ru. Data is cached with TinyDB, if INN was requested earlier, the data will be given from the cache.

# How does it work?

You can just import `crawler.py` module and use `get_org_data()` function that will return organization financial data details.

```python
import crawler

inns = [7729058675, 7736227885]

for inn in inns:
    print(crawler.get_org_data(inn))
```

Result:

```json
{
    "inn": 7729058675,
    "bfo_id": 7136976,
    "results": [
        {
            "2021": {
                "revenue": 28914838000,
                "income": 1834539000,
                "revenue_growth_yoy": "30%",
                "profit_margin": "6.3%",
                "ebit_margin": "8.0%",
                "sales_margin": "7.9%",
                "gross_margin": "23.7%",
                "roe": "19.6%"
            }
        },
        {
            "2020": {
                "revenue": 22153392000,
                "income": 1284849000,
                "revenue_growth_yoy": null,
                "profit_margin": "5.8%",
                "ebit_margin": "7.5%",
                "sales_margin": "6.4%",
                "gross_margin": "25.6%",
                "roe": null
            }
        }
    ]
}
...
{
    "inn": 7736227885,
    "bfo_id": 7152470,
    "results": [
        {
            "2021": {
                "revenue": 51718041000,
                "income": 133526000,
                "revenue_growth_yoy": "6%",
                "profit_margin": "0.3%",
                "ebit_margin": "0.4%",
                "sales_margin": "1.6%",
                "gross_margin": "12.9%",
                "roe": "5.1%"
            }
        },
        {
            "2020": {
                "revenue": 48738913000,
                "income": 281815000,
                "revenue_growth_yoy": null,
                "profit_margin": "0.6%",
                "ebit_margin": "0.7%",
                "sales_margin": "1.8%",
                "gross_margin": "12.7%",
                "roe": null
            }
        }
    ]
}
```
