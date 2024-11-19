import threading
import queue
import random
import time


class Table:
    def __init__(self, number):
        self.number = number
        self.quest = None

class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 10))

class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = queue.Queue()

    def guest_arrival(self, *quests):
        for quest in guests:
            for table in self.tables:
                if table.quest is None:
                    table.quest = quest
                    quest.start()
                    print(f'{quest.name} сел(-а) за стол номер {table.number}')
                    break
            else:
                self.queue.put(quest)
                print(f'{quest.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or any(table.quest is not None for table in self.tables):
            for table in self.tables:
                if table.quest is not None and not table.quest.is_alive():
                    print(f'{table.quest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.quest = None
            if not self.queue.empty():
                for table in self.tables:
                    if table.quest is None:
                        quest = self.queue.get()
                        table.quest = quest
                        quest.start()
                        print(f'{quest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                        break


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
