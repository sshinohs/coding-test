import copy
from collections import defaultdict

def solution(tickets):
    len_tickets = len(tickets)
    ticket_dict = defaultdict(list)
    for ticket in tickets:
        if ticket[0] not in ticket_dict:
            ticket_dict[ticket[0]] = [ticket[1]]
        else:
            ticket_dict[ticket[0]].append(ticket[1])
    
    for key in ticket_dict.keys():
        ticket_dict[key] = sorted(ticket_dict[key])
    
    st = "ICN"
    courses = ["empty" for _ in range(len_tickets+1)]
    trace_dfs(ticket_dict, st, 0, len_tickets, courses)
    answer = courses
    return answer

def trace_dfs(ticket_dict, now, count, len_tickets, courses):
    courses[count] = now
    
    if count == len_tickets:
        return True
    
    for nxt in ticket_dict[now]:
        ticket_dict_nxt = copy.deepcopy(ticket_dict)
        ticket_dict_nxt[now].remove(nxt)
        if trace_dfs(ticket_dict_nxt, nxt, count+1, len_tickets, courses):
            return True
