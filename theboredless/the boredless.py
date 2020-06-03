destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]


def get_destination_index(destination):
    for place in destinations:
        if place == destination:
            index = destinations.index(place)
            break
    return index


#print(get_destination_index("Paris, France"))

def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    destination_index = get_destination_index(traveler_destination)
    return destination_index


print(get_traveler_location(test_traveler))

attractions = [[] for destination in destinations]

#print(attractions)

def add_attraction(destination,attraction):
    try:
     destination_index = get_destination_index(destination)
     attractions_for_destination = attractions[destination_index]
     attractions_for_destination.append(attraction)
     return
    except ValueError:
     return

# ADDING ATTRACTIONS

add_attraction("Los Angeles, USA",['Venice Beach', ['beach']])
#print(attractions)

add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

def find_attraction(destination,interests):
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions(destination_index) #list item not callable
    attractions_with_interest = []
    for attraction in attractions_in_city:
        possible_attraction = attraction
        attraction_tags = attractions_in_city[1]
        for interest in interests:
            if interest in attraction_tags:
                attractions_with_interest.append(possible_attraction)
            else:
                continue
    return attractions_with_interest

print(find_attraction("Los Angeles, USA", ['art']))





#print(attractions)





