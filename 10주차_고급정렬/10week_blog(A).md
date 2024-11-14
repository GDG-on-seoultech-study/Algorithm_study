## 퀵정렬(Quick Sort)

→ 분할정복 알고리즘 사용

 → **분할 정복 알고리즘 :** 그대로 해결할 수 없는 문제를 작은 문제로 분할하여 해결

리스트에서 기준점(피벗)을 선택하고, 피벗을 기준으로 작은 값들은 왼쪽, 큰 값들은 오른쪽으로 나누어 정렬합니다. 재귀적으로 각 부분 리스트를 정렬하며 전체 리스트를 정렬합니다.

- **시간 복잡도**: 평균적으로 O(nlogn), 최악의 경우 O(n2)
- **특징**: 메모리 효율이 좋고, 리스트 내부에서 직접 교환이 이루어집니다.

퀵정렬 코드 구현

```java
public class QuickSort {
public static void quickSort(int[] arr, int low, int high) {
if (low < high) {
int pivotIndex = partition(arr, low, high);
quickSort(arr, low, pivotIndex - 1);
quickSort(arr, pivotIndex + 1, high);
}
}

private static int partition(int[] arr, int low, int high) {
    int pivot = arr[high];
    int i = low - 1;
    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(arr, i, j);
        }
    }
    swap(arr, i + 1, high);
    return i + 1;
}

private static void swap(int[] arr, int i, int j) {
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}
}
```

https://st-lab.tistory.com/250 → 참고자료, 조금 더 deep하게 알고 싶으면 참고!

## 병합정렬 (Merge Sort)

→ 분할정복 알고리즘 사용

- **시간 복잡도**: 항상 O(nlogn)
- **특징**: 안정적인 정렬 알고리즘이며, 추가적인 메모리가 필요합니다.

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/0549c8df-a5e5-49fc-b4e6-efdcae344756/81e70536-482c-4633-9854-1959b3ed95cc/image.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/0549c8df-a5e5-49fc-b4e6-efdcae344756/590f7585-4d8c-427c-bb6b-986a9446ef49/image.png)

병합 정렬 코드

```java
public class MergeSort {
    public static void mergeSort(int[] arr, int left, int right) {
        if (left < right) {
            int mid = (left + right) / 2;
            mergeSort(arr, left, mid);
            mergeSort(arr, mid + 1, right);
            merge(arr, left, mid, right);
        }
    }

    private static void merge(int[] arr, int left, int mid, int right) {
        int n1 = mid - left + 1;
        int n2 = right - mid;

        int[] L = new int[n1];
        int[] R = new int[n2];

        for (int i = 0; i < n1; i++) L[i] = arr[left + i];
        for (int i = 0; i < n2; i++) R[i] = arr[mid + 1 + i];

        int i = 0, j = 0;
        int k = left;

        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) arr[k++] = L[i++];
            else arr[k++] = R[j++];
        }

        while (i < n1) arr[k++] = L[i++];
        while (j < n2) arr[k++] = R[j++];
    }
}

```

→ https://st-lab.tistory.com/233

## 기수 정렬 (Radix Sort)

기수 정렬은 비교 기반 정렬이 아니며, **자릿수에 따라 분류**하여 정렬합니다. 가장 낮은 자릿수부터 시작해 큰 자릿수로 나아가며 정렬하며, 각 자릿수마다 안정적인 정렬(예: 계수 정렬)을 사용합니다.

- **시간 복잡도**: O(d×(n+k)), 여기서 d는 최대 자릿수, k는 자리 값의 범위
- **특징**: 특정한 경우에 매우 빠르며, 주로 정수에만 사용됩니다.

**사용에 적합한 경우**:

- **정수 또는 고정 자릿수 데이터**: 기수 정렬은 자릿수를 기준으로 정렬하기 때문에 주로 정수나 자릿수가 고정된 데이터에 최적화되어 있습니다. 예를 들어, 학번, 우편번호, 신용카드 번호 등에서 사용됩니다.
- **특정 범위의 숫자 데이터**: 데이터의 자릿수가 제한적일 때 매우 빠르며, 특히 비교 연산 없이도 효율적인 정렬이 가능합니다.
- **정렬 범위가 작을 때**: 기수 정렬은 데이터 값의 범위가 작고 자릿수가 적을 때 더 효율적입니다.

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/0549c8df-a5e5-49fc-b4e6-efdcae344756/b8549009-47cf-461f-8ff6-988a3497a131/image.png)

기수 정렬 코드
```java
import java.util.Arrays;

public class RadixSort {
    public static void radixSort(int[] arr) {
        int max = Arrays.stream(arr).max().getAsInt();
        for (int exp = 1; max / exp > 0; exp *= 10) {
            countingSortByDigit(arr, exp);
        }
    }

    private static void countingSortByDigit(int[] arr, int exp) {
        int n = arr.length;
        int[] output = new int[n];
        int[] count = new int[10];

        for (int i = 0; i < n; i++) count[(arr[i] / exp) % 10]++;

        for (int i = 1; i < 10; i++) count[i] += count[i - 1];

        for (int i = n - 1; i >= 0; i--) {
            int digit = (arr[i] / exp) % 10;
            output[count[digit] - 1] = arr[i];
            count[digit]--;
        }

        for (int i = 0; i < n; i++) arr[i] = output[i];
    }
}
```
