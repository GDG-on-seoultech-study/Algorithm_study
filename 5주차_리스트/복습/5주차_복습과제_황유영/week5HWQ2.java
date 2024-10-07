package Week5ListProblem;

import java.util.Scanner;

public class week5HWQ2 {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        int m = scanner.nextInt();

        scanner.nextLine();


        int[][] numArray = new int[n+1][n+1];                       // 행렬 만들기
        int[][] arraySum = new int[n+1][n+1];                       // 구간 누적 합 행렬 만들기


        for (int i = 1; i <= n; i++) {                              // 행렬 만들기
            for (int j = 1; j <= n; j++) {
                numArray[i][j] = scanner.nextInt();

                arraySum[i][j] = numArray[i][j] + arraySum[i - 1][j] + arraySum[i][j - 1] - arraySum[i - 1][j - 1];
            }
        }

        int[] result = new int[m];

        for (int k = 0; k < m; k++){                                // x1,y1,x2,y2 값 만들고 구간 합 구하기
            int x1 = scanner.nextInt();
            int y1 = scanner.nextInt();
            int x2 = scanner.nextInt();
            int y2 = scanner.nextInt();

            int sum = arraySum[x2][y2] - arraySum[x1 - 1][y2] - arraySum[x2][y1 - 1] + arraySum[x1 - 1][y1 - 1];
            result[k] = sum;

        }

        for (int i = 0; i < m; i++) {
            System.out.println(result[i]);
        }


        scanner.close();





    }
}