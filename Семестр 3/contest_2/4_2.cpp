#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main() {
    vector<double> numbers;
    double number;
    
    // Читаем числа до 0
    while (true) {
        cin >> number;
        if (number == 0) {
            break;
        }
        numbers.push_back(number);
    }

    int n = numbers.size();

    // Если меньше двух элементов, выводим 0 и завершаем программу
    if (n < 2) {
        cout << 0 << endl;
        return 0;
    }

    double sum = 0;
    
    // Вычисляем сумму всех чисел
    for (double num : numbers) {
        sum += num;
    }

    // Находим среднее арифметическое
    double s = sum / n;

    double variance = 0;

    // Вычисляем дисперсию
    for (double num : numbers) {
        variance += (num - s) * (num - s);
    }
    
    // Находим стандартное отклонение
    double k = sqrt(variance / (n - 1));

    cout.precision(12); // для вывода с точностью 12 знаков
    cout << k << endl;

    return 0;
}
