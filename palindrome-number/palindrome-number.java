class Solution {
    public boolean isPalindrome(int inputNum) {
        int reminder = 0;
        int sum = 0;
        int input = inputNum;
        while (inputNum > 0) {
            reminder = inputNum % 10;
            sum = sum * 10 + reminder;
            inputNum = inputNum / 10;
        }

        if (sum > 0x7FFFFFFF || input != sum) {
            return false;
        }
        return true;
        
    }
}