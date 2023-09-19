import random
import tkinter
import customtkinter
import os
import csv
from PIL import Image, ImageTk
from playsound import playsound
import threading
import time

output = "./data/output.csv"
background = "./data/stream_bg.png"
try:
    bg_frames = len([name for name in os.listdir("./data/bg")])
except FileNotFoundError as e:
    bg_frames = 0
amplifierDir = "./data/amplifiers"
playerDir = "./data/players"
amplifierCount = len([name for name in os.listdir(amplifierDir)])
amplifierName = []
playerName = []
playerData = {}

activeDir = "./data/amplifiers/active"
passiveDir = "./data/amplifiers/passive"
activeCount = len([name for name in os.listdir(activeDir)])
passiveCount = len([name for name in os.listdir(passiveDir)])
activeName = []
passiveName = []

for card in os.listdir(activeDir):
    activeName.append(card)

for card in os.listdir(passiveDir):
    passiveName.append(card)

for player in os.listdir(playerDir):
    path = player
    player = player.split(sep="$")
    playerName.append([player[1][:-4], player[0], path])


class Players:

    def __init__(self):
        self.players = "./data/players"
        self.playerCount = len([name for name in os.listdir(self.players)])
        self.current = 1

    def nextPlayer(self):
        clearCards()
        if self.current >= self.playerCount:
            self.current = 1
            return self.current
        self.current += 1
        return self.current

    def prevPlayer(self):
        clearCards()
        if self.current <= 1:
            self.current = self.playerCount
            return self.current
        self.current -= 1
        return self.current

    def getPlayerCount(self):
        print(self.playerCount)

    def getCurrentPlayer(self):
        return self.current


players = Players()


customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("1280x720")
app.title("ANZT Amplifiers")

