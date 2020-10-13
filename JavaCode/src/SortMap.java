package src;

import java.util.*;
import java.util.stream.Collector;

public class SortMap {

    public static void main(String[] args) {

        StringBuffer newString = new StringBuffer();
        HashMap<String, Integer> map = new HashMap<String, Integer>();
        map.put("e", 1);
        map.put("u", 1);
        map.put("i", 1);
        map.put("a", 1);
        map.put("o", 1);

        LinkedHashMap<String, Integer> sortedMap = sortMapMethod(map);
        Iterator<HashMap.Entry<String, Integer>> itr = sortedMap.entrySet().iterator();

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
        System.out.println(newString.toString().trim());
    }

    private static LinkedHashMap<String, Integer> sortMapMethod(HashMap<String, Integer> map) {
        LinkedHashMap<String, Integer> sortedHashMap = new LinkedHashMap<String, Integer>();
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
}