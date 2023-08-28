public class Dynamic_implementation{
    pubic class Dynamic_Array{
        private int[] arr;
        private int len;
        public static Dynamic_Array(){
            this.arr = new int[16];
        }
        public static Dynamic_Array(capacity){
            this.arr = new int[capacity];
            this.len = 0;
        }
        public static void append(int num){
            if this.len == this.arr.length{
                int[] new_arr = new int[len * 2];
                for( i = 0; i <= len ; i ++){
                    new_arr[i] = this.arr[i]
                }
                new_arr[len + 1] = num;
                this.arr = new_arr;
            }
            else{
                this.arr[len] = num;
                this.len ++;
            }
        }
    }
    public static void main(String[] args){
        My_array = Dynamic_Array();
        My_array.append(3);
        My_array.arr

    }
}