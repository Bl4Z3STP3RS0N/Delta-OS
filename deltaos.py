import random, sys, time, turtle, os, shutil
from datetime import datetime
from time import strftime

y1 = 'y'
y2 = y1
y3 = y1
y4 = y1
y5 = y1
y6 = y1
y7 = y1
y8 = y1
y10 = y1
y11 = y1
def info_screen():
    print("////About DeltaOS////")
    time.sleep(0.3)
    n()
    n()
    print("Version - 1.18")
    n()
    time.sleep(0.3)
    print(f"User name: {name}")
    n()
    time.sleep(0.3)
    print("Made by - Prathik")
    n()
    time.sleep(0.3)
    print("Storage used - 4 kb out of 10 kb")
    n()
    time.sleep(0.3)
    print("Total Ram - 8gb DDR4 SODIMM")
    n()
    time.sleep(0.3)
    print("Kernel level - 1023KF")
    n()
    time.sleep(0.3)
    print("Last Updated - 12/10/2025")
    n()
    time.sleep(0.3)
    input("Press the enter key to continue...")
    home_screen()
def seeker():
    global y11
    file_path = 'C:\\Users\\Delta_Os'
    while y11 == "y":
        print("//Welcome To Seeker//")

        print('\n'.join(os.listdir(file_path)))
        upp = input(
            'Do you want to do?:\n 1 - Create a new file or folder\n 2 - Read/write an existing file\n 3 - Delete a file or folder\n 4 - Open a folder\n Enter your choice: ')
        if upp == '1':
            uppp = input('New txt document, or New Folder?')
            if uppp == 'text':
                txt = input('What do you want to name it? ')
                txts = txt + '.txt'
                uhyo = input('What do you what to type in it?: ')
                try:
                    with open(file_path + txts, 'x') as f:
                        f.write(uhyo)
                        print("Text file created with the text!")
                except FileExistsError:
                    print('File already exists!!!')
            elif uppp == 'folder':
                name_filee = input('What do you want to name the file? ')
                try:
                    os.mkdir(file_path + name_filee)
                    print('File created!')
                except FileExistsError:
                    print('File already exists!')
            else:
                print('Wrong choice')


        elif upp == '2':
            file_name = input('Select by typing the file name: ')
            what_todo = input('what do you want to do with this file, (Read-r, Overwrite-w, Append-a or create c)')

            if what_todo == 'r':
                try:
                    with open(file_path + file_name, 'r') as f:
                        content = ''.join(f.readlines())
                        print(content)
                except FileNotFoundError:
                    print('File not found, Try  making it, or check if the file name is correct')
                except PermissionError:
                    print('You dont have permission to access this file')
            elif what_todo == 'w':
                write = input('What do you want to type?: ')
                try:
                    with open(file_path + file_name, 'w') as f:
                        f.write(write)
                        veiw_y_n = input('Written, Dow you want to veiw it? y/n')
                except FileNotFoundError:
                    print('File not found, Try  making it, or check if the file name is correct')
                except PermissionError:
                    print('You dont have permission to access this file')
            elif what_todo == 'a':
                writea = input('What do you want to type?: ')
                try:
                    with open(file_path + file_name, 'a') as f:
                        f.write(f'\n{writea}')
                        print('Text Appended!')
                except PermissionError:
                    print('You dont have permission to access this file')
                except FileNotFoundError:
                    print('File not found, Try  making it, or check if the file name is correct')
            else:
                print('Wrong choice')
        elif upp == '3':
            okkk = input('Name the file you want to delete: ')
            okkig = input('Is it an 1 - empty folder\n 2 - txt file\n 3 - folder?')
            if okkig == '1':
                try:
                    os.rmdir(file_path + okkk)
                    print('Folder deleted!')
                except PermissionError:
                    print('You dont have permission to delete this file')
            elif okkig == '2':
                try:
                    os.remove(file_path + okkk)
                    print('File deleted!')
                except PermissionError:
                    print('You dont have permission to delete this file')
            elif okkig == '3':
                try:
                    shutil.rmtree(file_path + okkk)
                    print('File deleted!')
                except PermissionError:
                    print('You dont have permission to delete this file')
            else:
                print('Wrong choice')
        elif upp == '4':
            name_fileee = input('Which folder do you want to open? ')
            print('\n'.join(os.listdir(file_path + name_fileee)))
            file_path = file_path + name_fileee + '\\'
            seeker()
        y11 = input("Do you want to continue? (y/n): ")



