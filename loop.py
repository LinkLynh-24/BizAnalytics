import pandas as pd
import os

# Folder containing your 100 Excel files
folder_path = r"C:\Users\User\Desktop\excels"

# Loop through all Excel files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".xlsx"):
        file_path = os.path.join(folder_path, filename)
        
        # Read Excel file
        df = pd.read_excel(file_path)
        
        # Clean columns (optional)
        df.columns = df.columns.str.strip()
        
        # Calculate sum of numeric columns
        sum_row = df.select_dtypes(include='number').sum()
        
        # Label the sum row in the first column
        sum_row[df.columns[0]] = 'Total'
        
        # Append the sum row to the dataframe
        df_with_sum = pd.concat([df, pd.DataFrame([sum_row])], ignore_index=True)
        
        # Save back to the same file (overwriting)
        df_with_sum.to_excel(file_path, index=False)
        
        print(f"Processed and updated {filename}")

   
print('End')

        
