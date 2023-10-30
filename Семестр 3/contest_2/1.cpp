#include <iostream>   
#include <cstdint>    

class DynamicArray {
private:
    int16_t* data;  // указатель на данные
    size_t size;  // размер массива

public:
    // конструктор с параметром
    DynamicArray(size_t sz) : size(sz) {
        data = new int16_t[size]();  // выделение памяти под массив и инициализация нулями
    }

    // конструктор копирования
    DynamicArray(const DynamicArray& other) : size(other.size) {
        data = new int16_t[size];  // выделение памяти
        for (size_t i = 0; i < size; i++) {
            data[i] = other.data[i];  // копирование данных
        }
    }

    // деструктор
    ~DynamicArray() {
        delete[] data;  // освобождение памяти
    }

    // геттер
    int16_t get(size_t index) const {
        if (index >= size) return 0;  // проверка на выход за границы массива
        return data[index];  // возврат значения по индексу
    }

    // сеттер
    void set(size_t index, int16_t value) {
        if (index >= size || value < -100 || value > 100) return;  // проверка условий
        data[index] = value;  // установка значения
    }

    // функция добавления элемента в конец массива
    void append(int16_t value) {
        if (value < -100 || value > 100) return;  // проверка значения
        int16_t* newData = new int16_t[size + 1];  // выделение новой памяти
        for (size_t i = 0; i < size; i++) {
            newData[i] = data[i];  // копирование данных
        }
        newData[size] = value;  // добавление нового элемента
        delete[] data;  // освобождение старой памяти
        data = newData;  // присвоение нового указателя
        size++;  // увеличение размера
    }

    // метод вывода массива
    void print() const {
        for (size_t i = 0; i < size; i++) {
            std::cout << data[i] << (i == size - 1 ? "\n" : " ");  // вывод элементов
        }
    }

    // функция сложения
    void add(const DynamicArray& other) {
        for (size_t i = 0; i < size; i++) {
            data[i] += other.get(i);  // сложение элементов
        }
    }

    // функция вычитания
    void subtract(const DynamicArray& other) {
        for (size_t i = 0; i < size; i++) {
            data[i] -= other.get(i);  // вычитание элементов
        }
    }
};

int main() {
    size_t size1, size2, n;
    std::cin >> size1;  // считывание размера первого массива

    DynamicArray arr1(size1);  // создание первого массива
    for (size_t i = 0; i < size1; i++) {
        int16_t value;
        std::cin >> value;  // считывание значения
        arr1.set(i, value);  // добавление в массив
    }

    std::cin >> size2;  // считывание размера второго массива
    DynamicArray arr2(size2);  // создание второго массива
    for (size_t i = 0; i < size2; i++) {
        int16_t value;
        std::cin >> value;  // считывание значения
        arr2.set(i, value);  // добавление в массив
    }

    std::cin >> n;  // считывание количества команд
    for (size_t i = 0; i < n; i++) {
        int cmd;
        std::cin >> cmd;  // считывание номера команды
        switch (cmd) {
        case 1: {  // команда вывода элемента
            size_t arrayNum, index;
            std::cin >> arrayNum >> index;  // считывание параметров
            if (arrayNum == 1) std::cout << arr1.get(index) << "\n";  // вывод элемента первого массива
            else if (arrayNum == 2) std::cout << arr2.get(index) << "\n";  // вывод элемента второго массива
            break;
        }
        case 2: {  // команда изменения элемента
            size_t arrayNum, index;
            int16_t value;
            std::cin >> arrayNum >> index >> value;  // считывание параметров
            if (arrayNum == 1) arr1.set(index, value);  // изменение в первом массиве
            else if (arrayNum == 2) arr2.set(index, value);  // изменение во втором массиве
            break;
        }
        case 3: {  // команда добавления элемента
            size_t arrayNum;
            int16_t value;
            std::cin >> arrayNum >> value;  // считывание параметров
            if (arrayNum == 1) arr1.append(value);  // добавление в первый массив
            else if (arrayNum == 2) arr2.append(value);  // добавление во второй массив
            break;
        }
        case 4: {  // команда вывода массива
            size_t arrayNum;
            std::cin >> arrayNum;  // считывание параметра
            if (arrayNum == 1) arr1.print();  // вывод первого массива
            else if (arrayNum == 2) arr2.print();  // вывод второго массива
            break;
        }
        case 5: {  // команда сложения массивов
            size_t arrayNum;
            std::cin >> arrayNum;  // считывание параметра
            if (arrayNum == 1) arr1.add(arr2);  // первый массив += второй массив
            else if (arrayNum == 2) arr2.add(arr1);  // второй массив += первый массив
            break;
        }
        case 6: {  // команда вычитания массивов
            size_t arrayNum;
            std::cin >> arrayNum;  // считывание параметра
            if (arrayNum == 1) arr1.subtract(arr2);  // первый массив -= второй массив
            else if (arrayNum == 2) arr2.subtract(arr1);  // второй массив -= первый массив
            break;
        }
        }
    }

    return 0; 
}
