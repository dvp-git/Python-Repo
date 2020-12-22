// Circular LinkedList
#include <iostream>

using namespace std;

struct node 
{
    int data;
    node *next;
};

class CircularList
{
private :
    node *last;
public:
    CircularList()
    {
        last = NULL;
    }

    // Returns the last node
    node* get_last()
    {
        return last;
    }

    // Traversing the circular linked list 
    static void display(node *last)
    {
        //no nodes
        if(last==NULL)
            cout<<"NULL"<<endl;
        else
        {
            node *tmp = new node;
            // Set first node to last , and traverse it
            tmp = last;
            cout << tmp->data <<endl;
            // Setting to first node
            tmp = tmp->next;
            while(tmp!= last)
            // Iterate till last node
            {
            // recursion
            cout << tmp->data <<endl;
            tmp = tmp->next;
            }
        }
    }
    // Insert node at beginning of the list 
    void insert_front(int n)
    {
        node *tmp = new node;
        node *a = new node;
        tmp->data = n;
        if (last==NULL)
        {
            // If list is empty, set last node and 
            tmp->next = tmp;
            last = tmp;
        }
        else if (last!= NULL)
        {
            a = last;
            while(a->next != last)
                a = a->next;
             tmp->next = last->next;
             last->next = tmp;
        }
    }
    
    // Insert node after another existing one ( no updating last pointer)
    void insert_after(node* a, int n)
    {
        node *tmp = new node;
        tmp->data = n;
        tmp->next = a->next;
        a->next = tmp;
        if (a->next == NULL)
            last = tmp;
    }   


    // Deleting a node from a circular linked list.
    void del(node* a)
    {
        node *tmp = new node;
        tmp = last;
        while(tmp->next != a)
            tmp = tmp->next;
        // if node to be deleted is last , then
        if (a == last)
            {
                // a) either last is the only node (single node)
                if (a->next == a)
                    last = NULL;
                else 
                    {
                        // b) last-> next points to another node 
                        tmp->next = a->next;
                        last = tmp;
                    } 
            }
        else
            // node is not last node
            tmp->next = a->next;
    }

};

int main()
{
    CircularList C1;
    C1.insert_front(5);   // 5 [ last ]
    C1.insert_front(6);   // 6--> 5
    C1.insert_front(7);  //  7--> 6--> 5
    C1.insert_after(C1.get_last(),200);  //  200--> 7--> 6--> 5
    C1.insert_after(C1.get_last()->next->next,500);  //   200--> 7--> 500 --> 6--> 5 
    CircularList::display(C1.get_last());   //   200--> 7--> 500 --> 6--> 5 
    C1.del(C1.get_last()->next->next->next->next);  //   deletes 6
    cout << "After delete" << endl;
    CircularList::display(C1.get_last()); //   200--> 7--> 500 -->s 5 
    return 0;
}



