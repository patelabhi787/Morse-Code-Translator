from tkinter import *
import pickle


class window1:
    def __init__(self):
        self.root=Tk()
        self.root.geometry("350x300")
        self.root.title('MORSE CODE TRANSLATOR')
        self.f1=Frame(self.root,height=300,width=300)
        self.f1.propagate(0)
        self.f1.pack()
        self.l1=Label(self.f1,text="What will you like to do ?")
        self.l1.config(font=('Verdana',15,'bold'))
        self.l1.place(x=10,y=10)
        self.b1=Button(self.f1,text="ENGLISH to MORSE CODE",command=self.e_m,font=("Comic Sans MS",10,'bold'))
        self.b1.place(x=65,y=80)
        self.b2=Button(self.f1,text="MORSE CODE to ENGLISH",command=self.m_e,font=("Comic Sans MS",10,'bold'))
        self.b2.place(x=65,y=140)
        self.b3=Button(self.f1,text="EXIT",command=self.exit,font=("Comic Sans MS",10,'bold'))
        self.b3.place(x=135,y=200)
        self.root.mainloop()

    def e_m(self):
        self.root.destroy()
        ob=window2()
        
    def m_e(self):
        self.root.destroy()
        ob=window3()

    def exit(self):
        self.root.destroy()
        

class window2:
    def __init__(self):
        self.root=Tk()
        self.root.geometry("600x500")
        self.root.title('English to Morse Code')
        self.f1=Frame(self.root,height=600,width=500)
        self.f1.propagate(0)
        self.f1.pack()
        self.l1=Label(self.f1,text="Enter the Message",font=("Verdana",12,'bold'))
        self.l1.place(x=10,y=190)


        self.d={'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.',
                   'F':'..-.','G':'--.','H':'....','I':'..','J':'.---',
                   'K':'-.-','L':'.-..','M':'--','N':'-.','O':'---',
                   'P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-',
                   'U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--',
                   'Z':'--..','1':'.----','2':'..---','3':'...--','4':'....-',
                   '5':'.....','6':'-....','7':'--...','8':'---..','9':'----.',
                   '0':'-----'}

        for i in self.d:
            self.l2=Label(self.root,text="A => . -           B => - . . .        C => - . - .       D => - . .          E => .            F => . . - . ",font='Helvetica 10 bold')
            self.l3=Label(self.root,text="G => - - .         H => . . . .        I => . .            J => . - - -        K => - . -        L => . - . . ",font='Helvetica 10 bold')
            self.l4=Label(self.root,text="M => - -          N => - .            O => - - -         P => . - - .        Q => - - . -      R => . - . ",font='Helvetica 10 bold')
            self.l5=Label(self.root,text="S => . . .         T => -              U => . . -         V => . . . -        W => . - -        X => - . . - ",font='Helvetica 10 bold')
            self.l6=Label(self.root,text="Y => - . - -       Z => - - . .        1 => . - - - -     2 => . . - - -      3 => . . . - -    4 => . . . . - ",font='Helvetica 10 bold')
            self.l7=Label(self.root,text="5 => . . . . .     6 => - . . . .      7 => - - . . .     8 => - - - . .      9 => - - - - .    0 => - - - - - ",font='Helvetica 10 bold')
            self.l2.place(x=10,y=10) 
            self.l3.place(x=10,y=35)
            self.l4.place(x=10,y=60)
            self.l5.place(x=10,y=85)
            self.l6.place(x=10,y=110)
            self.l7.place(x=10,y=135)
            
        self.t=Text(self.f1,width=25,height=3,font=('Verdana',16,'bold'),wrap=WORD)
        self.t.place(x=30,y=230)
    
        self.b1=Button(self.f1,text="BACK",command=self.back,font=("Verdana",10,'bold'))
        self.b1.place(x=180,y=430)
        self.b2=Button(self.root,text="CLEAR",command=self.clear,font=("Verdana",10,'bold'))
        self.b2.place(x=340,y=430)
        self.b3=Button(self.root,text="Translate",command=self.encrypt,font=("Verdana",10,'bold'))
        self.b3.place(x=270,y=380)
        self.root.mainloop()

    def back(self):
        self.root.destroy()
        ob=window1()

    def clear(self):
        self.t.delete('1.0',END)
        self.l8["text"]=" "

    def encrypt(self):
        code=' '
        for letter in self.t.get("1.0","end-1c").upper():
            if letter!=' ':
                code=code+self.d[letter]+'/'
            else:
                code=code+'    '
        
        self.l8=Label(self.root,text="Encrypted to:",font=("Verdana",10,'bold'))
        self.l8["text"]="Encrypted to :=>  "+code
        self.l8.place(x=30,y=330)

