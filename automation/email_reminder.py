import pandas as pd
from datetime import datetime

# Paths
INPUT_FILE = 'data/cleaned_retainer_data.csv'
OUTPUT_FILE = 'data/alert_summary.csv'

def send_reminders():
    print("📧 Checking for overdue/partial clients...")

    try:
        df = pd.read_csv(INPUT_FILE, parse_dates=['Next Due Date'])
    except FileNotFoundError:
        print(f"❌ File not found: {INPUT_FILE}")
        return

    today = pd.Timestamp(datetime.today().date())

    # Filter clients with overdue or partial payments
    alerts_df = df[
        df['Payment Status'].isin(['Overdue', 'Partial']) &
        (df['Next Due Date'] <= today)
    ]

    if alerts_df.empty:
        print("✅ No overdue or partial clients found.")
    else:
        for _, row in alerts_df.iterrows():
            print(f"\n🚨 ALERT: {row['Client Name']} ({row['Email']})")
            print(f" - Retainer: ${row['Retainer Amount']} | Paid: ${row['Paid Amount']}")
            print(f" - Status: {row['Payment Status']} | Due: {row['Next Due Date'].date()}")

        # Save alert summary
        alerts_df.to_csv(OUTPUT_FILE, index=False)
        print(f"\n✅ Alert summary saved to: {OUTPUT_FILE}")

if __name__ == "__main__":
    send_reminders()