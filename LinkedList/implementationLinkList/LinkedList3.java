public class LinkedList3{
    Node head;
    LinkedList3(int data){
        // Node head = new Node(data);
        this.head = new Node(data);
    }
    public static void main(String[] args){
        LinkedList3 l1 = new LinkedList3(293);
        System.out.print(l1.head.data);
    }
}
class Node{
    int data;
    Node next;
    Node(int data){
        this.data = data;
        this.next = null;
    }
}