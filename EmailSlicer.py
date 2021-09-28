#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

def emailSlicer():
    try:
        emailFile = input("Please enter the path of the file you would like to analyze\n Make sure that each email is spaced on different lines\n")
        slicer(readFile(emailFile))
    except:
        print("File not found!")
    
    
def slicer(email):
    masterList = []
    
    for i in email:
        masterList.append(i.split("@"))
        
    count(masterList)

    
def count(masterList):
    domains = []
    usernames = []
    
    for i in range(len(masterList)):
        domains.append(masterList[i][1])
        usernames.append(masterList[i][0])
    
    domainCounter = Counter(domains)
    usernameCounter = Counter(usernames)
    
    analyze = int(input("\nWhat would you like to analyze?\n [1] Usernames\n [2] Domains \n [3] Both\n"))
    
    if analyze == 1: 
        plotUsernames(usernameCounter)
    elif analyze == 2:
        plotDomain(domainCounter)
    elif analyze == 3:
        plotUsernames(usernameCounter)
        plotDomain(domainCounter)
    else:
        print("Sorry I dont understand, exiting program now!")
    
    
def plotDomain(domainCounter):
    domains = []
    prompt = " "
    print("\nPlease type the domains you wish to graph!\n Example: gmail.com \nPress enter when finished\n")
    line = input(prompt)
    
    while line:
        domains.append(line)
        line = input(prompt)
        
    domainy = []
    
    for i in range(len(domains)):
        domainy.append(domainCounter[domains[i]])
    
    try:
        plotType = int(input("How would you like the data plotted?\n [1] Bar graph\n [2] Pie Chart\n"))
    except:
        print("Sorry an error occured!")
        quit()
    
    if plotType == 1:
        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])
        ax.bar(domains,domainy)
        ax.set_title("Occurences of duplicate domains")
        ax.set_xlabel("Domains")
        ax.set_ylabel("Frequency")
        plt.yticks(np.arange(min(domainy), max(domainy)+1, 1.0))
        plt.show()
    elif plotType == 2:
        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])
        ax.axis('equal')
        ax.pie(domainy, labels = domains,autopct=make_autopct(domainy))
        ax.set_title("Occurences of duplicate domains")
        plt.show()
    else:
        print("Sorry I dont understand, exiting program now!")
    
def plotUsernames(usernameCounter):
    usernames = []
    prompt = " "
    print("\nPlease type the usernames you wish to graph!\n Example: username123 \nPress enter when finished")
    line = input(prompt)
    
    while line:
        try:
            usernames.append(line)
            line = input(prompt)
        except:
            print("Sorry an error occured!")
        
    usernamesy = []
    
    for i in range(len(usernames)):
        usernamesy.append(usernameCounter[usernames[i]])
    try:
        plotType = int(input("How would you like the data plotted?\n [1] Bar graph\n [2] Pie Chart\n"))
    except:
        print("Sorry an error occured!")
        quit()
        
    if plotType == 1:
        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])
        ax.bar(usernames,usernamesy)
        ax.set_title("Occurences of duplicate usernames")
        ax.set_xlabel("Usernames")
        ax.set_ylabel("Frequency")
        plt.yticks(np.arange(min(usernamesy), max(usernamesy)+1, 1.0))
        plt.show()
    elif plotType == 2:
        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])
        ax.axis('equal')
        ax.pie(usernamesy, labels = usernames,autopct=make_autopct(usernamesy))
        ax.set_title("Occurences of duplicate usernames")
        plt.show()
    else:
        print("Sorry I dont understand, exiting program now!")
    
def readFile(file):
    f = open(file, "r")
    emailList = []
    
    for i in f:
        emailList.append(i)
    
    f.close()
    emailListEdited = []
    
    for i in range(len(emailList)):
        emailListEdited.append(emailList[i].rstrip("\n"))
    
    return emailListEdited   
    
def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct
    
emailSlicer()


# In[ ]:




