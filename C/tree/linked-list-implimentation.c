#include <stdio.h>
struct Node
{
    int data;
    struct node *left;
    struct node *right;
};
typedef struct Node Node;
Node *root;
Node *CreateTreeNode(int data)
{
    if (root->data == NULL)
    {
        Node *l = malloc(sizeof(Node));
        Node *r = malloc(sizeof(Node));
        root->data = data;
        l->data = NULL;
        r->data = NULL;
        root->left = l;
        root->right = r;
        return;
    }
    Node *i = root;
    Node *temp = malloc(sizeof(Node));
    temp->data = NULL;
    while (1)
    {
        if (root->data == NULL)
        {
            root->data = data;
            Node *l = malloc(sizeof(Node));
            Node *r = malloc(sizeof(Node));
            l->data = NULL;
            r->data = NULL;
            root->left = l;
            root->right = r;

            if (temp->data > data)
            {
                temp->left = root;
            }
            else
            {
                temp->right = root;
            }
            root = i;
            return;
        }
        else if (root->data > data)
        {
            temp = root;
            root = root->left;
        }
        else if (root->data < data)
        {
            temp = root;
            root = root->right;
        }
    }
}
void Traverse(Node *root)
{
    Node *i;
    i = root->left;
    if (i->data != NULL)
    {
        Traverse(root->left);
    }
    printf("%d ", root->data);
    i = root->right;
    if (i->data != NULL)
    {
        Traverse(root->right);
    }
}
void main()
{
    root = malloc(sizeof(Node));
    root->data = NULL;
    CreateTreeNode(69);
    CreateTreeNode(5);
    CreateTreeNode(420);
    CreateTreeNode(727);
    CreateTreeNode(57);
    CreateTreeNode(201);
    CreateTreeNode(389);
    CreateTreeNode(123);
    CreateTreeNode(321);
    Traverse(root);
}