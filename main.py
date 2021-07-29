import tkinter as tk
# import time
# from PIL import ImageTk, Image
import os
import xlsxwriter
import util
import controller
from tkinter import ttk
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


def mcq_question(frame_name, label_row, options, text, num_options):
    label = tk.Label(frame_name, text=text)
    label.grid(row=label_row, column=0, padx=10, pady=10, columnspan=num_options)
    variable = tk.IntVar(frame_name)
    for idx, option in enumerate(options):
        button = tk.Radiobutton(frame_name, text=option, value=idx+1, variable=variable)
        button.grid(row=label_row + 1, column=idx, padx=10, pady=10)

    return variable


root= tk.Tk()
root.title("Анкета Опроса Населения")
root.iconbitmap("images/icon.ico")
<<<<<<< Updated upstream
root.geometry("1200x900")  #

scroll = tk.Scrollbar(root)

# vertical = tk.Scale(root, from_=0, to=600, sliderlength=80, showvalue=0)
# vertical.pack(side=tk.RIGHT, fill="y")

head_frame = tk.LabelFrame(root, borderwidth=0, highlightthickness=0, padx=10, pady=10)
=======
root.geometry("1200x700") ###########

# adding a scrollbar
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=1)
canvas = tk.Canvas(main_frame)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind("<Configure>", 
            lambda event: canvas.configure(scrollregion=canvas.bbox("all")))

canvas.bind_all("<MouseWheel>",
                lambda event: canvas.yview_scroll(-1 * int((event.delta / 120)), "units"))

inside_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=inside_frame, anchor="nw")

# Start of questionnaire
head_frame = tk.LabelFrame(inside_frame, borderwidth=0, highlightthickness=0, padx=10, pady=10)
>>>>>>> Stashed changes
head_frame.pack()

label_head = tk.Label(head_frame, borderwidth=0, highlightthickness=0,
                      text="Ўзбекистон Республикасида  ижтимоий-сиёсий вазиятни ўрганиш (2021 июль)")
label_head.grid(row=0, column=0)
label_head.config(font=("helvetica", 14), fg="dark blue")

# bg_image = ImageTk.PhotoImage(Image.open("survey_background.png"))
# background_label = tk.Label(root, image=bg_image)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)


info_frame = tk.LabelFrame(inside_frame, borderwidth=0, highlightthickness=0, padx=10, pady=10)
info_frame.pack() # grid(row=1, column=0, columnspan=10)
label_info = tk.Label(info_frame, text="Сўров иштирокчиларининг ижтимоий-демографик хусусиятлари")
label_info.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
label_info.config(font=("helvetica", 12), fg="green")

# Question 1
label_1 = tk.Label(info_frame, text="1. Исмингиз нима?")  # , justify=tk.LEFT, anchor="w"
label_1.grid(row=1, column=0, padx=10, pady=10, columnspan=3)  # , sticky = tk.W
entry_1 = tk.Entry(info_frame, width=50)
entry_1.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Question 2
label_2_row = 3
text_2 = "2. Сиз вилоятда доимий яшайсизми ва рўйхатдан ўтганмисиз?"
options_2 = ["Ҳа", "Йўқ"]
region = mcq_question(info_frame, label_2_row, options_2, 
                    text=text_2, num_options=2)


# region = tk.IntVar(info_frame)
# button_2_1 = tk.Radiobutton(info_frame, text="Ҳа", value=1, variable=region)
# button_2_1.grid(row=2, column=1, padx=10, pady=10)
# button_2_2 = tk.Radiobutton(info_frame, text="Йўқ", value=2, variable=region)
# button_2_2.grid(row=2, column=2, padx=10, pady=10)

# label_3 = tk.Label(info_frame, text="3. Сиз вилоятнинг қайси тумани(шаҳри)да яшайсиз?")
# label_3.grid(row=3, column=0, padx=10, pady=10)
# entry_3 = tk.Entry(info_frame, width=50)
# entry_3.grid(row=3, column=1, columnspan=3, padx=10, pady=10)

