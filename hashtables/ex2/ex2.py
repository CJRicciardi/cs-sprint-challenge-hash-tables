#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    source = {}
    # destination = {}
    # Slist = []
    # Dlist = []

    for t in range(length):
        source[tickets[t].source] = tickets[t].destination
        # destination[tickets[t].destination] = t
        # Slist[t] = tickets[t].source
        # Dlist[t] = tickets[t].destination


    # start = source['None']
    # index = 0

    route = [source['NONE']]
   

    for i in range(length-1):
        # if source[route[i]] != 'NONE':
        route.append(source[route[i]])

    return route
