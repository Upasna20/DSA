public class prefixSum{
    public static void main(String[] args){
        int[] arr = {2, 4, 6, 8, 10};
        System.out.println(prefixSumgen(arr));

    }
    private static int prefixSumgen(int[] arr){
        int[] prefixArray = new int[arr.length];
        int largest = Integer.MIN_VALUE;
        for(int lower_bound = 0; lower_bound < arr.length; lower_bound++){
            int sum = arr[lower_bound];
            for(int upper_bound = lower_bound + 1; upper_bound < arr.length; upper_bound++){
                sum += arr[upper_bound];
                // prefixArray = sum;
                if(largest < sum){
                    largest = sum;
                }
            }

        }
       return largest;
    }
    private static void printArray(int[] arr){
        System.out.print("(");
        for(int i = 0; i < arr.length; i++){
            if(i != arr.length - 1){
            System.out.print(arr[i] + ",");}
            else{
                System.out.println(arr[i] + ")");
            }
        }
    }
}