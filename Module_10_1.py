import threading
from time import sleep
from datetime import datetime


start_time = datetime.now()
# Функция, которая будет выполняться в потоке
def write_words(word_count: int, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(1, word_count+1):
            f.write("Какое-то слово №" + str(i) + "\n")
            sleep(0.1)


# Создаем поток и указываем, что он будет выполнять функцию write_words


print("Включился первый поток в работу")
write_words(10, 'example1.txt')
thread = threading.Thread(target = write_words, args = (10,"example1.txt" ))
print("Завершилась запись в файл example1.txt")

write_words(30, 'example2.txt')
thread2 = threading.Thread(target = write_words, args = (30,"example2.txt" ))
print("Завершилась запись в файл example2.txt")

write_words(200, 'example3.txt')
thread3 = threading.Thread(target = write_words, args = (200,"example3.txt" ))
print("Завершилась запись в файл example3.txt")
write_words(100, 'example4.txt')
thread4 = threading.Thread(target = write_words, args = (100,"example4.txt" ))
print("Завершилась запись в файл example4.txt")

end_time = datetime.now()
result = end_time - start_time
print(f"Работа потоков: {result}")
# Запускаем поток
thread.start()
# Ожидаем завершения потока (это не блокирует основной код)
thread.join()
start_time1 = datetime.now()
print("Пока пока второй поток не запишет все файлы, программа  будет продолжать работу!")

write_words(10, 'example5.txt')
thread = threading.Thread(target = write_words, args = (10,"example5.txt" ))
print("Завершилась запись в файл example5.txt")


write_words(30, 'example6.txt')
thread5 = threading.Thread(target = write_words, args = (30,"example6.txt" ))
print("Завершилась запись в файл example6.txt")

write_words(200, 'example7.txt')
thread6 = threading.Thread(target = write_words, args = (200,"example7.txt" ))
print("Завершилась запись в файл example7.txt")

write_words(100, 'example8.txt')
thread7 = threading.Thread(target = write_words, args = (100,"example8.txt" ))
print("Завершилась запись в файл example8.txt")

thread.start()
thread.join()

end_time1 = datetime.now()
result1 = end_time1 - start_time1
print(f"Работа потоков: {result1}")
print("Все потоки завершили работу.")