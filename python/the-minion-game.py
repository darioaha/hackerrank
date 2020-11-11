def minion_game(string):
    size = len(string)
    vocals = ["A","E","I","O","U"]
    stuart = 0
    kevin = 0
    i=0
    while i < size: 
        if (string[i] not in vocals):
            pos = size
            stuart += size - i
            # while pos > 0:
            #     stuart.append(string[i:pos])
            #     pos = pos - 1
        if (string[i] in vocals):
            pos = size
            kevin += size - i
            # while pos > 0:
            #     kevin.append(string[i:pos])
            #     pos = pos - 1
        i+=1     
        
    # stuart = len(list(filter(None, stuart)))
    # kevin = len(list(filter(None, kevin)))
    if stuart > kevin:
        print("Stuart",stuart)
    elif stuart < kevin:
        print("Kevin",kevin)    
    else:
        print("Draw")
    
if __name__ == '__main__':
    s = input()
    minion_game(s)