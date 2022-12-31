# Push Conflict & gitignore

### **Push Conflict**

- 협업을 하다보면 자주 확인하게 되는 메시지가 있다.
  ```
  $ git push origin master
  To https://github.com/kimsuminn/kimsuminn.git
   ! [rejected]     master -> master (fetch first)
   error: failed to push some refs to 'https://github.com/kimsuminn/kimsuminn.git'
   hint: Updates were rejected because the remote contains work that you do
   hint: not have locally. This is usually caused by another repository pushing
   hint: to the same ref. You may want to first integrate the remote changes
   hint: (e.g., 'git pull ...') before pushing again.
   hint: See the 'Note about fast-forwards' in 'git push --help' for details.
   ```

   - 로컬과 원격 저장소의 커밋 이력이 다른 경우 발생한다.
   - 해결방법
    1. 원격저장소의 커밋을 원격저장소로 가져와서 (pull)
    2. 로컬에서 두 커밋을 병합 (추가 커밋 발생)
    3.  다시 GitHub로 push


### **gitignore**

- 일반적인 개발 프로젝트에서 버전 관리를 별도로 하지 않는 파일 / 폴더가 생긴다.
- Git 저장소에 .gitignore 파일을 생성 후 해당 내용을 관리한다.
- 작성 예시
  - 특정 파일: a.txt(모든 a.txt), test/a.txt(test 폴더에 있는 a.txt)
  - 특정 폴더: /my_secret
  - 특정 확장자: *.pptx
  - 예외 처리: !b.pptx
- 이미 커밋된 파일은 무시할 수 없기때문에 미리 .gitignore를 잘 설정하자!