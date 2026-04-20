class Solution {
    public int[] getConcatenation(int[] nums) {
        int len = nums.length + nums.length;
        int[] ans = new int[len];

        int n = nums.length;

        for (int i = 0; i<len; i++){
            if (i<n){
                ans[i] = nums[i];
            }
            else{
                int z = i - n;
                ans[i] = nums[z];
            }            
        }
        return ans;
    }
}