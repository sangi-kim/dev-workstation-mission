import requests

print("--- 파이썬 환경 테스트 ---")
try:
    response = requests.get("https://www.google.com")
    print(f"구글 접속 상태: {response.status_code} (200이면 성공!)")
    print("파이썬 환경 구축이 완벽하게 완료되었습니다! 🎉")
except Exception as e:
    print(f"에러 발생: {e}")