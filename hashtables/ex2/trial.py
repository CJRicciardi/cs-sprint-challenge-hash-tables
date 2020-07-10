from ex2 import Ticket

ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")
tickets = [ticket_1, ticket_2, ticket_3]

# source / destination

# dictionary = {}
# for i in range(3):
#     dictionary[tickets[i].source] = i

# print(dictionary)

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


print(reconstruct_trip(tickets, 3))