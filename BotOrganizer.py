import os
import datetime
from time import sleep
from random import randint
x = datetime.datetime.now()
print("Зраствуй глупый человечек я - BotOrganizer\n"
"для того чтобы ваша команда читалась нужен префикс: /\n"
"чтобы узнать список команд введите: /help\n"
,x.strftime("%x"),
"\n",x.strftime("%X"))
Y_N = 0
while True:
    Y_N = ""
    answer = input(">>")
    if answer[0] != "/":
        continue
    
    
    elif answer == "/help":
        print("1. /help","2. /create","3. /edit","4. /delete","5. /read","6. /end", sep="\n")
    
    
    elif answer == "/create":
        print("Назвать файл?")
        while Y_N != "Y" and Y_N != "N":
            print("Y(yes) N(no):")
            Y_N = input(">>")
        if Y_N == "Y":
            print("Как хотите назвать файл")
            file_Name = str(input(">>"))
            if os.path.exists(file_Name + ".txt"):
                print("Файл с таким названием уже существует")
            else:
                f = open(file_Name + ".txt","x")
                print("Файл создан!")      
        else:
            file_Name = "Untiled-" + str(randint(1000,9999))
            f = open(file_Name + ".txt","x")
            print("Файл создан!")
    
    
    elif answer == "/delete":
        print("Какой файл хотите удалить")
        file_Name = str(input(">>"))
        if os.path.exists(file_Name + ".txt"):
            print("Вы точно хотите удалить файл",file_Name)
            while Y_N != "Y" and Y_N != "N":
                print("Y(yes) N(no):")
                Y_N = input(">>")
            if Y_N == "Y":
                os.remove(file_Name + ".txt")
                print("Файл удален!")
            else:
                print("Отмена")
        else:
            print("Такого файла не существует")
    
    elif answer == "/edit":
        print("Какой файл хотите редактировать")
        file_Name = str(input(">>"))
        if os.path.exists(file_Name + ".txt"):
            print("Что хотите добавить")
            edit = str(input(">>"))
            f = open(file_Name + ".txt", "a")
            f.write("\n" + edit)
            f.close
            print("Добавлено!")
        else:
            print("Такого файла не существует")

    elif answer == "/read":
        print("Какой файл хотите прочитать")
        file_Name = str(input(">>"))
        if os.path.exists(file_Name + ".txt"):
            f = open(file_Name + ".txt", "r")
            print("Содержимое файла:",
            f.read())
        else:
            print("Такого файла не существует")
    
    elif answer == "/end":
        print("Само уничтожение через")
        i = 4
        while i > 0:
            i -= 1
            sleep(1)
            print(i)
        break
    
    else:
        print("Не извесная команда")
    answer = ""