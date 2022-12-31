# Branch & Merge

### **Branch**

- branch란
  - 독립적인 작업흐름을 만들고 관리
  - 각자 독립된 버전의 흐름을 만들 수있다
  - 무한대로 생성이 가능하다
- branch의 주요 명령어
    > Git branch를 위해 root-commit을 발생시키고 진행

    ```bash
    $ git init
    (master) $ touch README.md
    (master) $ git add .
    (master) $ git commit -m 'Init'
    ```
  1. 브랜치 생성

      `$ git branch {branch name}`
  
  2. 브랜치 이동
  
      `$ git checkout {branch name}`

  3. 브랜치 생성 및 이동
  
      `$ git checkout -b {branch name}`

  4. 브랜치 목록
  
      `$ git branch`

  5. 브랜치 삭제
  
      `$ git brach -d {branch name}`


### **Merge**

- 각 branch에서 작업 한 이후 합치기 위해 사용

    `$ git merge {branch name}`

- 병합을 할 때,
  - 동일한 파일을 수정한 경우 충돌이 발생
    - 반드시 직접 해당 파일을 확인하고 적절하게 수정
    - 수정한 후 commit
  - 다른 파일을 수정 한 경우
    - 충돌 없이 Merge commit이 완료됨
- master 상태에서 파생된 것만 합친다.
- 브랜치에서 또 브랜치로 나눠서 작업 가능한 대신 Merge를 하게되면 상위 브랜치로 합쳐짐