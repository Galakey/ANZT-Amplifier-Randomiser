import random
import tkinter
import customtkinter
import os
import csv
from PIL import Image, ImageTk

output = "./data/output.csv"
background = "./data/stream_bg.png"
amplifierDir = "./data/amplifiers"
playerDir = "./data/players"
amplifierCount = len([name for name in os.listdir(amplifierDir)])
amplifierName = []
playerName = []
playerData = {}

for card in os.listdir(amplifierDir):
    amplifierName.append(card)

for player in os.listdir(playerDir):
    playerName.append(player)


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

background_image = tkinter.PhotoImage(file=background)
background_label = tkinter.Label(image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

image1 = Image.open(f"./data/Box.png")
image1 = image1.resize((int(836 / 2.8), int(1077 / 2.8)))
test1 = ImageTk.PhotoImage(image1)
width, height = test1.width(), test1.height()

label_image1 = tkinter.Label(app, bg="#10172d", width=width, height=height, image=test1)
label_image1.place(x=120, y=290)

label_image2 = tkinter.Label(app, bg="#10172d", width=width, height=height, image=test1)
label_image2.place(x=490, y=290)

label_image3 = tkinter.Label(app, bg="#10172d", width=width, height=height, image=test1)
label_image3.place(x=860, y=290)


currentPlayerIcon = Image.open(f"./data/players/{playerName[0]}")
currentPlayerIcon = currentPlayerIcon.resize((int(150), int(150)))
currentPlayerIcon = ImageTk.PhotoImage(currentPlayerIcon)
width, height = currentPlayerIcon.width(), currentPlayerIcon.height()
label_playerIcon = tkinter.Label(app, bg="#10172d", width=width, height=height, image=currentPlayerIcon)
label_playerIcon.place(x=250, y=35)

font = ("Crimson Pro", 24)

label_playerName = tkinter.Label(app, bg="#10172d", text=playerName[0][:-4], fg="white", font=font, anchor=tkinter.CENTER)
label_playerName.place(x=255, y=190)


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
    cur = players.nextPlayer()
    updateCurrentPlayer(cur)
    print(cur)


def buttonPrev():
    cur = players.prevPlayer()
    updateCurrentPlayer(cur)
    print(cur)


def updateCurrentPlayer(num):
    newPlayer = playerName[num-1][:-4]
    newPlayerIcon = Image.open(f"./data/players/{playerName[num-1]}")
    newPlayerIcon = newPlayerIcon.resize((int(150), int(150)))
    newPlayerIcon = ImageTk.PhotoImage(newPlayerIcon)

    label_playerIcon.configure(image=newPlayerIcon)
    label_playerIcon.image = newPlayerIcon

    label_playerName.configure(text=newPlayer)


def buttonRoll():
    total = list(range(1, amplifierCount))
    random.shuffle(total)
    amplifier1 = total[0]
    amplifier2 = total[1]
    amplifier3 = total[2]
    result = [amplifier1, amplifier2, amplifier3]

    saveRoll(result)
    count = 1
    for i in result:
        image = Image.open(f"./data/amplifiers/{amplifierName[i]}")
        image = image.resize((int(836 / 2.8), int(1077 / 2.8)))
        imageFinal = ImageTk.PhotoImage(image)
        if count == 1:
            label_image1.configure(image=imageFinal)
            label_image1.image = imageFinal
        elif count == 2:
            label_image2.configure(image=imageFinal)
            label_image2.image = imageFinal
        elif count == 3:
            label_image3.configure(image=imageFinal)
            label_image3.image = imageFinal
        count += 1


def saveRoll(amplifiers):
    for x in amplifiers:
        print(x)
        x = amplifierName[x][:-4]
    playerData[players.getCurrentPlayer()] = [playerName[players.getCurrentPlayer() - 1], amplifiers]
    saveOutput()


def saveOutput():
    header = ["Player Num", "Player Name", "Amplifier #1" , "Amplifier #2", "Amplifier #3"]
    with open(output, "r+", newline='') as file:
        writer = csv.writer(file)

        writer.writerow(header)

        for item in playerData:
            playerFormatted = [item, playerData[item][0][:-4], playerData[item][1][0], playerData[item][1][1], playerData[item][1][2]]
            writer.writerow(playerFormatted)


# Previous
button = customtkinter.CTkButton(master=app, text="Prev", command=buttonPrev)
button.place(width=90, relx=0.12, rely=0.08, anchor=tkinter.CENTER)

# Next
button = customtkinter.CTkButton(master=app, text="Next", command=buttonNext)
button.place(width=90, relx=0.12, rely=0.18, anchor=tkinter.CENTER)

# Roll
button = customtkinter.CTkButton(master=app, text="Roll", command=buttonRoll)
button.place(width=90, relx=0.12, rely=0.28, anchor=tkinter.CENTER)


app.mainloop()
