# 1. 베이스 이미지 선택 (Nginx 최신버전)
FROM nginx:latest

# 2. 내가 만든 index.html을 컨테이너 안의 웹 서버 경로로 복사
# Nginx의 기본 웹 경로: /usr/share/nginx/html
COPY index.html /usr/share/nginx/html/index.html

# 3. 컨테이너가 사용할 포트 번호 명시 (안내용)
EXPOSE 80
