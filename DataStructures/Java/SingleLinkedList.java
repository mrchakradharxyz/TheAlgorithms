// Single Linked List implementation in Java (java 21.0.5)
// java 21.0.5 2024-10-15 LTS
// Java(TM) SE Runtime Environment (build 21.0.5+9-LTS-239)
// Java HotSpot(TM) 64-Bit Server VM (build 21.0.5+9-LTS-239, mixed mode, sharing)

package Java;

interface LinkedList {
    void addAtTop(int data); // Insert data at beginning
    void addAtEnd(int data); // Insert data at End
    void addAtPos(int data, int pos); // Insert data at Position
    void deleteAtTop(); // Delete data at Top
    void deleteAtEnd(); // Delete data at End
    void deleteAtPos(int pos); // Delete data at Position
    void display(); //  Display the list
}

// Node: The SINGLE~LINKED~LIST
class Node {

    int data;
    Node next;

    public Node(int data) {
        this.data = data;
        this.next = null;
    }
}

class SingleLinkedListImpl implements LinkedList {

    // Single Linked List Implementation
    // Usage: SingleLinkedListImpl list = new SingleLinkedListImpl();

    // The First Node
    private Node head;

    // Insert data at top
    // Usage: list.addAtTop(10)
    public void addAtTop(int data) {
        Node newNode = new Node(data);
        newNode.next = head;
        head = newNode;
    }

    // Insert data at end
    // list.addAtEnd(20);
    public void addAtEnd(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
            return;
        }
        Node temp = head;
        while (temp.next != null) temp = temp.next;
        temp.next = newNode;
    }

    // Insert data at Pos
    // list.addAtPos(15, 2);
    public void addAtPos(int data, int pos) {
        if (pos < 0) return;
        if (pos == 0) {
            addAtTop(data);
            return;
        }

        Node newNode = new Node(data);
        Node temp = head;
        for (int i = 0; i < pos - 1 && temp != null; i++) {
            temp = temp.next;
        }
        if (temp == null) return;
        newNode.next = temp.next;
        temp.next = newNode;
    }

    // Delete data at Top
    // list.deleteAtTop();
    public void deleteAtTop() {
        if (head != null) head = head.next;
    }

    // Delete data at end
    // list.deleteAtEnd()
    public void deleteAtEnd() {
        if (head == null) return;
        if (head.next == null) {
            head = null;
            return;
        }
        Node temp = head;
        while (temp.next.next != null) {
            temp = temp.next;
        }
        temp.next = null;
    }

    // Delete data at Position
    // list.deleteAtPos(1);
    public void deleteAtPos(int pos) {
        if (pos < 0 || head == null) return;
        if (pos == 0) {
            deleteAtTop();
            return;
        }
        Node temp = head;
        for (int i = 0; i < pos - 1 && temp.next != null; i++) {
            temp = temp.next;
        }
        if (temp.next == null) return;
        temp.next = temp.next.next;
    }

    // Display the list
    // list.display();
    public void display() {
        Node temp = head;
        while (temp != null) {
            System.out.print(temp.data + " -> ");
            temp = temp.next;
        }
        System.out.println("null");
    }
}

// Main class
public class SingleLinkedList {

    public static void main(String[] args) {
        System.out.println("Linked List Demo:");
        SingleLinkedListImpl list = new SingleLinkedListImpl();

        list.addAtTop(10);
        list.addAtEnd(20);
        list.addAtEnd(30);
        list.addAtPos(15, 1);
        list.display();

        list.deleteAtTop();
        list.deleteAtEnd();
        list.deleteAtPos(1);
        list.display();
    }
}
