#include<stdio.h>
int main(void) {
    int m_a[2][2] = { { 6,5 }, { 10,9 } };
    int m_b[2][2] = { { 4,7 }, { 9,8 } };
    int sizeofarr = (int)sizeof(m_a) / (int)sizeof(m_a[0]);
    int static m_c[2][2];
    for (int i = 0; i < sizeofarr; i++) {
        for (int j = 0; j < sizeofarr; j++) {
            m_c[i][j] = m_a[i][j] - m_b[i][j];
            printf("%d ", m_c[i][j]);
        }
    }
}