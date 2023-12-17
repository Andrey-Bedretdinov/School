#include <iostream>  
#include <vector>  
#include <string> 

struct Item {
    std::string name;
    int length;  // длина
    int width;  // ширина
    int height;  // высота
    float weight;  // вес
};

//поиск по имени

// чтение объектов
std::vector<Item> readItems(int count) {
    std::vector<Item> items;
    for (int i = 0; i < count; ++i) {  // цикл для считывания каждого объекта
        Item item;  // временный объект
        // чтение параметров объекта
        std::cin >> item.name >> item.length >> item.width >> item.height >> item.weight;
        items.push_back(item);
    }
    return items;
}

// печать объектов
void printItems(const std::vector<Item>& items) {
    if (items.empty()) {
        std::cout << "empty\n";
    } else {
        for (const auto& item : items) {
            std::cout << item.name << " " << item.length << " " << item.width << " " 
                      << item.height << " " << item.weight << "\n";
        }
    }
}

// поиск объектов по заданным критериям
std::vector<Item> searchItems(const std::vector<Item>& items, int param, char op, std::string value) {
    std::vector<Item> result;
    for (const auto& item : items) {
        bool match = false;
        switch (param) {
            case 1: // Сравнение по названию
                if (op == '=') match = (item.name == value);
                break;
            case 2: // Сравнение по длине
                if (op == '>') match = item.length > std::stoi(value);
                if (op == '<') match = item.length < std::stoi(value);
                if (op == '=') match = item.length == std::stoi(value);
                break;
            case 3: // Сравнение по ширине
                if (op == '>') match = item.width > std::stoi(value);
                if (op == '<') match = item.width < std::stoi(value);
                if (op == '=') match = item.width == std::stoi(value);
                break;
            case 4: // Сравнение по высоте
                if (op == '>') match = item.height > std::stoi(value);
                if (op == '<') match = item.height < std::stoi(value);
                if (op == '=') match = item.height == std::stoi(value);
                break;
            case 5: // Сравнение по весу
                if (op == '>') match = item.weight > std::stof(value);
                if (op == '<') match = item.weight < std::stof(value);
                if (op == '=') match = item.weight == std::stof(value);
                break;
        }
        if (match) {
            result.push_back(item);
        }
    }
    return result;
}

int main() {
    int itemCount;  // количество объектов
    std::cin >> itemCount;
    auto items = readItems(itemCount);  // чтение объектов

    int commandCount;  // количество команд
    std::cin >> commandCount;
    for (int i = 0; i < commandCount; ++i) {  // цикл обработки команд
        int command, param;  // команда и параметр
        char op;  // оператор сравнения
        std::string value;  // значение для сравнения
        std::cin >> command;
        if (command == 1) {
            std::cin >> param >> op;
            if (param == 1) {
                std::cin >> value;  // Считывание строки для поиска по имени
            } else {
                std::cin >> value;  // Считывание числа в виде строки для остальных параметров
            }
            items = searchItems(items, param, op, value);
        } else if (command == 2) {  // команда вывода
            printItems(items); 
        } else if (command == 3) {  // команда сброса поиска
            items = readItems(itemCount);
        }
    }

    return 0;
}

