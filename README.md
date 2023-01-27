This repository contains canonical copies of useful reference datasets for the Wikimedia movement. It is maintained jointly by the Wikimedia Foundation's [Product Analytics](https://www.mediawiki.org/wiki/Product_Analytics) and [Data Engineering](https://wikitech.wikimedia.org/wiki/Data_Engineering) teams. 

# Data format
The data here is stored in [comma-separated values](https://en.wikipedia.org/wiki/Comma-separated_values) (CSV) format. Ideally, our CSVs would follow [RFC-4180](https://datatracker.ietf.org/doc/html/rfc4180#section-2), as [Pandas does by default](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html).

However, because of limitations in Hive, [Wmfdata-Python](https://github.com/wikimedia/wmfdata-python) [currently cannot handle quoted values](https://phabricator.wikimedia.org/T327983) when loading these files into the [Data Lake](https://wikitech.wikimedia.org/wiki/Analytics/Data_Lake).

As a result, until that issue is fixed, CSVs in this repository should use backslash escaping rather than quoting. In Pandas, this can be done with `df.to_csv("df.csv", quoting=csv.QUOTE_NONE, escapechar="\\")`.