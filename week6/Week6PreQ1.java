package 예습문제.week6;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Week6PreQ1 {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        scanner.nextLine();

        Queue<Integer> queue = new LinkedList<>();
        int lastVar = -1;

        for (int i = 0; i < n; i++) {
            String oper = scanner.nextLine();

            switch (oper.split(" ")[0]) {
                case "push":
                    int var = Integer.parseInt(oper.split(" ")[1]);
                    queue.add(var);
                    lastVar = var;
                    break;

                case "pop":
                    if (queue.isEmpty()) {
                        System.out.println("-1");
                    } else {
                        System.out.println(queue.poll());
                    }
                    break;

                case "size":
                    System.out.println(queue.size());
                    break;

                case "empty":
                    if (queue.isEmpty()) {
                        System.out.println("1");
                    } else {
                        System.out.println("0");
                    }
                    break;

                case "front":
                    if (queue.isEmpty()) {
                        System.out.println("-1");
                    } else {
                        System.out.println(queue.peek());
                    }
                    break;

                case "back":
                    if (queue.isEmpty()) {
                        System.out.println("-1");
                    } else {
                        System.out.println(lastVar);
                    }
                    break;
            }
        }

        scanner.close();
    }
}
