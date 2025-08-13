import sys
import time

def flash_indicator():
    """Flash visual indicator (I/O operation)"""
    print('\r* ', end='')
    sys.stdout.flush()
    time.sleep(1)
    print('\r *', end='\n')
    sys.stdout.flush()
    time.sleep(1)

def alert_issues(issues):
    """Alert about vital sign issues (I/O operation)"""
    if issues:
        for issue in issues:
            print(issue)  # Show first critical issue
        for _ in range(1):
            flash_indicator()