/*
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
*/


class Solution {
    public int climbStairs(int n) {
        if(n <= 2){
            return n;
        }

        int a = 1;
        int b = 2;

        for(int i=2; i<n; i++){
            int c = a+b;
            a = b;
            b = c;
        }
        return b;
    }
}