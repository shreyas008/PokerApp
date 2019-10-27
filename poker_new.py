from tkinter import *
from PIL import ImageTk, Image
import os

def table(window):
    C = Canvas(window, bg="black", height=500, width=1050 ,bd = 0,borderwidth = 0, highlightthickness=0, relief='ridge')
    C.pack(side = "top")
    #C.create_rectangle(0, 0, 1000, 450, fill= "black")
    C.create_oval(40,40,1000,460,fill= "green",width = 10, outline = "brown")

def table_cards(window):

    #initial 3 cards to display.
    global card_1_image,card_2_image,card_3_image,card_4_image,card_river_image
    card_1_image = Image.open("images/card.jpg")
    card_1_image = card_1_image.resize((70, 80), Image.ANTIALIAS)
    card_1_image = ImageTk.PhotoImage(card_1_image)
    card_1_image_label = Label(window, image = card_1_image, width =60, height = 70) 
    #card_1_image_label.place(x = 450, y = 250)


    # card_2_image = ImageTk.PhotoImage(Image.open("images/card.jpg"))
    card_2_image = Image.open("images/card.jpg")
    card_2_image = card_2_image.resize((70, 80), Image.ANTIALIAS)
    card_2_image = ImageTk.PhotoImage(card_2_image)
    card_2_image_label = Label(window, image = card_2_image, width =60, height = 70) 
    card_2_image_label.place(x = 520, y = 250)

    # card_3_image = ImageTk.PhotoImage(Image.open("images/card.jpg"))
    card_3_image = Image.open("images/card.jpg")
    card_3_image = card_3_image.resize((70, 80), Image.ANTIALIAS)
    card_3_image = ImageTk.PhotoImage(card_3_image)
    card_3_image_label = Label(window, image = card_3_image, width =60, height = 70) 
    card_3_image_label.place(x = 590, y = 250)

#if condition to display according to Poker rules.

    # card_4_image = ImageTk.PhotoImage(Image.open("images/card.jpg"))
    card_4_image = Image.open("images/card.jpg")
    card_4_image = card_4_image.resize((70, 80), Image.ANTIALIAS)
    card_4_image = ImageTk.PhotoImage(card_4_image)
    card_4_image_label = Label(window, image = card_4_image, width =60, height = 70) 
    card_4_image_label.place(x = 660, y = 250)    


    # card_river_image = ImageTk.PhotoImage(Image.open("images/card.jpg"))
    card_river_image = Image.open("images/card.jpg")
    card_river_image = card_river_image.resize((70, 80), Image.ANTIALIAS)
    card_river_image = ImageTk.PhotoImage(card_river_image)
    card_river_image_label = Label(window, image = card_river_image, width =60, height = 70) 
    card_river_image_label.place(x = 730, y = 250)

