#capitals = {
    #"France": ["Paris", "Lille", "Dijon"],
   # "Deutschland": ["Stuttgart", "Berlin"]
#}

#city = capitals["France"]
#print (city[1])   

#nested_list = ["A", "B", ["C", "D"]]

#print (nested_list [2][1])

travel_log = {
    "Frankreich": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visites": 12
    },
    "Deustchland": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visites": 5
    }
}

city = travel_log["Deustchland"]

#print (city["cities_visited"][2])
print (city[1])
