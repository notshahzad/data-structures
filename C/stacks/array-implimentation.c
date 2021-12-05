#include <stdio.h>
int stack[8];
int top = -1;
max = 8;
void push(int data)
{
    if (top == max - 1)
        return -1;
    top++;
    stack[top] = data;
}
int pop()
{
    if (isEmpty())
    {
        printf("stack is empty...");
        return -1;
    }
    top--;
    return top + 1;
}
int isEmpty()
{
    return (top == -1);
}
void printStack()
{
    int i = 0;
    if (top == -1)
    {
        printf("err");
        return;
    }
    while (i != top + 1)
    {
        printf("%d\n", stack[i]);
        i++;
    }
    printf("\n");
}
void main()
{
    push(5);
    printStack();
    pop();
}