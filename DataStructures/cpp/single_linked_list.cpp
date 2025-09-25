#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
};

class SingleLinkedList {
private:
    Node* head;

public:
    SingleLinkedList(int data) {
        if(data){
            head = new Node{data, nullptr};
        }
        else {
            cout << "initial data missing";
        }
    }

    ~SingleLinkedList() {
        Node* current = head;
        while (current != nullptr) {
            Node* next = current->next;
            delete current;
            current = next;
        }
    }

    void print() {
        Node* current = head;
        while (current != nullptr) {
            cout << current->data << " ";
            current = current->next;
        }
        cout << endl;
    }

    void addAtTop(int data) {
        Node* newNode = new Node{data, head};
        head = newNode;
    }

    void append(int data){
        Node *cur = head;
        while (cur->next!=nullptr){
            cur=cur->next;
        }
        Node* newNode = new Node{data, nullptr};
        cur->next = newNode;
    }

    void addInBTW(int p1, int data, int p2) {
        if (head == nullptr) {
            return;
        }
        Node* cur = head;
        while (cur != nullptr && cur->next != nullptr) {
            if (cur->data == p1 && cur->next->data == p2) {
                Node* newNode = new Node{data, cur->next};
                cur->next = newNode;
                // cout << "Insertion Done in BTW\n";
                return;
            }
            cur = cur->next;
        }
        cout << "Could not find " << p1 << " and " << p2 << " in sequence." << endl;
    }

    void insert(int index,int data){
        if(index==0){
            addAtTop(data);
            return;
        }
        if (index==-1){
            append(data);
        }
        Node *cur = head;
        for(int i=0; i<index-1;i++){
            cur=cur->next;
        }
        if(cur==nullptr){
            cout << "List out of index";
            return;
        }
        Node *newnode = new Node{data,cur->next};
        cur->next = newnode;
    }

    void deleteAtTop(){
        Node *newnode = head->next;
        delete head;
        head = newnode;
    }

    void pop(){
        Node *cur = head;
        while(cur->next->next!=nullptr){
            cur = cur->next;
        }
        delete cur->next;
        cur->next = nullptr;

    }

    void pop(int index){
        if(index==0){
            deleteAtTop();
            return;
        }

        if(index==-1){
            pop();
            return;
        }

        Node *cur = head;

        for(int i=0;cur!=nullptr && i<index-1;i++){
            cur = cur->next;
        }

        if (cur == nullptr || cur->next == nullptr) {
                return;
            }

        Node *tmp = cur->next;
        cur->next = tmp->next;
        delete tmp;
        return;
    }

    void remove(int data){
        if (head->data == data) {
            deleteAtTop();
            return;
        }
        Node *cur = head;
        while(cur->next!=nullptr && cur->next!=nullptr){
            if(cur->next->data == data){
                Node *tmp = cur->next;
                cur->next = tmp->next;
                delete tmp;
            }
            else{
            cur = cur->next;
        }}
    }
};

int main() {
    SingleLinkedList list(2);
    list.print();

    list.addAtTop(1);
    list.print();

    list.append(3);
    list.print();

    list.insert(3, 5);
    list.print();

    list.addInBTW(3, 4, 5);
    list.print();

    list.deleteAtTop();
    list.print();

    list.pop();
    list.print();

    list.pop(2);
    list.print();

    list.remove(3);
    list.print();

    return 0;
}
