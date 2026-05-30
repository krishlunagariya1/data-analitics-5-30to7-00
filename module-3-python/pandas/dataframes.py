import pandas as pd

data ={
    "name": ["brijesh", "het", "divyand", "krish"],
    "age": [25, 20, 28, 29],
    "salary": [35500, 15500, 55000, 20500]
}

res = pd.DataFrame(data)
print(res)

#output