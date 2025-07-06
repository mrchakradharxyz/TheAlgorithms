#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SIZE 100

// Define Node
struct Node {
    int data;
    struct Node* left;
    struct Node* right;
};

// Queue for level order traversal
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

// Create a new node
struct Node* createNode(int data) {
    struct Node* node = (struct Node*)malloc(sizeof(struct Node));
    node->data = data;
    node->left = NULL;
    node->right = NULL;
    return node;
}

// Insert node into Binary Tree using Level Order
struct Node* insert(int data, struct Node* root) {
    struct Node* newNode = createNode(data);
    if (root == NULL) return newNode;

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

// Inorder traversal (Left, Root, Right)
void traverse(struct Node* root) {
    if (root == NULL) return;
    traverse(root->left);
    printf("%d ", root->data);
    traverse(root->right);
}

// Find the deepest and rightmost node
struct Node* getDeepestRightmostNode(struct Node* root) {
    if (root == NULL) return NULL;

    enqueue(root);
    struct Node* temp = NULL;

    while (!isEmpty()) {
        temp = dequeue();
        if (temp->left) enqueue(temp->left);
        if (temp->right) enqueue(temp->right);
    }

    return temp;
}

// Delete the deepest node
void deleteDeepestNode(struct Node* root, struct Node* delNode) {
    enqueue(root);

    while (!isEmpty()) {
        struct Node* temp = dequeue();

        if (temp->left) {
            if (temp->left == delNode) {
                free(temp->left);
                temp->left = NULL;
                return;
            } else {
                enqueue(temp->left);
            }
        }

        if (temp->right) {
            if (temp->right == delNode) {
                free(temp->right);
                temp->right = NULL;
                return;
            } else {
                enqueue(temp->right);
            }
        }
    }
}

// Delete a node with given value
struct Node* delete(struct Node* root, int key) {
    if (root == NULL) return NULL;

    if (root->left == NULL && root->right == NULL) {
        if (root->data == key) {
            free(root);
            return NULL;
        } else {
            return root;
        }
    }

    struct Node* keyNode = NULL;
    enqueue(root);

    struct Node* temp;
    while (!isEmpty()) {
        temp = dequeue();

        if (temp->data == key)
            keyNode = temp;

        if (temp->left)
            enqueue(temp->left);
        if (temp->right)
            enqueue(temp->right);
    }

    if (keyNode != NULL) {
        struct Node* deepest = getDeepestRightmostNode(root);
        keyNode->data = deepest->data;
        deleteDeepestNode(root, deepest);
    }

    return root;
}

// Main function
int main() {
    struct Node* root = NULL;

    root = insert(10, root);
    root = insert(20, root);
    root = insert(30, root);
    root = insert(40, root);
    root = insert(50, root);

    printf("Inorder traversal before deletion:\n");
    traverse(root);

    printf("\nDeleting 30...\n");
    root = delete(root, 30);

    printf("Inorder traversal after deletion:\n");
    traverse(root);
    printf("\n");

    return 0;
}
