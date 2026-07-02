fav_cities = []
for i in range(1, 5):
    print("enter your fav city at position", i, " : ")
    Str = input()
    fav_cities.append(Str)
for i in range(len(fav_cities) -1 , -1, -1):
    print("my fav city at position ", i, " is ",fav_cities[i])