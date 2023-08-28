// private class TernarySearchObject<T>{
//     TernarySearch(int[] arr, int key){
//         this.arr = arr;
//         this.key = key;
//     }
//     int search(){
//         int start = 0;
//         int end = arr.length;
//         while(start > end){
//              int mid = (int)(start + end)/2;
//              if(arr[mid] > key){
//                 end = mid - 1;
//              }
//              else if(arr[mid] < key){
//                 start = mid + 1;
//              }
//              else{
//                 return mid
//              }
//         }
//     }
    

// }   
public class TernarySearch{
    public static void main(String[] args){
        int[] arr = {1, 4, 6, 7, 9, 12, 20};
        int key = 6;
        int ans = search(arr, key);
        System.out.println(ans);
    }  
    
    private static int search(int[] arr, int key){
        int start = 0;
        int end = arr.length;
        while(start <= end){
             int mid = (int)((start + end)/2);
             if(arr[mid] > key){
                end = mid - 1;
             }
             else if(arr[mid] < key){
                start = mid + 1;
             }
             else{
                return(mid);
             }
        }
        return(-1);
    }
       
    
}