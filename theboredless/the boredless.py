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
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
#print(attractions)

def find_attraction(destination,interests):
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]
    attractions_with_interest = []
    for attraction in attractions_in_city:
        possible_attraction = attraction
        attraction_tags = possible_attraction[1]
        for interest in interests:
            if interest in attraction_tags:
                attractions_with_interest.append(possible_attraction[0])
            else:
                continue
    return attractions_with_interest

la_arts = find_attraction("Los Angeles, USA", ['art'])

#print(la_arts)


#main event // See The Parts of a City You want to See

def get_attractions_for_traveler(traveler):
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]
    traveler_attraction = find_attraction(traveler_destination,traveler_interests)
    attractions_str = "the "
    for attraction in traveler_attraction:
        attractions_str += attraction
    interests_string = "Hi " + traveler[0] + "! We think you'll like these places around " + traveler_destination + ": "+ attractions_str + "."
    return interests_string

print(get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']]))






