#include <stdio.h>
struct Node
{
    int data;
    struct node *next;
};
typedef struct Node node;
node *front;
node *rear;
void enqueue(data)
{
    if (front->data == NULL)
    {
        front->data = data;
        rear = front;
        rear->next = front->next = NULL;
        return;
    }
    node *n;
    n = malloc(sizeof(node));
    n->data = data;
    rear->next = n;
    rear = n;
    rear->next = NULL;
}
void printQueue(node *frnt)
{
    node *i = frnt;
    if (i->data == NULL)
    {
        return -1;
    }
    while (1)
    {
        printf("%d ", i->data);
        if (i->next == NULL)
        {
            break;
        }
        i = i->next;
    }
}
int deQueue()
{
    if (front->data == NULL)
        return -1;
    if (front->next == NULL)
    {
        int i = front->data;
        front->data = NULL;
        return i;
    }
    node *temp = front;
    int i = temp->data;
    front = front->next;
    free(temp);
    return i;
}
void main()
{
    front = malloc(sizeof(node));
    front->data = NULL;
    enqueue(26);
    enqueue(321);
    enqueue(5134);
    enqueue(727);
    enqueue(1235);
    enqueue(253);
    enqueue(628);
    deQueue();
    deQueue();
    deQueue();
    printQueue(front);
}