# starsigns
# tool to understand and momorize starsigns
# startsigns class is subclass from classes modalities and elements
# 
# written by
# Andreas Schiedermeier
# Munich, August 2019
# aschiedermeier@gmail.com

# dev var
# if True: developer mode - print variables troughout the program to track
# if False: user mode - no variables shown 
dev = False 

# function to clear screen
# import ystem from os 
from os import system, name 

# import sleep to show output for some time period 
from time import sleep 
  
# define clear function to wipe screen 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

##############################################################
## DEFINE CLASSES

class Element():
    ''' element class '''
    def __init__(self,name="",aspect=""):
        '''initialze name and aspect attributes'''
        self.name = name
        self.aspect = aspect

    def get_descriptive_name(self):
        '''return a neatly formatted name and desctiption'''
        if self.aspect != "":
            long_name = "Element " + self.name + " represents " + self.aspect + "."
            return long_name
        else:
            long_name = "Element " + self.name + "."
            return long_name         

fire = Element("fire","action & creativity")
water = Element("water","emotions")
air = Element("air","intellect")
earth = Element ("earth","substance & practicality")

class Modality():
    ''' class modality '''
    def __init__(self,name="",power=""):
        '''initialze name and power attributes'''
        self.name = name
        self.power = power

    def get_descriptive_name(self):
        '''return a neatly formatted name and desctiption'''
        if self.power != "":
            long_name = "The " + self.name + " modality marks the power of " + self.power + "."
            return long_name
        else:
            long_name = self.name + " modality" + "." 
            return long_name.capitalize()         

cardinal = Modality("cardinal","initiation")
fixed = Modality("fixed","sustaining")
mutable = Modality("mutable","change")

