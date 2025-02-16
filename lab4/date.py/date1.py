from datetime import datetime, timedelta

now = datetime.now()
five_days_ago = now - timedelta(days=5)

print(f"today: {now.strftime('%Y-%m-%d')}")
print(f"5 days ago: {five_days_ago.strftime('%Y-%m-%d')}")
