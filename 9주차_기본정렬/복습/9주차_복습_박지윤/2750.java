import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;
public class Main {
        public static void main(String[] args) {
            Scanner n=new Scanner(System.in);
            int num=n.nextInt();
            
            ArrayList<Integer> arr=new ArrayList<>();

            for(int i=0;i<num;i++)
            {
                int input=n.nextInt();
                arr.add(input);
            }
            Collections.sort(arr);

            for(int i=0;i<num;i++){
                System.out.println(arr.get(i));
            }
        }
    }
