# 우선순위 큐(Priority Queue)

### **우선순위 큐(Priority Queue)**

- 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조
- 데이터를 우선순위에 따라 처리하고 싶을 때 사용
    - ex) 물건 데이터를 자료구조에 넣었다가 가치가 높은 물건부터 꺼내서 확인해야 하는 경우

    | 자료구조 | 추출되는 데이터 |
    | ------- | -------------- |
    | 스택(Stack) | 가장 나중에 삽입된 데이터 |
    | 큐(Queue) | 가장 먼저 삽입된 데이터 |
    | 우선순위 큐(Priority Queue) | 가장 우선순위가 높은 데이터 | 

- 우선순위 큐를 구현하는 방법
    
    1) 리스트를 이용하여 구현
    2) [힙(Heap)](#힙heap의-특징)을 이용하여 구현

- 데이터의 개수가 N개일 때, 구현방식에 따른 시간 복잡도

    | 우선순위 큐 구현 방식 | 삽입 시간 | 삭제 시간 |
    | ------------------- | -------- | --------- |
    | 리스트 | *O(1)* | *O(N)* |
    | 힙(Heap) | *O(logN)* | *O(logN)* |

- 단순히 N개의 데이터를 힙에 넣었다가 모두 꺼내는 작업은 정렬과 동일 **(힙 정렬)**
    - 이 경우 시간 복잡도는 **O(NlogN)**


### **힙(Heap)의 특징**

- [완전 이진 트리](#완전-이진-트리complete-binary-tree) 자료구조의 일종
- 항상 루트 노드(root node)를 제거
- 최소 힙(mini heap)
    - 루트 노드가 가장 작은 값을 가짐
    - 값이 작은 데이터가 우선적으로 제거됨

        ![최소 힙(mini heap) 예시](./Img/mini%20heap%20example.PNG)

- 최대 힙(max heap)
    - 루트 노드가 가장 큰 값을 가짐
    - 큰 데이터가 우선적으로 제거됨


### **완전 이진 트리(Complete Binary Tree)**

- 루트(root) 노드부터 시작하여 왼쪽 자식 노드, 오른쪽 자식 노드 순서대로 데이터가 차례대로 삽입되는 트리(tree)를 의미

    ![완전 이진 트리](./Img/Complete%20Binary%20Tree.PNG)


### **최소 힙 구성 함수: Min-Heapify()**

- (상향식) 부모 노드로 거슬러 올라가며, 부모보다 자신의 값이 더 작은 경우에 위치를 교체한다.

    ![최소 힙 구성 함수](./Img/Min%20Heapify.PNG)

- 힙에 새로운 원소가 삽입되었을 때 **O(logN)**의 시간 복잡도로 힙 성질을 유지할 수있도록 함

- 힙에 원소가 제거될 때 **O(logN)**의 시간 복잡도로 힙 성질을 유지하도록 할 수 있음
    - 원소를 제거할 때는 가장 마지막 노드가 루트 노드의 위치에 오도록 함
    - 이후에 루트 노드에서부터 하향식으로(더 작은 자식 노드로) Heapify()를 진행


### **우선순위 큐라이브러리를 활용한 힙 정렬 구현 예제**

- Python
    ```python
    import sys
    import heapq
    input = sys.stdin.readline

    def heapsort(iterable):
        h = []
        result = []
        # 모든 원소를 차례대로 힙에 삽입
        for value in iterable:
            heapq.heappush(h, value)
        # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
        for i in range(len(h)):
            result.append(heapq.heappop(h))
        return result

    n = int(input())
    arr = []

    for i in range(n):
        arr.append(int(input()))

    res = heapsort(arr)

    for i in range(n):
        print(res[i])   
    ```

- C++
    ```C++
    #include <bits/stdc++.h>

    using namespace std;

    void heapSort(vector<int>& arr) {
        priority_queue<int> h;
        // 모든 원소를 차례대로 삽입
        for (int i = 0; i < arr.size(); i++) {
            h.push(-arr[i]);
        }
        // 힙에 삽입된 모든 원소를 차례대로 꺼내어 출력
        while (!h.empty()) {
            printf("%d\n", -h.top());
            h.pop();
        }
    }

    int n;
    vector<int> arr;

    int main() {
        cin >> n;
        for (int i = 0; i < n; i++) {
            int x;
            scanf("%d", &x);
            arr.push_back(x);
        }
        heapSort(arr);
    }
    ```