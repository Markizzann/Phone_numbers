## functions модуль для импорта функций для работы

import pandas as pd
import os

def process_row(row):
    s = row['phone_number']
    s_new = ''.join(filter(str.isdigit, str(s)))
    row['phone_number'] = s_new
    return row
    
def process_file():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'phone_numbers.xlsx')
    output_file_path = os.path.join(script_dir, 'cleaned_phone_numbers.xlsx')
    df = pd.read_excel(file_path)
    df = df.apply(process_row, axis=1)
    df.to_excel(output_file_path, index=False, engine='openpyxl')