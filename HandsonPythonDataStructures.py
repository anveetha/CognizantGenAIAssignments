#Hands on Python Data Structures
#Task 1
fruits = ['apple', 'orange', 'cherry', 'date', 'blueberry']
print('original list:', fruits)
fruits.append('mango')
print('after appending mango:', fruits)
fruits.remove('cherry')
print('after removing cherry:', fruits)
print('reversed list:', fruits[::-1])

#Task 2 
person = {"name" : "Anveetha", "age" : 20, "city" : "Dallas"}
person.update({"favorite color" : "brown"})
person.update({"city" : "New York"})
print("\nKeys: " + str(person.keys()))
print("Values: " + str(person.values()))

#Task 3 
favorites = ("Raayan", "Go! by Weston Estate", "Algorithms for Life")
print("\nFavorite things:" + str(favorites))
#favorites.append("Python Programming")
print("Length of tuple: " + str(len(favorites)))