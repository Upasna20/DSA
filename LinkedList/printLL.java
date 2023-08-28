public class printLL{
    public static void main(String[] args){
        LinkedList l1 = new LinkedList(13);
        l1.addAtHead(23);
        l1.addAtHead(45);
        System.out.println(l1.head.data);
        System.out.println(l1.tail.data);
        l1.addAtLast(78);
        System.out.println("changed tail data is: " + l1.tail.data);
        l1.printLL();
    }

}

class LinkedList{
    Node head;
    Node tail;
    LinkedList(int data){
        this.head = this.tail = new Node(data);
    }

    void addAtHead(int data){
        Node firstNode = new Node(data);
        firstNode.next = this.head ;
        this.head = firstNode;
    }

    void addAtLast(int data){
        Node endNode = new Node(data);
        this.tail.next = endNode;
        this.tail = endNode;
    }

    void printLL(){
        int count = 0;
        Node currNode = this.head;
        while(currNode != null){
            System.out.println(count + ") The data is " + currNode.data);
            currNode = currNode.next;
            count ++;
        }
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