class Starsign ():
    '''class starsign with classes Element & Modality as attributes'''
    # max_grade defines the length of the recall_list
    max_grade = 3
    def __init__(self,name,month,dates,last_round=-10,recalled = 0,correct=0,incorrect=0):
        '''initialze name and aspect attributes'''
        self.name = name
        self.month = month
        self.dates = dates
        self.last_round=last_round
        # how often recall method was used
        self.recalled = recalled
        # how often answered correctly
        self.correct = correct
        # how often answered incorrectly
        self.incorrect = incorrect
        # list of recall stats, list length can be parameter for tuning later
        self.recall_list=[0]*self.max_grade
        self.grade =  sum(self.recall_list)
        self.modality = Modality()
        self.element = Element()
         
    def get_descriptive_name(self):
            '''return a neatly formatted name and desctiption'''
            long_name = "The starsign " + self.name + " is born in " + self.month + "\nIt's root power is " + self.modality.name + " " + self.element.name + "."
            return long_name

    def get_dates(self):
            '''return dates of sign'''
            long_name = "The starsign " + self.name + " is born in the time of " + self.dates + "."
            return long_name    
            
    def get_month(self):
            '''return main month of sign'''
            long_name = "The starsign " + self.name + " is born mainly in " + self.month + " and before."
            return long_name

    def get_element(self):
            '''return element of sign'''
            long_name = "The starsign " + self.name + "'s element is " + self.element.name + ", which represents " + self.element.aspect + "."
            return long_name
                
    def get_modality(self):
            '''return modality of sign'''
            long_name = "The starsign " + self.name + "'s modality is " + self.modality.name + " with the power of " + self.modality.power + "."
            return long_name

    def get_recall_stats(self):
        '''return how often been recalled: correct and incorrect'''
        recall_stats = ("The starsign " + self.name + " has been recalled " + str(self.recalled) + " times.\nCorrect: " 
        + str(self.correct) + "\t\tIncorrect: " + str(self.incorrect)+ "\nStats: " + str(self.recall_list)
        + "\tGrade: " + str(self.grade) )
        return recall_stats
        
    def set_element(self,element):
        '''set the element of a starsign'''
        self.element = element

    def set_modality(self,modality):
        '''set the modality of a starsign'''
        self.modality = modality 

    def recall_dates(self):
        ''' recall starsign with given birthdate range'''
        print ("Which sign is born on the days of " + self.dates + "?")
        if dev == True:
            print ("Hint:",self.name)
        ans = input("Answer: ").lower()
        ans = ans[0:3]
        self.recalled += 1
        self.last_round = round # last_round is current round
        if ans == self.name[0:3].lower():
            print ("Yes, it's " + self.name + "!")
            input("\nPress 'return' for next item!\n")
            # call clear function we defined above 
            if dev == False:
                clear() 
            self.correct += 1
            del(self.recall_list[0])
            self.recall_list.append(1)
        else:
            print ("No, it's " + self.name + "!")
            input("\nPress 'return' for next item!\n")
            # call clear function we defined above 
            if dev == False:
                clear() 
            self.incorrect += 1
            del(self.recall_list[0])
            self.recall_list.append(-1)
        self.grade = sum(self.recall_list)

    def recall_month(self,round): ##
        ''' recall month of starsign '''
        print ("When is the time of " + self.name + "?")
        if dev == True:
            print ("Hint:",self.month) ##
        ans = input("Answer: ").lower()
        ans = ans[0:3]
        self.recalled += 1
        self.last_round = round # last_round is current round
        if ans == self.month[0:3].lower():
            print ("Yes, it's " + self.month + "!")
            input("\nPress 'return' for next item!\n")
            # call clear function we defined above 
            if dev == False:
                clear() 
            self.correct += 1
            del(self.recall_list[0])
            self.recall_list.append(1)
        else:
            print ("No, it's " + self.month + "!")
            input("\nPress 'return' for next item!\n")
            # call clear function we defined above 
            if dev == False:
                clear() 
            self.incorrect += 1
            del(self.recall_list[0])
            self.recall_list.append(-1)
        self.grade = sum(self.recall_list)
        
    def recall_element(self):
        ''' recall element of starsign '''
        print ("What is the element of " + self.name + "?")
        if dev == True:
            print ("Hint:",self.element.name)
        ans = input("Answer: ").lower()
        ans = ans[0:3]
        self.recalled += 1
        self.last_round = round # last_round is current round
        if ans == self.element.name[0:3].lower():
            print ("Yes, it's " + self.element.name + "!")
            input("\nPress 'return' for next item!\n")
            # call clear function we defined above 
            if dev == False:
                clear() 
            self.correct += 1
            del(self.recall_list[0])
            self.recall_list.append(1)
        else:
            print ("No, it's " + self.element.name + "!")
            input("\nPress 'return' for next item!\n")
            # call clear function we defined above 
            if dev == False:
                clear() 
            self.incorrect += 1
            del(self.recall_list[0])
            self.recall_list.append(-1)
        self.grade = sum(self.recall_list)

    def recall_modality(self):
        ''' recall momodaliy of starsign '''
        print ("What is the modality of " + self.name + "?")
        if dev == True:
            print ("Hint:",self.modality.name)
        ans = input("Answer: ").lower()
        ans = ans[0:3]
        self.recalled += 1
        self.last_round = round # last_round is current round
        if ans == self.modality.name[0:3].lower():
            print ("Yes, it's " + self.modality.name + "!")
            input("\nPress 'return' for next item!\n")
            # call clear function we defined above 
            if dev == False:
                clear()            
            self.correct += 1
            del(self.recall_list[0])
            self.recall_list.append(1)
        else:
            print ("No, it's " + self.modality.name + "!")
            input("\nPress 'return' for next item!\n")
            # call clear function we defined above 
            if dev == False:
                clear() 
            self.incorrect += 1
            del(self.recall_list[0])
            self.recall_list.append(-1)
        self.grade = sum(self.recall_list)
    
    def recallable(self,round):
        ''' return if recallable in this round '''
        if (round - self.last_round - self.grade)>1:
            return 1
        else:
            return 0      

# define 12 starsign objects
aries = Starsign("Aries","April","21 March – 20 April")
aries.set_modality(cardinal)
aries.set_element(fire)
taurus = Starsign("Taurus","May","21 April – 21 May")
taurus.set_modality(fixed)
taurus.set_element(earth)
gemini = Starsign("Gemini","June","22 May – 21 June")
gemini.set_modality(mutable)
gemini.set_element(air)
cancer = Starsign("Cancer","July","22 June – 22 July")
cancer.set_modality(cardinal)
cancer.set_element(water)
leo = Starsign("Leo","August","23 July – 22 August")
leo.set_modality(fixed)
leo.set_element(fire)
virgo = Starsign("Virgo","September","23 August – 23 September")
virgo.set_modality(mutable)
virgo.set_element(earth)
libra = Starsign("Libra","October","24 September – 23 October")
libra.set_modality(cardinal)
libra.set_element(air)
scorpio = Starsign("Scorpio","November","24 October – 22 November")
scorpio.set_modality(fixed)
scorpio.set_element(water)
sagittarius = Starsign("Sagittarius","December","23 November – 21 December")
sagittarius.set_modality(mutable)
sagittarius.set_element(fire)
capricorn = Starsign("Capricorn","January","22 December – 20 January")
capricorn.set_modality(cardinal)
capricorn.set_element(earth)
aquarius = Starsign("Aquarius","February","21 January – 19 February")
aquarius.set_modality(fixed)
aquarius.set_element(air)
pisces = Starsign("Pisces","March","20 February – 20 March")
pisces.set_modality(mutable)
pisces.set_element(water)

