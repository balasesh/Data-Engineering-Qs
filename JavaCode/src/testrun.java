package src;

class testrun {
    public static void main(String [] args) {
        String str = "hello";
        System.out.println(str);
        
    }

    public String everyNth(String str, int n) {
        char [] a = str.toCharArray();
        StringBuffer str1 = new StringBuffer();
        
        for(int i=0; i< str.length() ; i++){
          if(i==0){
            str1.append(a[0]);
          }
          else if(i%n == 0){
            str1.append(a[i]);
          }
          else{
            continue;
          }
        }
        return str1.toString();
      }
      
}