## 큐, 우선순위 큐

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

## 원형 큐의 특징
- **선입선출(FIFO)** 방식: 먼저 들어온 데이터가 먼저 나갑니다.
- **고정된 크기**: 한정된 크기의 메모리를 사용하여 구현됩니다.
- **연결된 구조**: 큐의 끝이 다시 처음과 연결된 형태로, 배열의 양 끝이 연결된 것처럼 동작합니다.

![원형 큐의 형태](https://prod-files-secure.s3.us-west-2.amazonaws.com/a8c02eb2-d622-48cd-b20f-5cf5f51eb8df/f9ae0903-80da-4c69-a2b9-1d37ead0d799/image.png)

---

## 삽입 (Enqueue)

1. **rear** 포인터가 가리키는 곳에 데이터를 삽입.
2. 삽입이 완료되면 **rear** 포인터를 한 칸 앞으로 이동. 만약 **rear** 포인터가 배열의 끝에 도달하면 **원형**으로 돌아가 다시 배열의 처음을 가리킴.

### 삽입 과정
![원형 큐 삽입](https://prod-files-secure.s3.us-west-2.amazonaws.com/a8c02eb2-d622-48cd-b20f-5cf5f51eb8df/aa14f09b-bc23-44cb-bdd9-f0a829d767cb/image.png)

---

## 삭제 (Dequeue)

1. **front** 포인터가 가리키는 곳에서 데이터를 제거.
2. 제거가 완료되면 **front** 포인터를 한 칸 앞으로 이동. 만약 **front** 포인터가 배열의 끝에 도달하면 **원형**으로 돌아가 다시 배열의 처음을 가리킴.

### 삭제 과정
![원형 큐 삭제](https://prod-files-secure.s3.us-west-2.amazonaws.com/a8c02eb2-d622-48cd-b20f-5cf5f51eb8df/4e1a34c8-c5bc-49b6-a4ce-12164ff1e33e/image.png)

---

## 원형 큐가 가득 찬 경우
- **rear**가 **front**보다 한 칸 앞에 있을 때, 즉 `front == (rear + 1) % 큐 크기`인 상태일 때는 큐가 가득음.

![원형 큐가 가득 찬 상태](https://prod-files-secure.s3.us-west-2.amazonaws.com/a8c02eb2-d622-48cd-b20f-5cf5f51eb8df/03386271-910b-4fee-9d03-216702ecf381/image.png)

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
