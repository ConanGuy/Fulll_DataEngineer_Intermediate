from models import engine
import pandas as pd

CSV_FILE_PATH = 'files/retail_15_01_2022.csv'

def extract():
    # Load the CSV file into a DataFrame
    df = pd.read_csv(CSV_FILE_PATH)
    return df

def transform(df):
    # Rename the columns
    df = df.rename(columns={
        'description': 'name',
    })
    
    # Add transaction_date column
    transaction_date = CSV_FILE_PATH.replace('.csv', '').replace('retail_', '')
    transaction_day, transaction_month, transaction_year = transaction_date.split('_')
    df['transaction_date'] = f'{transaction_year}-{transaction_month}-{transaction_day}'
        
    return df

def load(df):
    # Save the DataFrame to the database
    df.to_sql('transactions', engine, if_exists='append', index=False)

if __name__ == '__main__':
    df = extract()
    df = transform(df)
    load(df)
    