public class subarray{
    public static void main(String[] args){
        int[] arr = {2, 4, 6, 8, 10};
        subarraygen(arr);
    }
    private static void subarraygen(int[] arr){
        for(int i = 0; i < arr.length; i++){
            for(int j = i+1; j < arr.length; j++ ){
                System.out.print("(");
                for(int h = i; h < j+ 1; h++){
                    System.out.print(arr[h] + ",");
                }
                System.out.print("), ");
            }
            System.out.println();
        }
    }
}