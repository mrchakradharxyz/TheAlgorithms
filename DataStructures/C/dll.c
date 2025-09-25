#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *prev;
    struct Node *next;
};

struct Node* createNode(int data) {
    struct Node *newNode = (struct Node *)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->prev = NULL;
    newNode->next = NULL;
    return newNode;
}
struct Node* addDataAtTop(int data, struct Node* node) {
    struct Node* newNode = createNode(data);
    newNode->next = node;
    if (node != NULL) {
        node->prev = newNode;
    }
    return newNode;
}

struct Node* addDataAtEnd(int data, struct Node* node) {
    struct Node* newNode = createNode(data);
    if (node == NULL) {
        return newNode;
    }
    struct Node* tmp = node;
    while (tmp->next != NULL) {
        tmp = tmp->next;
    }
    tmp->next = newNode;
    newNode->prev = tmp;
    return node;
}

struct Node* addAtPos(int data, int p1, int p2, struct Node* node) {
    struct Node* newNode = createNode(data);
    if (node == NULL) {
        return newNode;
    }
    struct Node* tmp = node;
    while (tmp->next != NULL) {
        if (tmp->data == p1 && tmp->next->data == p2) {
            newNode->next = tmp->next;
            newNode->prev = tmp;
            tmp->next->prev = newNode;
            tmp->next = newNode;
            return node;
        }
        tmp = tmp->next;
    }
    printf("Position with (%d, %d) not found.\n", p1, p2);
    return node;
}

struct Node* deleteAtTop(struct Node* node) {
    if (node == NULL) {
        return NULL;
    }
    struct Node *tmp = node;
    node = node->next;
    if (node != NULL) {
        node->prev = NULL;
    }
    free(tmp);
    return node;
}

struct Node* deleteAtEnd(struct Node* node) {
    if (node == NULL) {
        return NULL;
    }
    if (node->next == NULL) {
        free(node);
        return NULL;
    }
    struct Node* tmp = node;
    while (tmp->next != NULL) {
        tmp = tmp->next;
    }
    tmp->prev->next = NULL;
    free(tmp);
    return node;
}

struct Node* deleteAtPos(int p1, struct Node* node) {
    if (node == NULL) {
        return NULL;
    }
    struct Node* tmp = node;
    while (tmp != NULL) {
        if (tmp->data == p1) {
            // Head node
            if (tmp->prev == NULL) {
                node = tmp->next;
                if (node != NULL) {
                    node->prev = NULL;
                }
            }
            else if (tmp->next == NULL) {
                tmp->prev->next = NULL;
            }
            else {
                tmp->prev->next = tmp->next;
                tmp->next->prev = tmp->prev;
            }
            free(tmp);
            return node;
        }
        tmp = tmp->next;
    }
    return node;
}

void display(struct Node* node) {
    if (node == NULL) {
        printf("NULL\n");
        return;
    }
    struct Node* tmp = node;
    while (tmp != NULL) {
        printf("%d", tmp->data);
        if (tmp->next != NULL) {
            printf(" <-> ");
        }
        tmp = tmp->next;
    }
    printf(" -> NULL\n");
}

int main() {
    struct Node* node = NULL;

    node = addDataAtTop(30, node);
    node = addDataAtTop(20, node);
    node = addDataAtTop(10, node);
    node = addDataAtEnd(40, node);
    node = addDataAtEnd(50, node);

    printf("Initial List: ");
    display(node);

    node = addAtPos(25, 20, 30, node);
    printf("After Adding 25 between 20 and 30: ");
    display(node);

    node = deleteAtTop(node);
    printf("After Deleting Top: ");
    display(node);
    node = deleteAtEnd(node);
    printf("After Deleting End: ");
    display(node);

    node = deleteAtPos(30, node);
    printf("After Deleting 30: ");
    display(node);

    return 0;
}
