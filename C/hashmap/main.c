#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<stddef.h>
#include<assert.h>
#define key_int 0x01 
#define key_string 0x02 
struct Map{
  size_t size;
  struct keyValue **KeyValues;
};
struct keyValue{
  char *key;
  int hash;
  union{
    int _int;
    char *_string;
  };
  int type;
  struct keyValue* next;
};
int CreateAsciiHash(char *str){
  size_t Hash=0;
  for (size_t i = 0; i < strlen(str); i ++){
    Hash += str[i];
  }
  return Hash;
}
char *GetValue_String(struct keyValue *keyvalue){
  if (keyvalue->type == key_string){
    return keyvalue->_string;
  }
  return NULL;
}
int GetValue_int(struct keyValue *keyvalue){
  if (keyvalue->type){
    return keyvalue->_int;
  }
  return 0;
}
void printValue(struct keyValue *pair){
  switch(pair->type){
    case(key_int):
      printf("%d\n",pair->_int);
      break;
    case(key_string):
      printf("%s\n",pair->_string);
      break;
  }
  return;
}
int get_type(struct keyValue *pair){
  return pair->type;
}
void CreateKeyValuePair_int(struct keyValue **keyvalnode,char *strkey,size_t hash,int value){
  *keyvalnode = malloc(sizeof(struct keyValue));
  (* keyvalnode )->key = strkey;
  (* keyvalnode )->hash= hash;
  (* keyvalnode )->type = key_int;
  (* keyvalnode )->_int= value;
  (* keyvalnode )->next= NULL;
  return;
}
void CreateKeyValuePair_string(struct keyValue **keyvalnode,char *strkey,size_t hash,char *strval){
  *keyvalnode = malloc(sizeof(struct keyValue));
  (* keyvalnode )->key = strkey;
  (* keyvalnode )->hash= hash;
  (* keyvalnode )->type = key_string;
  (* keyvalnode )->_string = strval;
  (* keyvalnode )->next= NULL;
  return;
}
void InsertKeyValuePair_int(struct Map **map,char *key,int value){
  char *strkey= malloc(strlen(key));
  memcpy(strkey,key,strlen(key));
  size_t hash = CreateAsciiHash(key);
  size_t index = ( hash / (*map)->size ) % 10;
  struct keyValue **keyvalnode =(( (*map)->KeyValues ) + index  ); 
  if (*keyvalnode == NULL) {
    CreateKeyValuePair_int(keyvalnode,strkey,hash,value);
  }else{
   struct keyValue *i = *keyvalnode; 
    while (1){
      if (strcmp(strkey,i->key)){
        printf("can't insert on same key\n");
        break;
      }
      if (i->next == NULL){
        CreateKeyValuePair_int(keyvalnode,strkey,hash,value);
        break;
      }
      i = i->next;
    }
  }
}
void InsertKeyValuePair_string(struct Map **map,char *key,char *value){
  char *strval = malloc(strlen(value));
  memcpy(strval,value,strlen(value));
  char *strkey= malloc(strlen(key));
  memcpy(strkey,key,strlen(key));
  size_t hash = CreateAsciiHash(key);
  size_t index = ( hash / (*map)->size ) % 10;
  struct keyValue **keyvalnode =(( (*map)->KeyValues ) + index  ); 
  if (*keyvalnode == NULL) {
    CreateKeyValuePair_string(keyvalnode,strkey,hash,strval);
  }else{
   struct keyValue *i = *keyvalnode; 
    while (1){
      if (strcmp(strkey,i->key) == 0){
        printf("can't insert on same key\n");
        break;
      }else{
        printf("%s %ld\n%s %ld",strkey,strlen(strkey),i->key,strlen(i->key));

      }
      if (i->next == NULL){
        CreateKeyValuePair_string(keyvalnode,strkey,hash,strval);
        break;
      }
      i = i->next;
    }
  }
}
int retintvaluefromkey(struct Map **map,char *key,int *res){
  size_t hash = CreateAsciiHash(key);
  size_t index = ( hash / (*map)->size ) % 10;
  struct keyValue *keyvalnode =*(( (*map)->KeyValues ) + index  ); 
  while (keyvalnode != NULL){
    if (strcmp(key,keyvalnode->key) == 0){
      *res = keyvalnode->_int;
      return 1;
    }
    keyvalnode = keyvalnode->next;
  }
  return 0;
}
int retstringvaluefromkey(struct Map **map,char *key,char **buffer,char mode){
  size_t hash = CreateAsciiHash(key);
  size_t index = ( hash / (*map)->size ) % 10;
  struct keyValue *keyvalnode =*(( (*map)->KeyValues ) + index  ); 
  while (keyvalnode != NULL){
    if (strcmp(key,keyvalnode->key) == 0){
      if (mode == 'd'){
        *buffer = keyvalnode->_string;
        return 1;
      }else if (mode == 'c'){
        *buffer = malloc(strlen(keyvalnode->_string));
        strcpy(*buffer,keyvalnode->_string);
        return 1;
      }else{
        assert("undefined Mode");
        return 0;
      }
    keyvalnode = keyvalnode->next;
    }
  }
  return 0;
}

void init_hashMap(struct Map** map,size_t size){
  *map = malloc(sizeof(struct Map));
  ( *map )->KeyValues = malloc(sizeof(struct keyValue*) * size);
  memset( ( *map )->KeyValues,0,size);
  (* map )->size = size;
  return ;
}
int main(void){
  struct Map *map;
  init_hashMap(&map,10);
  char *buff1;
  InsertKeyValuePair_string(&map,"name","jhon");
  retstringvaluefromkey(&map,"name",&buff1,'d');
  printf("%s\n",buff1);
  InsertKeyValuePair_int(&map,"marks",69);
  int buff;
  retintvaluefromkey(&map,"marks",&buff);
  printf("%d\n",buff);
  return 0;
}
