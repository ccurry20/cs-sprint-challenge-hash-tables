#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    route = []
    storage = {}
    for i in tickets:
        storage[i.source] = i.destination
    curr = storage['NONE']
    route.append(curr)
    while curr != "NONE":
        route.append(storage[curr])
        curr = storage[curr]  
    print(route)
    return route