def timer():
    global y8
    while y8 == 'y':
        print("Welcome to Stopwatch")
        n()
        n()
        lahhh = int(input("How much time should it count down till (Second only!): "))
        looshh = 0
        for bloop in range(lahhh):
            print(looshh)
            looshh += 1
            time.sleep(1)
        print("Time is up!")
        y8 = input("Do you want to continue? (y/n): ")
    home_screen()
def shape_maker():
    print("Welcome to ShapeMaker")
    n()
    n()
    print("What shape do you want?")
    time.sleep(0.3)
    n()
    print("1 - Circle")
    time.sleep(0.3)
    n()
    print("2 - Rectangle")
    time.sleep(0.3)
    n()
    print("3 - Square")
    time.sleep(0.3)
    n()
    print("4 - Triangle")
    time.sleep(0.3)
    n()
    print("5 - Hexagon")
    time.sleep(0.3)
    n()
    labanana = int(input("Your choice: "))
    n()
    lac = input("Which color do you want?: ")
    print("Loading", end='')
    screen = turtle.Screen()
    screen.bgcolor("black")
    pen = turtle.Turtle()
    pen.shape("circle")
    pen.pensize(3)
    for uy in range(4):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.6)
    pen.color(lac)
    if labanana == 1:
        pen.circle(80)
    elif labanana == 2:
        for _ in range(2):
            pen.forward(100)
            pen.right(90)
            pen.forward(150)
            pen.right(90)

    elif labanana == 3:
        for labababa in range(4):
            pen.forward(100)
            pen.right(90)
    elif labanana == 4:
        for labababa in range(3):
            pen.forward(100)
            pen.right(120)
    elif labanana == 5:
        for labababa in range(6):
            pen.forward(100)
            pen.left(60)
    else:
        print("Wrong choice")
    home_screen()
a = 'uhh'
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def n():
    print()
def calc():
    global y2
    while y2 == 'y':
        n()
        aa = int(input("First number: "))
        n()
        ab = int(input("Second number: "))
        n()
        loll = input("What do you want to do? add (a), subtract (s), multiply (m), or divide (d): ")
        n()
        if loll == "a":
            bruh = aa + ab
            print("Their sum is", bruh)
        elif loll == "s":
            bruh = aa - ab
            print("Their difference is", bruh)
        elif loll == "m":
            bruh = aa * ab
            print("Their Product is", bruh)
        elif loll == "d":
            bruh = aa / ab
            print("Their quotient is", bruh)
        else:
            print("Wrong choice")
        n()
        y2 = input("Do you want to Continue? (y/n): ")

    home_screen()

def word_finder():
    global y3
    while y3 == 'y':
        n()
        ab = input(" Enter you're essay : ")
        n()
        ac = input(" Which word do you want to search for ?  ")
        n()
        acc = ab.find(ac)
        print(ab.replace(ac, "-" + ac + "-"))
        n()
        print(f"This essay has {acc} {ac}s")
        n()
        y3 = input("Do you want to continue? (y/n): ")
    home_screen()

