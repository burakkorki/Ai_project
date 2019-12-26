from tkinter import *
from find_sol import *
from datetime import date
import textwrap

mainwindow = Tk()
mainwindow.title("Suzzle Polver")
mainwindow.geometry("2000x1000")


leftFrame = Frame(mainwindow)
leftFrame.pack(side = LEFT,padx = 50)
rightFrame = Frame(mainwindow)
rightFrame.pack(side = LEFT)



for i in range(25):
    
    #print(solutions[i][0])
    if solutions[i][0] == '':
        l1 = Label(leftFrame,bd=1,font="Times 30",height = 3,width =7,background="black",justify=LEFT)
    else: 
        try:
            int(solutions[i][0])
            
            sol = " " +solutions[i][0] +"\n      " + solutions[i][1] 
            l1 = Label(leftFrame,bd=1,font="Times 30",text=sol,relief="solid",height = 3,width =7,background="white",justify=LEFT,anchor=NW) 
            
        except:
            sol = "\n      " + solutions[i][0]
            l1 = Label(leftFrame,bd=1,text=sol,font="Times 30",relief="solid",height = 3,width =7,background="white",justify=LEFT,anchor=NW) 
    l1.grid(row=1+int(i/5),column=1+int(i%5))


clues_accross_txt = ""
for i in range(0, len(clues_across), 2):
    clues_accross_txt += clues_across[i] + " - " + textwrap.fill(clues_across[i+1],60) + "\n\n"
    

clues_down_txt = ""
for i in range(0, len(clues_down), 2):
    clues_down_txt += clues_down[i] + " - " + textwrap.fill(clues_down[i+1],60) + "\n\n"

new_clues_accross_txt = ""
for i in range(0, len(new_clues_accross), 2):
    new_clues_accross_txt += new_clues_accross[i] + " - " + textwrap.fill(new_clues_accross[i+1],60) + "\n\n"
    

new_clues_down_txt = ""
for i in range(0, len(clues_down), 2):
    new_clues_down_txt += new_clues_down[i] + " - " + textwrap.fill(new_clues_down[i+1],60) + "\n\n"
    
lab_across = Label(rightFrame,text="Accross",justify=LEFT,font ="Times 30 bold",anchor=N)
lab_across.grid(row = 0, column = 1,sticky=NW)  

lab_across = Label(rightFrame,text=clues_accross_txt,justify=LEFT,font ="Times 16",anchor=N)
lab_across.grid(row = 1, column = 1,sticky=NW)  

lab_down = Label(rightFrame,text="Down",justify=LEFT,font="Times 30 bold",anchor=N)
lab_down.grid(row = 0, column = 2,sticky=NW)

lab_down = Label(rightFrame,text=clues_down_txt,justify=LEFT,font="Times 16",anchor=N)
lab_down.grid(row = 1, column = 2,sticky=NW)

new_lab_across = Label(rightFrame,text="New Accross",justify=LEFT,font ="Times 30 bold",anchor=N)
new_lab_across.grid(row = 2, column = 1,sticky=NW) 

new_lab_down = Label(rightFrame,text=new_clues_accross_txt,justify=LEFT,font="Times 16",anchor=N)
new_lab_down.grid(row = 3, column = 1,sticky=NW)

new_lab_across = Label(rightFrame,text="New Down",justify=LEFT,font ="Times 30 bold",anchor=N)
new_lab_across.grid(row = 2, column = 2,sticky=NW)  

new_lab_down = Label(rightFrame,text=new_clues_down_txt,justify=LEFT,font="Times 16",anchor=N)
new_lab_down.grid(row = 3, column = 2,sticky=NW)

#today = date.today()
#today = today.strftime("%d %B, %Y")
today += " Suzzle Polver"
dayLabel = Label(mainwindow,text = today, bd = 1,font="Times 22",height = 2,width =40,background="white")
dayLabel.place(x=150,y=750,in_=mainwindow)
mainwindow.mainloop()

