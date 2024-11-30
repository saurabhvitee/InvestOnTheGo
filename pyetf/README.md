# pyetf to get market data

pyetf is a Python library for dealing extracting ETF data from etfdb.com.

## Installation

* Install with pip as a package [pip](https://pypi.org/project/pyetfdb/0.1.0/)
```
pip install pyetfdb
```

```
from pyetf import etfdb
```


* Clone repostiory
```bash
# clone repository
git clone https://github.com/JakubPluta/pyetf.git
```
```bash
# navigate to cloned project and create virtual environment
python -m venv env 
```
```bash
# activate virtual environment
source env/Scripts/activate
```

```python
# install poetry
pip install poetry
```

```python
# install packages
poetry install
```




## Usage

```python
# Run update_etf.py
./update_etf.py
```

The script can take multiple hours to complete pulling data for all funds. For quick testing, use the SQL dumps in ETFDataDump folder to populate the tables with market data