def dice_game():
    global y4
    while y4 == 'y':
        print(
            "Rules\n In this game, you can roll the dice, and even the computer rolls the dice\nAt the end, whoever gets the highest score wins\n There are only 10 tries")
        p1 = 0
        p2 = 0
        for prr in range(10):
            n()
            lah = random.randint(1, 6)
            lahh = random.randint(1, 6)
            print(f"You got {lah} and I got {lahh}")
            p1 = lah + p1
            p2 = lahh + p2
        if p1 > p2:
            print("You win!")
        elif p2 > p1:
            print("I win!")
        y4 = input("Do you want to continue? (y/n): ")
    home_screen()

def typing_animating():
    global y5
    while y5 == 'y':
        t = input("Type What you want to say in type animation: ")
        bloo = 0
        print("", end="")
        for blud in range(len(t)):
            sys.stdout.write(t[bloo])
            sys.stdout.flush()
            time.sleep(0.5)
            bloo = bloo+1
        n()
        y5 = input("Do you want to continue? (y/n): ")
    home_screen()





def get_grade(score, subject):
    if score >= 80 and score <= 100:
        grade, msg = "A", "Good"
    elif score >= 60:
        grade, msg = "B", "Good"
    elif score >= 40:
        grade, msg = "C", "Okay"
    elif score >= 20:
        grade, msg = "D", "Better luck next time"
    else:
        grade, msg = "F", "It is high time you start studying"

    print(f"{msg}, you got a {grade} in {subject}")
    n()  # Spacing after each result
    return score


def grade_calculator():
    global y6
    while y6 == 'y':
        print("Give the marks out of 100, and this program will give the grades")
        n()

        grd = int(input("What is your grade/class level? "))
        n()

        # Input Section
        math = float(input("Maths: "))
        n()
        eng = float(input("English: "))
        n()
        lang2 = float(input("2nd language: "))
        n()
        lang3 = float(input("3rd language: "))
        n()

        scores = [math, eng, lang2, lang3]

        # High School Branch
        if 5 < grd <= 10:
            chem = float(input("Chemistry: "))
            n()
            bio = float(input("Biology: "))
            n()
            phys = float(input("Physics: "))
            n()
            hist = float(input("History: "))
            n()
            geo = float(input("Geography: "))
            n()

            get_grade(chem, "Chemistry")
            get_grade(bio, "Biology")
            get_grade(phys, "Physics")
            get_grade(hist, "History")
            get_grade(geo, "Geography")
            scores.extend([chem, bio, phys, hist, geo])

        # Primary/Middle School Branch
        elif 0 < grd <= 5:
            sci = float(input("Science: "))
            n()
            sst = float(input("SST: "))
            n()

            get_grade(sci, "Science")
            get_grade(sst, "SST")
            scores.extend([sci, sst])

        # Core Subjects Results
        get_grade(math, "Math")
        get_grade(eng, "English")
        get_grade(lang2, "2nd Language")
        get_grade(lang3, "3rd Language")

        # Final Calculation
        avg = sum(scores) / len(scores)
        print(f"Your average mark is: {avg:.2f}")
        get_grade(avg, "the entire exam")

        y6 = input("Do you want to continue? (y/n): ").lower()
        n()
    home_screen()






def palindrome_checker():
    global y7
    while y7 == 'y':
        ae = input('what is the word you think will be the same whene you reverse it? ')

        if ae == ae[-1::-1]:
            print('yeh, it is true')
        else:
            print(f'no , it isnt true, see for yourself: {ae[-1::-1]}')
        y7 = input('Do you want to continue? (y/n): ')
    home_screen()

