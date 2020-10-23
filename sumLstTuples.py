# Made with ❤️ in Python 3 by Alvison Hunter - October 8th, 2020
def find_last_passengers(bus_stops):
    try:
        last_passengers = sum(people_in - people_out for people_in, people_out in bus_stops)
    except:
        print("Uh oh! Something went really wrong!")
        quit
    finally:
        if(last_passengers >= 0):
            print('Remaining Passengers for last stop: ', last_passengers)
            return last_passengers
        else:
            print('No passengers where on the bus')
            last_passengers = 0
            return last_passengers

#let's try three different scenarios
find_last_passengers([[10,0],[3,5],[5,8]])#this will return 5
find_last_passengers([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]) #this will return 17
find_last_passengers([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]) #this will return 21
