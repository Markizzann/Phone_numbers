# project_4

# Дан файл .xlsx с номерами телефонов. 
# Напишите скрипт, который очищает телефоны от ненужных символов. 
# Результат сохраните в новый файл с расширением .xlsx. 
# Например, 
# 8(645) 590-10-12 -> 86455901012.  

# Используйте библиотеку pandas, openpyxl

# Ссылка на файл.
# https://drive.google.com/drive/folders/1FpCRKyCTgAuWS9h2O0tWmJZ5erTPYxQ1?usp=sharing


import pandas as pd
import os
from openpyxl import load_workbook

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'phone_numbers.xlsx')
output_file_path = os.path.join(script_dir, 'cleaned_phone_numbers.xlsx')
df = pd.read_excel(file_path, engine='openpyxl')
df = df.apply(process_row, axis=1)
df.to_excel(output_file_path, index=False, engine='openpyxl')