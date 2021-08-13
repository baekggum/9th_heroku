# 🛠 작업내역 🛠

- [x] DB models.py 작업 (채팅빼고완료)
- [x] 이메일 인증 API
- [x] 회원가입 API
- [x] LOGIN (TEST 필요)
- [ ] 홍보글CRUD & 지원양식
- [x] 커뮤니티CRUD (TEST 필요)
- [ ] 댓글
- [ ] 마이페이지(내가 쓴 글, 내가 쓴 댓글, 내가 지원한 동아리 현황, 관심분야 수정)
- [ ] 동아리 신청 승인(페이지 운영 관리자에게)
- [ ] 동아리원 신청 승인
- [ ] 키워드 검색
- [ ] 관심분야 검색
- [ ] 동아리 채팅


## email 전송 form 형식

```html
<form action="http://localhost:8000/sendmail" method="POST">
  {% csrf_token %}
  <input type="text" name="username" />
  <input type="date" name="birth" />
  <input type="text" name="email" />
  <input type="submit" />
</form>
```

# 동아리 앱 DB 설계

## User

| 이름          | 자료형   | 옵션             |
| ------------- | -------- | ---------------- |
| id            | INT      | AUTOINCREASE, PK |
| login_ID      | VARCHAR  | UNIQUE           |
| NickName      | VARCHAR  | UNIQUE           |
| PassWord      | VARCHAR  |                  |
| username      | VARCHAR  |                  |
| birth         | DATE     |
| 입학년도      | INT      |
| School        | VARCHAR  |
| Email         | VARCHAR  | UNIQUE           |
| 인증          | BOOLEAN  |
| Admin         | BOOLEAN  |
| 서비스가입일  | DATETIME |
| 프로필img경로 | VARCHAR  |

## UserInterest

| 이름          | 자료형  | 옵션                       |
| ------------- | ------- | -------------------------- |
| id            | INT     | AUTOINCREASE, PK           |
| user_ID       | INT     | FK[user table(id)]:CASCADE |
| 문화,예술     | BOOLEAN |
| 봉사/사회활동 | BOOLEAN |
| 학술/교양     | BOOLEAN |
| 창업/취업     | BOOLEAN |
| 어학          | BOOLEAN |
| 체육          | BOOLEAN |
| 코딩          | BOOLEAN |
| 스터디        | BOOLEAN |

## Circle

| 이름   | 자료형   | 옵션             |
| ------ | -------- | ---------------- |
| id     | INT      | AUTOINCREASE, PK |
| Name   | VARCHAR  | UNIQUE           |
| 개설일 | DATETIME |
| 소개   | VARCHAR  |
| 주제   | VARCHAR  |

## CircleMember

| 이름         | 자료형   | 옵션                                                      |
| ------------ | -------- | --------------------------------------------------------- |
| id           | INT      | AUTOINCREASE, PK                                          |
| 동아리\_ID   | INT      | FK[동아리 Table(id)]:CASCADE                              |
| User_ID      | INT      | FK[동아리 Table(id)]:CASCADE                              |
| 역직         | INT      | 0(default): 가입대기, 1: 일반동아리원, 2: 부회장, 3: 회장 |
| 동아리가입일 | DATETIME |

## PromotionPost

| 이름          | 자료형   | 옵션                         |
| ------------- | -------- | ---------------------------- |
| id            | INT      | AUTOINCREASE, PK             |
| title         | VARCHAR  |
| 모집기간Start | DATETIME |
| 모집기간END   | DATETIME |
| 모집인원      | INT      |
| 키워드\_ID    | INT      | FK[키워드 Table(id)]         |
| 상세내용      | VARCHAR  |
| 이미지        | VARCHAR  |
| 동아리\_ID    | INT      | FK[동아리 Table(id)]:CASCADE |
| user_ID       | INT      | FK[User Table(id)]:CASCADE   |
| 작성일        | DATETIME |
| 조회수        | INT      |

## ApplyForm

| 이름       | 자료형  | 옵션                         |
| ---------- | ------- | ---------------------------- |
| id         | INT     | AUTOINCREASE, PK             |
| 홍보글\_ID | INT     | FK[홍보글 Table(id)]:CASCADE |
| 질문       | VARCHAR |
| 임시저장   | BOOLEAN |

## Cummunity

| 이름       | 자료형   | 옵션                       |
| ---------- | -------- | -------------------------- |
| id         | INT      | AUTOINCREASE, PK           |
| title      | VARCHAR  |
| 키워드\_ID | INT      | FK[키워드 Table(id)]       |
| 상세내용   | VARCHAR  |
| 이미지     | IMAGE  |
| user_ID    | INT      | FK[User Table(id)]:CASCADE |
| 작성일     | DATETIME |
| 조회수     | INT      |

# 추후작성

## ~~CircleChat~~

| 이름       | 자료형  | 옵션                         |
| ---------- | ------- | ---------------------------- |
| id         | INT     | AUTOINCREASE, PK             |
| 홍보글\_ID | INT     | FK[홍보글 Table(id)]:CASCADE |
| 질문       | VARCHAR |
| 임시저장   | BOOLEAN |


# 9th_heroku
