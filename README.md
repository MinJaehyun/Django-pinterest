# 🐍Pinterest
    - Python 의 대표 웹 프레임워크인 django를 통해 핀터레스트 특유의 카드형 레이아웃을 벤치마킹한 웹서비스를 만들었습니다.
    - 15일 이라는 짧은 기간 동안 기획, 디자인에 소요되는 시간을 단축시키고 화면 & 기능 구현과 리팩토링에 중점을 두기 위한 프로젝트입니다.
<br>

## 🐝프로젝트 기간 및 인원
    2021.07.23 ~ 2021.08.06. 
- [민재현](https://github.com/MinJaehyun/pinterest)

<br>

## 🌎배포 사이트 
- [weone.website](https://www.weone.website)

<br>

## ⚡️적용 기술
    Front-End : Html5, css, javascript, django-bootstrap4, 
    Back-End  : Python, Django web framework, mariadb, Nginx, Gunicorn,  
    Common    : POSTMAN, FileZilla, Git, Github, Docker, Portainer, AWS EC2, AWS Load Balancer, AWS Route53, AWS Elastic IP, 
<br><br>

# 💡구현 기능

## 👉Front-End
    # TODO: 작성하기
<br><br>


## 👉Back-End

### API Endpoint
![image](https://user-images.githubusercontent.com/43669992/128618868-e57e7efb-0aed-435d-b864-9316ed8d44e4.png)
<br><br>

### Accounts App 
    - 회원가입 
    - MyPage                 (paginate_by = 5)
    - 비밀번호 변경           (login_required, account_ownership_required)
    - 회원탈퇴               (login_required, account_ownership_required)
    - 로그인, 로그아웃

### Article App
    - 게시글 생성            (login_required)
    - 게시글 뷰
    - 게시글 변경            (article_ownership_required)
    - 게시글 삭제            (article_ownership_required)
    - 모든 게시글의 목록 뷰   (paginate_by = 5)

### Project App
    - 프로젝트 생성           (login_required ) 
    - 프로젝트 상세 뷰        (paginate_by = 25) 
    - 프로젝트 리스트 뷰      (paginate_by = 25)  

### Comment App
    - 댓글 생성
    - 댓글 삭제               (comment_ownership_required)
    
### Profile App
    - 프로필 생성
    - 프로필 변경             (profile_ownership_required)

### Subscribe App
    * 구독 기능 구현          (login_required)
    * 구독한 프로젝트의 모든 게시글을 보여주는 기능 구현 (login_required) (paginate_by = 5)

### Deploy
    - 개발 환경과 배포 환경을 분리하였습니다.

    - AWS EC2 에 Docker 를 설치했습니다.
    - Docker 안에는 django, nginx, gunicorn 을 컨테이너로 만들어 적용 했습니다.
    - Docker 는 GUI 프로그램인 Portainer 를 사용했습니다.
    - Docker Swarm 에 SECRET_KEY 사용하여 보안을 적용 했습니다.
    - docker-compose.yml 로 손쉽게 배포 적용 했습니다.

    - AWS Route53 설정하고 도메인 및 EC2 와 연결하여 도메인 이름을 설정하였습니다. 
    - AWS Load Balancer 사용하여 https 적용하여 보안을 높였습니다.
    - AWS Elastic IP 적용 하였습니다.  