package src;

public class FindDigit {
  public boolean lastDigit(int a, int b) {

  if (getLastDigit(a) == getLastDigit(b))
    return true;
  return false;
  }

  public int getLastDigit( int digit){
  while(digit > 9){
    digit = digit%10;
  }
  return digit;
  }
}