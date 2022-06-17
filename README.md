## 1. args, kwargs를 사용하는 예제 코드 짜보기

```
def prac(*args, **kwargs):
    print(args)
    print(kwargs)
    return True


sample_list = [1, 2, 3, 4, 5]
sample_dict = {
    "이름1": "김태인",
    "이름2": "황영상",
    "이름3": "김희정",
    "이름4": "이민기",
}

prac(*sample_list, **sample_dict)
```

## 2. mutable과 immutable은 어떤 특성이 있고, 어떤 자료형이 어디에 해당하는지 서술하기

- 스트링은 immutable에 속하며 immutable 객체는 값을 할당해줄때 value를 집어넣음
- 리스트는 mutable에 속하며 mutable 객체는 값을 할당해줄때 주소 값을 집어넣음
- mutable 또한 값을 할당할때 value로 넣고싶다면 deepcopy라이브러리, [:] 을 활용하면 됨

## 3. DB Field에서 사용되는 Key 종류와 특징 서술하기

- PK : Primary Key 약자이며 테이블에서 반드시 존재해야한다
  (단 PK는 한테이블당 두개 이상 존재할 수 없고, UK와 마찬가지로 중복 값을 허용하지 않는다)
  (Foreign key를 사용할 경우 참조 테이블의 PK를 바라보게 된다)
- UK : Unique Key의 약자이며 중복 값을 허용하지 않는다 (PK와 비슷하나 PK의 하위호환)
- FK : Foreign Key 약자이며 다른 테이블을 참조할때 사용함

## 4. django에서 queryset과 object는 어떻게 다른지 서술하기

- 쿼리셋(QuerySet) : 데이터베이스에서 전달받은 '객체 목록' (object의 집합)

- object : 데이터베이스를 하나의 '단일 객체' 덩어리로 봄

---

2일차 과제

### 1. Django 프로젝트를 생성하고, user 라는 앱을 만들어서 settings.py 에 등록해보세요.

#### 2. user/models.py에 `Custom user model`을 생성한 후 django에서 user table을 생성 한 모델로 사용할 수 있도록 설정해주세요

### 3. user/models.py에 사용자의 상세 정보를 저장할 수 있는 `UserProfile` 이라는 모델을 생성해주세요

### 4. blog라는 앱을 만든 후 settings.py에 등록해주세요

### 5. blog/models.py에 <카테고리 이름, 설명>이 들어갈 수 있는 `Category`라는 모델을 만들어보세요.

### 6. blog/models.py에 <글 작성자, 글 제목, 카테고리, 글 내용>이 들어갈 수 있는 `Article` 이라는 모델을 만들어보세요.(카테고리는 2개 이상 선택할 수 있어야 해요)

### 7. Article 모델에서 외래 키를 활용해서 작성자와 카테고리의 관계를 맺어주세요

### 8. admin.py에 만들었던 모델들을 추가해 사용자와 게시글을 자유롭게 생성, 수정 할 수 있도록 설정해주세요

### 9. CBV 기반으로 로그인 / 로구아웃 기능을 구현해주세요

### 10. CBV 기반으로 로그인 한 사용자의 게시글의 제목을 리턴해주는 기능을 구현해주세요

---

3일차 과제

### 1. blog 앱에 <게시글, 사용자, 내용>이 포함된 comment 테이블을 작성해주세요 (완)

### 2. 외래 키를 사용해서 Article, User 테이블과 관계를 맺어주세요 (완)

### 3. admin.py에 comment를 추가해 자유롭게 생성, 수정 할 수 있도록 해주세요

### 4. serializer를 활용해 로그인 한 사용자의 기본 정보와 상세 정보를 리턴해 주는 기능을 만들어주세요

### 5. 4번의 serializer에 추가로 로그인 한 사용자의 게시글, 댓글을 리턴해주는 기능을 구현해주세요

### 6. blog 앱에 title / category / contents를 입력받아서 게시글을 작성하는 기능을 구현해주세요

- 만약 title이 5자 이하라면 게시글을 작성할 수 없다고 리턴해주세요
- 만약 contents가 20자 이하라면 게시글을 작성할 수 없다고 리턴해주세요
- 만약 카테고리가 지정되지 않았다면 카테고리를 지정해야 한다고 리턴해주세요

6. custom permission class를 활용해 가입 후 3일 이상 지난 사용자만 게시글을 쓸 수 있도록 해주세요

- 테스트 할 때에는 가입 후 3분 이상 지난 사용자가 게시글을 쓸 수 있게 해주세요
- join_date는 datetime field로 만들어주세요
