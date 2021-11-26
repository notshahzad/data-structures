#include <stdio.h>

int arr[] = {8, 423, 727, 69, 420, 1};
void PrintArray(int array[])
{
    int lenarr = (int)sizeof(arr) / (int)sizeof(arr[0]);
    for (int i = 0; i < lenarr; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int partition(int l, int r)
{
    int pivot = arr[r];
    int i = l - 1;
    for (int j = l; j < r; j++)
    {
        if (arr[j] < pivot)
        {
            i++;
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    int temp = arr[i + 1];
    arr[i + 1] = arr[r];
    arr[r] = temp;
    return i + 1;
}

int quicksort(int l, int r)
{
    if (l >= r)
        return;
    int p = partition(l, r);
    quicksort(l, p - 1);
    quicksort(p + 1, r);
}

int main(void)
{
    int lenarr = (int)sizeof(arr) / (int)sizeof(arr[0]);
    printf("before sort : ");
    PrintArray(arr);
    quicksort(0, lenarr - 1);
    printf("after sort  : ");
    PrintArray(arr);
}