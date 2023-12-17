#include <iostream>
#include <list>

// структура для хранения элементов списка
template <typename T>
struct ListItem {
    int id; 
    T data; 
    int accessCount = 0;  // счетчик количества обращений к элементу

    ListItem(int id, T data) : id(id), data(data) {}
};

template <typename T>
class CacheList {
private:
    std::list<ListItem<T>> items;  // двунаправленный список элементов

    // поиск итератора на элемент списка по его id
    typename std::list<ListItem<T>>::iterator findIterator(int id) {
        for (auto it = items.begin(); it != items.end(); ++it) {
            if (it->id == id) {
                return it;
            }
        }
        return items.end();
    }

    // перемещение элемента на правильную позицию после увеличения его accessCount
    void moveItemToCorrectPosition(typename std::list<ListItem<T>>::iterator it) {
        while (it != items.begin()) {
            auto prevIt = std::prev(it);
            if (prevIt->accessCount > it->accessCount) {
                break; // элемент уже на правильной позиции
            }
            std::iter_swap(it, prevIt); // меняем местами элементы
            --it;
        }
    }

public:
    // добавление нового элемента в список
    void addItem(int id, T data) {
        items.push_back(ListItem<T>(id, data));
    }

    // обновление данных элемента по его id
    void updateItem(int id, T newData) {
        auto it = findIterator(id);
        if (it != items.end()) {
            it->data = newData;
        }
    }

    // поиск элемента по id и увеличение его счетчика обращений
    ListItem<T>* findItem(int id) {
        auto it = findIterator(id);
        if (it != items.end()) {
            it->accessCount++;
            moveItemToCorrectPosition(it);
            return &(*findIterator(id)); // повторный поиск элемента после его перемещения
        }
        return nullptr;
    }

    // вывод текущего списка
    void printList() {
        for (const auto& item : items) {
            std::cout << "{" << item.id << " " << item.accessCount << " " << item.data << "} ";
        }
        std::cout << std::endl;
    }
};

int main() {
    CacheList<int> list;
    int N, id, data, Q, cmd;

    std::cin >> N;
    for (int i = 0; i < N; ++i) {
        std::cin >> id >> data;
        list.addItem(id, data);
    }

    std::cin >> Q;
    for (int i = 0; i < Q; ++i) {
        std::cin >> cmd;
        switch (cmd) {
            case 1: // обновление данных элемента
                std::cin >> id >> data;
                list.updateItem(id, data);
                break;
            case 2: // вывод элемента списка по id
                std::cin >> id;
                if (auto item = list.findItem(id)) {
                    std::cout << "{" << item->id << " " << item->accessCount << " " << item->data << "}" << std::endl;
                }
                break;
            case 3: // поиск элемента в списке по данным
                std::cin >> data;
                if (list.findItem(data)) {
                    std::cout << "YES" << std::endl;
                } else {
                    std::cout << "NO" << std::endl;
                }
                break;
            case 4: // вывод всего списка
                list.printList();
                break;
        }
    }

    return 0;
}
