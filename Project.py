req = str(input("Please Enter a String The Last Char is $ \n"))
req =req.replace(" ", "")
req = list(req)
token = []

def digit(req):
    counter = 0
    summ = 0 
    sreq = []
    while counter < len(req):
        if(req[counter].isdigit() == True):
            for j in range(counter , len(req)):
                if(req[j].isdigit() == True):
                    summ = summ * 10
                    summ = summ + int(req[j])                    
                else:
                    sreq.append(summ)
                    counter = j - 1 
                    summ = 0
                    break
        else:
            sreq.append(req[counter])
        counter = counter + 1 
    return sreq
def dfa(req):
    if(isinstance(req[0],int)):
        token.append(["num", req[0]])
        return 1
    elif(req[0]=="i" and req[1]=="f"):
        token.append(["if","reserved word"])
        return 2
    elif(req[0]=="w" and req[1]=="h" and req[2]=="i" and req[3]=="l" and req[4]=="e"):
        token.append(["while","reserved word"])
        return 5
    elif(req[0]=="i" and req[1]=="n" and req[2]=="t"):
        token.append(["int","reserved word"])
        return 3
    elif(req[0]=="v" and req[1]=="o" and req[2]=="i" and req[3]=="d"):
        token.append(["void","reserved word"])
        return 4
    elif(req[0]=="r" and req[1]=="e" and req[2]=="t" and req[3]=="u" and req[4]=="r" and req[5]=="n"):
        token.append(["return","reserved word"])
        return 6
    elif(req[0]=="r" and req[1]=="e" and req[2]=="a" and req[3]=="d"):
        token.append(["read","reserved word"])
        return 4
    elif(req[0]=="w" and req[1]=="r" and req[2]=="i" and req[3]=="t" and req[4]=="e"):
        token.append(["write","reserved word"])
        return 5
    elif(req[0]=="p" and req[1]=="r" and req[2]=="i" and req[3]=="n" and req[4]=="t"):
        token.append(["print","reserved word"])
        return 5
    elif(req[0]=="c" and req[1]=="o" and req[2]=="n" and req[3]=="t" and req[4]=="i" and req[5]=="n" and req[6]=="u" and req[7]=="e"):
        token.append(["continue","reserved word"])
        return 8
    elif(req[0]=="b" and req[1]=="r" and req[2]=="e" and req[3]=="a" and req[4]=="k"):
        token.append(["break","reserved word"])
        return 5
    elif(req[0]=="b" and req[1]=="i" and req[2]=="n" and req[3]=="a" and req[4]=="r" and req[5]=="y"):
        token.append(["binary","reserved word"])
        return 6
    elif(req[0]=="d" and req[1]=="e" and req[2]=="c" and req[3]=="i" and req[4]=="m" and req[5]=="a" and req[6]=="l"):
        token.append(["decimal","reserved word"])
        return 7
    elif(req[0]=="("):
        token.append(["(", "symbol"])
        return 1
    elif(req[0]==")"):
        token.append([")", "symbol"])
        return 1
    elif(req[0]=="{"):
        token.append(["{", "symbol"])
        return 1
    elif(req[0]=="}"):
        token.append(["}", "symbol"])
        return 1
    elif(req[0]=="["):
        token.append(["[", "symbol"])
        return 1
    elif(req[0]=="]"):
        token.append(["]", "symbol"])
        return 1
    elif(req[0]==","):
        token.append([",", "symbol"])
        return 1
    elif(req[0]==";"):
        token.append([";", "symbol"])
        return 1
    elif(req[0]=="+"):
        token.append(["+", "symbol"])
        return 1
    elif(req[0]=="-"):
        token.append(["-", "symbol"])
        return 1
    elif(req[0]=="*"):
        token.append(["*", "symbol"])
        return 1
    elif(req[0]=="/"):
        token.append(["/", "symbol"])
        return 1
    elif(req[0]=="=="):
        token.append(["==", "symbol"])
        return 1
    elif(req[0]=="!="):
        token.append(["!=", "symbol"])
        return 1
    elif(req[0]==">"):
        token.append([">", "symbol"])
        return 1
    elif(req[0]==">="):
        token.append([">=", "symbol"])
        return 1
    elif(req[0]=="<"):
        token.append(["<", "symbol"])
        return 1
    elif(req[0]=="<="):
        token.append(["<=", "symbol"])
        return 1
    elif(req[0]=="="):
        token.append(["=", "symbol"])
        return 1
    elif(req[0]=="&&"):
        token.append(["&&", "symbol"])
        return 1
    elif(req[0]=="||"):
        token.append(["||", "symbol"])
        return 1
    elif(req[0]=="#"):
        token.append(["#", "symbol"])
        return 1
    elif(req[0]=="//"):
        token.append(["//", "symbol"])
        return 1
    elif(req[0]=="$"):
        token.append(["$", "$"])
        return 1
    else:
        token.append(["identifier",req[0]])
        return 1
def lexicalAnalysis(req):
    for i in range(dfa(req)):
        req.pop(0)
    if(len(req)==0):
        print("\n is okie")
    else:
        lexicalAnalysis(req)

lexicalAnalysis(digit(req))
# Work with File ...
f = open("2.txt" , "w+")
f.write(str(token))
f.close()
