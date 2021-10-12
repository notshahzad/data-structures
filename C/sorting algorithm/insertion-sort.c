#include <stdio.h>
int main(void)
{
    int arr[5] = {8, 727, 69, 420, 1};
    int sizeofarr = (int)sizeof(arr) / (int)sizeof(arr[0]);
    for (int i = 1; i < sizeofarr; i++)
    {
        int j = i;
        int crnt = arr[i];
        while (j > 0 && crnt < arr[j - 1])
        {
            arr[j] = arr[j - 1];
            j -= 1;
        }
        arr[j] = crnt;
    }
    for (int i = 0; i < sizeofarr; i++)
    {
        printf("%d\n", arr[i]);
    }
}