import pandas as pd
import os

def filter_excel_by_keywords(input_file, output_file, keywords, designation_column):
    # Ensure the file exists before proceeding
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' not found.")
        return
    
    # Detect if it's CSV or Excel
    if input_file.endswith(".csv"):
        try:
            df = pd.read_csv(input_file, encoding="utf-8-sig", sep=",", engine="python", on_bad_lines='skip')
        except Exception as e:
            print(f"Error reading CSV file: {e}")
            return
    else:
        try:
            df = pd.read_excel(input_file, engine='openpyxl')
        except Exception as e:
            print(f"Error reading Excel file: {e}")
            return
    
    print("File loaded successfully.")
    
    # Create a dictionary to store filtered DataFrames
    filtered_data = {}
    
    # Filter rows based on keywords
    for keyword in keywords:
        filtered_df = df[df.apply(lambda row: row.astype(str).str.contains(keyword, case=False, na=False).any(), axis=1)]
        if not filtered_df.empty:
            filtered_data[keyword] = filtered_df
    
    # Save results
    try:
        with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
            # Ensure at least one sheet exists
            if not filtered_data:
                df.head(5).to_excel(writer, sheet_name="Sample_Data", index=False)  # Prevent empty file issue
            else:
                for keyword, filtered_df in filtered_data.items():
                    filtered_df.to_excel(writer, sheet_name=f'Keyword_{keyword[:30]}', index=False)
                
                # Group data by designation
                if designation_column in df.columns:
                    for designation, group in df.groupby(designation_column):
                        group.to_excel(writer, sheet_name=f'Designation_{str(designation)[:30]}', index=False)
        
        print(f'Filtered data saved to {output_file}')
    except PermissionError:
        print(f"Error: Please close '{output_file}' and run the script again.")

# Example Usage
input_file = r'C:\Users\ajitk\OneDrive\Desktop\Connections.csv'  # Use raw string format
output_file = r'C:\Users\ajitk\OneDrive\Desktop\Arpit.xlsx' # Use raw string format
keywords = ['HR', 'Director', 'Founder', 'vice president', 'CEO', 'Head', 'Advisor', 'Chairman', 'Vice chairman', 'Executive', ]  # Keywords to filter data
designation_column = 'Designation'  # Column name to group similar designations

filter_excel_by_keywords(input_file, output_file, keywords, designation_column)
