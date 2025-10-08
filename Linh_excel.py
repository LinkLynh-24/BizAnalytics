import pandas as pd

# Load Excel file
df = pd.read_excel('Financial_Sample.xlsx')

# Show the first few rows
# print(df)

total_sales = df[' Sales'].sum()

# print(df.columns.tolist())

# print("Total Sales:", total_sales)

sum = df.select_dtypes(include='number').sum()
#print(sum)

df_with_total = pd.concat([df, pd.DataFrame([sum])], ignore_index=True)

df_with_total.to_excel("Financial_Sample_1.xlsx", index=False)
