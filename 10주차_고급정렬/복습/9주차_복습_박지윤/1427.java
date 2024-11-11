import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.Scanner;

public class Main {
    public static void main( String[]args){
        Scanner input=new Scanner(System.in);
        String n=input.nextLine();

        ArrayList<Integer> arr=new ArrayList<>();

        for(int i=0;i<n.length();i++){
            int num = Character.getNumericValue(n.charAt(i));
            arr.add(num);
        }
        
        Collections.sort(arr,Collections.reverseOrder());

        for(int i=0;i<arr.size();i++){
            System.out.print(String.valueOf(arr.get(i)));
        }
    }
}
