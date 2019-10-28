# starSigns
quiz game to study starsigns

# starsigns

my first personal project
tool to understand and memorize starsigns
defines classes for signs and elements
https://cosmicnavigator.com/about/astrology/the-four-elements-and-three-modalities

# classes
class Signs:
variants:
methods:
recallable(self,round): 
input: current round
output: 1 if can be recalled this round, else 0
the higher the grade, the longer distance between rounds

#lists


# bugs:


can still see stuff after clear, after reviewing stuff (only on linux/mac (??))

# next step:
ask for signs number first, then propose automatically default rounds
default rounds is dependent on chosen amount of starsigns, so it is possible to solve all of them (e.g. 4 signs need at least 12 rounds, so 20 would be appropriate)

overview diagram at beginning to vidualize elements, modalities and signs
ask for another round if finished
choose difficulty levels (lenght of recall_list)
class Session (recalled, rounds, how many, result)
class User (Session history, signsStats)
seperate recall_list for element and modality
learnfactor (def 0) sigmoid learn factor (def 0.5)
simgoid learn factor: SLF= =1/(1+EXP(-LF))

# done:
rounds go from 1 to round of number: 1, 2, 3, .. 20
added method recallable (round - last_round - grade)>1
if sign not recallable kicked out of quiz_list
added again from StarsignsToAdd if recallable
show recallable: (round - last_round - grade)>1 before recall
attribute last round tested, default -10 
recalltype: present dates, recall sign, option to choose that recall type.
attribute dates: start and enddate
choose standard parameters(3 signs, 12 rounds)
clear screen after every round, so i cant cheat. but leave result first, then clear with return
at end: first grades, then "you mastered all" message
if mastered none, give extra message
round choice at beginning
##hide all helper print commands
outro and feedback
intro and manual
tip: only 3 letters as answer ok.
let user choose to see review first
Introduce starsigns in quizlist so user can review first
make introduction specific (month,element,modality)
chose different recall modes based on choice
give choice between month and element recall
method ask zodiac element and modality
recall game element and modality
ask for input how many rounds
ask for input how long StarsignList: if below 3, then quizlist short too
final result number differs after all rounds and finished early
starsigntoadd has elements of quizlist, need to take them out
tell how many rounds i did at the end
good_list: list with words i learnt (max level)
check when to add new sign
check if there is anything to add
if yes, then add out of to addlist (avoid double)
List StarsignListGrades: grades of all signs
List StarsignsToAdd: grade below max, so i can add to quiz_list
evaluate quiz_list with list quiz_list_grades: grade of every sign in quiz_list
Grade as its own attribute (sum of recall_list)
during recall game: check if grade is max: then kick out of list
if quiz_list is empty, give feedback that game is finished
make quiz list of 4 items to recall, in each round choose randomly from them
recall list is a 3 element stack list
fixed bug: recall list is now instance attribute, not class attribute. hat to be initiated with constructor
method ask month: changed answered right or wrong and edit LF: +1 wenn richtig, -1 wenn falsch, 
3 object attributes: recalled, correct and incorrect 
object list stats to collect correct and incorrect results
recall only 2 signs
recall 5 times
































done:
define element class
define modality class
define starsign class

todo:
basic riddle: 
- tell me month of starsign
- tell me element of starsign
- tell me modality of starsign
- tell me power and 

real date attribute:
- enter your date and i tell you the starsign
- incorporate into riddle

advanced riddle:
- rememeber how many i had correct
- rememebr which zodiacs i had most success
- show me the harder ones more oftern
- remember my stats and write in json.file.

1	zodiac app
1.	functionality
a.	Enter data and receive star sign
b.	Gib zfufall datum und ich rate sternzeichen
c.	Statistik über gute und schlechte zeichen
d.	Radominze nach guten und schlechten zeichen
e.	Remember statistik
f.	Remember name: aks for name, propose names in database
g.	
2.	methods
a.	Library {zodiac, datum; learnfaktor: 0.5}
b.	Funciton: date -> starsign
3.	tricks
a.	dezember datum needs other evaluation