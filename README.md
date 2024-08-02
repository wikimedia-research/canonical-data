# Wikimedia canonical data
This repository contains canonical copies of useful reference datasets for the Wikimedia movement. It is maintained by the Wikimedia Foundation's [Movement Insights team](https://meta.wikimedia.org/wiki/Movement_Insights). 

For documentation on the individual datasets, see the readmes in their directories.

## Data format
The data here is stored in [tab-separated values](https://en.wikipedia.org/wiki/Tab-separated_values) (TSV) format. For simplicity, values should not contain any tabs or newlines.

This approach avoids the escaping and quoting issues often caused by the CSV format (for an example, see [T327983](https://phabricator.wikimedia.org/T327983)).