def home_screen():
    clear_screen()
    print("////Home screen////")
    n()
    time.sleep(0.3)
    print("Time is", datetime.now().strftime("%H:%M"))
    n()
    time.sleep(0.3)
    print("1 - Rock Paper Scissors")
    n()
    time.sleep(0.3)
    print("2 - Calculator")
    n()
    time.sleep(0.3)
    print("3 - Word Finder")
    n()
    time.sleep(0.3)
    print("4 - Dice Game")
    n()
    time.sleep(0.3)
    print("5 - Typing animating")
    n()
    time.sleep(0.3)
    print("6 - grade calculator")
    n()
    time.sleep(0.3)
    print("7 - Palindrome Checker")
    n()
    time.sleep(0.3)
    print("8 - Stopwatch")
    n()
    time.sleep(0.3)
    print("9 - Shape maker")
    n()
    time.sleep(0.3)
    print("10 - Seeker")
    n()
    time.sleep(0.3)
    print("About")
    n()
    time.sleep(0.3)
    print("Or you can Shut down")
    n()
    time.sleep(0.3)
    bb = input("Your choice: ")
    if bb == "1":
        clear_screen()
        rock_paper_scissors()
    elif bb == "2":
        clear_screen()
        calc()
    elif bb == "3":
        clear_screen()
        word_finder()
    elif bb == "4":
        clear_screen()
        dice_game()
    elif bb == "5":
        clear_screen()
        typing_animating()
    elif bb == "6":
        clear_screen()
        grade_calculator()
    elif bb == "7":
        clear_screen()
        palindrome_checker()
    elif bb == "8":
        clear_screen()
        timer()
    elif bb == "shut down":
        print("Shutting down", end="")
        for u in range(8):
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(0.6)
        sys.exit()
    elif bb == "9":
        clear_screen()
        shape_maker()
    elif bb == "10":
        clear_screen()
        seeker()
    elif bb == "about":
        clear_screen()
        info_screen()
    else:
        clear_screen()
        print("Wrong choice")
        home_screen()


def rock_paper_scissors():
    global y1
    clear_screen()
    while y1 == 'y':  # run while player wants to play
        print("Welcome to Rock Paper Scissors")
        n()
        how_much = int(input("How many points should we play to? "))
        n()
        p1 = 0
        p2 = 0

        while p1 < how_much and p2 < how_much:  # loop until someone wins
            lol = random.randint(1, 3)  # 1 = rock, 2 = paper, 3 = scissors
            your_choice_haha = input("Choose your option (rock/paper/scissors): ")
            n()
            print("rock")
            time.sleep(1)
            print("paper")
            time.sleep(1)
            print("scissors")
            n()

            if lol == 1:
                if your_choice_haha == 'rock':
                    print('tie')
                elif your_choice_haha == 'paper':
                    print('You win a point')
                    p1 += 1
                elif your_choice_haha == 'scissors':
                    print('I win a point')
                    p2 += 1
                else:
                    print('Wrong choice')

            elif lol == 2:
                if your_choice_haha == 'rock':
                    print('I win a point')
                    p2 += 1
                elif your_choice_haha == 'paper':
                    print("tie")
                elif your_choice_haha == 'scissors':
                    print("You win a point")
                    p1 += 1
                else:
                    print('Wrong choice')

            elif lol == 3:
                if your_choice_haha == 'rock':
                    print('You win a point')
                    p1 += 1
                elif your_choice_haha == 'paper':
                    print('I win a point')
                    p2 += 1  # fixed bug: you had p2 = p1+1
                elif your_choice_haha == 'scissors':
                    print('tie')
                else:
                    print('Wrong choice')

            n()
        if p1 > p2:
            print(f"{name} You win !!!")
        elif p2 > p1:
            print("I win !!!")
    y1 = input("Do you want to play again? (y/n): ")
time.sleep(1)
print("Booting", end="")
for i in range(8):
    sys.stdout.write(".")
    sys.stdout.flush()
    time.sleep(0.6)
print()
x= 0
print("Loading files", end="")
for x in range(8):
    sys.stdout.write(".")
    sys.stdout.flush()
    time.sleep(0.6)
clear_screen()
print("Welcome to Delta OS")
n()
name = input("What is the user's name?: ")
n()
print("Hello ", end="")
ll = 0
for y in range(len(name)):
    sys.stdout.write(name[ll])
    sys.stdout.flush()
    time.sleep(0.3)
    ll = ll + 1
clear_screen()
home_screen()