# place = tk.IntVar(info_frame)
# place.set("Шаҳар")
# label_4 = tk.Label(info_frame, text="4. Шаҳар ёки қишлоқ тугмасини танланг.")
# label_4.grid(row=4, column=0, padx=10, pady=10)
# button_4_1 = tk.Radiobutton(info_frame, text="Шаҳар", value=1, variable=place)
# button_4_1.grid(row=4, column=1, padx=10, pady=10)
# button_4_2 = tk.Radiobutton(info_frame, text="Қишлоқ", value=2, variable=place)
# button_4_2.grid(row=4, column=2, padx=10, pady=10)
# button_4_3 = tk.Radiobutton(info_frame, text="Бош Тортиш", value=3, variable=place)
# button_4_3.grid(row=4, column=3, padx=10, pady=10)

# gender = tk.IntVar(info_frame)
# gender.set("Эркак")
# label_5 = tk.Label(info_frame, text="5. Респондентнинг жинсини киритинг.")
# label_5.grid(row=5, column=0, padx=10, pady=10)
# button_5_1 = tk.Radiobutton(info_frame, text="Эркак", value=1, variable=gender)
# button_5_1.grid(row=5, column=1, padx=10, pady=10)
# button_5_2 = tk.Radiobutton(info_frame, text="Аёл", value=2, variable=gender)
# button_5_2.grid(row=5, column=2, padx=10, pady=10)

# label_6 = tk.Label(info_frame, text="6. Респондентнинг ёшини киритинг.")
# label_6.grid(row=6, column=0, padx=10, pady=10)
# entry_6 = tk.Entry(info_frame)
# entry_6.grid(row=6, column=1, columnspan=3, padx=10, pady=10)


# welfare_frame = tk.LabelFrame(root, borderwidth=0, highlightthickness=0, padx=10, pady=10)
# welfare_frame.pack()
# label_7 = tk.Label(welfare_frame, text="7. Мамлакатдаги умумий вазиятдан (ҳолатдан) қониқиш\nдаражангизни 7 баллик шкалада баҳоланг. (1 энг паст баҳо\n– умуман қониқмаслик, 7 энг юқори баҳо – тўлиқ қониқиш).")
# label_7.grid(row=0, column=0, padx=10, pady=10)


# prezident section
prezident_frame = tk.LabelFrame(inside_frame, borderwidth=0, highlightthickness=0, padx=10, pady=10)
prezident_frame.pack()
table_frame = tk.LabelFrame(prezident_frame, borderwidth=0, highlightthickness=0, padx=10, pady=10)
table_frame.grid(row=4, column=0, padx=10, pady=10)
options_19_26 = [1, 2, 3, 4]


# Question 19
label_19_row = 2
text_19 = "19. Абдулла Арипов, Ўзбекистон Республикаси Бош вазири"
question_19 = mcq_question(table_frame, label_19_row, options_19_26,
                            text=text_19, num_options=4)

# Question 20
label_20_row = 4
text_20 = "20. Танзила Нарбаева, Ўзбекистон Республикаси Олий Мажлиси Сенати раиси"
question_20 = mcq_question(table_frame, label_20_row, options_19_26,
                            text=text_20, num_options=4)

# Question 21
label_21_row = 6
text_21 = "21. Нурдинжон Исмоилов, Ўзбекистон Республикаси Олий Мажлиси Қонунчилик палатасининг спикери"
question_21 = mcq_question(table_frame, label_21_row, options_19_26,
                            text=text_21, num_options=4)

# Question 22
label_22_row = 8
text_22 = "22. Актам Хаитов, Ўзбекистон Либерал-демократик партияси етакчиси"
question_22 = mcq_question(table_frame, label_22_row, options_19_26,
                            text=text_22, num_options=4)

