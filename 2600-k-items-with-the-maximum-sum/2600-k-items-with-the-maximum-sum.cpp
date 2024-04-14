class Solution {
public:
    int kItemsWithMaximumSum(int numOnes, int numZeros, int numNegOnes, int k) {
        int total = 0;
        total += min(numOnes, k);
        k -= total;
        k -= numZeros;
        if (k > 0)
            total -= min(numNegOnes,k);
        return total;
    }
};