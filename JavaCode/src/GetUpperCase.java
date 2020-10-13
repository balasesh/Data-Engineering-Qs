package src;

public class GetUpperCase {
    public String endUp(String str) {
        if(str.length() > 3){
            String str1 = str.substring(0, str.length()-3) ;
            String str2 = str.substring(str.length()-3, str.length());
            return str1+str2.toUpperCase();
        }
        else{
            return str.toUpperCase();
        }
    }

}