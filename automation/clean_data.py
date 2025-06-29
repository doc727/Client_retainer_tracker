import pandas as pd
import os

INPUT_FILE = 'data/sample_retainer_data.csv'
OUTPUT_FILE = 'data/cleaned_retainer_data.csv'

def clean_data():
    print("🔄 Cleaning data...")

    if not os.path.exists(INPUT_FILE):
        print(f"❌ File not found: {INPUT_FILE}")
        return

    # Load dataset
    df = pd.read_csv(INPUT_FILE)

    # Remove duplicate rows
    df.drop_duplicates(inplace=True)

    # Strip whitespace from column names
    df.columns = [col.strip() for col in df.columns]

    # Drop rows with all null values
    df.dropna(how='all', inplace=True)

    # Parse date columns (ignore errors)
    date_cols = ['Start Date', 'Payment Date', 'Next Due Date']
    for col in date_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')

    # Drop rows with invalid critical info
    df.dropna(subset=['Client Name', 'Retainer Amount', 'Payment Status'], inplace=True)

    # Save cleaned data
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"✅ Cleaned data saved to: {OUTPUT_FILE}")

if __name__ == "__main__":
    clean_data()