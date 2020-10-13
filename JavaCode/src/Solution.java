package src;


// you can also use imports, for example:
import java.util.*;

class Solution {
    public static String solution(String S) {
        // write your code in Java SE 8
        if (S == null || S.length() == 0)
            return "";
        StringBuffer newString = new StringBuffer();
        HashMap<String, Integer> charMap = new HashMap<String, Integer>();
        try {
            // Get the counts
            Integer acount = (S.length() - S.replaceAll("a", "").length())
                    + (S.length() - S.replaceAll("A", "").length());
            if (acount > 0)
                charMap.put("a", acount);

            Integer ecount = (S.length() - S.replaceAll("e", "").length())
                    + (S.length() - S.replaceAll("E", "").length());
            if (ecount > 0)
                charMap.put("e", ecount);

            Integer icount = (S.length() - S.replaceAll("i", "").length())
                    + (S.length() - S.replaceAll("I", "").length());
            if (icount > 0)
                charMap.put("i", icount);

            Integer ocount = (S.length() - S.replaceAll("o", "").length())
                    + (S.length() - S.replaceAll("O", "").length());
            if (ocount > 0)
                charMap.put("o", ocount);

            Integer ucount = (S.length() - S.replaceAll("u", "").length())
                    + (S.length() - S.replaceAll("U", "").length());
            if (ucount > 0)
                charMap.put("u", ucount);

            // Sort the HashMap
            LinkedHashMap<String, Integer> sortedcharMap = (LinkedHashMap<String, Integer>) sortByValues(charMap);

            // Print the Map
            Iterator<HashMap.Entry<String, Integer>> itr = sortedcharMap.entrySet().iterator();
            while (itr.hasNext()) {
                Map.Entry<String, Integer> entry = itr.next();
                if (entry.getValue() > 1) {
                    newString.append(entry.getKey());
                    newString.append(" appears ");
                    newString.append(entry.getValue());
                    newString.append(" times");
                    newString.append("\n");
                } else {
                    newString.append(entry.getKey());
                    newString.append(" appears ");
                    newString.append(entry.getValue());
                    newString.append(" time");
                    newString.append("\n");
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return newString.toString().trim();
    }

    private static LinkedHashMap<String, Integer> sortByValues(HashMap<String, Integer> map) {
        LinkedHashMap<String, Integer> sortedHashMap = new LinkedHashMap<>();
        Object[] a = map.entrySet().toArray();
        Arrays.sort(a, new Comparator() {
            public int compare(Object o1, Object o2) {
                return ((Map.Entry<String, Integer>) o2).getValue()
                        .compareTo(((Map.Entry<String, Integer>) o1).getValue());
            }
        });
        for (Object entry : a) {
            sortedHashMap.put(((Map.Entry<String, Integer>) entry).getKey(),
                    ((Map.Entry<String, Integer>) entry).getValue());
        }
        return sortedHashMap;
    }

    public static void main(String[] args) {
        // String S = solution("The quick brown fox jumps over the lazy dog");
        // String S = "The Chicago Bears are a professional American football team based
        // in Chicago, Illinois. The Bears compete in the National Football League as a
        // member club of the league's National Football Conference North division.";
        String S = "this is a sentence";
        S = solution(S);
        System.out.println(S);

    }

}
