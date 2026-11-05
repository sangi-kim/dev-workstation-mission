import json
import ssl
from pathlib import Path

try:
    import requests
except ModuleNotFoundError:  # pragma: no cover - fallback for environments without requests
    requests = None

from urllib import request as urllib_request


def _fetch_json(url: str):
    if requests is not None:
        response = requests.get(url, timeout=10, verify=False)
        response.raise_for_status()
        return response.json()

    req = urllib_request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    context = ssl._create_unverified_context()
    with urllib_request.urlopen(req, timeout=10, context=context) as response:
        return json.loads(response.read().decode("utf-8"))


def fetch_data():
    # 1. 무료 테스트용 API 서버에서 데이터 가져오기 (할 일 목록)
    url = "https://jsonplaceholder.typicode.com/todos/1"

    try:
        data = _fetch_json(url)

        print("SUCCESS: data collection succeeded!")
        print(f"Content: {data}")

        # 3. 수집한 데이터를 파일로 저장 (result.json)
        output_path = Path(__file__).resolve().parent / "result.json"
        with output_path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        print("Saved the result to 'result.json'.")

    except Exception as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    fetch_data()