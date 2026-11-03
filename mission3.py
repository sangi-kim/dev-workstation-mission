import requests
import json

def fetch_data():
    # 1. 무료 테스트용 API 서버에서 데이터 가져오기 (할 일 목록)
    url = "https://jsonplaceholder.typicode.com/todos/1"
    
    try:
        response = requests.get(url)
        response.raise_for_status() # 에러 발생 시 예외 처리
        
        # 2. JSON 데이터 파싱
        data = response.json()
        
        print("✅ 데이터 수집 성공!")
        print(f"내용: {data}")

        # 3. 수집한 데이터를 파일로 저장 (result.json)
        with open("result.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        
        print("💾 결과가 'result.json' 파일에 저장되었습니다.")

    except Exception as e:
        print(f"❌ 오류 발생: {e}")

if __name__ == "__main__":
    fetch_data()