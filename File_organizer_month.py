import os
import shutil
from datetime import datetime


source_directory = r'C:\Users\ajitk\OneDrive\Desktop\indimator\indianimator - Copy'  
destination_directory = r'C:\Users\ajitk\OneDrive\Desktop\indimator\New one'  
os.makedirs(destination_directory, exist_ok=True)


for filename in os.listdir(source_directory):
    file_path = os.path.join(source_directory, filename)
    

    if os.path.isdir(file_path):
        continue
    
   
    mod_time = os.path.getmtime(file_path)
    

    file_month = datetime.fromtimestamp(mod_time).strftime('%Y-%m')
    

    month_folder = os.path.join(destination_directory, file_month)
    os.makedirs(month_folder, exist_ok=True)
    

    shutil.move(file_path, os.path.join(month_folder, filename))

print("Files have been organized by month.")
