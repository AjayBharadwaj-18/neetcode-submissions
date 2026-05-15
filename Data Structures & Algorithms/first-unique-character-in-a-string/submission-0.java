class Solution {
    public int firstUniqChar(String s) {
        Map<Character, Integer> map = new HashMap<>();
        
        for (char c : s.toCharArray()) {
            map.put(c, map.getOrDefault(c, 0) + 1);
        }

        for (int n = 0; n < s.length(); n++) {
            if (map.get(s.charAt(n)) == 1) {
                return n;
            }
        }
        return -1;
    }
}