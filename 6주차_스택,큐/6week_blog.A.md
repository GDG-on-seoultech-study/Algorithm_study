### 스택이란?

- 알고리즘에서 **중요한 자료구조** 중 하나
- 데이터 저장 방식 : 선형구조
- **후입선출** 방식(Last In, First Out, LIFO)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/0549c8df-a5e5-49fc-b4e6-efdcae344756/fe879dfe-a5c1-4f33-9d27-caa73f340fb6/image.png)

### 보충/ 선형구조 & 비선형구조

- **선형 구조 :** 데이터가 한 줄로 나열되고 순차적으로 접근. 배열이나 리스트처럼 연속된 메모리 위치에 저장
- **비선형 구조 :** 계층적이거나 네트워크 형식으로 데이터가 연결되어 있어 더 복잡한 관계를 표현 가능. 트리나 그래프는 각 노드가 여러 개의 자식이나 이웃 노드를 가질 수 있음

### 주요 연산

- **push**: 스택의 맨 위에 데이터를 추가하는 연산.
- **pop**: 스택의 맨 위에 있는 데이터를 제거하고 반환하는 연산.
- **peek (또는 top)**: 스택의 맨 위에 있는 데이터를 제거하지 않고 반환하는 연산.
- **isEmpty**: 스택이 비어 있는지 여부를 확인하는 연산.
- 스택은 최상단의 데이터만 접근할 수 있으며, 중간이나 바닥의 데이터는 직접 접근할 수 없음.

### 용도

- 함수 호출 관리: 함수가 호출될 때 스택에 현재 상태가 저장되고, 함수가 완료되면 상태가 복원됩니다.
- 역추적: 예를 들어, 웹 브라우저의 뒤로 가기 기능은 스택을 사용하여 이전 페이지로 돌아갑니다.
- 수식 계산: 후위 표기법 같은 수식에서 스택을 이용해 계산을 수행합니다.

### **장점**

- 간단한 구조 : 스택은 구현이 간단하고 이해하기 쉬운 데이터 구조
- 빠른 접근 속도 : 스택은 최상단 요소에 대한 접근이 O(1) 시간 복잡도로 매우 빠름. 데이터 추가와 제거도 O(1)로 효율적

→ 스택은 괄호 검증, 후위 표기법 계산, DFS(깊이 우선 탐색) 등 다양한 알고리즘에서 **필수적**으로 사용

### 단점

- 제한된 접근 : 스택은 LIFO 구조로 인해 중간 요소에 직접 접근할 수 없음. 이로 인해 특정 요소를 찾거나 제거하기 어려움
- 고정된 크기 (배열 기반) : 배열 기반 스택의 경우 초기 크기를 설정해야 하며, 크기를 초과하면 스택 오버플로우가 발생할 수 있음
- 메모리 사용: 연결 리스트 기반 스택은 노드를 저장하기 위해 추가 메모리를 사용해야 하며, 이는 메모리 오버헤드로 이어질 수 있음
- 데이터 손실 위험 : 스택이 비어 있는 상태에서 팝 연산을 시도하면 데이터 손실이나 오류가 발생할 수 있음

```python
class Stack:
    def __init__(self):
        self.items = []  # 스택을 저장할 리스트

    def is_empty(self):
        return len(self.items) == 0  # 스택이 비어있는지 확인

    def push(self, item):
        self.items.append(item)  # 스택에 아이템 추가

    def pop(self):
        if self.is_empty():
            raise IndexError("스택 언더플로우: 더 이상 팝할 아이템이 없습니다.")  # 비어있을 때 팝 시 오류 발생
        return self.items.pop()  # 스택의 최상단 아이템 제거 및 반환

    def peek(self):
        if self.is_empty():
            raise IndexError("스택 언더플로우: 확인할 아이템이 없습니다.")  # 비어있을 때 피크 시 오류 발생
        return self.items[-1]  # 스택의 최상단 아이템 반환

    def size(self):
        return len(self.items)  # 스택의 크기 반환

# 사용 예시
if __name__ == "__main__":
    stack = Stack()
    
    stack.push(1)
    stack.push(2)
    stack.push(3)
    
    print("스택의 최상단 아이템:", stack.peek())  # 3 출력
    print("스택의 크기:", stack.size())  # 3 출력
    
    print("팝된 아이템:", stack.pop())  # 3 출력
    print("스택의 크기:", stack.size())  # 2 출력

    while not stack.is_empty():
        print("팝된 아이템:", stack.pop())  # 2, 1 출력

```

