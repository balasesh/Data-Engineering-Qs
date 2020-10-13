package src;

import java.util.ArrayList;
import java.util.List;

public class GetSingleDigits {
    public static void main(String [] args) {
        int number = 6579765;
        List<Integer> digits = getDigits(number);
        for (int i = digits.size()-1;i>=0;i--) {
            System.out.println(digits.get(i));
        }
    }

    private static List<Integer> getDigits(int num){
        List<Integer> tempNum = new ArrayList<Integer>();
        while (num > 10){
            tempNum.add(num%10);
            num = (num - num%10)/10;
        }
        tempNum.add(num);
        return tempNum;
    }

}