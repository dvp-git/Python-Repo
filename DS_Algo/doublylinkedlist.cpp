// Doubly linked list implementation
# include <iostream>

using namespace std;

struct node 
{
    int data;
    node *next;
    node *prev;
};

class DoublyLinkedList 
{ 
private:
    node *head,*tail;
public:
    DoublyLinkedList()
    {
        head = NULL;
        tail = NULL;
    }
    // Returns head node
    node* get_head()
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
    static void concatenate(node *a, node *b)
    {
        if (a!= NULL && b!= NULL)
        {
        // linked lists exists
            if( a->next == NULL && b->prev==NULL)
            {
            // a is tail and b is head
                a->next = b;
                b->prev = a;
            }
            else
            // If multiple nodes, traverse a till tail, and point it to b
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
        tmp->data = n;
        tmp->next = head;
        tmp->prev = NULL;
        head->prev = tmp;
        head = tmp;
    }

    // Insert node in between after node a
    void insert_after(node *a, int value)
    {
        node *tmp = new node;
        tmp->data = value;
        tmp->next = a->next;
        if (a->next == NULL)
        {
            a->next = tmp;
            tmp->prev = a;
            tail = tmp;    // Necessary to set it to tail, for display of doublylinkedlist
        }
        else
        {
            tmp->next = a->next;
            a->next->prev = tmp;
            a->next = tmp;
            tmp->prev = a;   
        }       
    }

    // Insert node at tail
    void insert_end(int n)
    {
        node *tmp = new node;
        tmp->data = n;
        tmp->next = NULL;
        tmp->prev = NULL;
        
        if (head ==NULL)
        {
            head = tmp;
            tail = tmp;
        }
        else
        {
            tail->next = tmp;
            tmp->prev = tail;
            tail = tmp;
       }
    }
    
    // Delete head node
    void del(node *tmp)
    {
        if(tmp->data == head->data)
        {
            tmp = head->next;
            tmp->prev = head->prev;
            delete head;
            head = tmp;
        }
    // Delete tail node
        else if(tmp->data == tail->data)
        {
            tmp = tail->prev;
            tmp->next = tail->next;
            delete tail;
            tail = tmp;
        }
        else
        {
            // Delete node in between
            tmp->prev->next = tmp->next;
            tmp->next->prev = tmp->prev;
        }
        
    }

};



int main() 
{
    DoublyLinkedList a,b;
    a.insert_end(1);
    // b.insert_end(70);
    // b.insert_end(90);   
    a.insert_end(2);
    a.insert_end(3);
    a.insert_end(6);
    a.insert_front(9);
    a.insert_after(a.get_head()->next->next, 100);
    a.insert_end(90);
    DoublyLinkedList::display(a.get_head());
    a.del(a.get_head()->next->next->next);
    DoublyLinkedList::concatenate(a.get_head(),b.get_head());
    DoublyLinkedList::display(a.get_head());
    return 0;
}