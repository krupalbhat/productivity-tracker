import datetime,csv,re,os
def record():
    get_time_n_date()
    if statuschecker():
        dicty = {"day":datetimelist[1] , "timein":datetimelist[0]} 
        with open("statuschecker.txt", "w") as file:
            file.write("0")
    else:
        dicty = [{"timeout":datetimelist[0]} ]
        with open("statuschecker.txt", "w") as file:
            file.write("1")
            
    keys = ["day","timein","timeout"] #have to revisit
    with open("productivity.csv", "a") as file:
        writer = csv.DictWriter(file,fieldnames = keys)
        if not os.path.isfile("productivity.csv"):
            writer.writeheader()
        writer.writerow(dicty)

def statuschecker():
    with open("statuschecker.txt", "r+") as file:
        if not os.path.isfile("statuschecker.txt"):
            file.write("1")
        string = file.read()
        if string == "1":
            #file.write("0")
            return True
        elif string == "0":
            #file.write("1")
            return False    

def time_converter(regexresult):
    return int(regexresult[2])*3600+int(regexresult[3])*60+int(regexresult[4])
datetimelist = []
def get_time_n_date():
    timey = str(datetime.datetime.now())
    regexstring = r"^202\d-\d\d-(\d\d) (\d\d):(\d\d):(\d\d)"
    regexresult = re.search(regexstring,timey)
    int_time = time_converter(regexresult)
    datetimelist.append(int_time)
    datetimelist.append(regexresult[1])

    



string = "p"
if statuschecker():
    user_input = input("press space to start")
    if user_input == "":
        record()
    else:
        print("invalid input")

else:
    user_input = input("press space to end")
    if user_input == "":
        record()
    else:
        print("invalid input")