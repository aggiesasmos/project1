import pandas as pd

data = {'Name': ['Aman', 'Akanksha', 'Akshit',
                 'Divyansha', 'Hardik'],
        'Age': [24, 26, 24, 22, 22],
        'City': ['New Delhi', 'Mumbai',
                 'Kolkata', 'Chennai', 'Bangalore'],
        'Salary': [80000, 70000,
                   65000, 60000, 55000]}
df = pd.DataFrame(data)
print(df.loc[3])
