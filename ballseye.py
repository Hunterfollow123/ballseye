# @Hunterfollow123
# Use for legal purposes only
import os
import random
import time
import sys

# clear
def c():
    os.system("clear")
    
c()

# Lists
list_1 = []
list_2 = []
list_3 = ["123", "1234", "159753", "123456789", "12345", "123456", "1234567", "12345678", "321", "0", "0000", "12", "13", "2", "1", "3", "666", "69", "2020", "2019", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010", "2009"]    


# input function
def ask(x):
    s = str(input("\nTarget \33[91m" + x + "\33[97m : \33[97m"))
    list_1.append(s)
    list_2.append(s)
    if s == "":
        print("\33[93mQuestion ignored\33[97m")
        list_1.remove(s)
        list_2.remove(s)   
        

def add():
    while True:
        a = str(input("\33[97m\nAdd any word you want :\33[97m "))
        list_1.append(a)
        list_2.append(a)
        if a == "":
            print("\33[93mQuestion ignored\33[97m")
            list_1.remove(a)
            list_2.remove(a)
            break


def w():
    for i in enumerate(list(range(101))):
        print("writing the list..", str(i) + "%", end="\r")
        time.sleep(0.02)


def rm():
    content = open(file_name_2, "r").readlines()
    content_set = set(content)
   
    cleandata = open(file_name_2, "w")
  
    for line in content_set:
       cleandata.write(line)

def t(s):
        for i in s + '\n':
                sys.stdout.write(i)
                sys.stdout.flush()
                time.sleep(10. / 2100)

def ban():
    os.system("clear")
    print(" ")
    t("  ____        _ _                     ") 
    t(" |  _ \      | | |                     ")
    t(" | |_) | __ _| | |___  ___ _   _  ___  ")
    t(" |  _ < / _` | | / __|/ _ \ | | |/ _ \ ")
    t(" | |_) | (_| | | \__ \  __/ |_| |  __/ ")
    t(" |____/ \__,_|_|_|___/\___|\__, |\___| ")
    t("                            __/ |       V2")
    t("                           |___/       ")
    t("       By : Hunter Follow    ")
    t("   ")
    t("  ")
    t("  \33[93m[\33[97m1\33[93m]\33[97m Make wordlist  ") 
    t("  \33[93m[\33[97m0\33[93m]\33[97m Exit\n")

    
banner = """

  ____        _ _                      
 |  _ \      | | |                     
 | |_) | __ _| | |___  ___ _   _  ___  
 |  _ < / _` | | / __|/ _ \ | | |/ _ \ 
 | |_) | (_| | | \__ \  __/ |_| |  __/ 
 |____/ \__,_|_|_|___/\___|\__, |\___| 
                            __/ |       V2
                           |___/       
       By : Hunter Follow    
   
  
  \33[93m[\33[97m1\33[93m]\33[97m Make wordlist   
  \33[93m[\33[97m0\33[93m]\33[97m Exit
"""

banner_2 = """

  ____        _ _                      
 |  _ \      | | |                     
 | |_) | __ _| | |___  ___ _   _  ___  
 |  _ < / _` | | / __|/ _ \ | | |/ _ \ 
 | |_) | (_| | | \__ \  __/ |_| |  __/ 
 |____/ \__,_|_|_|___/\___|\__, |\___| 
                            __/ |       V2
                           |___/       
       By : Hunter Follow    
   
"""
ban()

while True:
    cmd = str(input("ballseyeV2_> "))
    if cmd == "1":
        list_1.clear()
        list_2.clear()
        
        c()
        print(banner_2)
        ask("name")
        ask("family name")
        ask("phone number")
        ask("birth year")
        ask("birth month")
        ask("birth day")
        
        while True:
            nickname = str(input("\nTarget \33[91mnickname \33[97m: "))
            list_1.append(nickname)
            list_2.append(nickname)
            if nickname == "":
                print("\33[93mQuestion ignored\33[97m")
                list_1.remove(nickname)
                list_2.remove(nickname)
                break
      
        ask("gf\33[97m/\33[91mbf name")
        ask("pet name")
        ask("favourite game")
        ask("favourite show")
        ask("favourite show\33[97m/\33[91manime character")
        ask("favourite artist\33[97m(\33[91msinger\33[97m/\33[91mactor\33[97m)")
       
        add()
        file_name = str(input("\n\33[92mPlease name the file : \33[97m"))
        file_name_2 = file_name + ".txt"
        if ".txt" in file_name:
            file_name_2 = file_name + ""
        
        file = open(file_name_2, "w")
        
        def write():
            for i in range(15000):
                
                randomm = random.choice(list_1)
                randoom = random.choice(list_2)
                randooom = random.choice(list_3)
                rndm = randomm + randoom + "\n"
                randm = randomm + randoom + randooom + "\n"
                rndam = randomm + randooom + "\n"
                collab = randomm + randooom + randoom + "\n"
                collab_2 = randooom + randomm + randoom + "\n"
              
                             
                file.write(rndm)
                file.write(randm)
                file.write(rndam)
                file.write(collab)
                file.write(collab_2)
       
        start = input("\nPress Enter to start \33[91m>> \33[97m")
        c()
        print(banner)
        w()
        write()
        rm()
        print("\n\nDone :)\n\npath : " + "\33[92m" + file_name_2 + "\n\33[97m")
        
    elif cmd == "0":
        print("\nExiting...", end="\r")
        time.sleep(0.5)
        print("bye :D     \n")
        exit()
  
  
  
    elif cmd == "":
        None
 
 
 
    else:
        print("[\33[91mInvalid !\33[97m]")


