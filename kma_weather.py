# kma_weather.py
import requests
from datetime import datetime

SERVICE_KEY = "여기에_마이페이지에서_복사한_키_입력"

url = ("http://apis.data.go.kr/1360000/"
       "VilageFcstInfoService_2.0/getUltraSrtNcst")

# 오늘 날짜와 시각 자동 계산
now       = datetime.now()
base_date = now.strftime("%Y%m%d")
base_time = now.strftime("%H00")

params = {
    "serviceKey": SERVICE_KEY,
    "pageNo":     1,
    "numOfRows":  10,
    "dataType":   "JSON",
    "base_date":  base_date,
    "base_time":  base_time,
    "nx":         60,   # 서울
    "ny":         127,
}

res = requests.get(url, params=params)
print(f"상태 코드: {res.status_code}")
