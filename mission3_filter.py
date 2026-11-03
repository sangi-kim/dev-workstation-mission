import requests
import json

def fetch_and_filter():
    # 1. 전체 할 일 목록(200개) 가져오기
    url = "https://jsonplaceholder.typicode.com/todos"
    
    try:
        response = requests.get(url)
        todos = response.json() # 리스트 형태의 데이터
        
        # 2. 데이터 가공: 'completed'가 True인 항목만 추출 (List Comprehension)
        completed_tasks = [task for task in todos if task['completed'] == True]
        
        print(f"📊 전체 데이터 개수: {len(todos)}개")
        print(f"✅ 완료된 작업 개수: {len(completed_tasks)}개")

        # 3. 필터링된 결과만 저장
        result = {
            "total_count": len(todos),
            "completed_count": len(completed_tasks),
            "tasks": completed_tasks
        }

        with open("filtered_tasks.json", "w", encoding="utf-8") as f:
            json.dump(result, f, indent=4, ensure_ascii=False)
        
        print("💾 필터링된 결과가 'filtered_tasks.json'에 저장되었습니다.")

    except Exception as e:
        print(f"❌ 오류 발생: {e}")

if __name__ == "__main__":
    fetch_and_filter()