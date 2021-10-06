#include <stdio.h>
int main(int argc, char const *argv[])
{
    int arr[5] = {69, 8, 1, 727, 420};
    int sizeofarr = (int)sizeof(arr) / (int)sizeof(arr[0]);
    for (int i = 0; i < sizeofarr; i++)
    {
        int sorted = i;
        for (int j = sorted; j < sizeofarr; j++)
        {
            if (arr[i] > arr[j])
            {
                int temp = 0;
                temp = arr[j];
                arr[j] = arr[i];
                arr[i] = temp;
            }
        }
    }
    for (int i = 0; i < sizeofarr; i++)
    {
        printf("%d ", arr[i]);
    }

    return 0;
}
