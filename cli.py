import argparse
import os

def run_clean():
    os.system('python automation/clean_data.py')

def run_reminder():
    os.system('python automation/email_reminder.py')

def run_status_update():
    os.system('python automation/update_status.py')

parser = argparse.ArgumentParser(description="Client Retainer Tracker CLI")
parser.add_argument('task', choices=['clean', 'reminder', 'update'], help='Task to perform')

args = parser.parse_args()

if args.task == 'clean':
    run_clean()
elif args.task == 'reminder':
    run_reminder()
elif args.task == 'update':
    run_status_update()