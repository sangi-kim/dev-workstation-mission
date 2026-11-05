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


def fetch_and_filter():
    # 1. 전체 할 일 목록(200개) 가져오기
    url = "https://jsonplaceholder.typicode.com/todos"

    try:
        todos = _fetch_json(url)

        # 2. 데이터 가공: 'completed'가 True인 항목만 추출 (List Comprehension)
        completed_tasks = [task for task in todos if task.get("completed") is True]

        print(f"Total items: {len(todos)}")
        print(f"Completed items: {len(completed_tasks)}")

        # 3. 필터링된 결과만 저장
        result = {
            "total_count": len(todos),
            "completed_count": len(completed_tasks),
            "tasks": completed_tasks,
        }

        output_path = Path(__file__).resolve().parent / "filtered_tasks.json"
        with output_path.open("w", encoding="utf-8") as f:
            json.dump(result, f, indent=4, ensure_ascii=False)

        print("Saved the filtered result to 'filtered_tasks.json'.")

    except Exception as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    fetch_and_filter()