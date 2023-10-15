import pandas as pd
from datetime import datetime
import time

input_file_path = "some_name.xlsx"

output_file_path = "update_discounted_rates.py"


class BusinessType(Enum):
    TYPE_A = 1
    TYPE_B = 2
    TYPE_C = 3


class Currency(Enum):
    USD = 1
    EUR = 2
    GBP = 3


class DataTemplate:
    def __init__(self, row):
        self.cohort_month = row[1] if pd.notna(row[1]) and row[1] != 'nan' else None  # B
        self.cohort_year = row[2]  # C
        self.period_month = row[3]  # D
        self.period_year = row[4]  # E
        self.forecast_date = self.format_date(row[5])  # F
        self.business_type_id = BusinessType(row[6])  # G
        self.currency_id = Currency(row[7])  # H
        self.created_at = datetime.now()  # I
        self.modified_at = datetime.now()  # J
        self.value = row[8]  # K

    @staticmethod
    def format_date(date):
        date_str = str(date)
        date_formatted = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
        return date_formatted

    def to_dict(self):
        return {
            'cohort_month': self.cohort_month,
            'cohort_year': self.cohort_year,
            'period_month': self.period_month,
            'period_year': self.period_year,
            'forecast_date': self.forecast_date,
            'business_type_id': self.business_type_id,
            'currency_id': self.currency_id,
            'created_at': self.created_at,
            'modified_at': self.modified_at,
            'value': self.value
        }


data = pd.read_excel(input_file_path)

first_10_records = data.head(277258)

start_time = time.time()

with open(output_file_path, 'w') as output_file:
    for index, row in first_10_records.iterrows():
        template = DataTemplate(row)
        template_dict = template.to_dict()
        output_file.write(str(template_dict) + ',\n')

end_time = time.time()
execution_time = end_time - start_time

print("Templates saved to file:", output_file_path)
print(f"Execution time: {execution_time} seconds.")