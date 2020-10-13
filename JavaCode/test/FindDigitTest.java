import src.FindDigit;

public class FindDigitTest {

    @Test
    public void testFindDigitTest() {
        FindDigit tester = new FindDigit(); // MyClass is tested

        // assert statements
        assertEquals(6, tester.getLastDigit(3289476), "Last digit must be 6");
        assertEquals(true, tester.lastDigit(3289476, 3234576), "Must Return True");
        assertEquals(false, tester.lastDigit(3289476, 3233547), "Must Return True");
    }
}