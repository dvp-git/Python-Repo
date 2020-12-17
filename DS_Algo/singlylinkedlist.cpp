// Singly linked list implementation
#include <iostream>

using namespace std;

struct node
{
    int data;
    node *next;
};

class linked_list
{
private:
    node *head,*tail;
public:
    linked_list()
    {
        head = NULL;
        tail = NULL;
    }
    // Returns head node
    node* gethead()
    {
        return head;
    }

    // Traversing the linked list using recursion
    static void display(node *head)
    {
        if(head == NULL)
        {
        // No nodes
            cout << "NULL" << endl;
        }
        else
        {
        // recursion
            cout << head->data << endl;
            display(head->next);
        }
    }
    // Concatenation of linked list . head node a and head node b
    static void concatenate(node *a,node *b)
    {
        if( a != NULL && b!= NULL )
        {
        // linked lists exists
            if (a->next == NULL)
                a->next = b;
            else
            // recursion to travel till a points to tail
                concatenate(a->next,b);
        }
        else
        {
            cout << "Either a or b is NULL\n";
        }
    }

    // Insert node at head
    void insert_front(int n)
    {
        node *tmp = new node;
        tmp -> data = n;
        tmp -> next = head;
        head = tmp;
    }

    // Insert node in between after node a
    void insert_after(node *a, int value)
    {
        node* p = new node;
        p->data = value;
        p->next = a->next;
        a->next = p;

    }
    // Insert node at tail
    void insert_end(int n)
    {
        node *tmp = new node;
        tmp->data = n;
        tmp->next = NULL;

        if(head == NULL)
        {
            head = tmp;
            tail = tmp;
        }
        else
        {
            tail->next = tmp;
            tail = tail->next;
        }
    }
    // Delete the node after "before_del" node
    void del(node *before_del)
    {
        node* temp;
        temp = before_del->next;
        before_del->next = temp->next;
        delete temp;
    }
};
int main()
{
    linked_list a;
    a.insert_end(1);
    a.insert_end(2);
    a.insert_front(3);
    a.insert_end(5);
    a.insert_end(15);
    a.insert_after(a.gethead()->next, 106);
    a.del(a.gethead());
    linked_list::display(a.gethead());
    return 0;
}