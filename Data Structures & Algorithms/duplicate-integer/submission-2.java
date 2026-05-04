class Solution {
    public boolean hasDuplicate(int[] nums) {
        Arrays.sort(nums);
        int s = 0;
        int n = nums.length;
        for (int i=1; i<n; i++){
            if (nums[s] == nums[i]){
                return true;
            }
            else{
                s += 1;
            }
        }
        return false;
    }
}