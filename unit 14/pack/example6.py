
import tkinter
    
def display(to_convert):
    amount = float(textVar.get())
    ch = choice.get()
    if ch == 1:
        if to_convert == 1:
            message = format(amount,".2f") + " EUR"
        elif to_convert==2:
            message = format(amount * 0.8863,".2f" )+ " GBP"
        elif to_convert == 3:
            message = format(amount * 1.2266,".2f") + " USD"
        
    elif ch == 2:
        if to_convert == 1:
            message = format(amount *1.1284,".2f") + " EUR"
        elif to_convert==2:
            message = format(amount,".2f") + " GBP"
        elif to_convert == 3:
            message = format(amount* 1.3841,".2f")  + " USD"
        
    elif ch == 3:
        if to_convert == 1:
            message = format(amount* 0.8153,".2f")  + " EUR"
        elif to_convert==2:
            message = format(amount* 0.7225,".2f")+ " GBP"
        elif to_convert == 3:
            message = format(amount,".2f") + " USD"
    else:
        message = ""
    messageLabel.configure(text=message)
    print(EuroVar)
top = tkinter.Tk()
top.title("Currency Converter")

fileMenuButton = tkinter.Menubutton(top,text="Choice")
fileMenuButton.grid(row=1,column=2)
fileMenu = tkinter.Menu(fileMenuButton,tearoff=0)
fileMenuButton.configure(menu=fileMenu)

EuroVar = tkinter.IntVar()
GbpVar =tkinter.IntVar()
UsdVar =tkinter.IntVar()

fileMenu.add_command(label="EUR",command=lambda : display(1) )
fileMenu.add_command(label="GBP",command=lambda : display(2))
fileMenu.add_command(label="USD",command=lambda : display(3))

textVar = tkinter.StringVar("")
textEntry = tkinter.Entry(top,textvariable=textVar,width=12)
textEntry.grid(row=0,column=0)
messageLabel = tkinter.Label(top,text="",width=12)
messageLabel.grid(row=1,column=0)

choice = tkinter.IntVar(0)

EurButton = tkinter.Radiobutton(top,text="EUR",
                                  variable=choice,value=1,command=display)
EurButton.grid(row=0,column=1)

GbButton = tkinter.Radiobutton(top,text="GBP",
                                  variable=choice,value=2,command=display)
GbButton.grid(row=0,column=2)

UsdButton = tkinter.Radiobutton(top,text="USD",
                                    variable=choice,value=3,command=display)
UsdButton.grid(row=0,column=3)

quitButton = tkinter.Button(top,text="Quit",command=top.destroy)
quitButton.grid(row=1,column=3)

tkinter.mainloop()
