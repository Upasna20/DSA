public class pairsInArray{
    public static void main(String[] args){
        int[] arr = {12, 3, 4, 55, 6};
        pairs(arr);
    }
    public static void pairs(int[] arr){
        for(int i = 0; i < arr.length - 2; i++){
            for(int j = i + 1; j < arr.length; j++){
                System.out.print("(" + arr[i] +", " + arr[j] + ") ");
            }
            System.out.println();
        }
    }
}