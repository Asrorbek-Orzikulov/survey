import tkinter as tk
# import time
# from PIL import ImageTk, Image
import os
import xlsxwriter
import util
import controller
# import glob


def save_data():
    column_names = ["Name", "Lives in Region", "District/City Name", 
                    "District or City", "Gender", "Age"]  
    input_widgets = [entry_1, region, entry_3, place, gender, entry_6]
    input_info = [widget.get() for widget in input_widgets]

    if not os.path.isdir("Database"):
        util.log('warn', 'Seems like a folder for database outputs does not exist. Let me create it for you...')
        os.mkdir("Database")

    try:
        os.chdir("Database")
        count = 0 
        file_exists = True
        while file_exists:
            if os.path.isfile(f"{util.filename(count)}.xlsx"):
                count += 1
            else: 
                name = util.filename(count)
                file_exists = False

        with xlsxwriter.Workbook(f"{name}.xlsx") as workbook:
            worksheet = workbook.add_worksheet()
            worksheet.write_row(0, 0, column_names)
            worksheet.write_row(1, 0, input_info)

        util.log('success', f"An Excel file has been created successfully as {os.getcwd()}/{name}.xlsx")       
        os.chdir("..")
        
        # ## here will be code for unifying files
        # os.chdir("/mydir")
        # for file in glob.glob("*.txt"):
        #     print(file)
        
        
    except Exception as error:
        util.log('error', "Could not create an Excel file")
        util.log('error', str(error))
    finally:
        root.quit()


root= tk.Tk()
root.title("Анкета Опроса Населения")
root.iconbitmap("images/icon.ico")
root.geometry("800x600")  #

vertical = tk.Scale(root, from_=0, to=600, sliderlength=80, showvalue=0)
vertical.pack(side=tk.RIGHT, fill="y")      #

head_frame = tk.LabelFrame(root, borderwidth=0, highlightthickness=0, padx=10, pady=10)
head_frame.pack()

label_head = tk.Label(head_frame, borderwidth=0, highlightthickness=0,
                      text="Ўзбекистон Республикасида  ижтимоий-сиёсий вазиятни ўрганиш (2021 июль)")
label_head.grid(row=0, column=0)
label_head.config(font=("helvetica", 14), fg="dark blue")

# bg_image = ImageTk.PhotoImage(Image.open("survey_background.png"))
# background_label = tk.Label(root, image=bg_image)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)


info_frame = tk.LabelFrame(root, borderwidth=0, highlightthickness=0, padx=10, pady=10)
info_frame.pack() # grid(row=1, column=0, columnspan=10)
label_info = tk.Label(info_frame, text="Сўров иштирокчиларининг ижтимоий-демографик хусусиятлари")
label_info.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
label_info.config(font=("helvetica", 12), fg="green")


label_1 = tk.Label(info_frame, text="1. Исмингиз нима?")  # , justify=tk.LEFT, anchor="w"
label_1.grid(row=1, column=0, padx=10, pady=10)  # , sticky = tk.W
entry_1 = tk.Entry(info_frame, width=50)
entry_1.grid(row=1, column=1, columnspan=3, padx=10, pady=10)

label_2 = tk.Label(info_frame, text="2. Сиз мазкур вилоятда доимий яшайсизми/рўйхатдан ўтганмисиз?")
label_2.grid(row=2, column=0, padx=10, pady=10)
region = tk.IntVar(info_frame)
button_2_1 = tk.Radiobutton(info_frame, text="Ҳа", value=1, variable=region)
button_2_1.grid(row=2, column=1, padx=10, pady=10)
button_2_2 = tk.Radiobutton(info_frame, text="Йўқ", value=2, variable=region)
button_2_2.grid(row=2, column=2, padx=10, pady=10)

label_3 = tk.Label(info_frame, text="3. Сиз вилоятнинг қайси тумани(шаҳри)да яшайсиз?")
label_3.grid(row=3, column=0, padx=10, pady=10)
entry_3 = tk.Entry(info_frame, width=50)
entry_3.grid(row=3, column=1, columnspan=3, padx=10, pady=10)

