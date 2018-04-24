import Canvas
from re import search

startpos = (100,100)
def read_text(fileName):
    command_line = []
    tmp =[]
    flag2 = False
    flag3 = False
    tmpstr = ""
    try:
        with open(fileName) as file:
            new_line = file.read().replace('\n', ' ').split(" ")
            if len(new_line) != 0:
                tmpnum = 0
                for line in new_line:
                    if line == "define":
                        flag2 = True
                    elif line == "loop":
                        flag3 = True
                if not flag2 and not flag3:
                    for num in range(int((len(new_line)-1)/3)):
                        for i in range(3):
                            tmp.append(new_line[tmpnum])
                            tmpnum +=1
                        command_line.append(tmp)
                        tmp = []
                    try :
                        for num2,el in enumerate(command_line):
                            print(el[0],el[1],el[2])
                            globals()[el[0]](el[1],el[2])
                        
    
                    except : 
                        print("The command is invalid at line %d"%num2)
                elif not flag3 and flag2:
                    tmpstr += "def "
                    flag4 = False
                    flag5 = True
                    fncname = ""
                    value_number = 0
                    for num2,line in enumerate(new_line):
                        if line == "end":
                            flag5 = False
                        elif flag5 :
                            if num2 == 0:
                                pass
                            elif num2 == 1:
                                tmpstr += str(line)+"(): \n"
                                flag4 = True
                                fncname = str(line)
                            elif num2%3 == 1 and flag4:
                                tmpstr += str(line)+")\n"
                            elif num2%3 == 0 and flag4:
                                tmpstr += str(line)+","
                            elif num2%3 == 2 and flag4:
                                tmpstr += "\t"+str(line)+"("
                            else:
                                print("call")
                        elif line == fncname:
                            tmpstr += fncname+"()\n"
                        else:
                            if line in ["position","line","move"]:
                                tmpstr += str(line)+"("
                                value_number = num2
                            elif value_number == num2-1:
                                tmpstr += str(line)+","
                            elif value_number == num2-2:
                                tmpstr += str(line)+")\n"
                elif flag3 and not flag2:
                    tmpstr = ""
                    to_send = ""
                    value_number = 0
                    number_to_run = 0
                    flag6 = False
                    for num2,line in enumerate(new_line):
                        if line == "loop":
                            value_number = num2
                            number_to_run = new_line[num2+1]
                            flag6 = True
                        elif line == "end":
                            flag6 = False
                        elif flag6:
                            print(value_number)
                            if line in ["position","line","move"]:
                                to_send += str(line)+"("
                                value_number = num2
                            elif value_number == num2-1:
                                if line != number_to_run:
                                    to_send += str(line)+","
                            elif value_number == num2-2:
                                to_send += str(line)+")\n"
                        elif not flag6:
                            if line in ["position","line","move"]:
                                tmpstr += str(line)+"("
                                value_number = num2
                            elif value_number == num2-1:
                                tmpstr += str(line)+","
                            elif value_number == num2-2:
                                tmpstr += str(line)+")\n"
                    print(tmpstr)
                    loop(number_to_run, to_send,tmpstr) 

            else :
                print("File is empty !")
                newfile = input("Enter a new file path : ")
                read_text(newfile)
    except : 
        print("There is no such file or file is invalid ")
        newfile = input("Enter a new file path : ")
        read_text(newfile)
    print(tmpstr)
    exec(tmpstr,globals()) 
    Canvas.complete()
def position(x1,y1):
    
    global startpos
    startpos = (x1,y1)
    print(startpos)
    
def line(x2,y2):
    global startpos
    Canvas.create_line(startpos[0], startpos[1],int(startpos[0])+int(x2), int(startpos[1])+int(y2))
    print(startpos[0], startpos[1], int(startpos[0])+int(x2), int(startpos[1])+int(y2))
    startpos = (int(startpos[0])+int(x2),int(startpos[1])+int(y2))
    print(startpos)
def move(x3,y3):
    global startpos
    tmp_x = int(x3)+int(startpos[0])
    tmp_y = int(y3)+int(startpos[1])
    startpos = (tmp_x,tmp_y)
    print(startpos) 
def loop(number,to_run,code_before):
    exec(code_before, globals())
    for i in range(int(number)):
        print("loop")
        print(to_run)
        exec(to_run, globals())  
read_text("test3.txt")

