This repository contains canonical copies of useful reference datasets for the Wikimedia movement. It is maintained jointly by the Wikimedia Foundation's [Product Analytics](https://www.mediawiki.org/wiki/Product_Analytics) and [Data Engineering](https://wikitech.wikimedia.org/wiki/Data_Engineering) teams. 

# Data format
The data here is stored in [tab-separated values](https://en.wikipedia.org/wiki/Tab-separated_values) (TSV) format. For simplicity, values should not contain any tabs or newlines.

This approach avoids the escaping and quoting issues often caused by the CSV format (for an example, see [T327983](https://phabricator.wikimedia.org/T327983)).