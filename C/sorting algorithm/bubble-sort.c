#include<stdlib.h>
int main(void) {
    int arr[5] = { 8,727,69,420,1 };
    int sizeofarr = (int)sizeof(arr) / (int)sizeof(arr[0]);
    for (int i = 0;i < sizeofarr;i++) {
        for (int j = 0; j < sizeofarr; j++)
        {
            if (arr[i] < arr[j])
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

}