```java
class Stack {
    private int maxSize; // 스택의 최대 크기
    private int[] stackArray; // 스택을 저장할 배열
    private int top; // 스택의 최상단 인덱스

    // 생성자
    public Stack(int size) {
        this.maxSize = size;
        this.stackArray = new int[maxSize];
        this.top = -1; // 스택이 비어있음을 나타냄
    }

    // 스택에 데이터 추가
    public void push(int value) {
        if (top >= maxSize - 1) {
            System.out.println("스택 오버플로우: 더 이상 추가할 수 없습니다.");
            return;
        }
        stackArray[++top] = value; // top을 증가시키고 값을 추가
    }

    // 스택에서 데이터 제거
    public int pop() {
        if (top < 0) {
            System.out.println("스택 언더플로우: 제거할 데이터가 없습니다.");
            return -1; // 에러 코드 반환
        }
        return stackArray[top--]; // 최상단 값을 반환하고 top을 감소시킴
    }

    // 스택의 최상단 데이터 확인
    public int peek() {
        if (top < 0) {
            System.out.println("스택이 비어있습니다.");
            return -1; // 에러 코드 반환
        }
        return stackArray[top]; // 최상단 값을 반환
    }

    // 스택이 비어 있는지 확인
    public boolean isEmpty() {
        return (top < 0);
    }

    // 스택의 크기 반환
    public int size() {
        return top + 1;
    }
}

// 사용 예시
public class Main {
    public static void main(String[] args) {
        Stack stack = new Stack(5); // 크기가 5인 스택 생성

        stack.push(10);
        stack.push(20);
        stack.push(30);

        System.out.println("최상단 데이터: " + stack.peek()); // 30 출력
        System.out.println("스택 크기: " + stack.size()); // 3 출력

        System.out.println("제거된 데이터: " + stack.pop()); // 30 출력
        System.out.println("제거된 데이터: " + stack.pop()); // 20 출력

        System.out.println("스택이 비어있나요? " + stack.isEmpty()); // false 출력

        stack.pop(); // 10 제거
        System.out.println("스택이 비어있나요? " + stack.isEmpty()); // true 출력
    }
}

```

# 큐

### Queue

: 선입선출(FIFO, First-In-First-Out) 방식을 따르는 자료구조로 먼저 저장된 데이터가 먼저 꺼내지는 형태. = 넣은 순서대로 나옴. 

데이터 추가 삭제가 쉬운 LinkedList가 적합함.

큐는 클래스로 제공 X. 인터페이스로 제공되기 때문에 구체적인 클래스를 통해 인스턴스 생성.

```python
import java.util.LinkedList;
import java.util.Queue;

Queue<Integer> q = new LinkedList<>(); // int형 queue 선언
Queue<String> q = new LinkedList<>(); // String형 queue 선언
```

| **메서드** | **설명** |
| --- | --- |
| **offer(E e)** | 큐의 맨 뒤에 지정된 요소를 추가합니다. 큐가 가득 차서 요소를 추가할 수 없는 경우 false를 반환합니다. |
| **add()** | 큐의 맨 뒤에 지정된 요소를 추가합니다. 큐가 가득 차서 요소를 추가할 수 없는 경우 IllegalStateException 예외를 발생시킵니다. |
| **poll()** | 큐의 맨 앞에서 요소를 제거하고 반환합니다. 큐가 비어 있으면 null을 반환합니다. |
| **peek()** | 큐의 맨 앞에서 요소를 반환합니다. 큐가 비어 있으면 null을 반환합니다. |
| **clear()** | 큐의 모든 요소를 제거합니다. |

차이는 주로 큐가 꽉 차 있거나 비어 있는 상황에서 어떻게 처리하는지에 따라 결정



```java
Queue<String> queue = new LinkedList<>();

try {
    queue.add("item1");  // 추가: 정상 동작
    queue.remove();      // 삭제: 정상 동작
    queue.remove();      // 큐가 비어 있으면 예외 발생
} catch (NoSuchElementException e) {
    System.out.println("큐가 비어 있습니다.");
}
```
⇒ 예외 발생 메서드를 사용할 때는 큐의 상태(비었거나 꽉 찼는지)를 사전에 알 수 없을 때. try-catch 구문을 활용해서 오류 상황을 처리함.
    e.g.) add(e), remove(), element()
⇒ 값을 리턴하는 메서드는 예외 처리가 필요 없는 간단한 상황에서 활용함. 
    e.g.) offer(e), poll(), peek()
    
```java
q.add(num); // 스택의 push
q.remove(); // 스택의 pop
q.size(); // 스택의 size
q.isEmpty(); // 스택의 isEmpty
q.peek(); // 스택의 peek, 큐에서는 가장 앞에 있는 값을 조회한다 
q.poll(); // 큐의 첫번째 항목을 제거
```

차이점 

| 항목           | 예외 처리 (try-catch)                               | 값 반환 처리 (false나 null)                 |
|----------------|-----------------------------------------------------|---------------------------------------------|
| **코드 흐름**    | 예외 발생 시 프로그램 흐름이 바뀌며 catch 블록으로 제어가 넘어감   | 코드 흐름이 끊기지 않고 계속 실행됨             |
| **에러 처리 방식**| 에러 발생 시 반드시 처리해야 하며, 예외가 발생한 원인 파악이 쉬움  | 단순히 실패 여부만 확인하고 넘어갈 수 있음       |
| **복잡도**      | 복잡한 에러 상황을 처리하기 용이                            | 간단한 실패 상황을 처리하기에 적합               |
| **성능 비용**    | 예외 발생 시 약간의 성능 비용이 있음                          | 성능 비용이 거의 없음                           |
| **코드 간결성**  | try-catch 구문으로 인해 코드가 길어질 수 있음                  | 간결하고 명료한 코드 작성 가능                  |


