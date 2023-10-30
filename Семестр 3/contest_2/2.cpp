#include <iostream> 
#include <stdexcept>

class DynamicArray { 
private:
    int16_t* data; // указатель на динамический массив данных
    size_t size; // размер массива

public:
    DynamicArray(size_t n) : size(n) { // конструктор класса
        data = new int16_t[n](); // выделяем память под массив
    }

    DynamicArray(const DynamicArray& other) : size(other.size) { // конструктор копирования
        data = new int16_t[size]; // выделяем память
        for (size_t i = 0; i < size; ++i) { // копируем данные
            data[i] = other.data[i];
        }
    }

    ~DynamicArray() { // деструктор класса
        delete[] data; // освобождаем память
    }

    int16_t get(size_t index) const { // метод для получения элемента по индексу
        if (index >= size) throw std::out_of_range("out_of_range:get"); // проверка на выход за границы массива
        return data[index]; // возвращаем элемент
    }

    void set(size_t index, int16_t value) { // метод для установки значения элемента
        if (index >= size) throw std::out_of_range("out_of_range:set"); // проверка на выход за границы массива
        if (value < -100 || value > 100) throw std::invalid_argument("invalid_argument:set"); // проверка значения на допустимый диапазон
        data[index] = value; // установка значения
    }

    void push_back(int16_t value) { // метод для добавления элемента в конец массива
        if (value < -100 || value > 100) throw std::invalid_argument("invalid_argument:push_back"); // проверка значения на допустимый диапазон
        int16_t* newData = new int16_t[size + 1]; // выделяем память под новый массив
        for (size_t i = 0; i < size; ++i) { // копируем существующие данные
            newData[i] = data[i];
        }
        newData[size++] = value; // добавляем новый элемент и увеличиваем размер
        delete[] data; // освобождаем старую память
        data = newData; // перенаправляем указатель
    }

    void print() const { // метод для вывода всех элементов массива
        for (size_t i = 0; i < size; ++i) { // проходим по всем элементам
            std::cout << data[i] << (i == size - 1 ? '\n' : ' '); // выводим элемент
        }
    }

    void add(const DynamicArray& other) { // метод для сложения двух массивов
        for (size_t i = 0; i < size; ++i) { // проходим по элементам первого массива
            data[i] += (i < other.size ? other.data[i] : 0); // складываем с элементом второго массива, если он существует
        }
    }

    void subtract(const DynamicArray& other) { // метод для вычитания массивов
        for (size_t i = 0; i < size; ++i) { // проходим по элементам первого массива
            data[i] -= (i < other.size ? other.data[i] : 0); // вычитаем элемент второго массива, если он существует
        }
    }
};

int main() {
    size_t n1, n2, commands; // размеры массивов и число команд
    std::cin >> n1;
    DynamicArray arr1(n1);
    for (size_t i = 0; i < n1; ++i) {
        int16_t value; 
        std::cin >> value; 
        arr1.set(i, value); // устанавливаем значение элемента в первом массиве
    }

    std::cin >> n2; 
    DynamicArray arr2(n2); 
    for (size_t i = 0; i < n2; ++i) { 
        int16_t value; 
        std::cin >> value; 
        arr2.set(i, value); // устанавливаем значение элемента во втором массиве
    }

    std::cin >> commands; // читаем количество команд
    for (size_t i = 0; i < commands; ++i) { // итерируемся по командам
        int cmd; // переменная для хранения кода команды
        std::cin >> cmd; // считываем код команды

        try { // блок обработки исключений
            if (cmd == 1) { // команда на вывод элемента
                size_t arrayNumber, index; 
                std::cin >> arrayNumber >> index; // считываем номер массива и индекс элемента
                std::cout << (arrayNumber == 1 ? arr1.get(index) : arr2.get(index)) << std::endl; // выводим элемент по индексу
            }
            else if (cmd == 2) { // команда на изменение элемента
                size_t arrayNumber, index;
                int16_t newValue;
                std::cin >> arrayNumber >> index >> newValue; // считываем данные
                if (arrayNumber == 1) {
                    arr1.set(index, newValue); // устанавливаем новое значение для первого массива
                } else {
                    arr2.set(index, newValue); // устанавливаем новое значение для второго массива
                }
            }
            else if (cmd == 3) { // команда на добавление элемента
                size_t arrayNumber;
                int16_t newValue;
                std::cin >> arrayNumber >> newValue; // считываем данные
                if (arrayNumber == 1) {
                    arr1.push_back(newValue); // добавляем элемент в конец первого массива
                } else {
                    arr2.push_back(newValue); // добавляем элемент в конец второго массива
                }
            }
            else if (cmd == 4) { // команда на вывод всего массива
                size_t arrayNumber;
                std::cin >> arrayNumber; 
                if (arrayNumber == 1) {
                    arr1.print();
                } else {
                    arr2.print(); 
                }
            }
            else if (cmd == 5) { // команда на сложение массивов
                size_t arrayNumber;
                std::cin >> arrayNumber; // считываем номер первого массива
                if (arrayNumber == 1) {
                    arr1.add(arr2); // складываем первый массив с вторым
                } else {
                    arr2.add(arr1); // складываем второй массив с первым
                }
            }
            else if (cmd == 6) { // команда на вычитание массивов
                size_t arrayNumber;
                std::cin >> arrayNumber; // считываем номер первого массива
                if (arrayNumber == 1) {
                    arr1.subtract(arr2); // вычитаем из первого массива второй
                } else {
                    arr2.subtract(arr1); // вычитаем из второго массива первый
                }
            }
        } catch (const std::exception& e) { // ловим исключения
            std::cout << "std:" << e.what() << std::endl; // выводим сообщение об ошибке
        }
    }

    return 0; 
}

