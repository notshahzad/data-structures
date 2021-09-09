#include<stdio.h>
int main(void) {
    int arr[100] = { 1,2,3,4,5,7,8,9,10 };
    int position;
    int element;
    scanf("%d", &position);
    scanf("%d", &element);
    int sizeofarr = (int)sizeof(arr) / (int)sizeof(arr[0]);
    arr[sizeofarr + 1] = 0;
    for (sizeofarr;sizeofarr >= position;sizeofarr--) {
        arr[sizeofarr + 1] = arr[sizeofarr];
    }
    arr[position] = element;
    for (int i = 0; i < 10;i++) {
        printf("%d ", arr[i]);
    }
}