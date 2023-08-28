public class KadaneAlgo{
    public static void main(String[] args){
        int[] arr = {-2,-3, 4, -1, -2, 1, 5, -3};
        System.out.println("The max of the subarray sum is: " + Kadane(arr));
    }
    public static int Kadane(int[] arr){
        int currSum = 0;
        int maxSum = 0;
        for(int index = 0; index < arr.length; index++){
            if(currSum < 0){
                currSum = 0;
            }
            currSum += arr[index];
            if(currSum > maxSum){
                maxSum = currSum;
            }
        }
        return maxSum;
    }
}