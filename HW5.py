#1

Transformers={"Оптімус Прайм":"Грузовик Peterbilt 379","Бамблбі":"Chevrolet Camaro","Джаз":"Porsche 935 Turbo"}
for i, x in Transformers.items():
    print(i,"-",x)

#2

for i in Transformers:
    if i=="Оптімус Прайм":
        print("Оптімус Прайм прибув")
        break

#3

TransformersWeight={ "Оптімус":5000,"Бамблбі":2500,"Джаз":3000}
x = 0
for i in TransformersWeight.values():
    x += i
print(x)

#4

megatron=("Megatron","Кібертронський винищувач","Танк","Кібертронський Зорельот.","Десептикон")

for i in megatron:
    if i=="Десептикон":
        print("Мегатрон - ворог")

#5

x={"Сентінел Прайм":"Пожежна машина"}
Transformers.update(x)
print(Transformers)