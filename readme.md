# What is it?

This tool is intended to collect and calculate the financial indicators of Russian companies based on public accounting data from the portal bo.nalog.ru. Data is cached with TinyDB, if INN was requested earlier, the data will be given from the cache.

# How does it work?

Install dependencies:

`pip install -r requirements.txt`

Then you can just run `harvester.py` that will read `./data/ru_cybersecurity_market_companies.csv` file, obtain and enrich it with financial results and store into SQLite database `db.sqlite`.

`python harvester.py`
