package Week6;

import java.io.InputStreamReader;
import java.util.Stack;
import java.io.BufferedReader;
import java.io.IOException;
public class Week6_9012 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Stack<Character> stack = new Stack<>();
        int N = Integer.parseInt(br.readLine());

        for(int i=0; i<N; i++){
            String str = br.readLine();

            for(int j=0; j < str.length(); j++){
                if(str.charAt(j) == '('){
                    stack.push(str.charAt(j));
                }
                else if (stack.isEmpty()) {
                    stack.push(str.charAt(j));
                    break;
                }
                else{
                    stack.pop();
                }
            }

            if(stack.isEmpty()) System.out.println("YES");
            else System.out.println("NO");

            stack.clear();
        }
    }
}
