import os
import requests
import datetime

WEBHOOK_URL = os.getenv("WEBHOOK_URL")
TARGET_DATE = datetime.date(2026, 6, 1)
today = datetime.date.today()
delta = (TARGET_DATE - today).days

message = f"📅 Còn {delta} ngày nữa đến ngày 01/06/2026!"
requests.post(WEBHOOK_URL, json={"content": message})
