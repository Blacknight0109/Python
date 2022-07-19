File = open("Jaishu.txt", "r")
lines = set()
CountJaishnav = 0
CountPrem = 0
CountDeepanshu = 0
for k in File:
    lines.add(k)
    if ("Jaishnav" in k):
        CountJaishnav = CountJaishnav + 1
        
    elif ("Prem" in k):
        CountPrem = CountPrem + 1
        
    elif ("Deepanshu" in k):
        CountDeepanshu = CountDeepanshu + 1
        
    #if ("Jaishnav" in k):
        #print("Jaishnav is present")
        #break
print("There are {} Jaishnav, {} Prem and {} Deepanshu".format(CountJaishnav, CountPrem, CountDeepanshu))
