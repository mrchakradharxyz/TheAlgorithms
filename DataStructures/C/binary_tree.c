#include <stdio.h>
#include <stdlib.h>

#define SIZE 100

// Node structure
struct Node {
    int data;
    struct Node* left;
    struct Node* right;
};

// Create a new node
struct Node* createNode(int data) {
    struct Node* node = (struct Node*)malloc(sizeof(struct Node));
    node->data = data;
    node->left = NULL;
    node->right = NULL;
    return node;
}

// Simple queue implementation for level-order insertion
struct Node* queue[SIZE];
int front = -1, rear = -1;

void enqueue(struct Node* node) {
    if (rear == SIZE - 1) return;
    if (front == -1) front = 0;
    queue[++rear] = node;
}

struct Node* dequeue() {
    if (front == -1 || front > rear) return NULL;
    return queue[front++];
}

int isEmpty() {
    return front == -1 || front > rear;
}

// Insert node in Binary Tree using level order
struct Node* insert(int data, struct Node* root) {
    struct Node* newNode = createNode(data);
    if (root == NULL) {
        return newNode;
    }
    enqueue(root);
    while (!isEmpty()) {
        struct Node* temp = dequeue();
        if (temp->left == NULL) {
            temp->left = newNode;
            break;
        } else {
            enqueue(temp->left);
        }
        if (temp->right == NULL) {
            temp->right = newNode;
            break;
        } else {
            enqueue(temp->right);
        }
    }
    return root;
}

void traverse(struct Node* root) {
    if (root == NULL) return;
    traverse(root->left);
    printf("%d ", root->data);
    traverse(root->right);
}

struct Node* delete(struct Node* root, int data) {
    printf("Delete not implemented.\n");
    return root;
}

// Main
int main() {
    struct Node* root = NULL;

    root = insert(10, root);
    root = insert(20, root);
    root = insert(30, root);
    root = insert(40, root);
    root = insert(50, root);

    printf("Inorder Traversal: ");
    traverse(root);
    printf("\n");

    return 0;
}
