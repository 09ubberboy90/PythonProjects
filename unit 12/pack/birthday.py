#book = {"John" : {"month" : "Sep", "day":15},"Johnr" : {"month" : "Aug", "day":28},"Johnu" : {"month" : "Jul", "day":5},"Johni" : {"month" : "Sep", "day":2}}
book = {}
month_list = ["Sep","Oct","Nov","Dec","Jan","Feb","Mar","Apr","May","Jun","Jul","Aug"]
date_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]

def name(search_name,file):
    try : 
        tmp = search_name+ "  " + str(file[search_name])
    except :
        print("Please input a correct name")
        newname = input("New name : ")
        name(newname, file)

    if tmp == "  ":
        print( "Sorry there is no birthday for this person")
    else : 
        print(tmp)
    gui(file)
def Formating(formatstr):
    tmp = []
    for i in formatstr:
        tmp.append(i)
    tmp[0] = tmp[0].upper()
    tmp[1] = tmp[1].lower()
    tmp[2] = tmp[2].lower()
    return "".join(tmp)
def month(search_month,file):
    search_month = Formating(search_month)
    if search_month in month_list:
        if search_month in month_list:
            for name in file:
                for date in file[name]:
                    if file[name][date] == search_month:
                        tmp = name + "  " +str(file[name])
                    else : 
                        tmp =""
            if tmp == "":
                print( "Sorry there is no upcomming birthday")
            else : 
                print(tmp)
    else:
        print("Please input a correct month")
        month1 = input("New month to input : ")
        month(month1, book)
    gui(file)
def upcomming(search_date,search_month,file):
    search_month = Formating(search_month)
    if search_date not in date_list:
        print("Please input correct value")
        newdate = input("New Date : ")
        upcomming(int(newdate), search_month, file)   
    if search_month not in month_list:
        newmonth = input("New Month : ")
        upcomming(search_date, newmonth, file)
    
    month_to_search = [search_month]
    days_to_search = []
    buffer= []
    results = []
    for num,months in enumerate(month_list):
        if months == search_month:
            if search_month == "Feb":
                if search_date > 21:
                    month_to_search.append(month_list[num+1])
                    days_to_search = date_list[search_date:28]+date_list[:28-search_date]
                else:
                    days_to_search = date_list[search_date:search_date+7]
            elif search_month == "Oct" or "Dec" or "Jan" or "Mar" or "May" or "Jul" or "Aug":
                if search_date > 24:   
                    if month_to_search == "Aug":
                        month_to_search.append(month_list[0])
                    else :
                        month_to_search.append(month_list[num+1])
                    days_to_search = date_list[search_date:31]+date_list[:7-(31-search_date)]
                    
                else:
                    days_to_search = date_list[search_date:search_date+7]
            else : 
                if search_date > 23:
                    month_to_search.append(month_list[num+1]) 
                    days_to_search = date_list[search_date:30]+date_list[:7-30-search_date]
                else:
                    days_to_search = date_list[search_date:search_date+7]
                    
    for month_enum in month_to_search:
        for day_enum in days_to_search:
            for name in file:
                for date in file[name]:
                    if file[name][date] == month_enum and day_enum:
                        buffer.append(name + "  " +str(file[name]))
    for el in buffer:
        if el not in results:          
            results.append(el)
    if results == []:
        print( "Sorry there is no upcomming birthday")
    else : 
        print(results)
    gui(file)
"""upcomming(4, "Sep", book)
upcomming(29, "Aug", book)
upcomming(15, "Mar", book)"""
def getBirthdays(fileName, book):
    try:
        with open(fileName) as file:
            new_line = file.read().replace('\n', ' ').split(" ")
            if len(new_line) != 0 :
                for el in new_line:
                    ndsplit = el.split(",")
                    book[ndsplit[0]] = {"Month":ndsplit[1],"Date":ndsplit[2]}
            else :
                print("File is empty !")
                newfile = input("Enter a new file path : ")
                getBirthdays(newfile, book)
    except : 
        print("There is no such file or file can't be accessed ")
        newfile = input("Enter a new file path : ")
        getBirthdays(newfile, book)
    else : 
        print(book)
        gui(book)
def adddate(file):
    name = input("Please Input name : ")
    date = input("Please Input date : ")
    months = input("Please Input month : ")
    months = Formating(months)
    if int(date) in date_list:
        pass
    if months in month_list:
        pass
    else : 
        print("Please input correct value")
        adddate(file)
    file[name] = {"Month":months,"Date":date}
    gui(file)
def gui(book):
    if type(book) == dict:
        choice = input("""choose : 
        1) Upcomming birthday
        2) Search by date
        3) Search by name
        4) Add a new birthday
        5) Add from database
        6) Show database
        7) Quit
        Choice : """)
        if choice == "1" :
            date_to_find = input("Date to search : ")
            month_to_find = input("Month to search : ")
            print(upcomming(int(date_to_find), month_to_find, book))
        elif choice == "2" :
            month_to_find = input("Month to search : ")
            print(month(month_to_find, book))
        elif choice == "3" :
            name_to_find = input("Name to search : ")
            print(name(name_to_find, book))
        elif choice == "4" :
            adddate(book)
        elif choice == "5" :
            path = input("Path to file : ")
            print(getBirthdays(path, book))
        elif choice == "6":
            print(book)
            gui(book)
        elif choice == "7" :
            quit()
        else : 
            print("THIS IS WRONG\nPlease enter a correct value")
            gui(book)
    else : 
        print("Please input a correct database")
        newbook = input("New databook : ")
        gui(newbook)
gui(book)