# list of 12 signs
StarsignList = [aries,taurus,gemini,cancer,leo,virgo,libra,scorpio,sagittarius,capricorn,aquarius,pisces]

##############################################################
## START INTRO TO GAME

# Intro text
clear()
print ()
print ("*"*60)
print (" "*20, "ZODIAC TRAINER")
print ("""Program to learn Dates, month, element and modality of the 12 western startsigns.

The twelve zodiac signs are grouped into four elements with their distinct traits. 
Each of the four elements has a cardinal , a fixed , and a mutable modality.
Four elements times three modalities equals twelve distinct energy fields and therefore the twelve signs. 

A sign is mastered, if you recall it correctly 3 times in a row.
To type in an answer, the first 3 letters are sufficient, e.g. 'apr' for April.

In this program, 'month' means the main month of a starsign.
The cutoff day is around the 20th of the main month and the rest of the month before.
This is not alwys 100% correct (E.g. Libra: September 24 – October 23), but an easy way to cover most people's birthdays. ;-)

Have fun studying!
""")

# Recall quiz of Starsigns using recall method

# ask what to recall: month, element or modality 
modeDict = {"dat":"dates","mon":"month","ele":"element","mod":"modality"}
if dev == False:
    entered = False
    while entered == False:
        mode = input("What do you want to recall?\nDates, month, element or modality: ")
        mode = mode.lower() 
        mode = mode[0:3]
        if  mode not in modeDict:
            print ("Please choose one of the 4!")
        else: 
            entered = True
    print ("We will recall the", modeDict[mode], "of starsigns.")
    print()

if dev == True:
    mode = "dat"
# ask how many rounds of recalling 
entered = False
while entered == False:
    rounds = input("Recall how many rounds? 'Return' for default 30.\nMin 1: ")
    if rounds == "":
        rounds = 30
    try:
        rounds = int(rounds)
    except ValueError:
        print ("Error: wrong input")
        continue
    if  not (1 <= rounds):
        print ("Error: the value is too low. (Min 1)")
    else: 
        entered = True
print()

# ask how many Starsigns to recall (1-12)
entered = False
while entered == False:
    signs = input("Recall how many Starsigns? 'Return' for default 4.\n1-12: ")
    if signs == "":
        signs = 4
    try:
        signs = int(signs)
    except ValueError:
        print ("Error: wrong input")
        print()
        continue
    if  not (1 <= signs <= 12):
        print ("Error: the value is not within permitted range (1-12)")
        print()
    else: 
        entered = True

# based on choice 'signs' shortening of StarsignList after shuffling
# those signs will be recalled in this session over several rounds
from random import shuffle

# in dev no shuffle, better to track progress
if dev == False:
    shuffle(StarsignList)

StarsignList = StarsignList[:signs]

print("\nSigns to recall:")
for sign in StarsignList:
    print ("- " + sign.name)
    
# review signs before quiz
entered = False
while entered == False:
    review = input("\nDo you want to review those starsigns first?\ny/n: ")
    print()
    if  review == "y":
        for sign in StarsignList:
            if mode == "dat":
                print(sign.get_dates())
            if mode == "mon":
                print(sign.get_month())
            if mode == "ele":
                print(sign.get_element())
            if mode == "mod":
                print(sign.get_modality())
        input("\nPress 'return' when you are ready!\n")
        # call clear function we defined above 
        if dev == False:
            clear() 
    else: 
        print ("Cool, let's go!")
        if dev == False:
            clear() 
    entered = True  
print()        


# quiz_list    
# list containing elements to choose from in the coming rounds
# beginning fixed number of elements
# take elements out if they reach max grade
# add elements later if elements progress
quiz_list=[] # list with object (hard to read, but callable)
quiz_list_names=[] # list with object names (easy to read, but as str not usable)

# len_quiz_list defines initial lenght of quiz_list
# should be 3, unless signs < 3
if signs < 3:
    len_quiz_list = signs
else:
    len_quiz_list = 3
