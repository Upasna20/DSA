public class LLinsertion{
    public static void main(String[] args){
        LinkedList l1 = new LinkedList(13);
        l1.addAtHead(23);
        l1.addAtLast(78);
        l1.addAtHead(45);
        l1.insertLL(4, 3454);
        // l1.printLL();
        l1.insertLL(2, 10);
        l1.printLL();
        System.out.println();
        System.out.println("The Size of th LL is "+ l1.size);
        // l1.removeAtFirst();
        // l1.removeAtFirst();
        // l1.printLL();
        // l1.removeData(2);
        // System.out.println();
        // System.out.println("The Size of th LL is "+ l1.size);
        // l1.printLL();
        System.out.println("The key is at index " + l1.searchIter(10));
        // System.out.println("The key is at index " + l1.searchRecur(10, l1.head, 0));
        // System.out.println("The key is at index " + l1.searchRecur(156, l1.head, 0));
        System.out.println("The key is at index " + l1.searchIter(1054));
        System.out.println("The key is at the index " + l1.RecSearch(78));
        l1.printLL();
        System.out.println();
        l1.reverseLL();
        l1.printLL();
        System.out.println();
        // l1.delFromEnd2(2);
        l1.delFromEndRec(2);
        l1.printLL();

    }
}

class LinkedList{
    int size;
    Node head;
    Node tail;
    LinkedList(int data){
        this.head = this.tail = new Node(data);
        this.size = 1;
    }

    void addAtHead(int data){
        Node firstNode = new Node(data);
        firstNode.next = this.head;
        this.head = firstNode;
        this.size += 1;
    }

    void addAtLast(int data){
        Node endNode = new Node(data);
        if(this.size == 0){
            this.tail = this.head = endNode;
        }
        else{
        this.tail.next = endNode;
        this.tail = endNode;
        }
        this.size += 1;
        
    }

    void printLL(){
        if(this.size == 0){
            System.out.println("The LinkedList is empty.");
        }
        else{
        Node currNode = this.head;
        while(currNode != null){
            System.out.print(currNode.data + "->");
            currNode = currNode.next;
        }
        }
    }

    void insertLL(int index, int data){
        Node prevNode = null;
        Node insertNode = new Node(data);
        if(this.size == 0){
            this.head = this.tail = insertNode;
        }
        else{
        Node currNode = this.head;
        for(int i = 1; i < index; i++){
            prevNode = currNode;
            currNode = currNode.next;
        }
        insertNode.next = currNode;
        prevNode.next = insertNode;
        }       
        this.size += 1;
    
    }

    void removeAtFirst(){
        if(this.size == 0){
            System.out.println("The LinkedList is Empty");
        }
        else{
        this.head = this.head.next;
        this.size -= 1;
        }
    }

    void removeData(int index){
        if(this.size == 0){
            System.out.println("The LinkedList is empty");
        }
        else{
            Node currNode = this.head;
            Node prevNode = null;
            for(int i = 0; i < index - 1; i++){
                prevNode = currNode;
                currNode = currNode.next;
            }
            prevNode.next = currNode.next;
            this.size -= 1;
        }
    }

    int searchIter(int key){
        Node currNode = this.head;
        int count = 0;
        // while(key != currNode.data && currNode != null){
        //     count ++;
        //     currNode = currNode.next;
        // }
        // if(currNode == null){
        //     return -1;
        // }
        // else{
        //     return count;
        // }
        while(currNode != null){
            if(key == currNode.data){
                return count;
            }
            count ++;
            currNode = currNode.next;
        }
        return -1;
    }

    // int searchRecur(int key, Node currNode, int count){
    //     if(currNode == null){
    //         return -1;
    //     }
    //     if(currNode.data == key){
    //         return count;
    //     }
    //     return searchRecur(key, currNode.next, count + 1);

    // }

    //recursive function made better using helper functions.
    int helperFunc(int key, Node currNode, int count){ //this function is just like the searchRecur that we just made.
        if(currNode == null){
            return -1;
        }
        if (currNode.data == key){
            return count;
        }
        return helperFunc(key, currNode.next, count + 1);
    }

    int RecSearch(int key){
        int count = 0;
        Node currNode = this.head;
        return helperFunc(key, currNode, count);
    }

    void reverseLL(){
        Node prevNode = null;
        Node currNode = this.tail = this.head;
        while(currNode != null){
            Node nextNode = currNode.next;
            currNode.next = prevNode;
            prevNode = currNode;
            currNode = nextNode;

        }
        this.head = prevNode;
    }

    void delFromEnd(int pos){
        int start_pos = (this.size - pos) + 1;
        Node currNode = this.head;
        Node prevNode = null;
        for(int i = 0; i < start_pos - 1; i++){
            prevNode = currNode;
            currNode = currNode.next;
        }
        prevNode.next = currNode.next;
    }

    void delFromEnd2(int pos){
        Node start = this.head;
        Node currNode = this.head;
        Node prevNode = null;
        for(int i = 0; i < pos - 1; i++){
            currNode = currNode.next;
        }

        while(currNode.next != null){
            prevNode = start;
            start = start.next;
            currNode = currNode.next;
        }

        prevNode.next = start.next;
    }

    Node recHelper(Node currNode, int pos){
        if(pos == 1){
            return currNode;
        }
        return recHelper(currNode.next, pos - 1);
    }

    void delFromEndRec(int pos){
        Node currNode = this.head;
        pos = (this.size - pos) + 1;
        Node prevNode = recHelper(currNode, pos - 1);
        prevNode.next = prevNode.next.next;
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