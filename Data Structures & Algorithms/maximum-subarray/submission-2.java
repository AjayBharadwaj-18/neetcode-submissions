class Solution {
    public int maxSubArray(int[] nums) {
        int maxSub = nums[0];
        int sum = 0;

        for(int num : nums){
            if (sum < 0){
                sum = 0;
            };
            sum += num;

            if (maxSub < sum){
                maxSub = sum;
            };

        };
        return maxSub;
    }
}
