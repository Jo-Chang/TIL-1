# Git Flow

### **Git Flow**

- Git을 활용하여 협업하는 흐름
- branch를 활용하는 전략을 의미


### **GitHub Flow 기본 원칙**

1. master branch는 반드시 배포 가능한 상태여야 함
2. feature branch는 각 기능의 의도를 알 수 있도록 작성
3. Commit message는 매우 중요하며, 명확하게 작성
4. Pull Request를 통해 협업 진행
5. 변경사항을 반영하고 싶다면, master branch에 병합


### **GitHub Flow Models**

- Github에서 제시하는 2가지 방법이 있다.
    - Shared Repository Model
    - Fork & Pull Model
- 가장 큰 차이점은 내가 원격 저장소에 직접적인 push 권한이 있는지의 여부

#### **Shared Repository Model**

- 동일한 저장소를 공유하여 활용하는 방식
- 작업 흐름을 master + feature branch로 구성하여 진행

1. 팀원 초대 및 저장소 Clone
2. branch 생성
3. 작업
4. Commit
5. Github로 branch를 push
6. Pull Request 생성
7. 코드 Review
8. Merge pull request
   
   이후 과정은 Master branch로 이동 후 계속 작업

#### **Fork & Pull Model**

- Repository에 Collaborator에 등록되지 않은 상태에서 진행
- Github 기반의 오픈소스 참여 과정에서 사용됨

1. Fork
2. Clone
   
   이후 작업은 Shared Repository Model과 동일