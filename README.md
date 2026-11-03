# 미션 1: 개발 워크스테이션 구축

## 1) 실행 환경
- OS: Windows 11
- Shell: PowerShell
- Docker: Docker version 29.9.2, build a82e528
- Git: git version 2.56.0.windows.4

## 2) 수행 체크리스트
- [x] 터미널 기본 조작 및 폴더 구성
- [x] Docker 설치/점검
- [ ] hello-world 실행
- [ ] Dockerfile 빌드/실행
- [ ] 포트 매핑 접속(2회)
- [ ] 바인드 마운트 반영
- [ ] 볼륨 영속성
- [x] Git 설정 + VSCode GitHub 연동

## 3) 수행 로그(발췌)
```powershell
# 폴더 구조 생성
mkdir -p workspace/dev-workstation-mission/evidence
cd workspace/dev-workstation-mission

# 도구 버전 확인
git --version
# 결과:git version 2.56.0.windows.4

docker --version
# 결과:Docker version 29.9.2, build a82e528