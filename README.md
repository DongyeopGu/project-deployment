# Final Project

> TMDB API를 활용해 사용자에게 영화정보를 제공.
>
> 사용자는 간단한 영화 리뷰와 평점을 남길 수 있고, 자유게시판을 사용하여 DB에 없는 영화를 신청 할 수 있음.
>
> 간단한 추천 알고리즘을 통해 사용자에게 영화를 추천
>
> 관리자는 유저 정보를 삭제 및 권한 수정이 가능하고 필요한 영화와 배우를 검색해 DB저장이 가능

#### 개발 환경

- Python
  - Python 3.7.6
  - Django 2.1.15
- vue
  - vue cli3
  - vue router
- Ubuntu 20.04 LTS server(배포환경)
  - gunicorn 20.0.4
  - nginx 1.17.10 (ubuntu)
  - docker 19.03.8



#### 1. 팀원 및 업무 분담

- 구동엽 / 정용우
- 시작만 영화 / 게시글 부분으로 업무를 분담
- 그 후, 전체적으로 필요한 부분이 생기면 같은 기능도 분담하여 진행
- 전체적인 분담 내용은 lab.ssafy에서 확인 가능



#### 2. 목표 서비스 구현 및 실제 구현 정도

- 매일 업데이트되는 영화를 메인 화면에 띄워 유저에게 제공

  - TMDB의 top_rate 정보를 활용하여 20개중 상위 5개만 제공
  - 새로고침시 API요청을 계속 보내는 것을 막고자 session 활용(쿠키에는 정보를 다 저장하기 어렵기 때문) - 더 좋은 방법 찾는 중

- 많은 사람이 사용하는 넷플릭스와 왓챠를 참고하여 영화 목록을 슬라이드 하여 확인 가능하고 전체 목록은 무한 스크롤이 가능함

  - vue-infinite-loader와 vue-swiper를 활용
  - 혼용을 불가능하다고 판단하여 적은 정보를 가져올 때는 swiper를 사용, 많은 정보는 infinite loader 활용

- Django Admin 페이지를 활용하면 유저 관리, 게시글 관리, DB관리가 가능하지만 좀 더 나은 UI를 제공하기 위해 관리자 페이지 따로 제작

  - 영화 제목 / 출연 배우로 영화 검색을 가능하게 하여 원하는 영화를 DB 저장

    - 복수 선택하여 DB에 저장하려 했지만 시간 부족으로 인해 한번에 하나씩 가능

    - 이런 이유로 사용자가 찾는 영화가 DB에 없을 때 요청 게시글을 작성하면 관리자가 확인 후 등록

  - 유저 정보를 선택 후 스태프 권한을 줄 수 있고, 유저를 삭제할 수 있음

    - 스태프 권한은 게시글 삭제, 수정과 리뷰 삭제, 수정 가능

  - 게시글 목록을 통해 바로 삭제 가능

- 영화 세부 정보 페이지에서 YOUTUBE 트레일러 영상 확인 가능



#### 3. 데이터베이스 모델링(ERD)

![DB ERD](DB ERD.jpg)



#### 4. 필수기능

1. 관리자 뷰
   - 영화 DB 관리, 유저 권한 관리, 유저 삭제, 게시글 삭제
2. 영화 정보
   - 평점, 장르, 줄거리, 트레일러
3. 추천 알고리즘
   - 좋아요 누른 영화를 기반으로 추천
4. 커뮤니티
   - 페이지 이동 가능, 스태프권한 삭제 수정 가능

#### 5. 배포 서버 URL

- [여기](http://dongyeop.tk) 

#### 6. 기타(느낀점)

- 기초적인 작업에선 문제 가 없었고 기능을 붙일 때 고려해야 할 부분이 많이 생겨 어려움이 있었음
- AWS를 이용하지 않고 안쓰던 개인 노트북을 서버로 사용해 배포하고 싶어 ubuntu server 설치했고, 어려움이 많았음
- 쉽게 배포하기 위해선 서버 관련 지식의 공부가 많이 필요하다는 것을 느낌



- Vue와 Django를 처음으로 같이 연계하여 프로젝트를 진행하였다. 

  - 흐름에 익숙치 않아 프론트엔드 / 백엔드로 나누지 않고 기능 별로 구현 후 합치는 방식으로 진행하였다
  - 백엔드와 프론트엔드가 구성되는 방식을 알게되었고, 전체적인 코드와 프로젝트의 진행이 어떻게 되는지 구체적으로 이해 할 수 있었다
  - 필수기능 구현 이후 여러 기능을 추가하였는데, 이런 방식으로 진행되다보니 기능 별 코드를 구조화, 변수 및 메소드 명을 체계화하는데 있어 다소 난잡해진 경향이 있었다. 
  - 시작 단계에서 프로젝트의 목표와 기능을 정하고 구조화 하는 것이 중요하다는 것을 실감 할 수 있었다.

  

#### 7. 배포시 어려움 발생한 부분들

- Django를 API로 서버로 사용하기 위해 gunicorn과 uswgi, nginx를사용해 Docker compose를 이용하는데 문제가 크게 없었지만 Vue에서 axios 요청 보낼 때 localhost로 보내는 문제가 컸음

- vue.config.js의 proxy를 사용해 원하는 주소로 요청을 보내려고 했지만 계속해서 문제가 발생함(vue.config.js가 작동하지 않았던 문제였음)

- 오류 발생 부분을 보니 docker build로 이미지를 만들기만 했기에 생긴 문제였음

- vue도 docker compose로 build시키니 요청이 아주 잘 갔음

- nginx.conf, vue.config.js의 proxy 이해하는데 오래걸림

- 이제 docker container, swarm, network 등 다양한 부분을 봐야함

  
