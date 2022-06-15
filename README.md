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
