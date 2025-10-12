import pandas as pd
import os as os
import glob as glob

folderName = r'D:\Python stuff\Excel samples'

# Return a list containing the names of the files in the directory
allFiles = os.listdir(folderName)
# print(allFiles)

# Return a list of paths matching a pathname pattern
allExcelFiles = glob.glob(f"{folderName}/*.xlsx")

for file in allExcelFiles:
    print(file)
    # read the files
    df = pd.read_excel(file)

    # calculate
    sumInt = df.select_dtypes('int').sum()
    sumIntDf = pd.DataFrame([sumInt])

    # append to the end
    result = pd.concat([df, sumIntDf], ignore_index=True)

    # write to the file
    with pd.ExcelWriter(file, mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
        result.to_excel(writer, index=False)

print('done')
