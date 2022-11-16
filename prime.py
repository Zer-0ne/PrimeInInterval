from cgitb import text
from functools import cache
from tkinter import *
from tkinter import messagebox
@cache
class prime:
    def __init__(self):
        self.window = Tk()
        self.window.title('Prime number')
        self.window.configure(bg='black')
        self.window.resizable(False,False)
        self.frame1 = Frame(self.window,bg='black')
        self.frame1.grid(row=0,column=0,columnspan=5)
        self.label = Label(self.frame1,text='PRIME NUMBER!!',fg='red',bg='black',font='helvetica 36',padx=50).pack(pady=(20,30))
        self.frame2 = Frame(self.window,bg='black',pady=100).grid(row=1,column=0,columnspan=5)
        self.label = Label(text='Enter The Lower Value :: ',padx=10,fg='red',bg='black',font='helvetica 16').grid(row=2,column=0,columnspan=2)
        self.lowest_limit = StringVar()
        self.lowest_value = Entry(self.frame2,textvariable=self.lowest_limit,bd=5,bg='black',fg='green',highlightcolor='red',insertbackground='red',relief='sunken',border=0)
        self.lowest_value.grid(row=2,column=2,columnspan=5)
        self.label = Label(text='Enter The Upper Value :: ',padx=10,fg='red',bg='black',font='helvetica 16').grid(row=4,column=0,columnspan=2)
        self.upper_limit = StringVar()
        self.upper_value = Entry(self.frame2,textvariable=self.upper_limit,bd=5,bg='black',fg='green',highlightcolor='red',insertbackground='red',relief='sunken',border=0)
        self.upper_value.grid(row=4,column=2,columnspan=5)
        self.button = Button(self.frame2,text='Enter',fg='red',bg='black',font='helvetica 16',command=lambda :self.check_number()).grid(row=6,column=0,columnspan=5,pady=30)
        self.answer = StringVar()
        self.ans = Label(self.frame2,textvariable=self.answer,padx=10,fg='red',bg='black',font='helvetica 16',wraplength='400p').grid(row=10,column=0,columnspan=5)
        self.nav_bar()
        self.window.mainloop()
    def check_number(self):
        self.list =[]
        try:
            if not (self.upper_limit.get()) and not (self.lowest_limit.get()):
                messagebox.showerror('Prime Number','Please fill the lowest and upper limit')
            if not (self.lowest_limit.get)() and (self.upper_limit.get()):
                messagebox.showerror('Prime Number','Please fill lowest limit number!!!')
            if not (self.upper_limit.get()) and (self.lowest_limit.get()):
                messagebox.showerror('Prime Number','Please fill upper limit number')
            self.upper = int(self.upper_limit.get())
            self.lower = int(self.lowest_limit.get())
            if int(self.lowest_limit.get())>=int(self.upper_limit.get()):
                messagebox.showerror('Prime Number','lowest value is greater than upper value!!')
        except:
            if not self.upper_limit.get() or not self.lowest_limit.get():
                pass
            else:
                if self.upper_limit.get() or self.lowest_limit.get():
                    messagebox.showerror('Prime Number','Only Integer allowed!!')
        for Number in range(self.lower, self.upper+1):
            if(self.isPrime(Number)):
                # self.Lab = Label(self.frame2,textvariable=,padx=10,fg='red',bg='black',font='helvetica 16',wraplength='400p',anchor='w',justify='left').grid(row=8,column=0,columnspan=5)
                self.list.append(Number)
                self.answer.set(f'The Prime number between {self.lower} to {self.upper}\n{str(self.list)}')
    def nav_bar(self):
        self.font = 'helvetica 16'
        self.frame1 = Frame(self.window).grid(sticky='n')
        self.menubar = Menu(self.frame1,background='black',
                            foreground='red',activebackground='red',
                            activeforeground='black',font=self.font)
        self.file = Menu(self.menubar,tearoff=0,background='black',foreground='red',activebackground='red',
                            activeforeground='black')
        self.file.add_command(label='Reset',font=self.font,command=lambda:self.reset())
        self.file.add_separator()
        self.file.add_command(label='Exit',font=self.font,command=lambda:self.exit_pro())
        self.menubar.add_cascade(label='File',menu=self.file)
        self.help = Menu(self.menubar,tearoff=0,background='black',foreground='red',activebackground='red',activeforeground='black')
        self.help.add_command(label='Help',font=self.font,command=lambda:self.help_())
        self.help.add_command(label='About',font=self.font,command=lambda:self.about())
        self.menubar.add_cascade(label='About',menu=self.help)
        self.window.config(menu=self.menubar)
    def about(self):
        messagebox.showinfo('Prime Number','Created By Sahil khan')
    def exit_pro(self):
        exit()
    def reset(self):
        self.upper_value.delete(0,'end')
        self.lowest_value.delete(0,'end')
        self.answer.set('')
    def help_(self):
        messagebox.showinfo('Prime Number','Fill the lowest value and enter the highest value and press enter\nThen all prime number in between lowest value to highest value will printed')
    @cache
    def isPrime(self,n):
        if(n==1 or n==0):
            return False
        for i in range(2,n):
            if(n%i==0):
                return False
        return True

if __name__ == '__main__':
    prime()