#include <stdio.h>
int main(void) {
    int arr[] = { 1,2,3,4,5,6,7,8,9 };
    int pos;
    scanf("%d", &pos);
    int arrlength = (int)sizeof(arr) / (int)sizeof(arr[0]);
    for (pos;pos <= arrlength;pos++) {
        arr[pos] = arr[pos + 1];
    }
    for (int i = 0;i <= arrlength;i++) {
        printf("%d ", arr[i]);
    }
}