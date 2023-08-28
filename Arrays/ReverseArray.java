public class ReverseArray{
    public static void main(String[] args){
        int[] arr = {12, 33, 4, 5, 66, 7};
        System.out.println("The original array is:");
        printArray(arr);
        System.out.println("The reversed Array is: ");
        printArray(reverseA(arr));
    }
    private static int[] reverseA(int[] arr){
        int start = 0;
        int end = arr.length - 1;
        while (start < end){
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start ++;
            end --;
        }
        return arr;
        
    }
    private static void printArray(int[] arr){
        System.out.print("[");
        for(int i = 0; i < arr.length; i++){
            System.out.print(arr[i]);
            if( i != arr.length - 1){
            System.out.print(", ");
            }
        }
        System.out.println("]");
    }
}

