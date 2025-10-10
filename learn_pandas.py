import pandas as pd

file_name = r"C:\Users\ADMIN\Downloads\file_example_XLSX_50.xlsx"
# df = pd.read_excel(file_name)
# print(df.head())

# read the sheet in the file, pass in sheet_name=indexOfSheet or sheet_name="name of sheet"
# sheet_name = None -> read all sheets, the df will be a dict with:
# Keys = sheet names (strings)
# Values = DataFrames for each sheet
df = pd.read_excel(file_name, sheet_name=1)
# print(df.head())

# print the values from specific columns
# df = pd.read_excel(file_name,usecols=['Note', 'Age'],sheet_name="Sheet 2")
# print(df.head())

# get all columns
# print(df['Sheet1'].columns)

# get a single column
# print(df["Age"])

# loop and print the keys(sheet names)
# for sheet in df:
#     print(sheet)

# Looping over a dict → loops through its keys.
# Looping over a DataFrame → loops through its column names.

# print the data frame
# for sheet_name, sheet_df in df.items():
#     print(f"Sheet: {sheet_name}")
#     print(sheet_df.columns.tolist())

# print each row according to its index in the dataframe
# print(df[1])
# at can only access one single value at the time
# print(df.at[0, 'Id'])

# loc can access multiple values(rows and/or cols)
# print(df.loc[0, 'Age': 'Id'])

# calculate the sum of a column
sumOfAge = df["Age"].sum()
# print(sumOfAge)

# cal the sum of specific col
sumAgeWeight = df[["Age", "Weight"]].sum()
print(sumAgeWeight)

# cal the sum of all cols with dtype
sumAll = df.select_dtypes('int').sum()
sumAll2 = df.select_dtypes(include='number').sum()
# print(sumAll)
# print(sumAll2)

# count (non missing value) rows in a specific col
numberOfAge = df["Age"].count()
# print(numberOfAge)

# count all, including NaN
totalNumberOfAge = len(df["Age"])
# print(totalNumberOfAge)

# count multiple cols
countAgeId = df[["Age", "Id"]].count()
# print(countAgeId)
countAgeIdAll = df[["Age", "Id"]].apply(len)
print(countAgeIdAll)

# cal the average
# print(df["Age"].mean())

# append the result to excel file
sumAgeWeight_df = pd.DataFrame([sumAgeWeight])
df_result = pd.concat([df, sumAgeWeight_df], ignore_index=True)
# df_result = pd.concat([df, pd.DataFrame([sumAgeWeight])], ignore_index=True)
# with pd.ExcelWriter(file_name, mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
    # df_result.to_excel(writer, sheet_name='Sheet2', index=False)
