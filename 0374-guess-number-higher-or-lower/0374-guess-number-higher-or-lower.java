/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

public class Solution extends GuessGame {
    public int guessNumber(int n) {
   int low = 0;
        int high = n;
        int guess;
        while(low<=high) {
            guess = low + (high-low)/2;
            int status = guess(guess);
            System.out.println("Guess: " + guess + " status: " + status);
            if (status == 0)
                return guess;
            else if(status == 1)
                low =guess+1;
            else
                high = guess-1;
        }
        return -1;
    }
}