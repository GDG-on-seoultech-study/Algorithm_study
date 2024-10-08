package Week6;

import java.util.Queue;
import java.util.LinkedList;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Week6_10845 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        Queue<Integer> q = new LinkedList<>();
        int last = 0;

        for(int i = 0; i < n; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            String command = st.nextToken();

            switch (command){
                case "push":
                    int num = Integer.parseInt(st.nextToken());
                    q.add(num);
                    last = num;
                    break;

                case "pop":
                    if(!q.isEmpty()) sb.append(q.remove() + "\n");
                    else sb.append("-1\n");
                    break;

                case "size":
                    sb.append(q.size() + "\n");
                    break;

                case "empty":
                    if(q.isEmpty()) sb.append("1\n");
                    else sb.append("0\n");
                    break;

                case "front":
                    if(q.isEmpty()) sb.append("-1\n");
                    else sb.append(q.peek() +"\n");
                    break;

                case "back":
                    if(q.isEmpty()) sb.append("-1\n");
                    else sb.append(last + "\n");
                    break;
            }
        }
        System.out.println(sb);
    }
}
