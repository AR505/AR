import customtkinter as ctk

#colourmode default
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green")


#main windo 
class Main_Windo(ctk.CTk):
    def __init__(self):
        super().__init__()
        #--------------------------------------wind
        self.geometry(f"{1024}x{720}")
        self.title("Modesty Manager")
        self.grid_columnconfigure(1, weight=1)
        # self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        # self.grid_rowconfigure(1, weight=1)
        #--------------top
        top_fram = ctk.CTkFrame(self,height=60)
        ctk.CTkButton(top_fram,text="logout").grid(pady=10)
        top_fram.grid(row=0,column=0,sticky="ew",pady=5,columnspan=2)
        #------------------------------------------------------------left farm
        left_farm = ctk.CTkFrame(self,width=300)
        left_farm.grid(row=1,column=0,sticky="ns",rowspan=2,pady=5)
        #-----------------------------------------------------------intry users
        intry= ctk.CTkEntry(self,width=500)
        intry.grid(row=2,column=1,padx=(40, 40), pady=(5, 30),sticky="nsew")
        #-------------------------------------------------------------------------


        self.mainloop()

Main_Windo()