background_image = tkinter.PhotoImage(file=background)
background_label = tkinter.Label(image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

image1 = Image.open(f"./data/Box.png")
image1 = image1.resize((int(836 / 2.8), int(1077 / 2.8)))
test1 = ImageTk.PhotoImage(image1)
width, height = test1.width(), test1.height()

label_image1 = tkinter.Label(app, bg="#10172d", width=width, height=height, image=test1)
label_image1.place(x=20, y=290)

label_image2 = tkinter.Label(app, bg="#10172d", width=width, height=height, image=test1)
label_image2.place(x=320, y=290)

label_image3 = tkinter.Label(app, bg="#10172d", width=width, height=height, image=test1)
label_image3.place(x=655, y=290)

label_image4 = tkinter.Label(app, bg="#10172d", width=width, height=height, image=test1)
label_image4.place(x=955, y=290)


currentPlayerIcon = Image.open(f"./data/players/{playerName[0][2]}")
currentPlayerIcon = currentPlayerIcon.resize((int(150), int(150)))
currentPlayerIcon = ImageTk.PhotoImage(currentPlayerIcon)
width, height = currentPlayerIcon.width(), currentPlayerIcon.height()

label_playerIcon = tkinter.Label(app, bg="#10172d", width=width, height=height, image=currentPlayerIcon)
label_playerIcon.place(x=220, y=27)

font = ("Crimson Pro", 16)
label_playerName = tkinter.Label(app, bg="#10172d", text=playerName[0][0], fg="white", font=font, anchor=tkinter.CENTER)
label_playerName.place(x=230, y=198)

font_rank = ("Crimson Pro", 42)
label_playerRank = tkinter.Label(app, width=2, height=1, bg="#10172d", text=playerName[0][1], fg="white", font=font_rank, anchor=tkinter.CENTER)
label_playerRank.place(x=398, y=100)


def clearCards():
    box = Image.open(f"./data/Box.png")
    clear = ImageTk.PhotoImage(box)
    label_image1.configure(image=clear)
    label_image1.image = clear
    label_image2.configure(image=clear)
    label_image2.image = clear
    label_image3.configure(image=clear)
    label_image3.image = clear
    label_image4.configure(image=clear)
    label_image4.image = clear



def buttonNext():
    buttonSound()
    cur = players.nextPlayer() - 1
    updateCurrentPlayer(cur)
    print(f"Current Player: {playerName[cur][0]}, #{cur}")


def buttonPrev():
    buttonSound()
    cur = players.prevPlayer() - 1
    updateCurrentPlayer(cur)
    print(f"Current Player: {playerName[cur][0]}, #{cur}")


def updateCurrentPlayer(num):
    newPlayer = playerName[num][0]
    newPlayerIcon = Image.open(f"./data/players/{playerName[num][2]}")
    newPlayerIcon = newPlayerIcon.resize((int(150), int(150)))
    newPlayerIcon = ImageTk.PhotoImage(newPlayerIcon)

    label_playerIcon.configure(image=newPlayerIcon)
    label_playerIcon.image = newPlayerIcon

    label_playerName.configure(text=newPlayer)
    label_playerRank.configure(text=playerName[num][1])


def fadeImage(img1, img2, label):
    alpha = 0
    while 1.0 > alpha:
        new_img = Image.blend(img1, img2, alpha)
        alpha = alpha + 0.01
        label.configure(image=new_img)
        label.update()


def buttonRoll():
    buttonSound()
    activeTotal = list(range(0, activeCount))
    passiveTotal = list(range(0, passiveCount))
    random.shuffle(activeTotal)
    random.shuffle(passiveTotal)
    active1 = activeTotal[0]
    active2 = activeTotal[1]
    passive1 = passiveTotal[0]
    passive2 = passiveTotal[1]

    activeResult = [active1, active2]
    passiveResult = [passive1, passive2]

    saveRoll(activeResult, passiveResult)

    count = 1
    for i in activeResult:
        image = Image.open(f"./data/amplifiers/active/{activeName[i]}")
        image = image.resize((int(836 / 2.8), int(1077 / 2.8)))
        imageFinal = ImageTk.PhotoImage(image)
        if count == 1:
            label_image1.configure(image=imageFinal)
            label_image1.image = imageFinal
        elif count == 2:
            label_image2.configure(image=imageFinal)
            label_image2.image = imageFinal
        count += 1

    count = 1
    for i in passiveResult:
        image = Image.open(f"./data/amplifiers/passive/{passiveName[i]}")
        image = image.resize((int(836 / 2.8), int(1077 / 2.8)))
        imageFinal = ImageTk.PhotoImage(image)
        if count == 1:
            label_image3.configure(image=imageFinal)
            label_image3.image = imageFinal
        elif count == 2:
            label_image4.configure(image=imageFinal)
            label_image4.image = imageFinal
        count += 1


def saveRoll(active, passive):
    text = f"Player {playerName[players.getCurrentPlayer() - 1][0]}, Amplifiers:"
    for x in active:
        text += f" {activeName[x][:-4]}"
    for x in passive:
        text += f" {passiveName[x][:-4]}"
    print(text)
    playerData[players.getCurrentPlayer() - 1] = [playerName[players.getCurrentPlayer() - 1][0], active, passive]
    saveOutput()


def saveOutput():
    header = ["Player Num", "Player Name", "Active #1", "Active #2", "Passive #1", "Passive #2"]
    with open(output, "r+", newline='') as file:
        writer = csv.writer(file)

        writer.writerow(header)

        for item in playerData:
            print(playerData[item])
            playerFormatted = [item, playerData[item][0], activeName[playerData[item][1][0]][:-4], activeName[playerData[item][1][1]][:-4], passiveName[playerData[item][2][0]][:-4], passiveName[playerData[item][2][1]][:-4]]
            writer.writerow(playerFormatted)

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
buttonImage = customtkinter.CTkImage(Image.open("./data/button_prev.png"), size=(106, 40))
buttonPrev = customtkinter.CTkButton(master=app, command=buttonPrev, corner_radius=0, text="", fg_color="#10172d", hover_color="#10172d", image=buttonImage)
buttonPrev.place(width=118, height=44, relx=0.1165, rely=0.07, anchor=tkinter.CENTER)

# Next
buttonImage = customtkinter.CTkImage(Image.open("./data/button_next.png"), size=(106, 40))
buttonNext = customtkinter.CTkButton(master=app, command=buttonNext, corner_radius=0, text="", fg_color="#10172d", hover_color="#10172d", image=buttonImage)
buttonNext.place(width=118, height=44, relx=0.1165, rely=0.185, anchor=tkinter.CENTER)

# Roll
buttonImage = customtkinter.CTkImage(Image.open("./data/button_roll.png"), size=(106, 40))
buttonRoll = customtkinter.CTkButton(master=app, command=buttonRoll, corner_radius=0, text="", fg_color="#10172d", hover_color="#10172d", image=buttonImage)
buttonRoll.place(width=118, height=44, relx=0.1165, rely=0.3, anchor=tkinter.CENTER)


app.mainloop()
