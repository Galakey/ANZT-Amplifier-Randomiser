import random
import tkinter
import customtkinter
import os
import csv
from PIL import Image, ImageTk
from playsound import playsound
import threading
import time

outputPath = "./data/output.csv"
background = "./data/stream_bg.png"
try:
    bg_frames = len([name for name in os.listdir("./data/bg")])
except FileNotFoundError as e:
    bg_frames = 0

class Player:
    def __init__(self, rank, name, icon):
        self.name = name
        self.rank = rank
        self.icon = icon

class Team:
    def __init__(self, name, players: [], rank, matchBlock):
        self.name = name
        self.players = players
        self.rank = rank
        self.matchBlock = matchBlock

    def __lt__(self, other):
        return self.rank < other.rank

choices = ["Silver", "Gold", "Prismatic"]
class MatchBlock:
    def __init__(self, ID):
        self.ID = ID
        self.amp1 = random.choice(choices)
        self.amp2 = random.choice(choices)
        self.amp3 = random.choice(choices)

    def getAmps(self):
        return [self.amp1, self.amp2, self.amp3]

matchBlockA = MatchBlock("A")
matchBlockB = MatchBlock("B")
matchBlockC = MatchBlock("C")
matchBlockD = MatchBlock("D")
matchBlockE = MatchBlock("E")
matchBlockF = MatchBlock("F")
matchBlockG = MatchBlock("G")
matchBlockH = MatchBlock("H")
matchBlockI = MatchBlock("I")
matchBlockJ = MatchBlock("J")
matchBlockK = MatchBlock("K")
matchBlockL = MatchBlock("L")
matchBlockM = MatchBlock("M")
matchBlockN = MatchBlock("N")
matchBlockO = MatchBlock("O")
matchBlockP = MatchBlock("P")

matchBlocks = [matchBlockA, matchBlockB, matchBlockC, matchBlockD, matchBlockE,
               matchBlockF, matchBlockG, matchBlockH, matchBlockI, matchBlockJ,
               matchBlockK, matchBlockL, matchBlockM, matchBlockN, matchBlockO, matchBlockP]

class MatchBlocks:
    def __init__(self):
        self.matchBlocks = matchBlocks

    def getMatchBlock(self, ID):
        for matchBlock in self.matchBlocks:
            if matchBlock.ID == ID:
                return matchBlock

    def getAmps(self, ID):
        for matchBlock in self.matchBlocks:
            if matchBlock.ID == ID:
                return matchBlock.getAmps()

mb = MatchBlocks()

amplifierDir = "./data/amplifiers"
teamsDir = "./data/teams"
amplifierCount = len([name for name in os.listdir(amplifierDir)])
amplifierName = []
teams = []
output = {}

silverDir = "./data/amplifiers/silver"
goldDir = "./data/amplifiers/gold"
prismaticDir = "./data/amplifiers/prismatic"
silverCount = len([name for name in os.listdir(silverDir)])
goldCount = len([name for name in os.listdir(goldDir)])
prismaticCount = len([name for name in os.listdir(prismaticDir)])

silvers = []
golds = []
prismatic = []

nodupe = {
    1: [],
    2: [],
    3: [4, 5],
    4: [3, 5],
    5: [3, 4],
    6: [],
    7: [],
    8: [27],
    9: [],
    10: [],
    11: [],
    12: [],
    13: [],
    14: [],
    15: [16, 17],
    16: [15, 17],
    17: [15, 16],
    18: [],
    19: [],
    20: [21, 22],
    21: [20, 22],
    22: [20, 21],
    23: [24],
    24: [23],
    25: [26],
    26: [25],
    27: [8],
    28: [29],
    29: [28],
    30: [],
    31: [32, 33],
    32: [31, 33],
    33: [31, 32],
    34: [],
    35: [],
    36: [],
    37: [38, 39],
    38: [37, 39],
    39: [37, 38],
    40: []
}

for card in os.listdir(silverDir):
    silvers.append(card)

for card in os.listdir(goldDir):
    golds.append(card)

for card in os.listdir(prismaticDir):
    prismatic.append(card)

for team in os.listdir(teamsDir):
    curPlayers = []
    for player in os.listdir(f"{teamsDir}/{team}"):
        player = player.split(sep="$")
        curPlayers.append(Player(player[0], player[1][:-4], f"{team}/{player[0]}${player[1]}"))
    rank, matchBlock, name = team.split(sep="$")
    t = Team(name, curPlayers, rank, matchBlock)
    teams.append(t)

teams = sorted(teams)

class Control:

    def __init__(self):
        self.teams = teams
        self.teamCount = len([name for name in os.listdir(teamsDir)])
        self.current = 1

    def next(self):
        clearCards()
        if self.current >= self.teamCount:
            self.current = 1
            return self.current
        self.current += 1
        return self.current

    def prev(self):
        clearCards()
        if self.current <= 1:
            self.current = self.teamCount
            return self.current
        self.current -= 1
        return self.current

    def getCount(self):
        print(self.teamCount)

    def getCurrent(self):
        return self.current

    def getCurrentTeam(self):
        return self.teams[self.current - 1]


