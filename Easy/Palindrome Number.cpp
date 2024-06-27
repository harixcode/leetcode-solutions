class Solution {
public:
    bool isPalindrome(int x) {
        long reversed_number = 0;
        int remainder = 0;
        bool b;
        if (x < 0){
            return false;
        }
        long n = x;
        while(n != 0) {
            remainder = n % 10;
            reversed_number = reversed_number * 10 + remainder;
            n /= 10;
        }
        return reversed_number == x;
    }
};