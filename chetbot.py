from tkinter import*
import tkinter as ttk
import random

class chatbot:
    def __init__(self,root):
        self.root = root
        self.root.geometry('700x600+250+30')
        self.root.title('ChatBot')
        self.root.bind('<Return>',self.ent_func)
        #===========title================
        lbl_title = Label(self.root,bg='green',text='Chatbot:Developed by Noor Saeed',font=('arial',25,'bold'))
        lbl_title.place(x=50,y=10)

        #========Main Frame with Text=========
        main_frame = Frame(self.root,relief=RAISED,bg='white')
        main_frame.place(x=0,y=60,width=700,heigh=400)

        # ===========Text area with scrollbar===
        self.scroll_y = ttk.Scrollbar(main_frame, orient=VERTICAL)
        self.text = Text(main_frame, width=65, height=20, font=('arial', 14), relief=RAISED, yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.text.pack()

        #====Search lable
        lbl_search = Label(self.root,text='Search Here',font=('arial',15,'bold'))
        lbl_search.place(x=30,y=480)

        #=====entry
        self.ent=StringVar()
        self.entry = ttk.Entry(self.root,textvariable=self.ent,bd=2,font=('times new roman',16,'bold'))
        self.entry.place(x=200,y=480,width=400,height=30)

        # =====btn save
        self.btn_send = ttk.Button(self.root,command=self.send, width=20, text='Send',font=('times new roman',14,'bold'),bg='black',fg='white')
        self.btn_send.place(x=200, y=520, width=200, height=30)
        # =====btn clr
        self.btn_clr = ttk.Button(self.root,command=self.clear, width=20, text='Clear',font=('times new roman', 14, 'bold'), bg='black', fg='white')
        self.btn_clr.place(x=410, y=520, width=200, height=30)

        # # ====lable message
        self.msg = StringVar()
        self.lbl_msg = Label(self.root,textvariable=self.msg)
        self.lbl_msg.place(x=100, y=580)

 # ======================================functions=============

    def ent_func(self,event):
        self.btn_send.invoke()
        self.ent.set("")

    def clear(self):
        self.text.delete('1.0',END)
        self.ent.set("")

    def send(self):
        user_input = "\t\t\t"+"You: "+self.entry.get()
        self.text.insert(END,"\n"+user_input)

        if(self.entry.get()==""):
            self.msg="Please Type somthing"
            self.lbl_msg.config(text=self.msg,fg='black')
            print(self.lbl_msg)
        else:
            self.msg = ""
            self.lbl_msg.config(text=self.msg,fg='black')


        input_list = ['hi','hey','helo','how are you','whats up']
        output_list = ['hi','I am good','nice to see you','helo']
        for mess in input_list:
            if self.entry.get() == mess:
                put_into_text = random.choice(output_list)
                self.text.insert(END,'\n\n'+"Bot :"+put_into_text)

        data_sience="data science is a growing field now a days. It has many \n"\
        "application in daily life. it has the following brachs \n1: machine learning\n2: deep learning \n3: LNP"
        if self.entry.get()=="what is data science" or self.entry.get()=="about data science":
            self.text.insert(END,'\n\n'+data_sience)
        google = "Google is a big tech company throghout the world.\nchrome is the leading app of google."
        if self.entry.get()=="google" or self.entry.get()=="about google":
            self.text.insert(END,'\n\n'+google)

        if self.entry.get()=="richest person of the world" or self.entry.get()=="richest person":
            self.text.insert(END,'\n\n'+"Elon must with $10,000 Bilion")
        # else:
        #     self.text.insert(END,'\n\n'+'Sorry! I didnt get you')

# ////////////////////////////////////////////////
if __name__ == '__main__':
    root = Tk()
    obj = chatbot(root)
    root.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
