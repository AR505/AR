import customtkinter as ctk

# إعدادات اللون
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green")


class Main_Windo(ctk.CTk):
    def __init__(self):
        super().__init__()

        # إعدادات النافذة
        self.geometry("1024x720")
        self.title("Modesty Manager")
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # ----- الشريط العلوي -----
        top_frame = ctk.CTkFrame(self, height=60)
        top_frame.grid(row=0, column=0, columnspan=3, sticky="ew", pady=5)
        ctk.CTkButton(top_frame, text="Logout").pack(anchor="e", pady=15, padx=10)

        # ----- الإطار الجانبي -----
        left_frame = ctk.CTkFrame(self, width=300)
        left_frame.grid(row=1, column=0, sticky="ns", rowspan=2, pady=5)

        # ----- الإطار الرئيسي -----
        self.task_frame = ctk.CTkFrame(self)
        self.task_frame.grid(row=1, column=1, sticky="nsew", columnspan=2, padx=10, pady=10)

        # ----- خانة الإدخال -----
        self.entry = ctk.CTkEntry(self, width=500)
        self.entry.grid(row=2, column=1, columnspan=2, padx=20, pady=(5, 30), sticky="nsew")

        # زرار لإضافة مهمة
        add_btn = ctk.CTkButton(self, text="Add Task", command=self.add_task)
        add_btn.grid(row=2, column=2, columnspan=2, padx=20, pady=(5, 30))

    def add_task(self):
        text = self.entry.get().strip()
        if text == "":
            text = "No task entered"

        # إنشاء الإطار الخاص بالمهمة
        task = ctk.CTkFrame(self.task_frame, height=50)
        task.pack(fill="x", padx=10, pady=5)
        task.grid_columnconfigure(1, weight=1)
        task.grid_columnconfigure(2, weight=2)
        task.grid_rowconfigure(1, weight=1)

        # إنشاء الخط العادي والمشطوب
        normal_font = ctk.CTkFont(family="Arial", size=30)
        striked_font = ctk.CTkFont(family="Arial", size=30, overstrike=True)

        # إنشاء التسمية (النص)
        label = ctk.CTkLabel(task, text=text, font=normal_font)
        label.grid(row=1, column=0, sticky="w", padx=10, pady=10)

        # دالة التبديل (تشطب النص عند الضغط)
        def toggle_strike():
            if checkbox.get() == 1:
                label.configure(font=striked_font)
            else:
                label.configure(font=normal_font)

        # إنشاء الـ CheckBox وربطها بالدالة
        checkbox = ctk.CTkCheckBox(task, text="", command=toggle_strike)
        checkbox.grid(row=1, column=2, sticky="e", padx=10)

        # مسح النص من الخانة بعد الإضافة
        self.clear_text()

    def clear_text(self):
        self.entry.delete(0, 'end')


# إنشاء وتشغيل التطبيق
app = Main_Windo()
app.mainloop()
