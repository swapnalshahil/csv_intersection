# csv_intersection


## Introduction
csv_intersection is basically a PyPI Package to get common rows from two tsv/csv files. Many a time we need common data from two tsv/csv files so using csv_intersection package will prolly solve this problem.

This package currently have one function `csv_intersection` which returns common rows between two csv/tsv in list of OrderedDict.

Default delimiter is `","` and default encoding is `"UTF-8"`

## Function

```csv_intersection(path_of_tsv1, path_of_tsv2, delimiter, encoding)```

## Table of contents
* [Setup](#setup)
* [Usage](#usage)
* [Dependencies](#dependencies)
* [Contacts](#contacts)

## Setup

```pip install csv-intersection```

## Usage

```
from csv_intersection import csv_intersection

common_rows = csv_intersection(tsv1, tsv2)

# if delimiter is other than ","
common_rows = csv_intersection(tsv1,tsv2,delimiter = delimiter_of_file)

# if encoding is different other than UTF-8
common_rows = csv_intersection(tsv1, tsv2, encoding = encoding_of_file)

```

## Dependencies
It requires csv module only which is a built-in module in Python.

## Contacts
* [Author](https://swapnalshahil.github.io/)
* [Github](https://github.com/swapnalshahil)
* [Linkedin](https://www.linkedin.com/in/swapnalshahil/)
* [Twitter](https://twitter.com/eulersgamma)
