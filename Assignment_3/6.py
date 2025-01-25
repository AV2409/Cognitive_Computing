import pandas as pd

employees = pd.DataFrame({
    'Employee_ID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Edward'],
    'Department': ['HR', 'IT', 'IT', 'Marketing', 'Sales'],
    'Age': [29, 34, 41, 28, 38],
    'Salary': [50000, 70000, 65000, 55000, 60000],
    'Years_of_Experience': [4, 8, 10, 3, 12],
    'Joining_Date': ['2020-03-15', '2017-07-19', '2013-06-01', '2021-02-10', '2010-11-25'],
    'Gender': ['Female', 'Male', 'Male', 'Female', 'Male'],
    'Bonus': [5000, 7000, 6000, 4500, 5000],
    'Rating': [4.5, 4.0, 3.8, 4.7, 3.5],
})

# 6-a
print("\nShape of the DataFrame:", employees.shape)

# 6-b
print("\nSummary of the DataFrame:\n", employees.info())

# 6-c
print("\nDescriptive Statistics:\n", employees.describe())

# 6-d
print("\nFirst 5 rows:\n", employees.head())
print("\nLast 3 rows:\n", employees.tail(3))

# 6-e
print("\nAverage Salary:", employees['Salary'].mean())
print("Total Bonus:", employees['Bonus'].sum())
print("Youngest Age:", employees['Age'].min())
print("Highest Rating:", employees['Rating'].max())

# 6-f
sorted_employees = employees.sort_values(by='Salary', ascending=False)
print("\nEmployees sorted by Salary:\n", sorted_employees)

# 6-g

employees['Performance'] = ''

for i in range(len(employees)):
    if employees.loc[i, 'Rating'] >= 4.5:
        employees.loc[i, 'Performance'] = 'Excellent'
    elif employees.loc[i, 'Rating'] >= 4.0:
        employees.loc[i, 'Performance'] = 'Good'
    else:
        employees.loc[i, 'Performance'] = 'Average'

print(employees)


# 6-h
print("\nMissing values in the DataFrame:\n", employees.isnull())

# 6-i
employees.rename(columns={'Employee_ID': 'ID'}, inplace=True)
print("\nDataFrame with renamed column:\n", employees)

# 6-j
print("\nEmployees with > 5 years experience:\n", employees[employees['Years_of_Experience'] > 5])
print("\nEmployees in IT department:\n", employees[employees['Department'] == 'IT'])

# 6-k
employees['Tax'] = employees['Salary'] * 0.1
print("\nDataFrame with Tax column:\n", employees)

# 6-l
employees.to_csv("modified_employees.csv")