### Priority Queue

: 큐 데이터 구조를 기반으로 데이터를 ‘일렬로 늘어놓은 다음’ 그 중에서 ‘가장 우선 순위가 높은 데이터’를 ‘가장 먼저 꺼내오는 방식’으로 동작.

저장 순서가 3,1,5,2,4 인데도 출력 결과는 1,2,3,4,5 ⇒ 숫자가 작을수록 높아져서 1이 먼저 출력.

숫자가 아닌 객체를 저장하려면 각 객체의 크기를 비교할 수 있는 방법을 제공해야함. 

PriorityQueue가 각 요소를 힙이라는 자료구조의 형태로 저장한 것이라서 그렇다.

힙 :  힙은 트리 구조의 일종으로, 최대값 또는 최소값을 빠르게 찾을 수 있도록 설계된 자료 구조.

### 트리 구조

```java
       50
      /  \
    30    20
   /  \   /
  15  10 5

# 최대힙

현재 최대 힙:
       10
      /  \
     5    3
    / \
   2   1

7을 삽입:
       10
      /  \
     5    3
    / \   /
   2   1 7

7이 부모 5보다 크므로 교환:
       10
      /  \
     7    3
    / \   /
   2   1 5
```

삽입 힙 : 힙의 마지막 위치(리프)에 추가된 후, **상향 이동**(Swim up)을 통해 힙의 성질을 유지

삭제 힙 : **루트 노드**(최대값 또는 최소값)를 제거하고, 마지막 리프 노드를 루트로 이동시킨 후 **하향 이동**(Sink down)을 통해 힙의 성질을 유지


## 원형 큐 (Circular Queue)

원형 큐는 고정된 크기를 가진 큐로, 배열의 양 끝이 연결되어 **원형으로** 동작하는 구조. 즉, 큐가 꽉 차지 않으면 항상 큐의 빈 공간을 재사용 가능. 

### 원형 큐의 특징
- **선입선출(FIFO)** 방식: 먼저 들어온 데이터가 먼저 나갑니다.
- **고정된 크기**: 한정된 크기의 메모리를 사용하여 구현됩니다.
- **연결된 구조**: 큐의 끝이 다시 처음과 연결된 형태로, 배열의 양 끝이 연결된 것처럼 동작합니다.

---

### 삽입 (Enqueue)

1. **rear** 포인터가 가리키는 곳에 데이터를 삽입.
2. 삽입이 완료되면 **rear** 포인터를 한 칸 앞으로 이동. 만약 **rear** 포인터가 배열의 끝에 도달하면 **원형**으로 돌아가 다시 배열의 처음을 가리킴.

---

### 삭제 (Dequeue)

1. **front** 포인터가 가리키는 곳에서 데이터를 제거.
2. 제거가 완료되면 **front** 포인터를 한 칸 앞으로 이동. 만약 **front** 포인터가 배열의 끝에 도달하면 **원형**으로 돌아가 다시 배열의 처음을 가리킴.

---

### 원형 큐가 가득 찬 경우
- **rear**가 **front**보다 한 칸 앞에 있을 때, 즉 `front == (rear + 1) % 큐 크기`인 상태일 때는 큐가 가득 참.

```java
public class CircularQueue {
    private static final int MAX_QSIZE = 10;
    private int front;
    private int rear;
    private Object[] items;  // 원형 큐의 아이템을 저장할 배열
    
    // 생성자
    public CircularQueue() {
        front = 0;
        rear = 0;
        items = new Object[MAX_QSIZE];  // 배열을 초기화
    }

    // 큐가 비어있는지 확인
    public boolean isEmpty() {
        return front == rear;
    }

    // 큐가 가득 찼는지 확인
    public boolean isFull() {
        return front == (rear + 1) % MAX_QSIZE;
    }

    // 큐에 항목을 추가
    public void enqueue(Object item) {
        if (!isFull()) {
            rear = (rear + 1) % MAX_QSIZE;
            items[rear] = item;
        } else {
            System.out.println("Queue is full");
        }
    }

    // 큐에서 항목을 제거하고 반환
    public Object dequeue() {
        if (!isEmpty()) {
            front = (front + 1) % MAX_QSIZE;
            return items[front];
        } else {
            System.out.println("Queue is empty");
            return null;
        }
    }

    // 큐의 첫 번째 항목을 반환
    public Object peek() {
        if (!isEmpty()) {
            return items[(front + 1) % MAX_QSIZE];
        } else {
            System.out.println("Queue is empty");
            return null;
        }
    }

    // 큐를 초기화(모든 항목 삭제)
    public void clear() {
        front = rear;
    }

    // 큐에 있는 항목 수를 반환
    public int size() {
        return (rear - front + MAX_QSIZE) % MAX_QSIZE;
    }
```
