package Week5ListProblem;

import java.util.Scanner;

public class week5HWQ1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int num = scanner.nextInt();
        scanner.nextLine();
        String noSpace = scanner.nextLine();
        int sum = 0;

        String[] numList = noSpace.split("");

        for (int i = 0 ; i < num ; i++){
            sum = sum + Integer.parseInt(numList[i]);
        }

        System.out.println(sum);

    }


}