# -*- coding: utf-8 -*-
"""
Created on Tue May 15 14:52:48 2018

@author: Lucas
"""
from queue import Queue


def BL(s0, obj, expansion):
    fifo = Queue()
    fifo.put(s0)
    oldstates = []
    while fifo.empty() == False:
        state = fifo.get()
        if state == obj:
            return(state)     
        else:
            if state not in oldstates:
                oldstates.append(state)
                newstates = expansion(state)
                for j in newstates:
                    if j not in oldstates:
                        fifo.put(j)    
    return(None)
    
    
def boat(state):
    newstates = []
    for i in range(0,2):
        for j in range(1,3):
            ns = list(state.st)
            ns[i] = ns[i] - j*ns[4]
            ns[i+2] = ns[i+2] + j*ns[4]
            ns[4] = -1*ns[4]
            if valid(ns):
                bs = boats_states(ns)
                bs.path = state.path + [state.st]
                newstates.append(bs)         
    ns = list(state.st)
    ns[0] = ns[0] - 1*ns[4]
    ns[1] = ns[1] - 1*ns[4]
    ns[2] = ns[2] + 1*ns[4]
    ns[3] = ns[3] + 1*ns[4]   
    ns[4] = -1*ns[4]
    if valid(ns):
        bs = boats_states(ns)
        bs.path = state.path + [state.st]
        newstates.append(bs)
    return(newstates)

def valid(state):
    for i in state[0:4]:
        if i < 0:
            return False
        elif i >3:
            return False
    if state [1] != 0:
        if state[0] > state [1]:
            return False
    if state [3] != 0:
        if state[2] > state[3]:
            return False
    return True
    
class boats_states:
    def __init__ (self,state):
        self.st = state
        self.path = []
    def __eq__ (self,other):
        return (self.st == other.st)

#Initial state
initial = boats_states([3,3,0,0,1])

#Objective state
final = boats_states([0,0,3,3,-1])

#Execution
result = BL(initial,final,boat) 
for i in result.path:
    print(i)       
print(result.st)
    
    
  