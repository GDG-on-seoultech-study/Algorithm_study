package Week5ListProblem;

import java.util.Scanner;

public class week5HWQ3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);


        int n = scanner.nextInt();
        int m = scanner.nextInt();

        long[] acummulSum = new long[n + 1];         // 합을 누적해서 배열로 저장
        int[] remainderCnt = new int[m];

        long cnt = 0;

        for (int i = 1; i <= n; i++) {
            int num = scanner.nextInt();
            acummulSum[i] = acummulSum[i - 1] + num;

            int remainder = (int)(acummulSum[i] % m);

            if (remainder < 0) {
                remainder += m;
            }

            if (remainder == 0) {
                cnt++;
            }

            cnt += remainderCnt[remainder];

            remainderCnt[remainder]++;
        }

        System.out.println(cnt);

        scanner.close();

    }
}
