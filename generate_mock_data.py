import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()
num_clients = 250
data = []

for _ in range(num_clients):
    name = fake.company()
    email = fake.company_email()
    start_date = fake.date_between(start_date='-2y', end_date='today')
    retainer_amount = random.choice([500, 1000, 1500, 2000, 2500])
    paid_amount = random.choice([0, retainer_amount, retainer_amount//2])
    
    payment_date = start_date + timedelta(days=random.randint(20, 90))
    next_due_date = payment_date + timedelta(days=30)
    
    if paid_amount == retainer_amount:
        payment_status = 'Paid'
    elif paid_amount == 0:
        payment_status = 'Overdue'
    else:
        payment_status = 'Partial'
        
    contract_status = 'Active' if next_due_date > datetime.today().date() else 'Ended'

    data.append({
        'Client Name': name,
        'Email': email,
        'Start Date': start_date,
        'Retainer Amount': retainer_amount,
        'Paid Amount': paid_amount,
        'Payment Date': payment_date,
        'Next Due Date': next_due_date,
        'Payment Status': payment_status,
        'Contract Status': contract_status
    })

df = pd.DataFrame(data)

# Save to Excel and CSV
df.to_excel('data/sample_retainer_data.xlsx', index=False)
df.to_csv('data/sample_retainer_data.csv', index=False)

print("✅ Data saved to 'data/sample_retainer_data.xlsx' and '.csv'")

