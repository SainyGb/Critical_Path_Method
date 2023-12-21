# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 16:35:00 2019

@author: Alfonso
"""
line = list() #contains a single line
singleElement = list()
tasks = dict() #contains all the tasks
number = -1
fhand = open('cpm1_new.txt') #TWO FILES: cpm.txt and cpm1.txt

count = 0
for line in fhand: #slide the file line by line
    singleElement=(line.split(',')) #split a line in subparts
    print(singleElement)
    number += 1
    for i in range(len(singleElement)): #creating the single task element
        tasks['task'+ str(singleElement[0])]= dict()
        tasks['task'+ str(singleElement[0])]['id'] = singleElement[0]
        tasks['task'+ str(singleElement[0])]['name'] = singleElement[1]
        tasks['task'+ str(singleElement[0])]['duration'] = singleElement[2]
        if(singleElement[3] != "\n"):
            tasks['task'+ str(singleElement[0])]['dependencies'] = singleElement[3].strip().split(';')
        else:
            tasks['task'+ str(singleElement[0])]['dependencies'] = ['-1']
        tasks['task'+ str(singleElement[0])]['ES'] = 0
        tasks['task'+ str(singleElement[0])]['EF'] = 0
        tasks['task'+ str(singleElement[0])]['LS'] = 0
        tasks['task'+ str(singleElement[0])]['LF'] = 0
        tasks['task'+ str(singleElement[0])]['float'] = 0
        tasks['task'+ str(singleElement[0])]['isCritical'] = False
        count +=1
print(count)
# =============================================================================
# FORWARD PASS
# =============================================================================

#Complexidade do foward pass: O(V^2)*O(E) => Considerando que E é O(V): O(V^2)*O(V)
for keys,taskFW in tasks.items(): #slides all the tasks                                                                     #faz isso para cada vértice(task) O(V)
    if('-1' in tasks[keys]['dependencies']): #checks if it's the first task
        taskFW['ES'] = 1
        taskFW['EF'] = (tasks[keys]['duration'])
    else: #not the first task
        for k, values in tasks.items():                                                                                     #faz isso para cara vértice(task)  O(V)
            for dipendenza in values['dependencies']: #slides all the dependency in a single task                           #faz isso para cada aresta(dependencies) O(E)
                #print('task ' + taskFW + ' k '+ k + ' dipendenza ' +dipendenza)
                if(dipendenza != '-1' and len(tasks[k]['dependencies']) == 1): #if the task k has only one dependency
                    values['ES'] = int(tasks['task'+ dipendenza]['EF']) +1
                    values['EF'] = int(tasks[k]['ES']) + int(tasks[k]['duration']) -1
                elif(dipendenza !='-1'): #if the task k has more dependency
                    if(int(tasks['task'+dipendenza]['EF']) > int(values['ES'])):
                        values['ES'] = int(tasks['task'+ dipendenza]['EF']) +1
                        values['EF'] = int(values['ES']) + int(values['duration']) -1




# =============================================================================
# BACKWARD PASS
# =============================================================================

#Complexidade do Backward pass: O(V)*O(E) => O(V*E)

bList = list() #list of task keys
for element in tasks:
    bList.append(element)
bList.reverse()

for taskBW in bList:                                                                                                        #faz isso para cara vértice(task)  O(V)
    if(bList.index(taskBW) == 0): #check if it's the last task (so no more task)ha
        tasks[taskBW]['LS']=tasks[taskBW]['ES']
        
    for dipendenza in tasks[taskBW]['dependencies']: #slides all the dependency in a single task                            #faz isso para cada aresta(dependencies) O(E)
        if(dipendenza != '-1'): #check if it's NOT the last task
            if(tasks['task'+ dipendenza]['LF'] == 0): #check if the the dependency is already analyzed
                #print('ID dipendenza: '+str(tasks['task'+dipendenza]['id']) + ' taskBW: '+str(tasks[taskBW]['id']))
                tasks['task'+ dipendenza]['LF'] = int(tasks[taskBW]['LS']) -1
                tasks['task'+ dipendenza]['LS'] = int(tasks['task'+ dipendenza]['LF']) - int(tasks['task'+ dipendenza]['duration']) +1
                tasks['task'+ dipendenza]['float'] = int(tasks['task'+ dipendenza]['LF']) - int(tasks['task'+ dipendenza]['EF'])
                #print('IF1 dip LS: '+str(tasks['task'+dipendenza]['LS']) +' dip LF: '+str(tasks['task'+dipendenza]['LF']) + ' taskBW: '+str(tasks[taskBW]['id'])+' taskBW ES '+ str(tasks[taskBW]['ES']))
            if(int(tasks['task'+ dipendenza]['LF']) >int(tasks[taskBW]['LS']) ): #put the minimun value of LF for the dependencies of a task
                tasks['task'+ dipendenza]['LF'] = int(tasks[taskBW]['LS']) -1
                tasks['task'+ dipendenza]['LS'] = int(tasks['task'+ dipendenza]['LF']) - int(tasks['task'+ dipendenza]['duration']) +1
                tasks['task'+ dipendenza]['float'] = int(tasks['task'+ dipendenza]['LF']) - int(tasks['task'+ dipendenza]['EF'])
                #print('IF2 dip LS: '+str(tasks['task'+dipendenza]['LS']) +' dip LF: '+str(tasks['task'+dipendenza]['LF']) + ' taskBW: '+str(tasks[taskBW]['id']))
# =============================================================================
# PRINTING  
# =============================================================================

#Complexidade total => O(V)*O(E)*O(V) + O(V)*O(E); Temos que a complexidade é O(V^2*E)

print('task id, task name, duration, ES, EF, LS, LF, float, isCritical')
for task in tasks:
    if(tasks[task]['float'] == 0):
        tasks[task]['isCritical'] = True
    print(str(tasks[task]['id']) +', '+str(tasks[task]['name']) +', '+str(tasks[task]['duration']) +', '+str(tasks[task]['ES']) +', '+str(tasks[task]['EF']) +', '+str(tasks[task]['LS']) +', '+str(tasks[task]['LF']) +', '+str(tasks[task]['float']) +', '+str(tasks[task]['isCritical']))
    
        

             
            
        
        
        
        
        
    



    














