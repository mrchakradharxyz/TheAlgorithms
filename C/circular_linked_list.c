#include <stdio.h>
#include <stdlib.h>

// Define the structure of a Node
struct Node {
    int data;
    struct Node* next;
};

// Create a new node with given data
struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    if (!newNode) {
        printf("Memory allocation failed\n");
        exit(1);
    }
    newNode->data = data;
    newNode->next = newNode;
    return newNode;
}

// Insert at the end of the circular linked list
struct Node* insertEnd(struct Node* head, int data) {
    struct Node* newNode = createNode(data);

    if (head == NULL) {
        return newNode;
    }

    struct Node* temp = head;
    while (temp->next != head)
        temp = temp->next;

    temp->next = newNode;
    newNode->next = head;

    return head;
}

// Insert at the beginning
struct Node* insertBeginning(struct Node* head, int data) {
    struct Node* newNode = createNode(data);

    if (head == NULL) {
        return newNode;
    }

    struct Node* temp = head;
    while (temp->next != head)
        temp = temp->next;

    temp->next = newNode;
    newNode->next = head;

    return newNode;  // New head
}

// Delete a node with given key
struct Node* deleteNode(struct Node* head, int key) {
    if (head == NULL) return NULL;

    struct Node *curr = head, *prev = NULL;

    // Special case: deleting head node
    if (head->data == key) {
        if (head->next == head) {
            free(head);
            return NULL;
        }

        // Find last node to update its next
        struct Node* temp = head;
        while (temp->next != head)
            temp = temp->next;

        temp->next = head->next;
        struct Node* toDelete = head;
        head = head->next;
        free(toDelete);
        return head;
    }

    // Deleting non-head node
    do {
        prev = curr;
        curr = curr->next;
        if (curr->data == key) {
            prev->next = curr->next;
            free(curr);
            return head;
        }
    } while (curr != head);

    printf("Node with data %d not found.\n", key);
    return head;
}

// Display the circular linked list
void display(struct Node* head) {
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }

    struct Node* temp = head;
    do {
        printf("%d -> ", temp->data);
        temp = temp->next;
    } while (temp != head);
    printf("(head)\n");
}

// Count the number of nodes in the circular list
int size(struct Node* head) {
    if (head == NULL) return 0;

    int count = 0;
    struct Node* temp = head;
    do {
        count++;
        temp = temp->next;
    } while (temp != head);

    return count;
}

int main() {
    struct Node* head = NULL;

    head = insertEnd(head, 10);
    head = insertEnd(head, 20);
    head = insertEnd(head, 30);
    head = insertBeginning(head, 5);

    printf("Circular Linked List:\n");
    display(head);

    printf("Size of list: %d\n", size(head));

    head = deleteNode(head, 20);
    printf("After deleting 20:\n");
    display(head);

    head = deleteNode(head, 5);
    printf("After deleting 5 (head):\n");
    display(head);

    return 0;
}
