# ๐  ์์๋ด์ญ ๐ 

- [x] DB models.py ์์ (์ฑํ๋นผ๊ณ ์๋ฃ)
- [x] ์ด๋ฉ์ผ ์ธ์ฆ API
- [x] ํ์๊ฐ์ API
- [x] LOGIN (TEST ํ์)
- [ ] ํ๋ณด๊ธCRUD & ์ง์์์
- [x] ์ปค๋ฎค๋ํฐCRUD (TEST ํ์)
- [ ] ๋๊ธ
- [ ] ๋ง์ดํ์ด์ง(๋ด๊ฐ ์ด ๊ธ, ๋ด๊ฐ ์ด ๋๊ธ, ๋ด๊ฐ ์ง์ํ ๋์๋ฆฌ ํํฉ, ๊ด์ฌ๋ถ์ผ ์์ )
- [ ] ๋์๋ฆฌ ์ ์ฒญ ์น์ธ(ํ์ด์ง ์ด์ ๊ด๋ฆฌ์์๊ฒ)
- [ ] ๋์๋ฆฌ์ ์ ์ฒญ ์น์ธ
- [ ] ํค์๋ ๊ฒ์
- [ ] ๊ด์ฌ๋ถ์ผ ๊ฒ์
- [ ] ๋์๋ฆฌ ์ฑํ


## email ์ ์ก form ํ์

```html
<form action="http://localhost:8000/sendmail" method="POST">
  {% csrf_token %}
  <input type="text" name="username" />
  <input type="date" name="birth" />
  <input type="text" name="email" />
  <input type="submit" />
</form>
```

# ๋์๋ฆฌ ์ฑ DB ์ค๊ณ

## User

| ์ด๋ฆ          | ์๋ฃํ   | ์ต์             |
| ------------- | -------- | ---------------- |
| id            | INT      | AUTOINCREASE, PK |
| login_ID      | VARCHAR  | UNIQUE           |
| NickName      | VARCHAR  | UNIQUE           |
| PassWord      | VARCHAR  |                  |
| username      | VARCHAR  |                  |
| birth         | DATE     |
| ์ํ๋๋      | INT      |
| School        | VARCHAR  |
| Email         | VARCHAR  | UNIQUE           |
| ์ธ์ฆ          | BOOLEAN  |
| Admin         | BOOLEAN  |
| ์๋น์ค๊ฐ์์ผ  | DATETIME |
| ํ๋กํimg๊ฒฝ๋ก | VARCHAR  |

## UserInterest

| ์ด๋ฆ          | ์๋ฃํ  | ์ต์                       |
| ------------- | ------- | -------------------------- |
| id            | INT     | AUTOINCREASE, PK           |
| user_ID       | INT     | FK[user table(id)]:CASCADE |
| ๋ฌธํ,์์      | BOOLEAN |
| ๋ด์ฌ/์ฌํํ๋ | BOOLEAN |
| ํ์ /๊ต์     | BOOLEAN |
| ์ฐฝ์/์ทจ์     | BOOLEAN |
| ์ดํ          | BOOLEAN |
| ์ฒด์ก          | BOOLEAN |
| ์ฝ๋ฉ          | BOOLEAN |
| ์คํฐ๋        | BOOLEAN |

## Circle

| ์ด๋ฆ   | ์๋ฃํ   | ์ต์             |
| ------ | -------- | ---------------- |
| id     | INT      | AUTOINCREASE, PK |
| Name   | VARCHAR  | UNIQUE           |
| ๊ฐ์ค์ผ | DATETIME |
| ์๊ฐ   | VARCHAR  |
| ์ฃผ์    | VARCHAR  |

## CircleMember

| ์ด๋ฆ         | ์๋ฃํ   | ์ต์                                                      |
| ------------ | -------- | --------------------------------------------------------- |
| id           | INT      | AUTOINCREASE, PK                                          |
| ๋์๋ฆฌ\_ID   | INT      | FK[๋์๋ฆฌ Table(id)]:CASCADE                              |
| User_ID      | INT      | FK[๋์๋ฆฌ Table(id)]:CASCADE                              |
| ์ญ์ง         | INT      | 0(default): ๊ฐ์๋๊ธฐ, 1: ์ผ๋ฐ๋์๋ฆฌ์, 2: ๋ถํ์ฅ, 3: ํ์ฅ |
| ๋์๋ฆฌ๊ฐ์์ผ | DATETIME |

## PromotionPost

| ์ด๋ฆ          | ์๋ฃํ   | ์ต์                         |
| ------------- | -------- | ---------------------------- |
| id            | INT      | AUTOINCREASE, PK             |
| title         | VARCHAR  |
| ๋ชจ์ง๊ธฐ๊ฐStart | DATETIME |
| ๋ชจ์ง๊ธฐ๊ฐEND   | DATETIME |
| ๋ชจ์ง์ธ์      | INT      |
| ํค์๋\_ID    | INT      | FK[ํค์๋ Table(id)]         |
| ์์ธ๋ด์ฉ      | VARCHAR  |
| ์ด๋ฏธ์ง        | VARCHAR  |
| ๋์๋ฆฌ\_ID    | INT      | FK[๋์๋ฆฌ Table(id)]:CASCADE |
| user_ID       | INT      | FK[User Table(id)]:CASCADE   |
| ์์ฑ์ผ        | DATETIME |
| ์กฐํ์        | INT      |

## ApplyForm

| ์ด๋ฆ       | ์๋ฃํ  | ์ต์                         |
| ---------- | ------- | ---------------------------- |
| id         | INT     | AUTOINCREASE, PK             |
| ํ๋ณด๊ธ\_ID | INT     | FK[ํ๋ณด๊ธ Table(id)]:CASCADE |
| ์ง๋ฌธ       | VARCHAR |
| ์์์ ์ฅ   | BOOLEAN |

## Cummunity

| ์ด๋ฆ       | ์๋ฃํ   | ์ต์                       |
| ---------- | -------- | -------------------------- |
| id         | INT      | AUTOINCREASE, PK           |
| title      | VARCHAR  |
| ํค์๋\_ID | INT      | FK[ํค์๋ Table(id)]       |
| ์์ธ๋ด์ฉ   | VARCHAR  |
| ์ด๋ฏธ์ง     | IMAGE  |
| user_ID    | INT      | FK[User Table(id)]:CASCADE |
| ์์ฑ์ผ     | DATETIME |
| ์กฐํ์     | INT      |

# ์ถํ์์ฑ

## ~~CircleChat~~

| ์ด๋ฆ       | ์๋ฃํ  | ์ต์                         |
| ---------- | ------- | ---------------------------- |
| id         | INT     | AUTOINCREASE, PK             |
| ํ๋ณด๊ธ\_ID | INT     | FK[ํ๋ณด๊ธ Table(id)]:CASCADE |
| ์ง๋ฌธ       | VARCHAR |
| ์์์ ์ฅ   | BOOLEAN |


# 9th_heroku
