import pandas as pd
import os
def parse_bank_statement(filepath):
    """
    Reads a CSV bank statement and returns a cleaned DataFrame.
    filepath: path to the CSV file
    """
    # Check the file actually exists
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"No file found at: {filepath}")

    # Read the CSV into a DataFrame (think: a programmable spreadsheet)
    df = pd.read_csv(filepath)

    # Standardize column names: lowercase, strip spaces
    df.columns = df.columns.str.lower().str.strip()

    # Rename columns to our standard names
    column_map = {
        'date': 'date',
        'description': 'description',
        'amount': 'amount',
        'type': 'type'
    }
    df = df.rename(columns=column_map)

    # Drop any rows where critical fields are missing
    df = df.dropna(subset=['date', 'amount'])

    # Make sure amount is a number, not text
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce')

    # Convert date column to proper date format
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # Drop rows where conversion failed
    df = df.dropna(subset=['date', 'amount'])

    # Sort by date, oldest first
    df = df.sort_values('date').reset_index(drop=True)

    return df

# This block only runs if you execute parser.py directly
# It won't run when other files import it
if __name__ == "__main__":
    df = parse_bank_statement("../sample_data/sample_statement.csv")
    print("Statement loaded successfully!")
    print(f"Total transactions: {len(df)}")
    print("\nFirst 5 rows:")
    print(df.head())
    print("\nData types:")
    print(df.dtypes)