import requests
import json
import datetime
import os
from dotenv import load_dotenv
import sys

# .env ファイルの読み込み（なければ無視される）
load_dotenv()

# APIキーを環境変数から取得
api_key = os.getenv('GOOGLE_MAPS_API_KEY')
if not api_key:
    print('⛔ GOOGLE_MAPS_API_KEY が環境変数に設定されていません。')
    sys.exit(1)

# Google Maps Directions API endpoint
endpoint = 'https://maps.googleapis.com/maps/api/directions/json'

print("=== Google Maps ルート検索ツール ===")
print("入力を終了したい場合は 'q' と入力してください。\n")

while True:
    origin = input('出発地を入力: ').strip()
    if origin.lower() in ['q', 'exit']:
        print("終了します。")
        break

    destination = input('目的地を入力: ').strip()
    if destination.lower() in ['q', 'exit']:
        print("終了します。")
        break

    dep_time = input('出発時間を入力 (yyyy/mm/dd hh:mm): ').strip()
    if dep_time.lower() in ['q', 'exit']:
        print("終了します。")
        break

    # UNIX時間を算出
    try:
        dtime = datetime.datetime.strptime(dep_time, '%Y/%m/%d %H:%M')
        unix_time = int(dtime.timestamp())
    except ValueError:
        print('⛔ 日時の形式が正しくありません。例: 2025/07/06 14:30\n')
        continue

    # パラメータ設定
    params = {
        'language': 'ja',
        'origin': origin.replace(' ', '+'),
        'destination': destination.replace(' ', '+'),
        'departure_time': unix_time,
        'key': api_key
    }

    try:
        response = requests.get(endpoint, params=params, timeout=10)
        response.raise_for_status()
        directions = response.json()

        if directions.get('status') != 'OK':
            print(f"⛔ APIエラー: {directions.get('status')}\n")
            continue

        for route in directions.get('routes', []):
            for leg in route.get('legs', []):
                print('\n=====')
                print(f"距離: {leg['distance']['text']}")
                print(f"所要時間（交通状況考慮）: {leg['duration_in_traffic']['text']}")
                print('=====')
        print('')

    except requests.exceptions.RequestException as e:
        print(f'⛔ 通信エラー: {e}\n')
    except KeyError as e:
        print(f'⛔ 必要な情報がレスポンスに含まれていません: {e}\n')
