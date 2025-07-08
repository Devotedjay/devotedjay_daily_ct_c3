import requests
import datetime

WEBHOOK_URL = "https://discord.com/api/webhooks/1392052960384778300/1TPnZkvq_KYytLoJLdcPV3fDIMXBLgRalQUCBTmyp6Q_022aiPDBheNQVVc79_xsfwku"
TARGET_DATE = datetime.date(2026, 6, 1)
today = datetime.date.today()
delta = (TARGET_DATE - today).days

requests.post(WEBHOOK_URL, json={"content": f"📅 Còn {delta} ngày nữa đến ngày 01/06/2026!"})
