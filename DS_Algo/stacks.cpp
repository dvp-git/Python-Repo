// Implementation of Stack using arrays
# include <iostream>

# define SIZE 3

using namespace std;

class CustomStack
{
private :
    int top;
    int stack[SIZE];
public:
    CustomStack()
    {
        top = -1;
    }

    // Check if stack is empty
    bool is_empty()
    {
        if (top < 0)
            return true;
        return false;
    }

    // Return top element , ( Not pop)
    int get_top()
    {
        if (top >= 0)
            return stack[top];
        else
            cout << "Empty Stack" << endl;
            return 0;   
    }

    // Push element to stack
    void push(int n )
    {
        if (top < SIZE - 1 )
        {   
            if (top < 0)
            // Stack is empty, add first item of stack
            {
                top = top + 1;
                stack[top] = n;
            }
            else 
            {
            // Update top element 
                stack[top+1] = n;
                top++;
            }
        }
        else
            // if top exceeds size of stack
            cout << "Stack Overflow!! " << endl;
    }
    
    // Pop element from stack
    int pop()
    {
        if (top >= 0)
        {
            // Stack is not empty, update top to previous element
            int n = stack[top];
            top = top - 1;
            return n;
        }
        else
        {
            // No elements in stack
            cout << "Stack underflow!!" << endl;
            return 0;
        }
    }


};

int main () 
{
    
    CustomStack S1;
    S1.push(2);
    S1.push(3);
    S1.push(4);
    cout << S1.get_top() << endl;  // 4
    S1.push(5);   // Stack Overflow
    cout << S1.pop() << endl;
    cout << S1.pop() << endl;
    cout << S1.pop() << endl;   // Stack underflow
    cout << "Is empty? : " << S1.is_empty() << endl;
    return 0;
}