control = Control()


customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("1280x720")
app.title("ANZT Amplifiers")

background_image = tkinter.PhotoImage(file=background)
background_label = tkinter.Label(image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

card_size = (int(728 / 2.2), int(895 / 2.2))

image1 = Image.open(f"./data/Box.png")
image1 = image1.resize(card_size)
test1 = ImageTk.PhotoImage(image1)
width, height = test1.width(), test1.height()

label_image1 = tkinter.Label(app, bg="#243953", width=width, height=height, image=test1)
label_image1.place(x=90, y=220)

label_image2 = tkinter.Label(app, bg="#243953", width=width, height=height, image=test1)
label_image2.place(x=460, y=220)

label_image3 = tkinter.Label(app, bg="#243953", width=width, height=height, image=test1)
label_image3.place(x=840, y=220)


player1Icon = Image.open(f"./data/teams/{control.getCurrentTeam().players[0].icon}")
player1Icon = player1Icon.resize((int(150), int(150)))
player1Icon = ImageTk.PhotoImage(player1Icon)
width, height = player1Icon.width(), player1Icon.height()

label_player1Icon = tkinter.Label(app, bg="#243953", width=width, height=height, image=player1Icon)
label_player1Icon.place(x=190, y=28)

font = ("Crimson Pro", 20)
label_player1Name = tkinter.Label(app, bg="#243953", text=control.getCurrentTeam().players[0].name, fg="white", font=font, anchor="w")
label_player1Name.place(x=350, y=28)

font_rank = ("Crimson Pro", 20)
label_player1Rank = tkinter.Label(app, width=7, height=1, bg="#243953", text=f"#{control.getCurrentTeam().players[0].rank}", fg="white", font=font_rank, anchor="w")
label_player1Rank.place(x=350, y=78)

player2Icon = Image.open(f"./data/teams/{control.getCurrentTeam().players[1].icon}")
player2Icon = player2Icon.resize((int(150), int(150)))
player2Icon = ImageTk.PhotoImage(player2Icon)
width, height = player2Icon.width(), player2Icon.height()

label_player2Icon = tkinter.Label(app, bg="#243953", width=width, height=height, image=player2Icon)
label_player2Icon.place(x=760, y=28)

font = ("Crimson Pro", 20)
label_player2Name = tkinter.Label(app, bg="#243953", text=control.getCurrentTeam().players[1].name, fg="white", font=font, justify="right", anchor="e")
label_player2Name.place(x=550, y=28, width=200)

font_rank = ("Crimson Pro", 20)
label_player2Rank = tkinter.Label(app, width=7, height=1, bg="#243953", text=f"#{control.getCurrentTeam().players[1].rank}", fg="white", font=font_rank, justify="right", anchor="e")
label_player2Rank.place(x=550, y=78, width=200)


font = ("Crimson Pro", 20)
label_teamName = tkinter.Label(app, bg="#243953", text=f"{control.getCurrentTeam().name} | #{control.getCurrentTeam().rank}", fg="white", font=font, justify="center", anchor=tkinter.CENTER)
label_teamName.place(x=380, y=130, width=350)
def clearCards():
    box = Image.open(f"./data/Box.png")
    clear = ImageTk.PhotoImage(box)
    label_image1.configure(image=clear)
    label_image1.image = clear
    label_image2.configure(image=clear)
    label_image2.image = clear
    label_image3.configure(image=clear)
    label_image3.image = clear


def buttonNext():
    buttonSound()
    cur = control.next() - 1
    updateCurrentTeam(cur)


def buttonPrev():
    buttonSound()
    cur = control.prev() - 1
    updateCurrentTeam(cur)


def updateCurrentTeam(num):
    currentTeam = teams[num]
    p1 = currentTeam.players[0]
    p2 = currentTeam.players[1]
    newPlayerIcon = Image.open(f"./data/teams/{p1.icon}")
    newPlayerIcon = newPlayerIcon.resize((int(150), int(150)))
    newPlayerIcon = ImageTk.PhotoImage(newPlayerIcon)

    label_player1Icon.configure(image=newPlayerIcon)
    label_player1Icon.image = newPlayerIcon
    label_player1Name.configure(text=p1.name)
    label_player1Rank.configure(text=f"#{p1.rank}")

    newPlayerIcon = Image.open(f"./data/teams/{p2.icon}")
    newPlayerIcon = newPlayerIcon.resize((int(150), int(150)))
    newPlayerIcon = ImageTk.PhotoImage(newPlayerIcon)

    label_player2Icon.configure(image=newPlayerIcon)
    label_player2Icon.image = newPlayerIcon
    label_player2Name.configure(text=p2.name)
    label_player2Rank.configure(text=f"#{p2.rank}")

    label_teamName.configure(text=f"{control.getCurrentTeam().name} | #{control.getCurrentTeam().rank}")


def fadeImage(img1, img2, label):
    alpha = 0
    while 1.0 > alpha:
        new_img = Image.blend(img1, img2, alpha)
        alpha = alpha + 0.01
        label.configure(image=new_img)
        label.update()


def buttonRoll():
    buttonSound()
    random.shuffle(silvers)
    random.shuffle(golds)
    random.shuffle(prismatic)
    tiersPath = {"Silver": silvers, "Gold": golds, "Prismatic": prismatic}

    tier1 = mb.getAmps(control.getCurrentTeam().matchBlock)[0]
    tier2 = mb.getAmps(control.getCurrentTeam().matchBlock)[1]
    tier3 = mb.getAmps(control.getCurrentTeam().matchBlock)[2]
    # Cheese way to randomise, since not checking if any tiers are duped
    amp1 = tiersPath[tier1][0]
    amp2 = tiersPath[tier2][1]
    amp3 = tiersPath[tier3][2]
    dupes = nodupe[int(amp1[:-4])] + nodupe[int(amp2[:-4])] + nodupe[int(amp3[:-4])]

    while int(amp1[:-4]) in dupes or int(amp2[:-4]) in dupes or int(amp3[:-4]) in dupes:
        random.shuffle(silvers)
        random.shuffle(golds)
        random.shuffle(prismatic)
        amp1 = tiersPath[tier1][0]
        amp2 = tiersPath[tier2][1]
        amp3 = tiersPath[tier3][2]
        dupes = nodupe[int(amp1[:-4])] + nodupe[int(amp2[:-4])] + nodupe[int(amp3[:-4])]

    amps = [amp1, amp2, amp3]
    saveRoll(amps)

    image = Image.open(f"./data/amplifiers/{tier1}/{amp1}")
    image = image.resize(card_size)
    imageFinal = ImageTk.PhotoImage(image)
    label_image1.configure(image=imageFinal)
    label_image1.image = imageFinal

    image = Image.open(f"./data/amplifiers/{tier2}/{amp2}")
    image = image.resize(card_size)
    imageFinal = ImageTk.PhotoImage(image)
    label_image2.configure(image=imageFinal)
    label_image2.image = imageFinal

    image = Image.open(f"./data/amplifiers/{tier3}/{amp3}")
    image = image.resize(card_size)
    imageFinal = ImageTk.PhotoImage(image)
    label_image3.configure(image=imageFinal)
    label_image3.image = imageFinal

def saveRoll(amps):
    output[control.getCurrentTeam().name] = amps
    saveOutput()


def saveOutput():
    header = ["Team", "Amp #1", "Amp #2", "Amp #3"]
    with open(outputPath, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        # Format and write the row for the current team
        for team in output:
            team_data = [team]
            for amp in output[team]:
                team_data.append(amp[:-4])
            writer.writerow(team_data)
    file.close()

def buttonSound():
    threading.Thread(target=playsound, args=("./data/button_sound.mp3",), daemon=True).start()


background_image_frames = []

def loadAnimatedBg():
    print("Processing animated background")
    print("")
    for x in range(bg_frames):
        text = f"Loading frame {x - 1} of {bg_frames}"
        print("\r", text, end="")
        background_image_frames.append(tkinter.PhotoImage(file=f"./data/bg/stars{x}.png"))
        time.sleep(0.005)
    print("", end="\r")

    print("Animated background loaded")
    time.sleep(0.01)
    threading.Thread(target=updateBg, args=(0,), daemon=True).start()


def updateBg(frame):
    while 1 != 0:
        if frame >= bg_frames:
            frame = 0
        background_image_frame = background_image_frames[frame]
        background_label.configure(image=background_image_frame)
        time.sleep(0.03)
        frame += 1


if bg_frames != 0:
    threading.Thread(target=loadAnimatedBg, args=(), daemon=True).start()
else:
    print("No animated background detected, using static background.")


# Previous
buttonImage = customtkinter.CTkImage(Image.open("./data/button_prev.png"), size=(80, 30))
buttonPrev = customtkinter.CTkButton(master=app, command=buttonPrev, corner_radius=0, text="", fg_color="#243953", hover_color="#243953", image=buttonImage)
buttonPrev.place(width=86, height=34, relx=0.1, rely=0.06, anchor=tkinter.CENTER)

# Next
buttonImage = customtkinter.CTkImage(Image.open("./data/button_next.png"), size=(80, 30))
buttonNext = customtkinter.CTkButton(master=app, command=buttonNext, corner_radius=0, text="", fg_color="#243953", hover_color="#243953", image=buttonImage)
buttonNext.place(width=86, height=34, relx=0.1, rely=0.1475, anchor=tkinter.CENTER)

# Roll
buttonImage = customtkinter.CTkImage(Image.open("./data/button_roll.png"), size=(80, 30))
buttonRoll = customtkinter.CTkButton(master=app, command=buttonRoll, corner_radius=0, text="", fg_color="#243953", hover_color="#243953", image=buttonImage)
buttonRoll.place(width=86, height=34, relx=0.1, rely=0.235, anchor=tkinter.CENTER)


app.mainloop()
