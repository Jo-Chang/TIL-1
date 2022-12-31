# 마크다운 기반 문서 작성

### **마크다운 개요**

- 2004년 존 그루버가 만든 텍스트 기반의 가벼운 마크업 언어
- 최초 마크다운에 비해 확장된 문법(표, 주석 등)이 있지만, 본 자료에서는 Github에서 사용 가능한 문법(Github Flavored Markdown)을 기준으로 설명


### **마크다운 특징**

- 워드프로세서(한글/MS word)는 다양한 서식과 구조를 지원하지만, 다른 프로그램으로 호환에 제약이 되며, 워드프롯스 상의 기능을 활용해야 함
- 마크다운은 최소한의 문법으로 구성되어 있으며 순수 텍스트로 작성 가능
- 단순 텍스트 문법으로 내용을 작성하며, 다양한 환경에서 변환하여 보여짐


### **마크다운 문법**

- Heading : 문서의 제목이나 소제목
  - #의 개수에 따라 대응되는 수준(Heading level)이 있음
    - h1 ~ h6까지 표현 가능
  - 문서의 구조를 위해 작성되며 글자 크기를 조절하기 위해 사용되어서는 안됨

# Heading level 1
## Heading level 2
### Heading level 3
#### Heading level 4
##### Heading level 5
###### Heading level 6

```
# Heading level 1
## Heading level 2
### Heading level 3
#### Heading level 4
##### Heading level 5
###### Heading level 6
```

- List : 목록
  - 순서가 있는 리스트와 순서가 없는 리스트로 구성
  - Tab으로 하위 항목으로 구성할 수 있음
  
    Ordered List
    1. First item
    2. Second item
    3. Third item

    Unordered List
    - First item
      - ....
    - Second item
      - ....
    * Third item
      * ....
    * Fourth item
      * ....

- Fenced Code block : 코드 블록
  - 코드 블록은 backtick 기호 3개를 활용하여 작성 (``````)
  - 코드  블록에 특정 언어를 명시하면 Syntax Highlighting 적용 가능

    ```
    code
    ```

- Inline Code block : 코드 블록
  - 코드 블록은 backtick 기호 1개를 인라인에 활용하여 작성(``)
    
    `code`

- link : 링크
  - `[문자열](url)`을 통해 링크 작성 가능

    [Google](https://google.com)
    
    [Naver](https://naver.com)

- image : 이미지
  - `![문자열](url)`을 통해 이미지를 사용 가능
  - 특정 파일들 포함하여 연결 가능

- Blockquotes : 인용문
  - `>`으로 인용문을 작성
    > 인용

- Table : 테이블

    ```
    | Syntax | Description |
    | ------ | ----------- |
    | Header | Title |
    | Paragraph | Text |
    ```

    
    | Syntax | Description |
    | ------ | ----------- |
    | Header | Title |
    | Paragraph | Text |

- 텍스트 강조
  - 굵게(bold), 기울임(Italic)을 통해 특정 글자들을 강조
    ```
    ***Bold+Italic***
    **Bold**
    *Italic*
    ~~취소~~
    ```

    ***Bold+Italic***

    **Bold**

    *Italic*

    ~~취소~~

- 수평선
  - 3개 이상의 asterisks(***), dashes(---), or underscores(___)