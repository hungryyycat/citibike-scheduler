import os
import requests
import json
import datetime
import pytz

# 設定紐約時區
ny_tz = pytz.timezone("America/New_York")
ny_time = datetime.datetime.now(ny_tz)

# 指定存放檔案的資料夾（注意：在 GitHub Actions 執行時，檔案系統是暫存的）
save_folder = "data2"

# 檢查資料夾是否存在，若不存在則建立它
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# 1. 呼叫 API 取得數據
gbfs_url = "https://gbfs.lyft.com/gbfs/2.3/bkn/en/station_status.json"
response = requests.get(gbfs_url)
data = response.json()

# 2. 加入時間戳記，使用紐約時間
data['fetched_at'] = ny_time.isoformat()

# 3. 生成檔案名稱（根據紐約時間）
filename = f"station_status_{ny_time.strftime('%Y%m%d_%H')}.json"
filepath = os.path.join(save_folder, filename)

# 4. 將數據寫入 JSON 檔案
with open(filepath, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("數據已儲存到檔案：", filepath)
