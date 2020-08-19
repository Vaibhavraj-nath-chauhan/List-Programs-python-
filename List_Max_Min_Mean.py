# # Q - Find Min Max and Mean
#      * For All data
#      * For Row wise
#      * For Col Wise


data = [
    [23,33,33,44,4],
    [213,32,32,3,3],
    [55,66,44,66,7]
]


# # For All Data.........................................................

def All_data(data):
    k = []
    for i in data:
        for j in i:
            k.append(j)
    print(k)
    print("Min Value is:-->",min(k),end="  ............  ")
    print("Max Value is:-->",max(k),end="  ............  ")
    print("Mean of Whole Data:-->",sum(k)/len(k))
    
All_data(data)


# # For Row data.........................................................

def Row_data(data):
    p =1
    for i in data:
        print(i)
        print("Max in row {}:-->".format(p),max(i),end="  ............  ")
        print("Min in row {}:-->".format(p),min(i),end="  ............  ")
        print("Mean of row {}:-->".format(p),sum(i)/len(i))
        print("\n")
        p+=1

Row_data(data)


# # For Col data.........................................................

def Col_data(data):
    k =[]
    for ran in range(len(data[0])):
        for i in data:
            k.append(i[ran])
        print(k)
        print("Max in Col:-->", max(k),end="  ............  ")
        print("Min in Col:--.", min(k),end="  ............  ")
        print("Mean in Col:-->",sum(k)/len(k))
        print("\n")
        k=[]
        
Col_data(data)




