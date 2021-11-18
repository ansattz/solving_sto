#include <iostream>
using namespace std;

int addDigits(int num) {
        return num - (num - 1) / 9 * 9;
    }
/** O inteiro de entrada será convertido em um inteiro de uma unidade por somas sucetivas
de seus dígitos. Ou seja, 13 = 1 + 3 = 4. 56 := 5 + 6 = 11, 11 := 1 + 1 = 2.
**/
int main(void)
{
    int n = 27;
    cout << "Entrada é o número "<< n << " que vira a unidade " << addDigits(n) << endl; 
    n = 18;
    cout << "\nEntrada é o número "<< n << " que vira a unidade " << addDigits(n) << endl; 
    return 0;   
}