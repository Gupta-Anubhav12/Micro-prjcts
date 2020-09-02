from tkinter import *
root = Tk()
root.title('Anubhavs Calculator')
Label(root, text = "Enter the input  ").grid(row = 0, sticky = W)
Label(root, text = "enter input type d/b/o/h").grid(row = 1, sticky = W)
Label(root, text = "enter expected output d/b/o/h").grid(row = 2, sticky = W)


inp = Entry(root)
intype = Entry(root)
outype = Entry(root)



inp.grid(row = 0, column = 1)
intype.grid(row = 1, column = 1)
outype.grid(row = 3, column = 1)


def getInput():

    a = inp.get()
    b = intype.get()
    c = outype.get()
    num = a
    frmt= b
    out = c
    if(frmt == 'b'):
    	dec = int(num,2)
    elif(frmt == 'o'):
        dec = int(num,8)
    elif(frmt == 'h'):
        dec = int(num,16)
    else:
        dec = int(num,10)

    # giving output according to user defined version
    if(out == 'b'):
        var = StringVar()
        var.set(bin(dec))

        
        
    elif(out == 'o'):
        var = StringVar()

        var.set(oct(dec))

    elif(out == 'h'):
        var = StringVar()

        var.set(hex(dec))


    elif(out == 'd'):
        var = StringVar()

        var.set(dec)
    Label(root,text='the required value is').grid(row=4, column=1, sticky=W, pady=4)
    Label(root,textvariable=var).grid(row=5, column=1, sticky=W, pady=4).pack()


    
   



Button(root, text = "submit",
           command = getInput).grid(row = 5, sticky = W)






          

   


mainloop()