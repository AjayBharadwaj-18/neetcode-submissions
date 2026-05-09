class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for(int num : nums){set.add(num);}

        int longestLength = 0;
        for (int num : set){
            if (!set.contains(num-1)){
               int currNum = num;
               int currSeqLen = 1;
               while(set.contains(currNum + 1)){
                currSeqLen ++;
                currNum ++;
               }
               longestLength = Math.max(longestLength, currSeqLen);
            }
        }
        return longestLength;
    }
}
