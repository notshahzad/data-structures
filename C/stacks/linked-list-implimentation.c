#include <stdio.h>
#include <stdlib.h>
struct node
{
    int data;
    struct node *next;
    struct node *previous;
};
struct node *head;
struct node *new;
struct node *tail;
void PrintStack(struct node *head)
{
    struct node *temp;
    temp = head;
    while (temp != NULL)
    {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}
int isEmpty(struct node *head, struct node *tail)
{
    if (head == tail)
        return 1;
    else
        return 0;
}
struct node *CreateStackNode(int d)
{
    struct node *n;
    n = malloc(sizeof(struct node));
    n->data = d;
    n->next = NULL;
    n->previous = NULL;
    return n;
}
int pop()
{
    if (isEmpty(head, tail) == 1)
    {
        int r;
        r = head->data;
        free(head);
        head = CreateStackNode(NULL);
        return r;
    }
    struct node *temp;
    temp = tail;
    int r = temp->data;
    tail = tail->previous;
    tail->next = NULL;
    free(temp);
    return r;
}
int main(void)
{

    head = CreateStackNode(NULL);
    int choice = 1;
    while (1)
    {
        scanf("%d", &choice);
        if (choice == 1)
        {
            int data;
            scanf("%d", &data);
            if (head->data == NULL)
            {
                head = CreateStackNode(data);
                tail = head;
            }
            else
            {
                new = CreateStackNode(data);
                tail->next = new;
                new->previous = tail;
                tail = new;
            }
        }
        else if (choice == 2)
        {
            int el = pop(tail);
            printf("element %d popped from the stack...\n", el);
        }

        else if (choice == 3)
        {
            PrintStack(head);
        }
        else
        {
            break;
        }
    }
}