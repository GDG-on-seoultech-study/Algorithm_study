package Week6;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Week6_9093 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Stack<Character> st = new Stack<>();
        int N = Integer.parseInt(br.readLine());

        for(int i=0; i<N; i++){
            String str = br.readLine();
            StringBuilder sb = new StringBuilder();

           for(int j=0; j<str.length();j++){
               if(str.charAt(j)==' '){
                   while(!st.isEmpty()){
                        sb.append(st.pop());
                   }
                   sb.append(" ");
               }else{
                   st.push(str.charAt(j));
               }
           }
            while(!st.isEmpty()){
                sb.append(st.pop());
            }
           System.out.println(sb);
        }

    }
}