# Question 23
label_23_row = 10
text_23 = "23. Алишер Қодиров, Ўзбекистон «Миллий тикланиш» демократик партияси етакчиси"
question_23 = mcq_question(table_frame, label_23_row, options_19_26,
                            text=text_23, num_options=4)

# Question 24
label_24_row = 12
text_24 = "24. Баҳром Абдухалимов, Ўзбекистон «Адолат»  демократик партияси етакчиси "
question_24 = mcq_question(table_frame, label_24_row, options_19_26,
                            text=text_24, num_options=4)

# Question 25
label_25_row = 14
text_25 = "25. Улуғбек Иноятов, Ўзбекистон Халқ демократик партияси етакчиси"
question_25 = mcq_question(table_frame, label_25_row, options_19_26,
                            text=text_25, num_options=4)

# Question 26
label_26_row = 16
text_26 = "26. Нарзулло Обломуродов, Ўзбекистон Экология партияси етакчиси"
question_26 = mcq_question(table_frame, label_26_row, options_19_26,
                            text=text_26, num_options=4)

# Question 27
label_27_row = 18
text_27 = "27.	Президент Шавкат Мирзиёев ўз лавозимида фикрингиз бўйича қандай фаолият кўрсатаётганлигини 7 баллик шкалада баҳоланг. (1 - энг паст баҳо, 7 - энг юқори баҳо )"
question_27 = mcq_question(table_frame, label_27_row, [1, 2, 3, 4, 5, 6, 7], text=text_27, num_options=7)

# Question 28
label_28_row = 20
text_28 = "28.	Ўтган икки ой мобайнида Шавкат Мирзиёевга Ўзбекистон Президенти сифатида муносабатингиз ўзгардими? Ва, агар ўзгарган бўлса, у қайси томонга - яхшиланди ёки ёмонлашди? (битта жавоб)"
question_28 = mcq_question(table_frame, label_28_row, ["Анча яхшиланди", "Озроқ яхшиланди", "Озроқ ёмонлашди", "Анча ёмонлашди", "Ҳеч нарса ўзгармади", "(БУНИ ЎҚИМАНГ) Жавоб беришга қийналаман"], text=text_28, num_options=6)

# Question 29
label_29_row = 22
text_29 = "29.	Шавкат Мирзиёевга ишонасизми ёки ишонмайсизми? (битта жавоб)"
question_29 = mcq_question(table_frame, label_29_row, ["Тўлиқ ишонаман", "Ишонаман", "Ишонмайман", "Тўлиқ ишонмайман", "(БУНИ ЎҚИМАНГ) Жавоб беришга қийналаман"], text=text_29, num_options=5)

# Question 30
label_30_row = 24

# Question 31
label_31_row = 26

# Question 32
label_32_row = 28
text_32 = "32.	Сизнингча, Шавкат Мирзиёев мамлакатдаги вазиятни яхши томонга ўзгартира оладими ёки йўқми? (битта жавоб)"
question_32 = mcq_question(table_frame, label_32_row, ["Аниқ ўзгартира олади", "Ўзгартириши мумкин", "Ўзгартириши қийин", "Аниқ ўзгартира олмайди", "(БУНИ ЎҚИМАНГ) Ҳеч нарса дея олмайман", "(БУНИ ЎҚИМАНГ) Жавоб беришга қийналаман "], text=text_32, num_options=6)

# Question 33
label_33_row = 30

# Question 34
label_34_row = 32
text_34 = "34.	Сизнингча, мамлакатга янги Президент керакми ёки ҳозирги Президент қолгани маъқулми? (буни ўқиманг, битта жавоб)"
question_34 = mcq_question(table_frame, label_34_row, ["Янги Президент керак", "Амалдаги Президентнинг қолгани яхши", "(БУНИ ЎҚИМАНГ) Менга фарқи йўқ", "(БУНИ ЎҚИМАНГ) Жавоб беришга қийналаман"], text=text_34, num_options=4)

