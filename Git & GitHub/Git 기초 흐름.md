# Git 기초 흐름

## Index📑
- [Git](#git)
- [분산버전관리시스템(DVCS)](#분산버전관리시스템dvcs)
- [Git의 버전 관리](#git의-버전-관리)
- [저장소 생성(초기화)](#저장소-생성초기화)
- [Git 버전 관리 기초 흐름](#git-버전-관리-기초-흐름)
- [기본 명령어](#기본-명령어)
- [Git 필수 설정 정보](#git-필수-설정-정보)
- [Git config의 이해](#git-config의-이해)


___


### **Git**

- Git은 분산버전관리시스템으로 코드의 버전을 관리하는 도구
- 2005년 리눅스 커널을 위한 도구로 리누스 토르발스가 개발
- 컴퓨터 파일의 변경사항을 추적하고 여러 명의 사용자들 간에 파일들의 작업을 조율


### **분산버전관리시스템(DVCS)**

- 중앙집중식버전관리시스템
  - 로컬에서는 파일을 편집하고 서버에 반영
  - 중앙 서버에서만 버전을 관리
- 분산버전관리시스템 -> Git
  - 로컬에서도 버전을 기록하고 관리
  - 원격 저장소를 활용하여 협업


### **Git의 버전 관리**

- Git은 데이터를 파일 시스템의 스냅샷으로 관리하고 매우 크기가 작음
- 파일이 달라지지 않으면 성능을 위해 파일을 새로 저장하지 않음
- 기존의 델타 기반 버전 관리시스템과 가장 큰 차이를 가짐


### **저장소 생성(초기화)**

- git init
  - 특정 폴더에 git 저장소를 만들고 버전 관리
    - .git 폴더가 생성됨
    - git bash에서는 (master)라는 표기를 확인할 수 있음

  ```bash
  $ git init
  Initialized empty Git repository in ~/OneDrive/바탕 화면/TIL/.git/
  ```


### **Git 버전 관리 기초 흐름**

1. 작업을 하고
2. 변경된 파일을 모아 (add)
3. 버전으로 남긴다. (commit)

- Git은 파일을 modified, staged, committed로 관리
  - modified: 파일이 수정된 상태(add 명령어를 통해 staging area로)
  - staged: 수정한 파일을 곧 커밋할 것이라고 표시한 상태(commit 명령어로 저장소)
  - committed: 커밋이 된 상태

- Working Directory: 파일의 변경사항 -> 1통
- Staging Area: 버전으로 기록하기 위한 파일 변경사항의 목록 -> 2통
- Reository: 커밋(버전)들이 기록되는 곳 -> 3통


### **기본 명령어**

- git add 파일명
  - Working directory상의 변경 내용을 Staging area에 추가하기 위해 사용
    - untracked 상태의 파일을 staged로 변경
    - modified 상태의 파일을 staged로 변경

```bash
$ git add .
```

```bash
$ git status
On branch master

No commits yet

Changes to be committed: # 커밋될 변경사항들 (2통)
  (use "git rm --cached <file>..." to unstage)
        new file:   README.md # 생성
```

- git commit -m 'message'
  - -m: message option
  - staged 상태의 파일들을 커밋을 통해 버전으로 기록
  - SHA-1 해시를 사용하여 40자 길이의 체크섬을 생성하여 고유한 커밋을 표기
  - 커밋 메시지는 변경 사항을 나타낼 수 있도록 명확히 작성해야 함

```bash
$ git commit -m 'first commit'
[master (root-commit) b561c19] first commit
  1 file changed, 7 insertions(+)
  create mode 100644 README.md
```

```bash
$ git status
On branch master
nothing to commit, working tree clean
```

```bash
$ git log
commit b561c19c1b9414aa8c15f2a6e4791bde845fa3ce (HEAD -> master)
Author: kimsuminn <suminkim0618@gmail.com>
Date:   Wed Dec 28 10:15:07 2022 +0900

    first commit

$ git log --oneline
b561c19 (HEAD -> master) first commit
```

- git log : commit history 조회
  - 현재 저장소에 기록된 커밋을 조회
  - 다양한 옵션을 통해 로그를 조회할 수 있음
    - git log -1 : 최근 1개
    - git log --oneline : 한줄로
    - git log -2 --oneline : 최근 2개를 한줄로

- git satus
  - Git 저장소에 있는 파일의 상태를 확인하기 위해 활용
    - 파일의 상태를 알 수 있음
      - untracted files
        - file을 만들었지만 add를 하지 않음
        - 트래킹되지 않은 파일들
      - Changes to be committed
        - file을 만들고 add함
        - 커밋될 변경사항들
      - Changes not staged for commit
        - 커밋된 적 있는 file을 수정한 상태
        - 커밋을 위한 staged에 없는 변경사항
    - nothing to commit, working tree clean
      - 커밋할게 없고, 작업트리가 깨끗합니다
      - 모두 add, commit한 이후
  - Status로 확인할 수 있는 파일 상태
      - Tracked : 이전부터 버전으로 관리되고 있는 파일
        - Unmodified: git status에 나타나지 않음
        - Modified: Changes not staged for commit
        - Staged: Changes to be committed
      - Untracked : 파일을 새로 만들었을 때


### **Git 필수 설정 정보**

- 사용자 정보 (commit author): 커밋을 하기 위해 반드시 필요
  - git config --global user.name "*username*"
    - *Github*에서 설정한 *username*으로 설정
  - git config --global user.email "*my@email.com*"
    - *Github*에서 설정한 *email*로 설정
- 설정 확인
  - git config -l
  - git config --global -l
  - git config user.name


### **Git config의 이해**

- --system
  - /etc/gitconfig
  - 시스템의 모든 사용자와 모든 저장소에 적용(관리자 권한)
- --global
  - ~/.gitconfig
  - 현재 사용자에게 적용되는 설정
- --local
  - .git/config
  - 특정 저장소에만 적용되는 설정