## print("signs:",signs)
## print("len_quiz_list:",len_quiz_list)


##############################################################
## START GAME

# initial filling of quiz_list can be made in round 
# fill quiz_list with len_quiz_list starsigns
# chosen randomly out of StarSignList
# no doubles allowed
from random import randint
while len(quiz_list) < len_quiz_list:
    i = randint(0,len(StarsignList)-1)
    new_sign = StarsignList[i]
    if new_sign not in quiz_list:
        quiz_list.append(new_sign)
        quiz_list_names.append(new_sign.name)

if dev == True:
    print ("quiz_list_names: ", quiz_list_names)
# print(quiz_list[0].name)
# quiz_list[0].recall_list = [0,1,1]
# quiz_list[0].grade = 2
# print(quiz_list[0].grade)

# print(quiz_list[1].name)
# quiz_list[1].recall_list = [1,1,1]
# quiz_list[1].grade = 3
# print(quiz_list[1].grade)

# print(quiz_list[2].name)
# quiz_list[2].recall_list = [1,1,1]
# quiz_list[2].grade = 3
# print(quiz_list[2].grade)

# recall quiz
for round in range(1,rounds+1):
    # call out mode and round
    print (modeDict[mode].capitalize(), "of starsigns: Round", round, "out of",rounds)

    # delete maxgades from focus_list
    quiz_list = [i for i in quiz_list if  i.grade < i.max_grade]
    quiz_list_names = [i.name for i in quiz_list if  i.grade < i.max_grade]
    if dev == True:
        print ("quiz_list_names: ", quiz_list_names)

    # bad_signs: signs with a grade 2 or more below max_grade
    # len(bad_signs) should be kept as quiz_list_len, 
    # so if some words become too good, i blend some more difficult words into the quiz_list
    bad_signs =[i.name for i in quiz_list if i.grade < i.max_grade-1]
    if dev == True:
        print ("bad_signs_",bad_signs)

    # good_list: signs i learnt
    # can be sorted at the end of the round, 
    # if i start saving signs, then i need to sort this list at the very beginning
    good_list = [i for i in StarsignList if i.grade == i.max_grade]
    good_list_names = [i.name for i in StarsignList if i.grade == i.max_grade]
    if dev == True:
        print ("good_list:",good_list_names)

    # refill quiz_list
    # 1. condition: less than e.g. 3 "bad signs" (should also work for first filling)
    # 2. still signs left to refill from StarsignList, otherwise all are in good_list or quiz_list
    while (len(bad_signs) < len_quiz_list) and ( len(good_list) + len(quiz_list) < len (StarsignList)):
        i = randint(0,len(StarsignList)-1)
        new_sign = StarsignList[i]
        # no doubles
        # no maxgrades 
        if new_sign not in quiz_list and new_sign.grade != new_sign.max_grade:
            quiz_list.append(new_sign)
            quiz_list_names.append(new_sign.name)
            print("New sign added to Quizlist:", new_sign.name)
            bad_signs =[i.name for i in quiz_list if i.grade < i.max_grade-1]
            if dev == True:
                print ("bad_signs after refill: ",bad_signs)

    if dev == True:
        print ("quiz_list after refill: ", quiz_list_names)     

    if dev == True:
        "quiz_list recallable attribute: ",
        for i in quiz_list:
            print (i.recallable(round))

    # pick_list: the final list to pick from
    # only the recallable ones from the quiz_list
    pick_list = [i for i in quiz_list if i.recallable(round) == 1]
    pick_list_names = [i.name for i in quiz_list if i.recallable(round) == 1]
    if dev == True:
        print("pick_list: ",pick_list_names)
    
    # if no recallables left, i loosen the rules step by step
    # trying to get the most recallable sign
    # if there are almost no signs left
    r = 1
    while len (pick_list) == 0:    
        pick_list = [i for i in quiz_list if i.recallable(round+r) == 1]
        pick_list_names = [i.name for i in quiz_list if i.recallable(round+r) == 1]
        if dev == True:
            print("!!! loosened_pick_ist: ",pick_list_names, "r: ",r)
        r += 1

    if dev == True:
        print("pick_ist: ",pick_list_names)        

    # if no recallables left, i can't avoid doubles, so i recall from quiz_list,
    # with the loosened pick list this should not be necassary any more        
    # pick_list = quiz_list

    # recall random sign out of pick_list
    i = randint(0,len(pick_list)-1) ## !!! if pick_list is empty, here comes error!!!
    ## print ("Starsign",i+1, "out of",len(pick_list))
    if dev == True:
        print(pick_list[i].get_recall_stats())##
        print ("Round: ",round)
        print ("Last_round: ",pick_list[i].last_round)
        print ("Grade: ",pick_list[i].grade)
        print ("Round - last_round - grade: ",round-pick_list[i].last_round-pick_list[i].grade)
        print ("Recallable?: ",(round-pick_list[i].last_round-pick_list[i].grade)>1)
        print ("Real Recallable?: ",pick_list[i].recallable(round))
        print()

    if mode == "dat":
        pick_list[i].recall_dates()
    if mode == "mon":
        pick_list[i].recall_month(round)
    if mode == "ele":
        pick_list[i].recall_element()
    if mode == "mod":
        pick_list[i].recall_modality()
    ## print(pick_list[i].get_recall_stats())
    
    #good_list: signs i learnt, if this list is as long as Starsignlist: game over
    good_list = [i for i in StarsignList if i.grade == i.max_grade]
    good_list_names = [i.name for i in StarsignList if i.grade == i.max_grade]
    if dev == True:
        print ("good_list after round:",round,":" ,good_list_names)

    if dev == True:
        print ("StarsignList: ", len(StarsignList))

    if len(good_list) == len(StarsignList):
        print("\nWohoo, you have mastered every item!")
        break