place = tk.IntVar(info_frame)
place.set("Шаҳар")
label_4 = tk.Label(info_frame, text="4. Шаҳар ёки қишлоқ тугмасини танланг.")
label_4.grid(row=4, column=0, padx=10, pady=10)
button_4_1 = tk.Radiobutton(info_frame, text="Шаҳар", value=1, variable=place)
button_4_1.grid(row=4, column=1, padx=10, pady=10)
button_4_2 = tk.Radiobutton(info_frame, text="Қишлоқ", value=2, variable=place)
button_4_2.grid(row=4, column=2, padx=10, pady=10)
button_4_3 = tk.Radiobutton(info_frame, text="Бош Тортиш", value=3, variable=place)
button_4_3.grid(row=4, column=3, padx=10, pady=10)

gender = tk.IntVar(info_frame)
gender.set("Эркак")
label_5 = tk.Label(info_frame, text="5. Респондентнинг жинсини киритинг.")
label_5.grid(row=5, column=0, padx=10, pady=10)
button_5_1 = tk.Radiobutton(info_frame, text="Эркак", value=1, variable=gender)
button_5_1.grid(row=5, column=1, padx=10, pady=10)
button_5_2 = tk.Radiobutton(info_frame, text="Аёл", value=2, variable=gender)
button_5_2.grid(row=5, column=2, padx=10, pady=10)

label_6 = tk.Label(info_frame, text="6. Респондентнинг ёшини киритинг.")
label_6.grid(row=6, column=0, padx=10, pady=10)
entry_6 = tk.Entry(info_frame)
entry_6.grid(row=6, column=1, columnspan=3, padx=10, pady=10)


welfare_frame = tk.LabelFrame(root, borderwidth=0, highlightthickness=0, padx=10, pady=10)
welfare_frame.pack()
label_7 = tk.Label(welfare_frame, text="7. Мамлакатдаги умумий вазиятдан (ҳолатдан) қониқиш\nдаражангизни 7 баллик шкалада баҳоланг. (1 энг паст баҳо\n– умуман қониқмаслик, 7 энг юқори баҳо – тўлиқ қониқиш).")
label_7.grid(row=0, column=0, padx=10, pady=10)



# Question 26
prezident_frame = tk.LabelFrame(root, borderwidth=0, highlightthickness=0, padx=10, pady=10)
prezident_frame.pack()
question_26 = tk.IntVar(prezident_frame)
question_26.set("Президент")
label_26 = tk.Label(prezident_frame, text="26. Нарзулло Обломуродов, Ўзбекистон Экология партияси етакчиси ")
label_26.grid(row=4, column=0, padx=10, pady=10)
button_26_1 = tk.Radiobutton(prezident_frame, text="1", value=1, variable=question_26)
button_26_1.grid(row=4, column=1, padx=10, pady=10)
button_26_2 = tk.Radiobutton(prezident_frame, text="2", value=2, variable=question_26)
button_26_2.grid(row=4, column=2, padx=10, pady=10)
button_26_3 = tk.Radiobutton(prezident_frame, text="3", value=3, variable=question_26)
button_26_3.grid(row=4, column=3, padx=10, pady=10)
button_26_4 = tk.Radiobutton(prezident_frame, text="4", value=4, variable=question_26)
button_26_4.grid(row=4, column=4, padx=10, pady=10)













major_frame = tk.LabelFrame(root, borderwidth=0, highlightthickness=0, padx=10, pady=10)
major_frame.pack()
label_35 = tk.Label(major_frame, text="35. Айтингчи, Сиз вилоят ҳокими  ___________________га ишонасизми ёки ишонмайсизми?")
label_35.grid(row=0, column=0, padx=10, pady=10, columnspan=5)
button_35_1 = tk.Radiobutton(major_frame, text="Тўлиқ ишонаман", value=1, variable=region)
button_35_1.grid(row=1, column=0, padx=10, pady=10)
button_35_2 = tk.Radiobutton(major_frame, text="Қисман ишонаман", value=2, variable=region)
button_35_2.grid(row=1, column=1, padx=10, pady=10)
button_35_3 = tk.Radiobutton(major_frame, text="Қисман ишонмайман", value=3, variable=region)
button_35_3.grid(row=1, column=2, padx=10, pady=10)









# button at the bottom
bottom_frame = tk.LabelFrame(root, borderwidth=0, highlightthickness=0, padx=10, pady=10)
bottom_frame.pack(side=tk.BOTTOM)
button_exit = tk.Button(bottom_frame, text="Exit Program", command=root.quit)
button_exit.grid(row=0, column=0, padx=80, pady=10)
button_save = tk.Button(bottom_frame, text="Save Responses", command=save_data)  ###############
button_save.grid(row=0, column=1, padx=80, pady=10)


util.main()
controller.main()
root.mainloop()
