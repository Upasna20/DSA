// // This is a different implementation
// public class LinkedList2{
//     public static void main(String[] args){
//         LinkedList2 ll = new LinkedList2();
//         // Node head = ll.new Node(12); // this doesn't work because no Node class is visible from the object ll upon instantiation because Node is actually not a part of the LinkedList2 class.
//         System.out.println(head.data);
//     }
// }
// class Node{ // in a java file, only one class can be public and that must contain the main method
//     int data; // you'll have to define the variables here, before using them in the constructor.
//     Node next;
//     Node(int data){
//         this.data = data;
//         this.next = null;
//     }
// }

//sort of correct implememtation
// public class LinkedList2{
//     public static void main(String[] args){
//         LinkedList2 ll = new LinkedList2();
//         LinkedList2.Node head = ll.new Node(12);
//         System.out.println(head.data);
//     }

//     class Node{ // in a java file, only one class can be public and that must contain the main method
//     int data; // you'll have to define the variables here, before using them in the constructor.
//     Node next;
//     Node(int data){
//         this.data = data;
//         this.next = null;
//     }
// }
// }

// third implementation
public class LinkedList2{
    public static void main(String[] args){
        LinkedList l1 = new LinkedList(20);
        System.out.println(l1.head.data);
    }
}

class LinkedList{
    Node head;
    LinkedList(int data){
        this.head = new Node(data);
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
