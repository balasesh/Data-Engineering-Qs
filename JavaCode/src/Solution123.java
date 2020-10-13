package src;

public class Solution123 {
  private static Integer functionA(Integer A) {

    // if (A == 0) {
    // return 1;
    // } else if (A == 1) {
    // return 2;
    // } else {
    // return functionA(A - 1) * functionA(A - 2);
    // }
    int sum = A - 1;
    for (int i = A - 2; i >= 0;i--) {
      if (i == 1) {
        sum *= 2;
      } else if (i == 0) {
        sum *= 1;
      } else {
        sum *= i;
      }
    }
    return sum;
  }

  public static void main(String[] args) {
    System.out.println(functionA(5));
  }
}