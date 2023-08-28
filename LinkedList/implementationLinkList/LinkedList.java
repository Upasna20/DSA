public class LinkedList{
    public static void main(String[] args){
        // here i'll inititalise a new linkedlist object because I might need multiple linkedLists.
        // Also, head and tail, addhead all these methods will be specific to a specific linkedlist.
        LinkedList ll = new LinkedList();
        LinkedList.Node head = ll.new Node(12); // at LHS, we specify the class, at RHS, we specify the location where the heap should instantiate the node and that instantiation must occur inside the heap of the linkedlist object so that the node is a part of the ll object.
        System.out.println(head.data);
    }
    public class Node{
        int data;
        Node next;

        Node(int data){
            this.data = data;
            this.next = null;
        }
    }
}