#include <stdio.h>
struct node
{
    int data;
    struct node *pointer;
};
void PrintLinkedList(struct node *head)
{
    struct node *temp;
    temp = head;
    while (temp != NULL)
    {
        printf("%d - ", temp->data);
        temp = temp->pointer;
    }
    printf("\n");
}
struct node *CreateNode(int d)
{
    struct node *n;
    // int d;
    // scanf("%d", &d);
    n = malloc(sizeof(struct node));
    n->data = d;
    n->pointer = NULL;
    return n;
}

int main(void)
{
    struct node *head;
    struct node *new;
    struct node *tail;
    head = CreateNode(NULL);
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
                head = CreateNode(data);
                tail = head;
            }
            else
            {
                new = CreateNode(data);
                tail->pointer = new;
                tail = new;
            }
        }
        else if (choice == 2)
        {
            PrintLinkedList(head);
        }
        else
        {
            break;
        }
    }
}