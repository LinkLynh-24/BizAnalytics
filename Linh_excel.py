import pandas as pd

# Load Excel file
df = pd.read_excel('Financial_Sample.xlsx')

# calculate the sum of the Sales col
total_sales = df[' Sales'].sum()
# print("Total Sales:", total_sales)

# print(df.columns.tolist())

# calculate the sum of all cols with datatype = number
sum = df.select_dtypes(include='number').sum()
# print(sum)

# append the sum to the end of the file
df_with_total = pd.concat([df, pd.DataFrame([sum])], ignore_index=True)

# export to file
df_with_total.to_excel("Financial_Sample.xlsx", index=False)
