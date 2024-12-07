#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
typedef struct node {
  int val;
  struct node *next;
} node;
void print_linked_list(node *head) {
  node *temp;
  temp = head;
  while (temp != NULL) {
    printf("%d - ", temp->val);
    temp = temp->next;
  }
  printf("\n");
}
node *create_node(int data) {
  node *n;
  n = malloc(sizeof(node));
  n->val = data;
  n->next = NULL;
  return n;
}
// note(shahzad): should allocate statically but idk
node *node_new(int data) {
  node *n = malloc(sizeof(*n));
  n->val = data;
  n->next = NULL;
  return n;
}
void node_link(node *n1, node *n2) { n1->next = n2; }

typedef struct ll {
  node *head;
  node *tail;
} ll;
void ll_append(ll *self, int data) {
  node *n = node_new(data);
  if (self->head == NULL) {
    self->head = self->tail = n;
  } else {
    node_link(self->tail, n);
    self->tail = n;
  }
}

int main(void) {
  ll ll1 = {0};
  ll_append(&ll1, 1);
  ll_append(&ll1, 2);
  ll_append(&ll1, 3);
  ll_append(&ll1, 4);
  ll_append(&ll1, 5);
}