class window3:
    def __init__(self):
        self.root=Tk()
        self.root.geometry("600x500")
        self.root.title('Morse Code to English')
        self.f1=Frame(self.root,height=600,width=500)
        self.f1.propagate(0)
        self.f1.pack()
        self.l1=Label(self.f1,text="Enter the Morse Code:",font=("Verdana",12,'bold'))
        self.l1.place(x=10,y=190)


        self.d={'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.',
                   'F':'..-.','G':'--.','H':'....','I':'..','J':'.---',
                   'K':'-.-','L':'.-..','M':'--','N':'-.','O':'---',
                   'P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-',
                   'U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--',
                   'Z':'--..','1':'.----','2':'..---','3':'...--','4':'....-',
                   '5':'.....','6':'-....','7':'--...','8':'---..','9':'----.',
                   '0':'-----'}

        for i in self.d:
            self.l2=Label(self.root,text="A => . -           B => - . . .        C => - . - .       D => - . .          E => .            F => . . - . ",font='Helvetica 10 bold')
            self.l3=Label(self.root,text="G => - - .         H => . . . .        I => . .            J => . - - -        K => - . -        L => . - . . ",font='Helvetica 10 bold')
            self.l4=Label(self.root,text="M => - -          N => - .            O => - - -         P => . - - .        Q => - - . -      R => . - . ",font='Helvetica 10 bold')
            self.l5=Label(self.root,text="S => . . .         T => -              U => . . -         V => . . . -        W => . - -        X => - . . - ",font='Helvetica 10 bold')
            self.l6=Label(self.root,text="Y => - . - -       Z => - - . .        1 => . - - - -     2 => . . - - -      3 => . . . - -    4 => . . . . - ",font='Helvetica 10 bold')
            self.l7=Label(self.root,text="5 => . . . . .     6 => - . . . .      7 => - - . . .     8 => - - - . .      9 => - - - - .    0 => - - - - - ",font='Helvetica 10 bold')
            self.l2.place(x=10,y=10) 
            self.l3.place(x=10,y=35)
            self.l4.place(x=10,y=60)
            self.l5.place(x=10,y=85)
            self.l6.place(x=10,y=110)
            self.l7.place(x=10,y=135)
            

        self.t=Text(self.f1,width=25,height=3,font=('Verdana',16,'bold'),wrap=WORD)
        self.t.place(x=20,y=220)
    
        self.b1=Button(self.f1,text="BACK",command=self.back,font=("Verdana",10,'bold'))
        self.b1.place(x=180,y=430)
        self.b2=Button(self.root,text="CLEAR",command=self.clear,font=("Verdana",10,'bold'))
        self.b2.place(x=340,y=430)
        self.b3=Button(self.root,text="Translate",command=self.decrypt,font=("Verdana",10,'bold'))
        self.b3.place(x=270,y=380)


        self.root.mainloop()

    def decrypt(self):
        message=self.t.get("1.0","end-1c")
        message=message+' '
        decipher=''
        citext=''
        for each in message:
            if each==' ':
                decipher+=' '
            elif each!="/":
                i=0
                citext+=each
            else:
                i+=1
                if i==2:
                    decipher+=' '
                else:
                    decipher+=list(self.d.keys())[list(self.d.values()).index(citext)]
                    citext=''
                              
        self.l8=Label(self.root,text="Decrypted to:",font=("Verdana",12,'bold'))
        self.l8["text"]="Decrypted to :=>  "+decipher
        self.l8.place(x=10,y=330)
    
    def back(self):
        self.root.destroy()
        ob=window1()

    def clear(self):
        self.t.delete('1.0',END)
        self.l8["text"]=" "
    
ob=window1()
