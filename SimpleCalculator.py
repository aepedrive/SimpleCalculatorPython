""" My first calculator
    by Armando Pedraza
    04/17/2014
"""

from Tkinter import *


def dis(symbol):    
    if str.isdigit(symbol) or symbol =='.':
        dis.op += symbol
        txt.configure(text=dis.op)
    elif symbol == '/' or symbol == '*' or symbol == '-' or symbol == '+':
        txt.configure(text='')
        

root = Tk()

root.title("Mini Calc")
#root.geometry('150x280')

txt = Label(root, bg='cyan', text='0', anchor=E)
txt.grid(row=0, column=0, columnspan=4, sticky=EW)

calc_buttons = ['7','8','9','/',
                '4','5','6','*',
                '1','2','3','-',
                '0','.','=','+']
dis.op = '' #Initialize dis.op static variable, otherwise it fails

for i, v in enumerate(calc_buttons):
    Button(root, text='%s'%v, width=2, height=2,command= lambda v=v:dis(v)).grid(
        row=1 if i/4==0 else (2 if i/4==1 else (3 if i/4==2 else 4)),
        column=i%4)


root.mainloop()

