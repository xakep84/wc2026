import json
import requests
import os
from datetime import datetime, timezone

API_KEY = os.environ.get("FOOTBALL_DATA_KEY")
API_URL = "https://api.football-data.org/v4"
HEADERS = {"X-Auth-Token": API_KEY}

def main():
    print("Запрос матчей ЧМ 2026...")
    try:
        resp = requests.get(
            f"{API_URL}/competitions/WC/matches",
            headers=HEADERS,
            params={"season": 2026},
            timeout=30
        )
        if resp.status_code == 200:
            data = resp.json()
            matches = data.get("matches", [])
            print(f"Получено матчей: {len(matches)}")
            output = {"updatedAt": datetime.now(timezone.utc).isoformat(), "matches": matches}
        else:
            print(f"Ошибка API: {resp.status_code}")
            output = {"updatedAt": datetime.now(timezone.utc).isoformat(), "matches": []}
    except Exception as e:
        print(f"Ошибка: {e}")
        output = {"updatedAt": datetime.now(timezone.utc).isoformat(), "matches": []}

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    print("data.json записан.")

if __name__ == "__main__":
    main()