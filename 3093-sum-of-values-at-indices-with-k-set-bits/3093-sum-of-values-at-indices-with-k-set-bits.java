class Solution {
    public int sumIndicesWithKSetBits(List<Integer> nums, int k) {
int sum = 0;

        for(int i = 0; i<nums.size();i++){
           String binary = Integer.toBinaryString(i);
           System.out.println(binary);
           int counter = 0;
           for(int j = 0; j < binary.length(); j++){
               if(binary.charAt(j) == '1')
                   counter++;
           }
           if(counter == k)
               sum += nums.get(i);
        }

        return sum;
    }
}