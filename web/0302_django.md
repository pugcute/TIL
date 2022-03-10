# 0302 장고



## web framework



- 정적 페이지 : 서버에 미리 저장된 파일이 사용자에게 그대로 전달되는 웹 페이지

  요청 시 별도의 처리 과정 없음. **모든 상황에서 모든 사용자에게 동일한 정보를 표시**

- 동적 웹 페이지 : 서버는 추가적인 처리 과정 이후 응답. 사용자마다 다르며 데이터 베이스와 상호작용

- 프레임워크 : 응용 프로그램 표준 구조를 구현하는 클래스와 라이브러리 모임. 개발에 필요한 환경과 도구를 제공.(틀에 박힌 일-큰 흐름은 바꿀 수 없음)

- MVC 디자인 패턴 (파이썬은 MT(Templete)V(view) 패턴): UI로부터 프로그램 로직을 분리. 이면에서 실행되는 부분을 서로 영향 없이 쉽게 고칠 수 있게 하는 디자인 패턴

  - model 데이터 구조를 정의하고 데이터베이스 기록 관리 -> db 관리
  - template 파일의 구조나 레이아웃(view) -> html
  - view 요청 수신하고 응답 반환, 요청을 충족시키는 데 필요한 데이터 접근, 응답의 서식을 template에게 맡김 -> 중간관리자 -> 기본적으로 함수

- ```bash
  247  python -m venv venv # 가상환경 만들기
  248  source venv/Scripts/activate # 가상환경 작동
  249  django-admin startproject firstpjt . # 띄어쓰기 유의, 프로젝트 생성
  250  python manage.py runserver # 장고 서버 작동
  251  python manage.py startapp articles # 애플(articles)를 시작
  ```

  - `__init__py` 이 디렉토리를 하나의 패키지로 인식하게 함(조작 따로 하지 않음)

  - ` --asgi.py` 비동기식 웹 서버와 연결 및 소통하는 것 도움

  - `settings.py`  애플리케이션의 모든 설정

  - `urls.py` 사이트의 url과 view와 연결 지정, urlpatterns 리스트의 path 함수

    첫 번째 인자는 요청에 있는 문자열, 두 번째 인자는 문자열에 대응되는 반응, 요청 객체는 request라는 객체에 저장됨(필수 인자)

  - `wsgi.py` 다른 웹서버와 연결 및 소통 도움(배포)

  - `manage.py` 프로젝트와 상호작용 하는 커맨드라인 유틸리티

  - `admin.py` 관리자용 페이지 설정
  - `apps.py` 앱의 정보 작성(수정 x)
  - `models.py` 모델 정의
  - `tests.py` 테스트 코드 작성(수정 x)
  - `views.py` view 함수 정의

- projest는 application의 집합/ application은 실제 요청 처리하고 페이지를 보여주는 역함, 하나의 역할 및 기능 단위, 프로젝트에서 앱을 사용하기 위해서는 installed list에 등록해야 함

- 이는 firstpjt에 settings.py에 작성, 반드시 앱을 생성 후 등록해야 함.(등록하면 생성되지 않음), 등록 순서는 #local apps (직접 만든 앱)-> third party apps(외부에서 설치한 앱) -> django apps

- 가장 바깥 쪽 폴더가 프로젝트 이름(**프로젝트 폴더이자 루트)**/ 폴더는 기본적으로 기능 단위(basic_tv는 **마스터앱**)/manage,py(**집사이자 대리인**: 컨트롤러 아님)



## django template





- 데이터 표현하기 위한 것
- 템플릿에 관련된 문법이 따로 존재
- DTL 조건, 반복, 변수 치환, 필터 기능 제공/PYTHON 코드로 실행되는 것이 아닌 프레젠테이션 표현하는 것
- Variable `{{}}`render() 사용, views.py에 정의한 변수를 template 파일로 넘겨 사용
- 탬플릿 참조 순서는 한 곳에 탬플릿들을 모음(모든 앱의 탬플릿), 모아놓은 곳(통합 시스템)에서 찾음/ 이후 settings.py에 적힌 순서대로 
- 해결 방법은 각각의 탬플릿들을 각각의 다른 폴더 안으로 보냄/ 'a/home.html'와 'b/home.html' / 폴더 이름은 앱 이름으로
- 