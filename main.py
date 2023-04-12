import pandas as pd

df_employee = pd.read_csv('Employee+Demographics.csv')
type(df_employee)
input_value = input("M or F\n")
count_employees = df_employee.loc[df_employee['Sex'] == input_value.upper()]
print(len(count_employees))