def BFHelp():
    print '> : go to next cell;'
    print '< : go to previous cell;'
    print '+ : add 1 to value in curren cell;'
    print '- : substract 1 from value in curren cell;'
    print '. : print value of current cell;'
    print ', : input value to current cell;'
    print '[ : if value of current cell is 0, go to appropriate ];'
    print '] : if value of current cell is not 0, go to appropriate [.'
    print 'Also there are additional operators:'
    print '* : asc for ASCII-code'
    print '? : help'
    print

def DefCycles (programm):
    cycles = {}
    temp_cycle = []
    for j in range(len(programm)):
        if programm[j] == '[':
            temp_cycle.append((j, 0))
        elif programm[j] == ']':
            temp_cycle.append((j, 1))
    while len(temp_cycle) > 0:
        flag = True
        for i in range(len(temp_cycle) - 1):
            if temp_cycle[i][1] == 0 and temp_cycle[i+1][1] == 1:
                flag = False
                cycles[temp_cycle[i][0]] = temp_cycle[i+1][0]
                cycles[temp_cycle[i+1][0]] = temp_cycle[i][0]
                del temp_cycle[i:i+2]
                break
        if flag == True:
            return None
    return cycles

def InterpProg (programm, startdata):
    i = 0
    data = startdata[:]
    cycles = DefCycles(programm)
    if cycles is None:
        print "Error cycle code!"
        return None
    j = 0
    while j < len(programm):
        x = programm[j]
        if x == '>':
            i += 1
            if i >= len(data):
                data.append(0)
            j += 1
        elif x == '<':
            if i == 0:
                print "Segmentation fault!"
                return None
            else:
                i -= 1
            j += 1
        elif x == "+":
            data[i] += 1
            if data[i] > 255:
                print "Value error!"
                return None
            j += 1
        elif x == "-":
            data[i] -= 1
            if data[i] < 0:
                print "Value error!"
                return None
            j += 1
        elif x == '.':
            print chr(data[i])
            j += 1
        elif x == ',':
            data[i] = ord(raw_input('> '))
            j += 1
        elif x == '[':
            if data[i] == 0:
                j = cycles[j]
        elif x == ']':
            if data[i] != 0:
                j = cycles[j]
        elif x == "*":
            print "This operator doesn't exist in initial language and is added for your comfort."
            c = raw_input("Which simbol? ")
            print ord(c)
            j += 1
        elif x == '?':
            print "This operator doesn't exist in initial language and is added for your comfort."
            BFHelp()
            j += 1
        else:
            print "Error programm code!"
            return None
    return data

def Coding():
    BFHelp()
    while True:
        print "Code:"
        s = raw_input()
        result = InterpProg(s, [0])
        if result is not None:
            print "Resulting string: ", result
        while True:
            answer = raw_input("Try again? y/n: ")
            if answer == 'y':
                break
            elif answer == 'n':
                return

Coding()
