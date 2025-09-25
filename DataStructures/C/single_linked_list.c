#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *next;
};

struct Node *createNode(int data) {
    struct Node *newNode = (struct Node *)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

struct Node *addNodeAtTop(int data, struct Node *node) {
    struct Node *newNode = createNode(data);
    newNode->next = node;
    return newNode;
}

struct Node *addData(int data, struct Node *node) {
    struct Node *newNode = createNode(data);
    if (node == NULL) {
        return newNode;
    }
    struct Node *tmp = node;
    while (tmp->next != NULL) {
        tmp = tmp->next;
    }
    tmp->next = newNode;
    return node;
}

struct Node *addNode(struct Node *newNode, struct Node *node) {
    if (node == NULL) {
        return newNode;
    }
    struct Node *tmp = node;
    while (tmp->next != NULL) {
        tmp = tmp->next;
    }
    tmp->next = newNode;
    return node;
}

struct Node *addNodeAtPos(int data, int p1, int p2, struct Node *node) {
    struct Node *tmp = node;
    while (tmp != NULL && tmp->next != NULL) {
        if (tmp->data == p1 && tmp->next->data == p2) {
            struct Node *newNode = createNode(data);
            newNode->next = tmp->next;
            tmp->next = newNode;
            return node;
        }
        tmp = tmp->next;
    }
    return node;
}

struct Node *deleteNodeAtTop(struct Node *node) {
    if (node == NULL) {
        return NULL;
    }
    struct Node *tmp = node;
    node = node->next;
    free(tmp);
    return node;
}

struct Node *deleteNodeAtEnd(struct Node *node) {
    if (node == NULL) {
        return NULL;
    }

    if (node->next == NULL) {
        free(node);
        return NULL;
    }

    struct Node *tmp = node;
    while (tmp->next->next != NULL) {
        tmp = tmp->next;
    }

    free(tmp->next);
    tmp->next = NULL;
    return node;
}

void freeAll(struct Node **node) {
    struct Node *tmp;
    while (*node != NULL) {
        tmp = *node;
        *node = (*node)->next;
        free(tmp);
    }
    *node = NULL;
}

void display(struct Node *node) {
    struct Node *tmp = node;
    while (tmp != NULL) {
        printf("%d -> ", tmp->data);
        tmp = tmp->next;
    }
    printf("NULL\n");
}

int main() {
    struct Node *head = createNode(10);

    head = addData(20, head);
    head = addData(30, head);
    head = addNode(createNode(50), head);
    head = addNodeAtTop(40, head);
    head = addNodeAtPos(12, 10, 20, head);

    display(head);

    head = deleteNodeAtEnd(head);
    display(head);

    head = deleteNodeAtTop(head);
    display(head);

    freeAll(&head);
    display(head);

    return 0;
}
