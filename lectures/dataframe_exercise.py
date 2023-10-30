import pandas as pd

indexes = ['c','d','e']
first_numbers = [1,2,3]
second_numbers = [4,5,6]

yeah = pd.Series(data=first_numbers, index=indexes)
nah = pd.Series(data=second_numbers, index=indexes)

okie = pd.DataFrame({"a": yeah, "b": nah })

print(okie)