package Week6;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Week6_4949 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Stack<Character> stack = new Stack<>();

        while (true) {
            String str = br.readLine();
            if (str.equals(".")) break;

            for(int i=0;i<str.length();i++){

                if(str.charAt(i)=='(' || str.charAt(i)=='['){
                    stack.push(str.charAt(i));
                } else if (str.charAt(i)==')') {
                    if(stack.isEmpty() || stack.peek()!='('){
                        stack.push('X');
                    }else stack.pop();
                } else if (str.charAt(i)==']'){
                    if (stack.isEmpty() || stack.peek()!='['){
                        stack.push('X');
                    }else stack.pop();
                }

            }

            if(stack.isEmpty()) System.out.println("yes");
            else System.out.println("no");

            stack.clear();
        }
    }
}
