from tkinter import *
from  find_sol import *
from datetime import date


mainwindow = Tk()
mainwindow.title("Suzzle Polver")
mainwindow.geometry("2000x1000")

leftFrame = Frame(mainwindow)
leftFrame.pack(side = LEFT,padx = 50)
rightFrame = Frame(mainwindow)
rightFrame.pack(side = LEFT)






for i in range(25):
    
    print(solutions[i][0])
    if solutions[i][0] == '':
        l1 = Label(leftFrame,bd = 1,font="Times 22",height = 5,width =10,background="black",justify=LEFT)
    else: 
        try:
            int(solutions[i][0])
            
            sol = solutions[i][0] +"\n\n         " + solutions[i][1] 
            l1 = Label(leftFrame,bd = 1,font="Times 22",text=sol,relief="solid",height = 5,width =10,background="white",justify=LEFT,anchor=NW) 
            
        except:
            sol = "\n\n         " + solutions[i][0]
            l1 = Label(leftFrame,text=sol,bd = 1,font="Times 22",relief="solid",height = 5,width =10,background="white",justify=LEFT,anchor=NW) 
    l1.grid(row=1+int(i/5),column=1+int(i%5))

clues_accross_txt = 'Accross \n'
for i in range(len(clues_across)-1):
    if not clues_across[i][0].isalpha():
        clues_accross_txt += clues_across[i] + " - " +clues_across[i+1] + "\n"
    

clues_down_txt = 'Down \n'
for i in range(len(clues_down)-1):
    if not clues_down[i][0].isalpha():
        clues_down_txt += clues_down[i] + " - " +clues_down[i+1] + "\n"
    

lab_across = Label(rightFrame,text=clues_accross_txt,justify=LEFT,font ="Times 16")
lab_across.grid(row = 1, column = 1)  

lab_down = Label(rightFrame,text=clues_down_txt,justify=LEFT,font="Times 16")
lab_down.grid(row = 1, column = 2)

today = date.today()
today = today.strftime("%d %B, %Y")
today += " Suzzle Polver"
dayLabel = Label(mainwindow,text = today, bd = 1,font="Times 25",height = 2,width =40,background="white")
dayLabel.place(x=300,y=850,in_=mainwindow)
mainwindow.mainloop()