## clear() 

# print out mastered signs, distinguish between one and several signs            
if len(good_list_names) == 1:
    print ("\nAfter",round,"rounds you have mastered the following sign:")
    for sign in good_list_names:
        print ("- " + sign)
elif len(good_list_names) != 0:
    print ("\nAfter",round,"rounds you have mastered the following", len(good_list), "signs:")
    for sign in good_list_names:
        print ("- " + sign)
elif len(good_list_names) == 0:
    print ("\nAfter",round,"rounds you have achieved the following grades:")
    for sign in good_list_names:
        print ("- " + sign)

# if len(quiz_list) == 0:
#     print("\nWohoo, you have mastered every item!")

#print ("good_list:",good_list_names)

print("\nGrades:")
for sign in StarsignList:
    print (sign.name, " --> Grade:", sign.grade)


print ("""\nThanks for playing. :-)
This is my first program in Python, for feedback email to: aschiedermeier@gmail.com
Andi
""")


### old code
## should be not necesary any more
# 
"""

    # evaluate quiz_list 
    quiz_list_grades = []
    for sign in quiz_list:
        quiz_list_grades.append(sign.grade)
    ## print("Quizlistgrades:",quiz_list_grades)
    
    ## all signs of this session
    print("\nSigns to recall:")
    for sign in StarsignList:
        print ("- " + sign.name)
    
    ## evaluate StarsignList 
    StarsignListGrades = []
    for sign in StarsignList:
        StarsignListGrades.append(sign.grade)
    print("StarsignListGrades:",StarsignListGrades)
    
    # Starsigns to add to quiz_list
    # grade below max, recallable (not in last round or sec to last round if better etc.) and not double
    StarsignsToAdd = []
    StarsignsToAddNames = []
    for sign in StarsignList:
        if (sign.grade < sign.max_grade) and ((round-sign.last_round-sign.grade)>0) and (sign not in quiz_list):
            StarsignsToAdd.append(sign)
            StarsignsToAddNames.append(sign.name)       
    ## print(StarsignsToAdd)
    ## print("StarsignsToAddNames:",StarsignsToAddNames)
    
    # check, if i need to add new items
    # bad_list: items in quiz_list, that are still bad (2 below max).
    # len(bad_list) must be like initial len(quiz_list), therefore needs to be refilled, if some items get too good(1 below max or max)
    bad_list = [i.name for i in quiz_list if i.grade < i.max_grade-1]
    print ("bad_list:",bad_list)
    if len(bad_list) < len_quiz_list:
        # check if i should add
        # if yes, add random item from StarsignsToAdd
        if len(StarsignsToAdd)!=0:
            i = rn.randint(0,len(StarsignsToAdd)-1)
            add_sign = StarsignsToAdd[i]
            quiz_list.append(add_sign)
            quiz_list_names.append(add_sign.name)
            print("New sign added to Quizlist:", add_sign.name)
    
    # game over, if quiz_list is empty
    if len(quiz_list) == 0:
        if len(good_list) == len(StarsignList):
            print ("You really finished all signs!")
            break
        else:
            print ("I need to fix the code, as so many signs are left:", len(StarsignList) - len(good_list) )
            break
    """ 