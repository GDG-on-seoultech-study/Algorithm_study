package Week6;

import java.util.Stack;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Week6_10828 {
    public static void main(String[] args) throws IOException{
        Stack<Integer> stack = new Stack<>();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());

        for(int i=0; i<N; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            String command = st.nextToken();

            switch(command){
                case "push":
                    int num = Integer.parseInt(st.nextToken());
                    stack.push(num);
                    break;

                case "pop":
                    if(stack.isEmpty()){
                        sb.append("-1\n");
                    }else{
                        sb.append(stack.pop() + "\n");
                    }
                    break;

                case "size":
                    sb.append(stack.size()+ "\n");
                    break;

                case "empty":
                    if(stack.isEmpty()){
                        sb.append("1\n");
                    }else{
                        sb.append("0\n");
                    }
                    break;

                case "top":
                    if(stack.isEmpty()){
                        sb.append("-1\n");
                    }else{
                        sb.append(stack.peek()+ "\n");
                    }
                    break;

            }
        }
        System.out.println(sb);
    }
}
