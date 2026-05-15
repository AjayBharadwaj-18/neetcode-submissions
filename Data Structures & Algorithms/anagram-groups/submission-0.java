class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> anagramMap = new HashMap<>();

        for(String str : strs){
            char[] words = str.toCharArray();
            Arrays.sort(words);
            String Key = new String(words);

            anagramMap
                .computeIfAbsent(Key, k -> new ArrayList<>())
                .add(str);
        }
        return new ArrayList<>(anagramMap.values());
    }
}
