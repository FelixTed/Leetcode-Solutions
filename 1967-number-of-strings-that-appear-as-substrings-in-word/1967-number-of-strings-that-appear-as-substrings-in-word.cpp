class Solution {
public:
    int numOfStrings(vector<string>& patterns, string word) {
        int numSubString = 0;

for (int i = 0; i < size(patterns); i++) {
    if (word.find(patterns[i]) != -1)
        numSubString++;
}

return numSubString;
    }
};