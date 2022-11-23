#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
struct Node {
  char c;
  char childcount;
  struct Node *childs[];
};
struct Node *ROOT = NULL;

void printTreeIguess(struct Node *root) {
  printf("%c ", root->c);
  if (root->childcount != 0) {
    for (int i = 0; i < root->childcount; i++) {
      printTreeIguess(root->childs[i]);
    }
  }
}
void init_tree(struct Node **root) {
  (*root) = malloc(sizeof(struct Node));
  (*root)->c = 0;
  (*root)->childcount = 0;
  *((*root)->childs) = NULL;
}
struct Node **AddNode(struct Node **root, char data) {
  for (int i = 0; i < (*root)->childcount; i++) {
    if ((*root)->childs[i]->c == data) {
      return &((*root)->childs[i]);
    }
  }
  (*root)->childcount++;
  *((*root)->childs) =
      realloc(*((*root)->childs), sizeof(struct Node *) * (*root)->childcount);
  (*root)->childs[(*root)->childcount - 1] = malloc(sizeof(struct Node));
  ((*root)->childs[(*root)->childcount - 1])->c = data;
  ((*root)->childs[(*root)->childcount - 1])->childcount = 0;
  return &((*root)->childs[(*root)->childcount - 1]);
  return NULL;
}

void CreateTreeFromString(char *data, struct Node **root) {
  struct Node **i = root;
  size_t len = strlen(data);
  for (size_t index = 0; index < len; index++) {
    i = AddNode(i, data[index]);
    if (i == NULL) {
      return;
    }
  }
}
int main(void) {
  char *t1 = "okeh";
  char *t2 = "okehg";
  char *t3 = "okaa";
  init_tree(&ROOT);
  CreateTreeFromString(t1, &ROOT);
  CreateTreeFromString(t2, &ROOT);
  CreateTreeFromString(t3, &ROOT);
  return 0;
}
