from tkinter import as Tk
from mydb import Database
from tkinter import messagebox

class NLPApp:
    
    
    def __init__(self):
        
        self.dbo = Database()

        self.root = Tk()
        self.root.title("NLP app")
        self.root.iconbitmap("resources/favicon.ico")
        self.root.configure(bg='#34495E')
        self.root.geometry('350x550')
        
        self.login_gui()
        self.root.mainloop()
        
        
    def login_gui(self):
        
        self.clear()
        
        heading = Label(self.root,text='NLPApp',bg='#34495E',fg='white')    
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold','italic'))
        
        label1 = Label(self.root,text='enter email')
        label1.pack(pady=(10,10))
        
        self.email_input = Entry(self.root,width=50)
        self.email_input.pack(pady=(5,10),ipady=5)
        
        label2 = Label(self.root,text='enter password')
        label2.pack(pady=(10,10))
        
        self.passwrod_input = Entry(self.root,width=50,show='*')
        self.passwrod_input.pack(pady=(5,10),ipady=5)
        
        login_btn = Button(self.root,text='login',width=30,height=2)
        login_btn.pack(pady=(10,10))
        
        label3 = Label(self.root,text='Not a Memeber?',bg='#34495E')
        label3.pack(pady=(20,10))
        
        redirect_btn = Button(self.root,text='Register now',command=self.register_gui)
        redirect_btn.pack(pady=(10,10))
        
    def register_gui(self):
        self.clear()
        
        
        heading = Label(self.root,text='NLPApp',bg='#34495E',fg='white')    
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold','italic'))
        
        label0 = Label(self.root,text='enter name')
        label0.pack(pady=(10,10))
        
        self.name_input = Entry(self.root,width=50)
        self.name_input.pack(pady=(5,10),ipady=5)
        
        label1 = Label(self.root,text='enter email')
        label1.pack(pady=(10,10))
        
        self.email_input = Entry(self.root,width=50)
        self.email_input.pack(pady=(5,10),ipady=5)
        
        label2 = Label(self.root,text='enter password')
        label2.pack(pady=(10,10))
        
        self.passwrod_input = Entry(self.root,width=50,show='*')
        self.passwrod_input.pack(pady=(5,10),ipady=5)
        
        register_btn = Button(self.root,text='Register',width=30,height=2,command=self.perform_registration)
        register_btn.pack(pady=(10,10))
        
        label3 = Label(self.root,text='Already Memeber?',bg='#34495E')
        label3.pack(pady=(20,10))
        
        redirect_btn = Button(self.root,text='Login now',command=self.login_gui)
        redirect_btn.pack(pady=(10,10))
    
    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()
            
    def perform_registration(self): 
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.passwrod_input.get()
        
        response = self.dbo.add_data(name,email,password)
        
        if response:
            messagebox.showinfo('success','you can login now')
            
        else:
            messagebox.showerror('error','please select another username password')     

nlp = NLPApp()
        
        