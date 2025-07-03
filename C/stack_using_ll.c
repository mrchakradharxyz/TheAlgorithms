#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *next;
};

/*
Create a new node with empty next node
Usage:
    struct Node *newNode = createNode(60);
*/
struct Node *createNode(int data){
    struct Node *list = (struct Node*)malloc(sizeof(struct Node));
    list->data = data;
    list->next = NULL;
    return list;
}

/*
POP the data from the given Linked List
Usage:
    struct Node *list = createNode(60);
    pop(list);
*/
struct Node *pop(struct Node *list) {
    struct Node *newlist = (*list).next;
    free(list);
    return newlist;
}

/*
PUSH the data into the given Linked List
Usage:
    struct Node *stack = push(10, createNode(60));
*/
struct Node *push(int data, struct Node *list){
    struct Node *newNode = createNode(data);
    newNode->next = list;
    return newNode;
}

/*
Display the data in the stack
Usage:
    display(list);
*/
void display(struct Node* list){
    while(list){
        printf("%d->",list->data);
        list = list->next;
    }
    printf("NULL\n");
}

/*
PEEK: Display's the data which is top of the stack
Usage:
    peek(list);
*/
void peek(struct Node *list){
    if (list==NULL){
        printf("Stack is empty");
    }
    printf("%d",list->data);
}

int main(){
    struct Node *list = createNode(10);
    list = push(9,list);
    display(list);
    list = push(8,list);
    display(list);
    list = pop(list);
    display(list);
    peek(list);
}
