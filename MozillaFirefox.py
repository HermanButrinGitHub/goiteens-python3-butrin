print("Первое задание")
RAM_total = 2
LastTab = 0.5
RAM_used = 0
Tabs = 0
while RAM_used < RAM_total:
    RAM_used = RAM_used + LastTab
    Tabs += 1    
    LastTab = LastTab / 2 
    if LastTab < 0.001:
        LastTab = 0.001 #(ограничение) вкладка не может занимать менее 1 мегабайта
print("на компьютере с",RAM_total,"Гигабайтами оперативной памяти можно открыть",Tabs,"вкладок")
input("нажмите Enter")
print("Второе задание")
LastTab = 0.5
RAM_used = 0
Tabs = 0
NumberOfTabs = int(input("введите количество вкладок:"))
while Tabs < NumberOfTabs:
    RAM_used = RAM_used + LastTab
    Tabs += 1    
    LastTab = LastTab / 2 
    if LastTab < 0.001:
        LastTab = 0.001
if RAM_used > RAM_total:
    True_False = "нельзя"
else:
    True_False = "можно"
print("на компьютере с",RAM_total,"гигабайтами оперативной памяти",True_False,"открыть",NumberOfTabs,"вкладок")
print(NumberOfTabs,"вкладок используют",RAM_used,"гигабайт памяти")
input()