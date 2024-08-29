class Solution {
public:
    int digArtifacts(int n, vector<vector<int>>& artifacts, vector<vector<int>>& dig) {
         
   std::vector<std::vector<bool>> digGrid(n,std::vector<bool>(n,false));

   
   for (int i = 0; i < dig.size(); ++i) {
       digGrid[dig[i][0]][dig[i][1]] = true;
   }


   int count = 0;

   for (int i = 0; i < artifacts.size(); ++i) {
       int startY = artifacts[i][0];
       int startX = artifacts[i][1];

       int endY = artifacts[i][2];
       int endX = artifacts[i][3];

       bool valid = true;

       for (int j = startY; j < endY+1; ++j) {
           for (int z = startX; z < endX+1; ++z) {
               if (!digGrid[j][z])
                   valid = false;
           }
       }
       if (valid)
           ++count;
   }
   return count;
    }
};