class Solution {
    public int[][] largestLocal(int[][] grid) {
        int[][] maxLocal = new int[grid.length-2][grid.length-2];
        for (int i = 1; i < grid.length - 1; i++) {
            for (int j = 1; j < grid[i].length - 1; j++) {
                //find the maximum in the nine values of the 3*3 matrix surrounding i*j
                maxLocal[i-1][j-1] =                Math.max(Math.max(Math.max(Math.max(Math.max(Math.max(Math.max(Math.max(grid[i-1][j-1]
                        ,grid[i][j-1]),grid[i+1][j-1]),grid[i-1][j]),grid[i][j]),grid[i+1][j]),grid[i-1][j+1]),grid[i][j+1]),grid[i+1][j+1]);
            }
        }

        return maxLocal;
    }
}