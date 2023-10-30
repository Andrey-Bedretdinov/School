#include <iostream>  
#include <sstream> // библиотека для работы со строковыми потоками
#include <map>      
#include <string>  

int main() {
    std::string input; // строка для хранения входных данных
    std::getline(std::cin, input);

    std::istringstream iss(input);  // создание строкового потока из входной строки
    
    std::map<std::string, int> wordCount;  // словарь для подсчета встречаемости слов

    std::string word; // строка для временного хранения слова
    
    while (iss >> word) { // цикл подсчета слов из строкового потока
        wordCount[word]++;
    }

    for (const auto &pair : wordCount) {
        std::cout << pair.first << " " << pair.second << std::endl; // вывод слова и его количества
    }

    return 0;  
}
