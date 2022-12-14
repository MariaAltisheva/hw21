from abc import ABC, abstractmethod

class Storage(ABC):
    @property
    @abstractmethod
    def items(self):
        pass

    @property
    @abstractmethod
    def capacity(self):
        pass

    @abstractmethod
    def add(self): #увеличивает запас
        pass

    @abstractmethod
    def remove(self): #уменьшает запас
        pass

    @abstractmethod
    def get_free_space(self): #возвращает кол-во свободных ест
        pass

    @abstractmethod
    def get_items(self): #возвращат содржание склада в словаре (товар: кол-во)
        pass

    @abstractmethod
    def get_unique_items_count(self): # возвращает кол-во уникальных товаров
        pass

class Store(Storage):
    @property
    def items(self):
        pass

    @property
    def capacity(self):
        pass

    def __init__(self, items: dict, capacity=100):
        self._items = items
        self._capacity = capacity

    def __repr__(self):
        string_ = ""
        for key, value in self._items.items():
            string_ += f"{key}: {value}\n"
        return string_

    def add(self, name, count): #увеличивает запас items с учетом лимита capacity
        if name in self._items.keys():
            if self.get_free_space() >= count:
                print("Товар добавлен")
                self._items[name] += count
                return True
            else:
                print("Недостаточно места на складе/магазине")
                return False
        else:
            if self.get_free_space() >= count:
                print("Товар добавлен")
                self._items[name] = count
                return True
            else:
                print("Недостатоно места на складе/магазине")
                return False

    def remove(self, name, count): #уменьшает запас товара
        if self._items[name] >= count:
            print("Такое количество товара на складе/в магазине есть")
            self._items[name] -= count
            print("Товар добавлен")
            return True
        else:
            print("Недостаточно места на складе/магазине")
            return False

    def get_free_space(self): # возвращаем кол-во свободных мест
        current_space = 0
        for value in self._items.values():
            current_space += value
        return self._capacity - current_space

    @property
    def get_items(self): # возвращает содержание склада в виде словаря
        return f'Всеего: {self._items}'

    def get_unique_items_count(self):
        pass

class Shop(Store):
    def __init__(self, items: dict, capacity=20):
        super().__init__(items, capacity)

    def add(self, name, count): # увеличивает запас товаров
        if self.get_unique_items_count() >= 5:
            print("Cлишком много разных товаров")
        else:
            super().add(name, count)

class Request:
    """Обрабатывает запрос типа "Доставить 3 печенька из склад в магазин" """

    def __init__(self, request_str):
        req_list = request_str.split(" ")
        self.__amount = int(req_list[1])
        self.__product = req_list[2]
        self.__from = req_list[4]
        self.__to = req_list[6]

    def move(self):
        if self.__to == 'магазин':
            self.__to = 'shop'
        if self.__to == 'склад':
            self.__to = 'store'
        if self.__from == 'магазин':
            self.__from = 'shop'
        if self.__from == 'склад':
            self.__from = 'store'

        if eval(self.__from).remove(self.__product, self.__amount):
            eval(self.__to).add(self.__product, self.__amount)


store = Store(items={"печенька": 25, "собачка": 25, "елка": 25})
shop = Shop(items={"печенька": 2, "собачка": 2, "елка": 2})


def main():
    print('\nДобро пожаловать.\n')
    while True:
        print(f'Сейчас на складе:\n{store}')
        print(f'Сейчас в магазине:\n{shop}')
        user_input = input('Введите команду в формате "Доставить 1 собачка из склад в магазин"\n'
                           'Введите "стоп", если хотите закончить\n').lower()

        if user_input in ['стоп', 'stop']:
            print('До свидания')
            break
        try:
            request = Request(user_input)
            request.move()
        except Exception as e:
            print(f'Произошла ошибка: {e}')


if __name__ == '__main__':
    main()