# major frame
major_frame = tk.LabelFrame(inside_frame, borderwidth=0, highlightthickness=0, padx=10, pady=10)
major_frame.pack()
label_35_row = 1
text_35 = "35. Айтингчи, Сиз вилоят ҳокимига ишонасизми ёки ишонмайсизми?"
options_35 = ["Тўлиқ ишонаман", "Қисман ишонаман", "Қисман ишонмайман", 
              "Умуман ишонмайман", "Жавоб беришга қийналаман"]
question_35 = mcq_question(major_frame, label_35_row, options_35, text_35, 5)

label_36_row = 3
text_36 = "36. Сизнингча, вилоят/республика хокими сифатида қандай ишлаяпти? 7 баллик  шкалада баҳоланг"
options_36 = ["1. Жуда ёмон", "2", "3", "4", "5", "6", "7. Жуда яхши"]
question_36 = mcq_question(major_frame, label_36_row, options_36, text_36, 7)

label_37_row =5 
text_37 = "37. Сизнингча вилоят/республикага янги ҳоким керакми ёки амалдаги ҳоким қолгани яхшими?"
options_37 = ["Янги ҳоким керак","Амалдаги қолгани яхши","Менга фарқи йўқ","Жавоб беришга қийналаман"]
question_37 = mcq_question(major_frame, label_37_row, options_37, text_37, 4)

label_38_row = 7
text_38 = "38. Туманингизнинг ҳокими. Сиз туманингиз ҳокимимга ишонасизми ёки ишонмайсизми?"
options_38 = ["Тўлиқ ишонаман","Ишонаман","Ишонмиман","Тўлиқ ишонмиман","Жавоб беришга қийналаман"]
question_38 = mcq_question(major_frame, label_38_row, options_38, text_38, 5)

label_39_row = 9
text_39 = "39. Сизнингча, туманингиз ҳокими ўз лавозимида қандай ишламоқда?"
options_39 = ["1. Жуда ёмон", "2", "3", "4", "5", "6", "7. Жуда яхши"]
question_39 = mcq_question(major_frame, label_39_row, options_39, text_39, 7)

label_40_row = 11
text_40 = "40. Сизнингча туманга янги ҳоким керакми ёки амалдаги ҳоким қолгани яхшими? "
options_40 = ["Янги ҳоким керак","Амалдаги қолгани яхши","Менга фарқи йўқ","Жавоб беришга қийналаман"]
question_40 = mcq_question(major_frame, label_40_row, options_40, text_40, 4)

label_41_row = 13
text_41 = "41. Сиз қандай фикрдасиз – қайси бири яхши: вилоят ҳокимини ҳозиргидек тайинлаган маъқулми ёки уни овоз бериш орқали сайлаганми?"
options_41 = ["Тайинланса яхши","Сайланса яхши","Менга фарқи йўқ","Жавоб беришга қийналаман"]
question_41 = mcq_question(major_frame, label_41_row, options_41, text_41, 4)

label_42_row = 15
text_42 = "42. Сиз қандай фикрдасиз – қайси бири яхши: туман ҳокимини ҳозиргидек тайинлаган маъқулми ёки уни овоз бериш орқали сайлаганми?"
options_42 = ["Тайинланса яхши","Сайланса яхши","Менга фарқи йўқ","Жавоб беришга қийналаман"]
question_42 = mcq_question(major_frame, label_42_row, options_42, text_42, 4)




















# button at the bottom
bottom_frame = tk.LabelFrame(inside_frame, borderwidth=0, highlightthickness=0, padx=10, pady=10)
bottom_frame.pack(side=tk.BOTTOM)
button_exit = tk.Button(bottom_frame, text="Exit Program", command=root.quit)
button_exit.grid(row=0, column=0, padx=80, pady=10)
button_save = tk.Button(bottom_frame, text="Save Responses", command=save_data)  ###############
button_save.grid(row=0, column=1, padx=80, pady=10)


util.main()
controller.main()
root.mainloop()
