import pandas as pd

data = {
    'year_of_manufacture': [2010, 2015, 2005, 2020, 2012, 2000, 1998, 2018, 2011, 2007],
    'product_age': [15, 10, 20, 5, 13, 22, 24, 7, 14, 18],
    'repair_status': ['fixed', 'repairable', 'fixed', 'end of life', 'fixed', 'unknown', 'fixed', 'repairable', 'fixed', 'fixed']
}

repair = pd.DataFrame(data)

repair = pd.DataFrame(data)
print(repair['repair_status'].describe())