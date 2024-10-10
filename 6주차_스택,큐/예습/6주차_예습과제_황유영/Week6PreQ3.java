package 예습문제.week;

import java.util.Scanner;
import java.util.Stack;

public class Week6PreQ3 {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        Stack<Integer> stack = new Stack<>();

        int n = scanner.nextInt();
        scanner.nextLine();

        for (int i = 0; i < n; i++) {
            String input = scanner.nextLine();
            String[] parts = input.split(" ");
            String oper = parts[0];

            switch (oper) {
                case "push":
                    int num = Integer.parseInt(parts[1]);
                    stack.push(num);
                    break;
                case "pop":
                    if (stack.isEmpty()) {
                        System.out.println(-1);
                    } else {
                        System.out.println(stack.pop());
                    }
                    break;
                case "size":
                    System.out.println(stack.size());
                    break;
                case "empty":
                    System.out.println(stack.isEmpty() ? 1 : 0);
                    break;
                case "top":
                    if (stack.isEmpty()) {
                        System.out.println(-1);
                    } else {
                        System.out.println(stack.peek());
                    }
                    break;
                default:                                    // 잘못된 입력 처리 (문제에서는 필요x)
                    System.out.println("다시 입력하세요.");
                    i = i - 1;
                    break;
            }
        }

        scanner.close();
    }
}
