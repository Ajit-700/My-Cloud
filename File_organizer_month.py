import os
import shutil
from datetime import datetime

# Use raw strings to handle file paths in Windows
source_directory = r'C:\Users\ajitk\OneDrive\Desktop\indimator\indianimator - Copy'  # Replace with your actual source directory
destination_directory = r'C:\Users\ajitk\OneDrive\Desktop\indimator\New one'  # Replace with your actual destination directory

# Ensure destination directory exists
os.makedirs(destination_directory, exist_ok=True)

# Iterate over files in the source directory
for filename in os.listdir(source_directory):
    file_path = os.path.join(source_directory, filename)
    
    # Skip if it's a directory
    if os.path.isdir(file_path):
        continue
    
    # Get the modification time of the file
    mod_time = os.path.getmtime(file_path)
    
    # Convert modification time to a year-month string (e.g., '2024-10')
    file_month = datetime.fromtimestamp(mod_time).strftime('%Y-%m')
    
    # Create a folder with the file month if it doesn't exist
    month_folder = os.path.join(destination_directory, file_month)
    os.makedirs(month_folder, exist_ok=True)
    
    # Move the file to the month folder
    shutil.move(file_path, os.path.join(month_folder, filename))

print("Files have been organized by month.")
