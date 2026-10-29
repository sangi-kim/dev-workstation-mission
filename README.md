# 개발 워크스테이션 구축 미션

## 1. 프로젝트 개요
이 문서는 개발 환경 세팅 과제를 수행한 결과를 기록한 보고서입니다.
## 2. 터미널 명령어 실습

### 1) 현재위치 확인 (pwd)
터미널에서 현재 내가 위치한 폴더 경로를 확인했습니다.

```bash
PS C:\Users\User\dev-workstation-mission> pwd

Path                                 
----                                 
C:\Users\User\dev-workstation-mission

### 2) 폴더 생성 및 이동 (mkdir, ls, cd)

```bash
PS C:\Users\User\dev-workstation-mission> mkdir practice


    디렉터리: C:\Users\User\dev-wor
    kstation-mission


Mode                 LastWriteTime
----                 -------------
d-----      2026-10-29   오후 7:04
PS C:\Users\User\dev-workstation-mission> ls


    디렉터리: C:\Users\User\dev-wor
    kstation-mission


Mode                 LastWriteTime
----                 -------------
d-----      2026-10-29   오후 7:04
-a----      2026-10-29   오후 6:52


PS C:\Users\User\dev-workstation-mission> cd practice
PS C:\Users\User\dev-workstation-mission\practice> 

### 3) 파일 생성 및 읽기, 상위 폴더 이동 (echo, cat, cd ..)
터미널에서 텍스트 파일을 생성하고 내용을 확인한뒤, 다시 원래 폴더로 돌아왔습니다.

```bash
PS C:\Users\User\dev-workstation-mission> cd practice
PS C:\Users\User\dev-workstation-mission\practice> echo "hello Developer!" > hello.txt
PS C:\Users\User\dev-workstation-mission\practice> ls


    디렉터리: C:\Users\User\dev-wor
    kstation-mission\practice


Mode                 LastWriteTime
----                 -------------
-a----      2026-10-29   오후 7:15


PS C:\Users\User\dev-workstation-mission\practice> cat hello.txt
hello Developer!
PS C:\Users\User\dev-workstation-mission\practice> cd ..
PS C:\Users\User\dev-workstation-mission> 

## 2. Docker 설치
- WSL 설치 및 재부팅 완료
- Docker Desktop 설치 완료
- `docker run hello-world` 실행 성공!