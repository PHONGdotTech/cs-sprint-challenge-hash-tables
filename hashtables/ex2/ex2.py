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
    route = [""]
    cache = {}
    for each in tickets:
        if each.source not in cache:
            cache[each.source] = each.destination

    next_source = None
    for each in cache:
        if each == 'NONE':
            next_source = cache[each]
            break

    while route[-1] != "NONE":
        if route[0] == "":
            route[0] = next_source
        else:
            next_source = cache[next_source]
            route.append(next_source)

    return route

if __name__ == "__main__":
    # ticket_1 = Ticket("NONE", "PDX")
    # ticket_2 = Ticket("PDX", "DCA")
    # ticket_3 = Ticket("DCA", "NONE")

    # tickets = [ticket_1, ticket_2, ticket_3]

    ticket_1 = Ticket("PIT", "ORD")
    ticket_2 = Ticket("XNA", "SAP")
    ticket_3 = Ticket("SFO", "BHM")
    ticket_4 = Ticket("FLG", "XNA")
    ticket_5 = Ticket("NONE", "LAX")
    ticket_6 = Ticket("LAX", "SFO")
    ticket_7 = Ticket("SAP", "SLC")
    ticket_8 = Ticket("ORD", "NONE")
    ticket_9 = Ticket("SLC", "PIT")
    ticket_10 = Ticket("BHM", "FLG")

    tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
                ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]
    reconstruct_trip(tickets, 10)