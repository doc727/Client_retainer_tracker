import pandas as pd
from datetime import datetime

INPUT_FILE = 'data/cleaned_retainer_data.csv'
OUTPUT_FILE = 'data/updated_retainer_data.csv'

def update_status():
    print("🔄 Updating payment and contract status...")

    try:
        df = pd.read_csv(INPUT_FILE, parse_dates=['Next Due Date'])
    except FileNotFoundError:
        print(f"❌ File not found: {INPUT_FILE}")
        return

    today = pd.Timestamp(datetime.today().date())

    def get_payment_status(row):
        if row['Paid Amount'] == row['Retainer Amount']:
            return 'Paid'
        elif row['Paid Amount'] == 0 and row['Next Due Date'] < today:
            return 'Overdue'
        else:
            return 'Partial'

    def get_contract_status(row):
        return 'Active' if row['Next Due Date'] >= today else 'Ended'

    df['Payment Status'] = df.apply(get_payment_status, axis=1)
    df['Contract Status'] = df.apply(get_contract_status, axis=1)

    df.to_csv(OUTPUT_FILE, index=False)
    print(f"✅ Statuses updated and saved to: {OUTPUT_FILE}")

if __name__ == "__main__":
    update_status()