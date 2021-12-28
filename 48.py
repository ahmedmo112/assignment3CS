
dic_of_cities={"cairo": "9.54 M","giza":"8,8 M" ,"alex":"5.23 M" ,"hellwan":"643 th" ,"fayom":"2.1 M" ,"mansora":"1.2 M" ,"aswan":"2 M" ,"luxor":"3 M" ,"domyat":"1 M" }

def listing_cities_and_there_information(dic_of_cities):
    for key in dic_of_cities:
        print(key,"=>",dic_of_cities.get(key))


def query_of_city_and_its_populaion(dic_of_cities):
    x=dic_of_cities.get(input("enter the city : "))
    print(f"The populaion of the city : {x}")

def update_The_dictionary(dic_of_cities):
    city=input("enter the city: ")
    population=str(input("enter the population: "))
    dic_of_cities[city]=population+" M"
    print(f"The update of the dictionary :")    
    for key in dic_of_cities:
        print(key,"=>",dic_of_cities.get(key))

print("1.Listing all cities and their information\n2.Query the dictionary for a city\n3.Add a new city")

user = input("Please chosse a number from the list: ") 
if user in ['1','2','3']:
    if user=="1" :
        listing_cities_and_there_information(dic_of_cities)
    elif user=="2" :
        query_of_city_and_its_populaion(dic_of_cities)    
    elif user=="3" :
        update_The_dictionary(dic_of_cities)
else:
    print("the number you enter is uncorrect \nplease chosse a Number from the list\nTry Again")
