public class LinkList{
    Node head;
    Node tail;
    LinkList(int data){
        this.head = this.tail = new Node(data);
    }

    void addAtHead(int data){
        Node newNode = new Node(data);
        newNode.next = this.head;
        this.head = newNode;
    }

    void addAtLast(int data){
        // Node next_node = this.head.next; // this method is redundant if we keep track of the tail variable
        // while( next_node.next != null){ // this method produce O(n)
        //     next_node = next_node.next;
        // }
        Node endNode = new Node(data);
        this.tail.next = endNode;
        this.tail = endNode;


    }
    public static void main(String[] args){
        LinkList l1 = new LinkList(10);
        l1.addAtHead(20);
        l1.addAtHead(3456);
        System.out.println(l1.head.data);// output is 3456
        // Node next_node = l1.head.next;
        // while( next_node.next != null){
        //     next_node = next_node.next;
        // }
        // System.out.println(next_node.data); // output is 10
        System.out.println(l1.tail.data);
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