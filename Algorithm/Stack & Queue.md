# 스택과 큐

### **스택 자료구조**

- 먼저 들어 온 데이터가 나중에 나가는 형식 (선입후출)
- 입구와 출구가 동일한 형태로 스택을 시각화 가능


### **스택 구현 예제**

- Python
    ```python
    # 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()

    stack.append(5)
    stack.append(2)
    stack.append(3)
    stack.append(7)
    stack.pop( )
    stack.append(1)
    stack.append(4)
    stack.pop( )

    print(stack[::-1]) # 최상단 원소부터 출력
    print(stack) # 최하단 원소부터 출력
    ```
    실행결과
    ```
    [1, 3, 2, 5]
    [5, 2, 3, 1]
    ```

- C++
    ```C++
    #include <bits/stdc++.h>

    using namespace std;

    stack<int> s;

    int main(void) {
        s.push(5);
        s.push(2);
        s.push(3);
        s.push(7);
        s.pop();
        s.push(1);
        s.push(4);
        s.pop();

        // 스택의 최상단 원소부터 출력
        while (!s.empty()){
            cout << s.top() << ' ';
            s.pop();
        }
    }
    ```
    실행결과
    ```
    1 3 2 5
    ```

- Java
    ```Java
    import java.util.*;

    public class Main {
        public static void main(String[] args) {
            Stack<Integer> s = new Stack<>();

            // 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
            s.push(5);
            s.push(2);
            s.push(3);
            s.push(7);
            s.pop();
            s.push(1);
            s.push(4);
            s.pop();

            // 스택의 최상단 원소부터 출력
            while (!s.empty()) {
                System.out.print(s.peek() + " ");
                s.pop();
            }
        }
    }
    ```
    실행결과
    ```
    1 3 2 5
    ```


### **큐 자료구조**

- 먼저 들어 온 데이터가 먼저 나가는 형식(선입선출)
- 큐는 입구와 출구가 모두 뚫려 있는 터널과 같은 형태로 시각화 가능


### **큐 구현 예제**

- 그냥 리스트로 구현가능 but 시간복잡도가 높기때문에 deque를 이용

- Python
    ```python
    from collections import deque

    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()

    # 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
    queue.append(5)
    queue.append(2)
    queue.append(3)
    queue.append(7)
    queue.popleft()
    queue.append(1)
    queue.append(4)
    queue.popleft()

    print(queue) # 먼저 들어온 순서대로 출력
    queue.reverse() # 역순으로 바꾸기
    print(queue) # 나중에 들어온 원소부터 출력
    ```
    실행결과
    ```
    deque([3, 7, 1, 4])
    deque([4, 1, 7, 3])
    ```

- C++
    ```C++
    #include <bits/stdc++.h>

    using namespace std;

    queue<int> q;

    int main(void) {
        q.push(5);
        q.push(2);
        q.push(3);
        q.push(7);
        q.pop();
        q.push(1);
        q.push(4);
        q.pop();

        // 먼저 들어온 원소부터 추출
        while (!q.empty()){
            cout << q.front() << ' ';
            q.pop();
        }
    }
    ```
    실행결과
    ```
    3 7 1 4
    ```

- Java
    ```Java
    import java.util.*;

    public class Main {
        public static void main(String[] args){
            Queue<Integer> q = new LinkedList<>();

            // 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
            q.offer(5);
            q.offer(2);
            q.offer(3);
            q.offer(7);
            q.poll();
            q.offer(1);
            q.offer(4);
            q.poll();

            // 먼저 들어온 원소부터 추출
            while (!q.isEmpty()) {
                System.out.print(q.poll() + " ");
            }
        }
    }
    ```
    실행결과
    ```
    3 7 1 4
    ```