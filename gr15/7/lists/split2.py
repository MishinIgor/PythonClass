line = "Whirling, twirling    round and    round"
print(line.split())
# ['Whirling,', 'twirling', 'round', 'and', 'round']
print(line.split(' ')) # ['Whirling,', 'twirling', '', '', '', 'round', 'and', '', '', '', 'round']
line = "Whirling, twirling    round and     round" #Между and и round табуляция 2 раза
print(line.split(' '))