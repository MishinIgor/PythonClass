#Определите общие элементы в двух списках
list_1 = ["Сони",'Нокиа',"Самсунг","Ксяоми","Мейзу","Эппл","Хуавей"]
list_2 = ["Сони","Ксяоми","Эппл"]

list_1, list_2 = set(list_1), set(list_2)

print(list_1,list_2)
intersection = list_1 & list_2
print(intersection)