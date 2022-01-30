#greedy algorithm small groups program
#designed and coded by Cypress Payne and Zachary Himes
#CSC 3430 instructed by Dr. Arias, Winter 2021

#import requirements
import cairocffi
import igraph as ig
import csv
import os.path

#basic setup
toPrint = open('smallgroups.txt', 'w') #open output file
fileName = input("Enter File of Names: ") #get file input
inputKey = input("Enter group size. Group size should be no less than four and no more than half the number people: ") #get group size
numKey = int(inputKey)
#variable initialization
namesList = []
weightList = [] #weight of graph nodes (married = 2, single = 1)
size = 0
totalWeeks = 1

if os.path.exists(fileName): #check file exists and open it
    reader = open(fileName)
    fileContent = reader.read()
    nameList = fileContent.split("\n") #put names into list
    size = len(nameList) #get number of people
    reader.close() #close file
    if numKey < 4 or numKey > (size//2):
        raise Exception("Not a valid group size") #error if group size is not valid
else:
    raise Exception("Not a valid name file") #error if file does not exist
for name in nameList: #determine whether nodes are single or couples
    substring = ","
    if substring in name:
        weightList.append(2) #if couples, add 2 to correct spot in weightList
        i = 1 + 1
    else:
        weightList.append(1) #else, they are single and add 1
        i = 1 + 1

#function to create nodes for graph
def CreateNodes(numPeople):
    groupGraph = ig.Graph(numPeople, directed=True) #create directed graph with correct number of nodes
    #attributes of nodes, give each node a name and weight
    groupGraph.vs["name"] = nameList
    groupGraph.vs["weight"] = weightList
    return groupGraph #return the created graph

#function to print groups to file
def PrintGroup(groupList):
    size = len(groupList)
    i = 1
    print("WEEK " + str(totalWeeks), file = toPrint)
    groupList.pop(0)
    for group in groupList:
        print("GROUP " + str(i) + ": ", file = toPrint)
        i = i + 1
        first = group.pop(0)
        print(first + " (Host)", end = '', file = toPrint)
        for person in group:
            print(" | " + person, end = '', file = toPrint)
        print("\n", file = toPrint)

g = CreateNodes(size) #create graph

#greedy algorithm function to create groups given the list of names and the size of groups
def CreateGroups(key, queue):
    #variable initialization
    size = len(queue) #total number of nodes (married couples are one node)
    weightSize = sum(weightList) #total number of people, including married couples
    totalGroups = weightSize//numKey #number of groups that will be created
    numGroups = 0 #number of groups that currently exist
    q = queue.copy() #copied version of list of names passed to function
    groupList = [[] for i in range(totalGroups + 1)] #list of lists to store groups

    while len(q): #while q is not empty
        while (numGroups < totalGroups): #while all of the groups have not been created yet
            #initialize variables
            host = "" #store host in this variable
            temp = "" #store current name popped from q in this variable
            hostSelect = False #bool to deteermine whether a host has been chosen
            round = 0 #number of names that have been popped from list in this while loop
            numGroups = numGroups + 1 #increase number of existing groups
            while hostSelect != True: #while a host has not been selected
                temp = q.pop(0) #get first name from q
                round = round + 1 #mark that a name has been popped from the list
                if round < size: #while there are still names that have not been viewed eyt
                    if (g.vs.find(name=temp).degree(mode="in") < (size - 1)): #once node has n-1 edges in, all people have visited
                        host = temp #set to host
                        groupList[numGroups].append(temp) #add host to list
                        hostSelect = True #mark that host has been selected
                    else:
                        q.append(temp) #if name has already been visited by everyone, return to q
                else: #if everyone has been visited but a host is still needed
                    host = temp #set first person available to host
                    groupList[numGroups].append(temp) #add host to hostList
                    hostSelect = True #mark that host has been selected

            i = g.vs.find(name=host)["weight"] #variable i tracks the amount of people (weight) in the current group
            round = 0 #reset rounds for visiting people
            while len(q) and (i < key): #while the q is not empty and there is still room in the group
                temp = q.pop(0) #get next name
                round = round + 1 #mark that someone has been popped from the q
                if ((i + g.vs.find(name=temp)["weight"]) > key): #if the total sum of people will be greater than the requested amount
                    q.append(temp) #return name to bottom of q
                    temp = q.pop(0) #retrieve a new name from the top of q
                    round = round + 1 #mark that someone has been popped from q

                if round <= len(q): #if there are still names that have not been viewed in the q
                    if (g.are_connected(g.vs.find(name=temp), g.vs.find(name=host))): #check if that person has already visited the current host
                        q.append(temp) #if they have, add back to bottom of q
                    else: #if they have not visited this host yet
                        groupList[numGroups].append(temp) #add to groupList
                        i = i + g.vs.find(name=temp)["weight"] #increase current number of people (weight) in this group
                        g.add_edge(g.vs.find(name=temp), g.vs.find(name=host)) #create directed edge from visitor to host

                else: #if the entire q has been traversed and the current group still needs more people
                    groupList[numGroups].append(temp) #add first available name to groupList
                    i = i + g.vs.find(name=temp)["weight"] #increase weight total of current group
                    if not(g.are_connected(g.vs.find(name=temp), g.vs.find(name=host))): #if there is not an edge between visitor and host
                        g.add_edge(g.vs.find(name=temp), g.vs.find(name=host)) #create edge
        while q: #if q is still not empty but all the groups have enough people, add remaining people to groups
            j = 0 #set variable j to 0, represents group number
            for j in range(totalGroups):
                if q: #if q is not empty (this seems repetitive but bc of for loop is necessary)
                    temp = q.pop(0) #pop name from q
                    j = j + 1 #move to next group of peopl
                    groupList[j].append(temp) #add person to this group
        PrintGroup(groupList) #algorithm is complete, call function to print groups to file

#while there are still people who have not visited everyone's house
while sum(g.degree(mode="in")) < (size*(size-1)): #this is marked by directed edges to each node
    CreateGroups(numKey, nameList) #create groups
    totalWeeks = totalWeeks + 1 #increase week count
toPrint.close() #close output file
g.vs["label"] = g.vs["name"]
#plot graph of visits in graph.pdf
ig.plot(g, vertex_color=['50, 168, 129'], vertex_frame_color=['white'], edge_color=['grey'], target = 'graph.pdf')
print("See smallgroups.txt for your smallgroup assignments.")

#EOF
