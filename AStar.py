# -*- coding: utf-8 -*-
"""
Created on Sat Dec 03 15:11:49 2016

@author: Owner
"""
from implementation import *
import math
# Sample code from http://www.redblobgames.com/pathfinding/
# Copyright 2014 Red Blob Games <redblobgames@gmail.com>
#
# Feel free to use this code in your own projects, including commercial projects
# License: Apache v2.0 <http://www.apache.org/licenses/LICENSE-2.0.html>

#This code has been modified to suit our needs.

def heuristic(a, b):
    (x, y) = a
    (x2, y2) = b
    return int(math.sqrt( math.pow(x2-x,2)+math.pow(y2-y,2) ))

def getAngle(a, b):
    (x, y) = a
    (x2, y2) = b
    diffx = x2-x
    diffy = y2-y
    if (diffx == 2 and diffy == 0):
        return 0
    elif (diffx == 2 and diffy == -1):
        return 1
    elif (diffx == 2 and diffy == -2):
        return 2   
    elif (diffx == 1 and diffy == -2):
        return 3
    elif (diffx == 0 and diffy == -2):
        return 4
    elif (diffx == -1 and diffy == -2):
        return 5   
    elif (diffx == -2 and diffy == -2):
        return 6
    elif (diffx == -2 and diffy == -1):
        return 7
    elif (diffx == -2 and diffy == 0):
        return 8    
    elif (diffx == -2 and diffy == 1):
        return 9
    elif (diffx == -2 and diffy == 2):
        return 10
    elif (diffx == -1 and diffy == 2):
        return 11  
    elif (diffx == 0 and diffy == 2):
        return 12
    elif (diffx == 1 and diffy == 2):
        return 13
    elif (diffx == 2 and diffy == 2):
        return 14  
    elif (diffx == 2 and diffy == 1):
        return 15
    print a, b
    print diffx, diffy
    

def a_star_search(graph, start, goal, facing):
    #How close to the target is acceptable
    #tolerance=3
    
    frontier = PriorityQueue()
    frontier.put((start,facing), 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while not frontier.empty():
        currentTup = frontier.get()
        current = currentTup[0]
        direction = currentTup[1]
        
        if current == goal:
            break
        #if heuristic(goal,current)<tolerance:
        #    break
        
        for next in graph.neighbors(current):
            goDirection = getAngle(current, next)
            maxDir = max(direction, goDirection)
            minDir = min(direction, goDirection)
            turnCost = maxDir - minDir
            if (turnCost <= -8):
                turnCost += 16
            else:
                turnCost += 8
            new_cost = cost_so_far[current] + graph.cost(current, next) + turnCost
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put((next, goDirection), priority)
                came_from[next] = current
    
    return reconstruct_path(came_from, start, goal)
    
#Source: http://www.redblobgames.com/pathfinding/a-star/implementation.html End
    
    