def players(window):
    #def __init__(self,name,money):
        #self.name = name
        #self.money = money    
    global player1_card_1_image,player1_card_2_image
    global player2_card_1_image,player2_card_2_image
    global player3_card_1_image,player3_card_2_image
    global player4_card_1_image,player4_card_2_image
    global player5_card_1_image,player5_card_2_image

    call = Button(window, text = "Call", highlightbackground = "red", fg = "black", width = 8, activebackground = "black", activeforeground = "red")
    call.pack(side = "bottom")
    fold = Button(window, text = "Fold", highlightbackground = "red", fg = "black", width = 8, activebackground = "black", activeforeground = "red")
    fold.pack(side = "bottom")
    player1_money = Label(window, text = "100", bg="black", fg="red", font = "Arial 20 bold")
    player1_money.pack(side = "bottom")
    player1_name = Label(window, text = "Client Player 1", bg="black", fg="red", font = "Arial 20 bold")
    player1_name.pack(side = "bottom") 


    player1_card_1_image = Image.open("images/card.jpg")
    player1_card_1_image = player1_card_1_image.resize((40, 50), Image.ANTIALIAS)
    player1_card_1_image = ImageTk.PhotoImage(player1_card_1_image)
    player1_card_1_image_label = Label(window, image = player1_card_1_image, width =30, height = 40) 
    player1_card_1_image_label.place(x = 640, y = 550)
    player1_card_2_image = Image.open("images/card.jpg")
    player1_card_2_image = player1_card_2_image.resize((40, 50), Image.ANTIALIAS)
    player1_card_2_image = ImageTk.PhotoImage(player1_card_2_image)
    player1_card_2_image_label = Label(window, image = player1_card_2_image, width =30, height = 40) 
    player1_card_2_image_label.place(x = 600, y = 550)
    
    # call = Button(window, text = "Call", highlightbackground = "red", fg = "black", width = 8, activebackground = "black", activeforeground = "red")
    # call.pack(side = "left")
    # fold = Button(window, text = "Fold", highlightbackground = "red", fg = "black", width = 8, activebackground = "black", activeforeground = "red")
    # fold.pack(side = "left")
    player2_move = Label(window, text = "Move = ", bg="black", fg="red", font = "Arial 20 bold")
    player2_move.place(x = 0, y = 530)
    player2_money = Label(window, text = "100", bg="black", fg="red", font = "Arial 20 bold")
    player2_money.place(x = 0, y = 500)
    player2_name = Label(window, text = "Client Player 2", bg="black", fg="red", font = "Arial 20 bold")
    player2_name.place(x = 0, y = 470)


    player2_card_1_image = Image.open("images/card.jpg")
    player2_card_1_image = player2_card_1_image.resize((40, 50), Image.ANTIALIAS)
    player2_card_1_image = ImageTk.PhotoImage(player2_card_1_image)
    player2_card_1_image_label = Label(window, image = player2_card_1_image, width =30, height = 40) 
    player2_card_1_image_label.place(x = 5, y = 420)
    player2_card_2_image = Image.open("images/card.jpg")
    player2_card_2_image = player2_card_2_image.resize((40, 50), Image.ANTIALIAS)
    player2_card_2_image = ImageTk.PhotoImage(player2_card_2_image)
    player2_card_2_image_label = Label(window, image = player2_card_2_image, width =30, height = 40) 
    player2_card_2_image_label.place(x = 45, y = 420)

    # call = Button(window, text = "Call", highlightbackground = "red", fg = "black", width = 8, activebackground = "black", activeforeground = "red")
    # call.pack(side = "right")
    # fold = Button(window, text = "Fold", highlightbackground = "red", fg = "black", width = 8, activebackground = "black", activeforeground = "red")
    # fold.pack(side = "right")
    player5_move = Label(window, text = "Move = ", bg="black", fg="red", font = "Arial 20 bold")
    player5_move.place(x = 1120, y = 530)
    player5_money = Label(window, text = "100", bg="black", fg="red", font = "Arial 20 bold")
    player5_money.place(x = 1120, y = 500)
    player5_name = Label(window, text = "Client Player 5", bg="black", fg="red", font = "Arial 20 bold")
    player5_name.place(x = 1120, y = 470)


    player5_card_1_image = Image.open("images/card.jpg")
    player5_card_1_image = player5_card_1_image.resize((40, 50), Image.ANTIALIAS)
    player5_card_1_image = ImageTk.PhotoImage(player5_card_1_image)
    player5_card_1_image_label = Label(window, image = player5_card_1_image, width =30, height = 40) 
    player5_card_1_image_label.place(x = 1120, y = 420)
    player5_card_2_image = Image.open("images/card.jpg")
    player5_card_2_image = player5_card_2_image.resize((40, 50), Image.ANTIALIAS)
    player5_card_2_image = ImageTk.PhotoImage(player5_card_2_image)
    player5_card_2_image_label = Label(window, image = player5_card_2_image, width =30, height = 40) 
    player5_card_2_image_label.place(x = 1160, y = 420)

    # call = Button(window, text = "Call", highlightbackground = "red", fg = "black", width = 8, activebackground = "black", activeforeground = "red")
    # call.place(x = 75, y = 160)
    # fold = Button(window, text = "Fold", highlightbackground = "red", fg = "black", width = 8, activebackground = "black", activeforeground = "red")
    # fold.place(x = 0, y = 160)
    player3_move = Label(window, text = "Move = ", bg="black", fg="red", font = "Arial 20 bold")
    player3_move.place(x = 0, y = 150)
    player3_money = Label(window, text = "100", bg="black", fg="red", font = "Arial 20 bold")
    player3_money.place(x = 0, y = 120)
    player3_name = Label(window, text = "Client Player 3", bg="black", fg="red", font = "Arial 20 bold")
    player3_name.place(x = 0, y = 90)


    player3_card_1_image = Image.open("images/card.jpg")
    player3_card_1_image = player3_card_1_image.resize((40, 50), Image.ANTIALIAS)
    player3_card_1_image = ImageTk.PhotoImage(player3_card_1_image)
    player3_card_1_image_label = Label(window, image = player3_card_1_image, width =30, height = 40) 
    player3_card_1_image_label.place(x = 5, y = 40)
    player3_card_2_image = Image.open("images/card.jpg")
    player3_card_2_image = player3_card_2_image.resize((40, 50), Image.ANTIALIAS)
    player3_card_2_image = ImageTk.PhotoImage(player3_card_2_image)
    player3_card_2_image_label = Label(window, image = player3_card_2_image, width =30, height = 40) 
    player3_card_2_image_label.place(x = 45, y = 40)

    # call = Button(window, text = "Call", highlightbackground = "red", fg = "black", width = 8, activebackground = "black", activeforeground = "red")
    # call.place(x = 1120, y = 160)
    # fold = Button(window, text = "Fold", highlightbackground = "red", fg = "black", width = 8, activebackground = "black", activeforeground = "red")
    # fold.place(x = 1195, y = 160)
    player4_move = Label(window, text = "Move = ", bg="black", fg="red", font = "Arial 20 bold")
    player4_move.place(x = 1120, y = 150)
    player4_money = Label(window, text = "100", bg="black", fg="red", font = "Arial 20 bold")
    player4_money.place(x = 1120, y = 120)
    player4_name = Label(window, text = "Client Player 4", bg="black", fg="red", font = "Arial 20 bold")
    player4_name.place(x = 1120, y = 90)
    
   
    player4_card_1_image = Image.open("images/card.jpg")
    player4_card_1_image = player4_card_1_image.resize((40, 50), Image.ANTIALIAS)
    player4_card_1_image = ImageTk.PhotoImage(player4_card_1_image)
    player4_card_1_image_label = Label(window, image = player4_card_1_image, width =30, height = 40) 
    player4_card_1_image_label.place(x = 1120, y = 40)
    player4_card_2_image = Image.open("images/card.jpg")
    player4_card_2_image = player4_card_2_image.resize((40, 50), Image.ANTIALIAS)
    player4_card_2_image = ImageTk.PhotoImage(player4_card_2_image)
    player4_card_2_image_label = Label(window, image = player4_card_2_image, width =30, height = 40) 
    player4_card_2_image_label.place(x = 1160, y = 40)

    #def insert(self,name,money):
        #self.player = Label(window,)
        
def main():
    window = Tk()
    window.title("Poker")
    window.configure(background = "black")
    center_name = Label(window, text = "Player_name's turn", bg="black", fg="white", font = "Helvetica 30 bold")
    center_name.pack(side="top")
    table(window)
    players(window)
    table_cards(window)
    # cards()
    window.mainloop()
main()