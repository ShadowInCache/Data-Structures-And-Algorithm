class Solution {
public:
    int lastStoneWeightII(vector<int>& stones) {
        int total = 0;

        for (int x : stones) {
            total += x;
        }

        int target = total / 2;

        vector<bool> dp(target + 1, false);
        dp[0] = true;

        for (int x : stones) {
            for (int s = target; s >= x; --s) {
                dp[s] = dp[s] || dp[s - x];
            }
        }

        for (int s = target; s >= 0; --s) {
            if (dp[s]) {
                return total - 2 * s;
            }
        }

        return 0;
    }
};