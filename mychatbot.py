from tkinter import*
import tkinter as ttk
import random

class chatbot:
    def __init__(self,root):
        self.root = root
        self.root.geometry('700x600+250+10')
        self.root.title('My ChatGPT')
        self.root.bind('<Return>',self.ent_funt)

        #========Title==============
        lbl_title = Label(self.root,text='ChatGPT Developed By Noor Saeed',font=('times new roman',20,'bold'))
        lbl_title.place(x=130,y=10)

        #=======main Frame with scroll bar and text area===============
        main_frame = Frame(self.root,bd=2,relief=RAISED,bg='green')
        main_frame.place(x=0,y=60,width=700,height=400)

        # ===========Text area with scrollbar===
        self.scroll_y = ttk.Scrollbar(main_frame, orient=VERTICAL)
        self.text = Text(main_frame, width=65, height=20, font=('arial', 14), relief=RAISED,yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.text.pack()


        #============searc lable===========
        lbl_search = Label(self.root,text='Search Here',font=('times new roman',20,'bold'))
        lbl_search.place(x=20,y=470)

        #============Entery area========
        self.ent = StringVar()
        self.entry=ttk.Entry(self.root,textvariable=self.ent, font=('times new roman',15,'bold'))
        self.entry.place(x=200,y=470,width=400,height=35)

        # =====btn save
        self.btn_send = ttk.Button(self.root,command=self.send,  width=20, text='Send',font=('times new roman', 14, 'bold'), bg='black', fg='white')
        self.btn_send.place(x=200, y=520, width=200, height=30)
        # =====btn clr
        self.btn_clr = ttk.Button(self.root,command=self.clear, width=20, text='Clear',font=('times new roman', 14, 'bold'), bg='black', fg='white')
        self.btn_clr.place(x=410, y=520, width=200, height=30)



# ==================Functions starts================
    def ent_funt(self,noor):
        self.btn_send.invoke()
        self.ent.set("")

    def clear(self):
        self.text.delete("1.0",END)
        self.ent.set("")

    def send(self):
        user_input = "\t\t\t"+"You :"+self.entry.get()
        self.text.insert(END,"\n\n"+user_input)

        input_list = ['hi','hey','helo','how are you','whats up']
        output_list = ['helo','good to see you','nice to see you','hi','good to meet you']

        for mess in input_list:
            if self.entry.get() == mess:
                mess_into_text = random.choice(output_list)
                self.text.insert(END,'\n\n'+'Bot :' + mess_into_text)

        richest_person = "Top 3 Richest person in the world are, \n 1 Elon musk \n3 Bil gates \n3 Noor Saeed"
        if self.entry.get() == "richest person" or self.entry.get() == "top richest person":
            self.text.insert(END,'\n\n'+"Bot : " + richest_person)

        data_sience = "data science is a growing field now a days. It has many \n" \
                      "application in daily life. it has the following brachs \n1: machine learning\n2: deep learning \n3: LNP"
        if self.entry.get() == "what is data science" or self.entry.get() == "about data science":
            self.text.insert(END, '\n\n' + data_sience)

        google = "Google is a big tech company throghout the world.\nchrome is the leading app of google."
        if self.entry.get() == "google" or self.entry.get() == "about google":
            self.text.insert(END, '\n\n' + google)

        google = "Google is a big tech company throghout the world.\nchrome is the leading app of google."
        if self.entry.get() == "google" or self.entry.get() == "about google":
            self.text.insert(END, '\n\n' + google)





# ====================================
if __name__ == "__main__":
    root = Tk()
    obj = chatbot(root)
    root.mainloop()