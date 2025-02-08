import numpy as np

# 3-a
X = ord('A')+ord('V')
sales = np.array([X, X + 50, X + 100, X + 150, X + 200])
print("Sales array:", sales)

# 3-b
tax_rate = ((X % 5) + 5) / 100
print(tax_rate)
sales_after_tax = sales * (1 - tax_rate)
print("Sales after tax:", sales_after_tax)

# 3-c
discounted_sales = np.where(sales < X+100, sales_after_tax * 0.95, sales_after_tax * 0.90)
print("Discounted sales:", discounted_sales)

# 3-d
sales_weeks = np.array([sales, sales * 1.02, sales * 1.02**2])
print("Sales over 3 weeks:\n", sales_weeks)