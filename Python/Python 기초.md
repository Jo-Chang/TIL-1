# Python 기초

## Index📑
- [컴퓨터 프로그래밍 언어](#컴퓨터-프로그래밍-언어)
- [파이썬](#파이썬python)
- [객체와 변수](#객체와-변수)
- [자료형](#자료형data-type)
    - [컨테이너](#컨테이너container)
    - [시퀀스형 컨테이너](#시퀀스형-컨테이너sequence-container)
    - [문자열](#문자열)
    - [리스트](#리스트list)
    - [None](#none)
- [연산자](#연산자operator)

___

### **컴퓨터 프로그래밍 언어**

- 컴퓨터(Computer)

    계산을 하는 것
    Caculation(조작)
    Remember(저장)

    -> 컴퓨터는 조작하고 저장하는 것이다.

- 프로그래밍(Programming)

    명령어의 모음(집합)

- 언어

    - 자신의 **생각을 나타내고 전달하기** 위해 사용하는 체계
    - **문법적**으로 맞는 말의 집합

- 프로그래밍 언어란

    **컴퓨터에게 명령하기 위한 약속**


### **파이썬(Python)**

#### 파이썬(python) 이란?
- Easy to learn
    - 다른 프로그래밍 언어보다 문법이 간단
    - 문법 표현이 간결하여 짧은 시간 내에 마스터 가능

- Expressive Language
    - 같은 작업에 대하여 C나 자바로 작성할 때 보다 더 간결하게 작성 가능

- 크로스 플랫폼 언어
    - 다양한 운영체제에서 실행가능

#### 파이썬의 특징
- 인터프리터 언어(Interpreter)
    - 소스코드를 기계어로 변환하는 컴파일 과정 없이 바로 실행 가능
    - 코드를 대화하듯 한 줄 입력하고 실행 후 바로 확인 가능

- 객체 지향 프로그래밍(Object Oriented Programming)
    - 파이썬은 객체지향 언어이며, 모든 것이 객체로 구현되어 있음
    - 객체(Object): 숫자, 문자, 클래스 등 값을 갖고 있는 모든 것


### **객체와 변수**

- 컴퓨터는 조작하여 저장하는 것이다.
- 조작과 저장을 하는 과정에 있어서 객체지향 프로그래밍을 활용한다.
- 파이썬은 모두 '객체'로 구성되어 있다.

#### 객체(Object) -> 사물
- 물건을 어려운 말로 얘기했을 뿐이다.
- 파이썬에 담기는 모든 것들을 객체라 부른다.

#### 변수(Variable)
- 객체를 참조하기 위해 사용되는 이름
- 동일 이름에 다른 객체를 언제든 할당 가능 그래서 변수라 불린다.
- 변수는 할당 연산자(=)를 통해 값을 할당(assignment)받는다.
- type(): 변수에 할당된 값의 타입
- id(): 변수에 할당된 값(객체)의 고유한 아이덴티티(identity) 값, 메모리주소

##### 변수할당
- 같은 값을 동시에 할당할 수있음
    ```python
    x = y = 1004
    ```

- 다른 값을 동시에 할당 할 수 있음(multiple assignment)
    ```python
    x, y = 1, 2
    ```

##### 실습 문제
- x = 10, y = 20 일 때, 각각 값을 바꿔서 저장하는 코드를 작성하시오.
    ```python
    x, y = 10, 20
    ```

    방법 1) 임시 변수 활용
    ```python
    tmp = x
    x = y
    y = tmp
    print(x, y)
    ```

    방법 2) Pythonic!
    ```python
    y, x = x, y
    print(x, y)
    ```

#### 식별자(Identifiers)
- 파이썬 객체(변수, 함수, 모듈, 클래스 등)를 식별하는데 사용하는 이름(name)
- 규칙
    - 이름은 영문 알파벳, 언더스코어(_), 숫자로 구성
    - 첫 글자에 숫자 X
    - 길이제한 X, 대소문자 구별
    - 예약어는 사용불가
    
        ```
        Flase, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield
        ```
    
    - 내장함수나 모듈 등의 이름으로도 만들면 안됨
        - 기존 이름에 다른 값을 할당하게 되므로 더 이상 동작하지 않음


### **자료형(Data Type)**

**자료형이란**

객체(Object)의 종류 Type

**자료형 분류**
- 숫자
    - 수치형(Numeric Type)
        - int(정수, integer)
        - float(부동소수점, 실수, floating point number)
        - complex(복소수, complex number)
    - 불린형(Boolean Type)

- 시퀀스(Sequence)
    - 문자열(String)
    - 튜플(Tuple)
    - 리스트(List)
    - 레인지(Range)

- 컬렉션(Collection)
    - 집합(Set)
    - 딕셔너리(Dictionary)

- None

#### **컨테이너(Container)**
**컨테이너(Container) 정의**

- 컨테이너란?
    - 여러 개의 값을 담을 수있는 것(객체)
- 컨테이너의 분류
    - 순서가 있는 데이터(Ordered) vs. 순서가 없는 데이터(Unordered)
    - 순서가 있다 != 정렬되어 있다.

**컨테이너 분류**

- 시퀀스
    - 문자열(immutable): 문자들의 나열
    - 리스트(mutable): 변경 가능한 값들의 나열
    - 튜플(immutable): 변경 불가능한 값들의 나열
    - 레인지(immutable): 숫자의 나열

- 컬렉션 / 비시퀀스
    - 세트(mutable): 유일한 값들의 모음
    - 딕셔너리(mutable): 키-값들의 모음

#### **시퀀스형 컨테이너(Sequence Container)**

- 시퀀스형 주요 공통 연산자
    
    | 연산 | 결과 |
    | ---- | ---- |
    | s[i] | s의 i번쨰 항목, 0에서 시작합니다 |
    | s[i:j] | s의 i에서 j까지의 슬라이스 |
    | s[i:j:k] | s의 i에서 j까지 스텝 k의 슬라이스 |
    | s + t | s와 t의 이어 붙이기 |
    | s * n 또는 n * s | s를 그 자신에 n번 더하는 것 |
    | x in s | s의 항목 중 하나가 x와 같으면 True, 그렇지 않으면 False |
    | x not in s | s의 항목 중 하나가 x와 같으면 False, 그렇지 않으면 True |
    | len(s) | s의 길이 |
    | min(s) | s의 가장 작은 항목 |
    | max(s) | s의 가장 큰 항목 |

#### **문자열**

**문자열(String type)**
- 모든 문자는 str 타입
- 문자열은 작은 따옴표(')나 큰 따옴표(")를 활용하여 표기
    - 문자열을 묶을 때 동일한 문장부호 활용

**중첩따옴표(Nested Quotes)**
- 따옴표 안에 따옴표를 표현할 경우
    - 작은 따옴표가 들어 있는 경우 큰 따옴표로 문자열 생성
    - 큰 따옴표가 들어 있는 경우 작은 따옴표로 문자열 생성

**삼중따옴표(Triple Quotes)**
- 작은 따옴표나 큰 따옴표를 삼중으로 사용
    - 따옴표 안에 따옴표를 넣을 때,
    - 여러줄을 나눠 입력할 때 편리

**인덱싱(Indexing)**
- 인덱스를 통해 특정 값에 접근 가능
- s[1] => 'b'

**슬라이싱(Slicing)**
- 예제

    s[] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

    s[2:5] => 'cde'
    
    s[2:5:2] => 'ce'

**기타**
- 결합(Concatenation)
    ```python
    'hello, ' + 'python!'
    # 'hello, python!'
    ```
- 반복(Repetition)
    ```python
    'hi!' * 3
    # 'hi!hi!hi!'
    ```
- 포함(Membership)
    ```python
    'a' in 'apple'
    # True
    'app' in 'apple'
    # True
    'b' in 'apple'
    # False
    ```

**Escape sequence**
- 문자열 내에서 특정 문자나 조작을 위해서 역슬래시(\\)를 활용하여 구분

    | 예약문자 | 내용(의미) |
    | -------- | --------- |
    | \n | 줄 바꿈 |
    | \t | 탭 |
    | \r | 캐리지리턴 |
    | \O | 널 |
    | \\\ | \ |
    | \' | 단일인용부호(') |
    | \" | 이중인용부호(") |

**문자열 특징**
- Immutable: 변경 불가능
- Iterable: 반복 가능

#### 리스트(List)

**리스트(List) 정의**
- 변경 가능한 값들의 나열된 자료형
- 순서를 가지며, 서로 다른 타입의 요소를 가질 수있음
- 변경 가능하며(mutable), 반복 가능함(iterable)
- 항상 대괄호 형태로 정의, 요소는 콤마로 구분

**생성과 접근**
- 대괄호([]) 혹은 list()를 통해 생성
- 순서가 있는 시퀀스로 인덱스를 통해 접근
    ```python
    # 생성
    my_list = []
    another_list = list()
    type(my_list)
    # <class 'list'>
    type(another_list)
    # <class 'list'>
    ```

**리스트 접근과 변경**
```python
# 접근
a = [1, 2, 3]
print(a[0])
# 1

# 값 변경
a[0] = '1'
print(a)
# ['1', 2, 3]
```

**리스트 값 추가 / 삭제**
- 값 추가는 .append()를 활용 추가하고자 하는 값 전달
    ```python
    numbers = [2, 4, 6, 8]
    numbers.append(10)
    numbers
    # => [2, 4, 6, 8, 10]
    ```
- 값 삭제는 .pop()를 활용 삭제하고자 하는 인덱스 전달
    ```python
    numbers = [2, 4, 6, 8]
    numbers.pop(0)
    numbers
    # => [4, 6, 8]
    ```

#### None
- 파이썬 자료형 중 하나
- 파이썬에서는 값이 없음을 표현하기 위해 None 타입 존재
- 일반적으로 반환 값이 없는 함수에서 사용

### **연산자(Operator)**

#### 산술 연산자(Arithmetic Operator)
- 기본적인 사칙연산 및 수식 계산
    
    | 연산자 | 내용 |
    | ----- | ---- |
    | + | 덧셈 |
    | - | 뺄셈 |
    | * | 곱셈 |
    | % | 나머지 |
    | / | 나눗셈 |
    | // | 몫 |
    | ** | 거듭제곱 |

#### 복합연산자(In-place Operator)
- 연산과 할당이 함께 이뤄짐

    | 연산자 | 내용 |
    | ----- | ---- |
    | a += b | a = a + b |
    | a -= b | a = a - b |
    | a *= b | a = a * b |
    | a /= b | a = a / b |
    | a //= b | a = a // b |
    | a %= b | a = a % b |
    | a **= b | a = a ** b |

#### 비교 연산자(Comparison Operator)
- 값을 비교하며, True / False 값을 리턴함

    | 연산자 | 내용 |
    | ----- | ---- |
    | < | 미만 |
    | <= | 이하 |
    | > | 초과 |
    | >= | 이상 |
    | == | 같음 |
    | != | 같지않음 |

#### 논리 연산자(Logical Operator)
- 논리식을 판단하여 참(True)과 거짓(False)를 반환함

    | 연산자 | 내용 |
    | ----- | ---- |
    | A and B | A와 B 모두 True시, True |
    | A or B | A와 B 모두 False시, False |
    | Not | True를 False로, False를 True로 |

- and: 모두 참인 경우 참, 그렇지 않으면 거짓

    | and | 내용 |
    | --- | ---- |
    | True and Ture | True |
    | True and False | False |
    | False and True | False |
    | False and False | False |

- or: 둘 중 하나만 참이라도 참, 그렇지 않으면 거짓

    | or | 내용 |
    | -- | ---- |
    | True or True | True |
    | True or False | True |
    | False or True | True |
    | False or False | False |

- not: 참 거짓의 반대의 결과

    | not | 내용 |
    | --- | ---- |
    | not True | False |
    | not False | True |