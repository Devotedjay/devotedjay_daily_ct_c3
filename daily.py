import requests
import datetime

WEBHOOK_URL = "https://discord.com/api/webhooks/1392061849813516369/9hfWDo5jghXYODrE2EL6czl9NmdiDC6zH-pA8II4tyJ-3lcMoGh9NkgpCFpt3y1Ncrj-"
TARGET_DATE = datetime.date(2026, 6, 1)
today = datetime.date.today()
delta = (TARGET_DATE - today).days

requests.post(WEBHOOK_URL, json={"content": f"📅 Còn {delta} ngày nữa đến ngày 01/06/2026!"})
