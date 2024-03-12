class Solution {
    public int minimumMoves(String s) {
        StringBuilder stringBuilder = new StringBuilder(s);

        int count = 0;

        for(int i = 0; i< s.length();i++){
            if (s.charAt(i) == 'X'){
                stringBuilder.replace(i,i+3,"OOO");
                i+=2;
                count++;
            }
        }
        
         return count;
        
    }
}