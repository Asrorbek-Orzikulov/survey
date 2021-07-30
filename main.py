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


def radio_button_question(frame_name, label_row, options, text, num_options):
    label = tk.Label(frame_name, text=text)
    label.grid(row=label_row, column=0, padx=10, pady=0, columnspan=num_options)
    variable = tk.IntVar(frame_name)
    for idx, option in enumerate(options):
        button = tk.Radiobutton(frame_name, text=option, value=idx+1, variable=variable)
        button.grid(row=label_row + 1, column=idx, padx=10, pady=30) #####################

    return variable

def checkbox_question(frame_name, label_row, options, text, has_other=False):
    results = []
    label = tk.Label(frame_name, text=text)
    label.grid(row=label_row, column=0, columnspan=10)    
    offset = 1
    for idx, option in enumerate(options):
        result = tk.IntVar()
        check_box = tk.Checkbutton(frame_name, text=option, variable=result)
        check_box.grid(row=label_row+offset, column=0, columnspan=7)
        results.append(result)
        offset += 1
    
    # taking care of 'Other'
    if has_other:
        entry = tk.Entry(frame_name, width=100)
        entry.grid(row=label_row+offset+1, column=0, columnspan=10, padx=10, pady=30)
        entry.configure(state=tk.DISABLED)
        button = tk.Button(
            frame_name, text="   Бошқа    ",
            command=lambda: entry.configure(state=tk.NORMAL))
        button.grid(row=label_row+offset, column=0, columnspan=7)
        results.append(entry)
    return results

def inputting_questions(frame_name, label_row, num_options, text):
    results = []
    label = tk.Label(frame_name, text=text)
    label.grid(row=label_row, column=0, columnspan=7) 
    for idx in range(1, num_options+1):
        entry = tk.Entry(frame_name, width=100)
        entry.grid(row=label_row+idx, column=0, columnspan=7, padx=10, pady=30)
        results.append(entry)
    
    is_difficult = tk.IntVar()
    check_box = tk.Checkbutton(frame_name, text="Жавоб беришга қийналаман", variable=is_difficult)
    check_box.grid(row=label_row+num_options+1, column=0, columnspan=7)
    results.append(is_difficult)
    return results





# start of the GUI
root= tk.Tk()
root.title("Анкета Опроса Населения")
root.iconbitmap("images/icon.ico")
root.geometry("1200x700")  

# adding a scrollbar
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=tk.YES)
canvas = tk.Canvas(main_frame)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)
scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind("<Configure>", 
            lambda event: canvas.configure(scrollregion=canvas.bbox("all")))

canvas.bind_all("<MouseWheel>",
                lambda event: canvas.yview_scroll(-1 * int((event.delta / 120)), "units"))

inside_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=inside_frame, anchor="nw")

# button at the bottom
bottom_frame = tk.LabelFrame(root, borderwidth=4, highlightthickness=4, padx=10, pady=0)
bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)
button_exit = tk.Button(bottom_frame, text="Exit Program", command=root.quit)
button_exit.pack(side=tk.LEFT, pady=5, padx=5)
# button_exit.grid(row=0, column=0, padx=10, pady=10)
button_save = tk.Button(bottom_frame, text="Save Responses", command=save_data)  ###############
button_save.pack(side=tk.RIGHT,   pady=5, padx=20)
# button_save.grid(row=0, column=1, padx=10, pady=10)
button_verify = tk.Button(bottom_frame, text="Verify Responses", command=save_data)  ###############
button_verify.pack(side=tk.RIGHT, pady=5, padx=20)

#
# Start of questionnaire
#

head_frame = tk.LabelFrame(inside_frame, borderwidth=10, highlightthickness=0, padx=10, pady=10)
head_frame.pack(fill=tk.BOTH, expand=True)
head_frame.grid_columnconfigure(0, weight=1)
head_frame.grid_rowconfigure(0, weight=1)

label_head = tk.Label(head_frame, borderwidth=0, highlightthickness=0,
                      text="Ўзбекистон Республикасида  ижтимоий-сиёсий вазиятни ўрганиш (2021 июль)")
label_head.grid(row=0, column=0, sticky=tk.NSEW)
label_head.config(font=("helvetica", 14), fg="dark blue")


#
# info section
#

info_frame = tk.LabelFrame(inside_frame, borderwidth=10, highlightthickness=0, padx=10, pady=10)
info_frame.pack() # fill=tk.BOTH, expand=tk.YES

info_frame.grid_columnconfigure(0, weight=1)
info_frame.grid_rowconfigure(8, weight=1)

label_info = tk.Label(info_frame, text="Сўров иштирокчиларининг ижтимоий-демографик хусусиятлари")
label_info.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
label_info.config(font=("helvetica", 12), fg="green")

# Question 1
label_1 = tk.Label(info_frame, text="1. Исмингиз нима?")  # , justify=tk.LEFT, anchor="w"
label_1.grid(row=1, column=0, padx=10, pady=10, columnspan=3)  # , sticky = tk.W
question_1 = tk.Entry(info_frame, width=50)
question_1.grid(row=2, column=0, columnspan=3, padx=10, pady=30)

# Question 2
label_2_row = 3
text_2 = "2. Сиз вилоятда доимий яшайсизми ва рўйхатдан ўтганмисиз?"
options_2 = ["Ҳа", "Йўқ"]
question_2 = radio_button_question(info_frame, label_2_row, options_2, 
                    text=text_2, num_options=3)

# Question 3
label_3 = tk.Label(info_frame, text="3. Сиз вилоятнинг қайси тумани(шаҳри)да яшайсиз?")
label_3.grid(row=5, column=0, padx=10, pady=10, columnspan=3)
question_3 = tk.Entry(info_frame, width=50)
question_3.grid(row=6, column=0, columnspan=3, padx=10, pady=30)


# Question 4
label_4_row = 7
text_4 = "4. Шаҳар ёки қишлоқ тугмасини танланг."
options_4 = ["Шаҳар", "Қишлоқ", "Бош Тортиш"]
question_4 = radio_button_question(info_frame, label_4_row, options_4, text_4, 3)

# Question 5
label_5_row = 9
text_5 = "5. Респондентнинг жинсини киритинг."
options_5 = ["Эркак", "Аёл"]
question_5 = radio_button_question(info_frame, label_5_row, options_5, text_5, 3)

# Question 6
label_6 = tk.Label(info_frame, text="6. Респондентнинг ёшини киритинг.")
label_6.grid(row=11, column=0, padx=10, pady=10)
question_6 = tk.Entry(info_frame)
question_6.grid(row=11, column=1, columnspan=3, padx=10, pady=10)

#
# welfare section
#

welfare_frame = tk.LabelFrame(inside_frame, borderwidth=10, highlightthickness=0, padx=10, pady=10)
welfare_frame.pack(fill=tk.BOTH, expand=tk.YES)

# Question 7
label_7_row = 3
text_7 = "7. Сизнингча, мамлакатдаги умумий вазият яхшиланмоқдами, ёмонлашмоқдами ёки деярли ўзгармаяптими? (битта жавоб)"
question_7 = radio_button_question(welfare_frame, label_7_row, ["Яхшиланмоқда", "Ёмонлашмоқда", "Деярли ўзгармаяпти", "Жавоб беришга қийналаман"],
                            text=text_7, num_options=4)

# Question 8
label_8_row = 5
text_8 = "8. Вилоятингиздаги умумий вазиятдан (ҳолатдан) қониқиш даражангизни 7 баллик шкалада баҳоланг. (1 энг паст баҳо – умуман қониқмаслик, 7 энг юқори баҳо – тўлиқ қониқиш)"
question_8 = radio_button_question(welfare_frame, label_8_row, [1, 2, 3, 4, 5, 6, 7],
                            text=text_8, num_options=7)

# Question 9
label_9_row = 7
text_9 = "9. Сизнингча, вилоятдаги умумий вазият яхшиланмоқда, ёмонлашмоқда ёки деярли ўзгармаяптими? (битта жавоб)"
question_9 = radio_button_question(welfare_frame, label_9_row, ["Яхшиланмоқда", "Ёмонлашмоқда", "Деярли ўзгармаяпти", "Жавоб беришга қийналаман"],
                            text=text_9, num_options=4)

# Question 10
label_10_row = 9
text_10 = "10. Маҳаллангиздаги умумий вазиятдан (ҳолатдан) қониқиш даражангизни 7 баллик шкалада баҳоланг. (1 энг паст баҳо – умуман қониқмаслик, 7 энг юқори баҳо – тўлиқ қониқиш)"
question_10 = radio_button_question(welfare_frame, label_10_row, [1, 2, 3, 4, 5, 6, 7],
                            text=text_10, num_options=7)

# Question 11
label_11_row = 11
text_11 = "11. Сизнингча, сиз яшаётган маҳаллада умумий вазият яхшиланмоқдами, ёмонлашмоқдами ёки ҳеч нарса ўзгармаяптими? (битта жавоб)"
question_11 = radio_button_question(welfare_frame, label_11_row, ["Яхшиланмоқда", "Ёмонлашмоқда", "Деярли ўзгармаяпти", "Жавоб беришга қийналаман"],
                            text=text_11, num_options=4)

# Question 12
label_12_row = 13
text_12 = "12. Сизнингча, атрофингиздаги одамлар ҳозир қандай кайфиятда: кўтаринки, хотиржам ёки тушкун (хавотирли)? (битта жавоб)"
question_12 = radio_button_question(welfare_frame, label_12_row, ["Кўтаринки", "Хотиржам", "Тушкун, хавотирли", "жавоб беришга қийналаман"],
                            text=text_12, num_options=4)

# Question 13
label_13_row = 15
text_13 = "13. “Мен Ўзбекистон иқтисодиёти ривожланишига ишонаман” Мазкур фикрга... (Ўқиб беринг)"
question_13 = radio_button_question(welfare_frame, label_13_row, ["Тўлиқ қўшиламан", "Қисман қўшиламан", "Қисман қўшилмайман", "Умуман қўшилмайман"],
                            text=text_13, num_options=4)

# Question 14
label_14_row = 17
text_14 = "14. “Мамлакатимизда олиб борилаётган ислоҳотлар тўғри йўлда кетмоқда”  Мазкур фикрга (Ўқиб беринг. Битта жавоб танланади)"
question_14 = radio_button_question(welfare_frame, label_14_row, ["Тўлиқ қўшиламан", "Қисман қўшиламан", "Қисман қўшилмайман", "Умуман қўшилмайман"],
                            text=text_14, num_options=4)

# Question 15
label_15_row = 19
text_15 = "15. Давлат томонидан қуйида келтирилган соҳалардан қай бирида амалга оширилаётган ишларни маъқуллайсиз?"
options_15 = [
    "Таълим тизими", 
    "Соғлиқни сақлаш тизими", 
    "Ҳудудлардаги инфратузилмани (газ, свет, йўл ва ҳ.к.) яхшилаш",
    "Коррупция қарши кураш",
    "Аҳолини уй-жой билан таъминлаш",
    "Камбағаликка қарши кураш",
    "Тадбиркорларни қўллаб-қувватлаш",
    "Халқ билан очиқ мулоқотнинг кучайиши",
    "Ҳеч бирини"
    ]
results_15 = checkbox_question(welfare_frame, label_15_row, options=options_15,
                               text=text_15, has_other=True)

#
# prezident section
#

prezident_frame = tk.LabelFrame(inside_frame, borderwidth=10, highlightthickness=0, padx=10, pady=10)
prezident_frame.pack(fill=tk.BOTH, expand=tk.YES)

# Question 16
label_16_row = 0
text_16 = "16. Сизнинг фикрингизча, ҳукумат фуқаролар билан очиқ мулоқотда бўлмоқда ва уларнинг муаммоларига ўз вақтида жавоб қайтармоқда?"
options_16 = ["Тўлиқ қўшиламан", "Қисман қўшиламан", "Қисман қўшилмайман", "Умуман қўшилмайман"]
question_16 = radio_button_question(prezident_frame, label_16_row, 
                                    options_16, text_16, 4)

# Question 17
label_17_row = 2
text_17 = "17. Илтимос, сиз фикрига қулоқ соладиган, ҳурмат қиладиган сиёсатчилар, жамоат арбоблари, бизнес вакиллари ёки бошқа соҳада фаолият кўрсатадиган одамлар исмларини айтинг"
num_options_17 = 5
results_17 = inputting_questions(prezident_frame, label_17_row, num_options_17, text_17)



table_frame = tk.LabelFrame(prezident_frame, borderwidth=5, highlightthickness=0, padx=10, pady=10)
table_frame.grid(row=10, column=0, padx=10, pady=10, columnspan=8)
options_18_25 = [1, 2, 3, 4]

# Question 18
label_18_row = 2
text_18 = "18. Абдулла Арипов, Ўзбекистон Республикаси Бош вазири"
question_18 = radio_button_question(table_frame, label_18_row, options_18_25,
                            text=text_18, num_options=4)

# Question 19
label_19_row = 4
text_19 = "19. Танзила Нарбаева, Ўзбекистон Республикаси Олий Мажлиси Сенати раиси"
question_19 = radio_button_question(table_frame, label_19_row, options_18_25,
                            text=text_19, num_options=4)

# Question 20
label_20_row = 6
text_20 = "20. Нурдинжон Исмоилов, Ўзбекистон Республикаси Олий Мажлиси Қонунчилик палатасининг спикери"
question_20 = radio_button_question(table_frame, label_20_row, options_18_25,
                            text=text_20, num_options=4)

# Question 21
label_21_row = 8
text_21 = "21. Актам Хаитов, Ўзбекистон Либерал-демократик партияси етакчиси"
question_21 = radio_button_question(table_frame, label_21_row, options_18_25,
                            text=text_21, num_options=4)

# Question 22
label_22_row = 10
text_22 = "22. Алишер Қодиров, Ўзбекистон «Миллий тикланиш» демократик партияси етакчиси"
question_22 = radio_button_question(table_frame, label_22_row, options_18_25,
                            text=text_22, num_options=4)

# Question 23
label_23_row = 12
text_23 = "23. Баҳром Абдухалимов, Ўзбекистон «Адолат»  демократик партияси етакчиси "
question_23 = radio_button_question(table_frame, label_23_row, options_18_25,
                            text=text_23, num_options=4)

# Question 24
label_24_row = 14
text_24 = "24. Улуғбек Иноятов, Ўзбекистон Халқ демократик партияси етакчиси"
question_24 = radio_button_question(table_frame, label_24_row, options_18_25,
                            text=text_24, num_options=4)

# Question 25
label_25_row = 16
text_25 = "25. Нарзулло Обломуродов, Ўзбекистон Экология партияси етакчиси"
question_25 = radio_button_question(table_frame, label_25_row, options_18_25,
                            text=text_25, num_options=4)

# Question 26
label_26_row = 12
text_26 = "26. Президент Шавкат Мирзиёев ўз лавозимида фикрингиз бўйича қандай фаолият кўрсатаётганлигини 7 баллик шкалада баҳоланг. (1 - энг паст баҳо, 7 - энг юқори баҳо )"
options_26 = [1, 2, 3, 4, 5, 6, 7]
question_26 = radio_button_question(prezident_frame, label_26_row, options_26,
                            text=text_26, num_options=7)

# Question 27
label_27_row = 14
text_27 = "27. Ўтган икки ой мобайнида Шавкат Мирзиёевга Ўзбекистон Президенти сифатида муносабатингиз ўзгардими? Ва, агар ўзгарган бўлса, у қайси томонга - яхшиланди ёки ёмонлашди? (битта жавоб)"
options_27 = ["Анча яхшиланди", "Озроқ яхшиланди", "Озроқ ёмонлашди", "Анча ёмонлашди", "Ҳеч нарса ўзгармади", "Жавоб беришга қийналаман"]
question_27 = radio_button_question(prezident_frame, label_27_row, 
                                    options_27, text=text_27, num_options=6)

# Question 28
label_28_row = 16
text_28 = "28.	Шавкат Мирзиёевга ишонасизми ёки ишонмайсизми?"
options_28 = ["Тўлиқ ишонаман", "Ишонаман", "Ишонмайман", "Тўлиқ ишонмайман", "Жавоб беришга қийналаман"]
question_28 = radio_button_question(prezident_frame, label_28_row, options=options_28,
                           text=text_28, num_options=5)

# Question 29
label_29_row = 18
text_29 = "29. Илтимос, Шавкат Мирзиёевнинг Президентлик даврида эришган асосий ютуқларини номлаб беринг."
options_29 = [
    "1. Конвертация очилганлиги (валюта сиёсати)",
    "2. Ташқи савдонинг эркинлашуви",
    "3. Солиқ сиёсати",
    "4. Сўз эркинлигининг кучайиши",
    "5. Яқин қўшнилар билан алоқанинг мустаҳкамланиши",
    "6. Дин ва эътиқод эркинлигининг кучайиши",
    "7. Камбағалликка қарши кураш ишлари",
    "8. Соғлиқни сақлаш тизимидаги ислоҳотлар",
    "9. Янги иш ўринларининг яратилиши",
    "10. Мигрантлар учун шароитларнинг яхшиланиши",
    "11. Халқ билан мулоқотнинг кучайиши",
    "12. Ёшларни қўллаб-қувватлашнинг кучайтирилиши",
    "13. Тадбиркорликни қўллаб-қувватлаш ишлари",
    "14. Аҳолини уй-жой билан таъминлаш",
    "15. Давлат хизматлари сифатининг ортиши",
    "16. Мактабгача таълим тизимидаги ишлар",
    "17. Олий таълим тизимидаги ислоҳотлар",
    "18. Мактаб таълимидаги ўзгаришлар",
    "19. Ҳеч қандай ютуғи йўқ",
    "20. Жавоб беришга қийналаман"
    ]
results_29 = checkbox_question(prezident_frame, label_29_row, options_29, 
                               text_29, True)

# Question 30
label_30_row = 42
text_30 = "30. Илтимос, Шавкат Мирзиёевнинг Президентлик давридаги асосий камчиликларини номлаб беринг"
options_30 = [
    "1. Коррупцияга қарши кураш ишлари",
    "2. Аҳолини тоза ичимлик суви билан таъминлаш",
    "3. Аҳолини электрэнергия билан таъминлаш",
    "4. Аҳолини табиий газ билан таъминлаш",
    "5. Етарли янги иш ўринларини яратиш",
    "6. Нарх-навонинг кўтарилиши",
    "7. Аҳолига ижтимоий моддий ёрдам кўрсатиш",
    "8. Ташқи қарзнинг кўпайиши",
    "9. Айрим соҳаларда монополиянинг сақланиб қолиниши",
    "10. Ҳеч қандай камчилиги йўқ",
    "11. Жавоб беришга қийналаман"
    ]
results_30 = checkbox_question(prezident_frame, label_30_row, options_30, 
                               text_30, True)

# Question 31
label_31_row = 56
text_31 = "31. Сизнингча, Шавкат Мирзиёев мамлакатдаги вазиятни яхши томонга ўзгартира оладими ёки йўқми?"
options_31 = ["Аниқ ўзгартира олади", "Ўзгартириши мумкин", "Ўзгартириши қийин", "Аниқ ўзгартира олмайди", "Ҳеч нарса дея олмайман", "Жавоб беришга қийналаман "]
question_31 = radio_button_question(
    prezident_frame, label_31_row, options=options_31, text=text_31, num_options=6)

# Question 32
label_32_row = 58
text_32 = "32. Сизнингча, Ўзбекистон Республикаси Президенти Шавкат Мирзиёев биринчи навбатда қандай вазифаларни ҳал этиши керак?"
num_options_32 = 3
results_32 = inputting_questions(prezident_frame, label_32_row, num_options_32, text_32)
                          

# Question 33
label_33_row = 63
text_33 = "33. Сизнингча, мамлакатга янги Президент керакми ёки ҳозирги Президент қолгани маъқулми?"
options_33 = ["Янги Президент керак", "Амалдаги Президентнинг қолгани яхши" , "Менга фарқи йўқ", "Жавоб беришга қийналаман"]
question_33 = radio_button_question(prezident_frame, label_33_row, options_33, text_33, 4)

#
# major section
#

major_frame = tk.LabelFrame(inside_frame, borderwidth=10, highlightthickness=0, padx=10, pady=10)
major_frame.pack(fill=tk.BOTH, expand=tk.YES)

# Question 34
label_34_row = 1
text_34 = "34. Айтингчи, Сиз вилоят ҳокимига ишонасизми ёки ишонмайсизми?"
options_34 = ["Тўлиқ ишонаман", "Қисман ишонаман", "Қисман ишонмайман", 
              "Умуман ишонмайман", "Жавоб беришга қийналаман"]
question_34 = radio_button_question(major_frame, label_34_row, options_34, text_34, 5)

# Question 35
label_35_row = 3
text_35 = "35. Сизнингча, вилоят/республика хокими сифатида қандай ишлаяпти? 7 баллик  шкалада баҳоланг"
options_35 = [1, 2, 3, 4, 5, 6, 7]
question_35 = radio_button_question(major_frame, label_35_row, options_35, text_35, 7)

# Question 36
label_36_row =5 
text_36 = "36. Сизнингча вилоят/республикага янги ҳоким керакми ёки амалдаги ҳоким қолгани яхшими?"
options_36 = ["Янги ҳоким керак","Амалдаги қолгани яхши","Менга фарқи йўқ","Жавоб беришга қийналаман"]
question_36 = radio_button_question(major_frame, label_36_row, options_36, text_36, 4)


# Question 37
label_37_row = 7
text_37 = "37. Туманингизнинг ҳокими. Сиз туманингиз ҳокимимга ишонасизми ёки ишонмайсизми?"
options_37 = ["Тўлиқ ишонаман","Ишонаман","Ишонмиман","Тўлиқ ишонмиман","Жавоб беришга қийналаман"]
question_37 = radio_button_question(major_frame, label_37_row, options_37, text_37, 5)

# Question 38
label_38_row = 9
text_38 = "38. Сизнингча, туманингиз ҳокими ўз лавозимида қандай ишламоқда?"
options_38 = [1, 2, 3, 4, 5, 6, 7]
question_38 = radio_button_question(major_frame, label_38_row, options_38, text_38, 7)

# Question 39
label_39_row = 11
text_39 = "39. Сизнингча туманга янги ҳоким керакми ёки амалдаги ҳоким қолгани яхшими? "
options_39 = ["Янги ҳоким керак","Амалдаги қолгани яхши","Менга фарқи йўқ","Жавоб беришга қийналаман"]
question_39 = radio_button_question(major_frame, label_39_row, options_39, text_39, 4)

# Question 40
label_40_row = 13
text_40 = "40. Сиз қандай фикрдасиз – қайси бири яхши: вилоят ҳокимини ҳозиргидек тайинлаган маъқулми ёки уни овоз бериш орқали сайлаганми?"
options_40 = ["Тайинланса яхши","Сайланса яхши","Менга фарқи йўқ","Жавоб беришга қийналаман"]
question_40 = radio_button_question(major_frame, label_40_row, options_40, text_40, 4)

# Question 41
label_41_row = 15
text_41 = "41. Сиз қандай фикрдасиз – қайси бири яхши: туман ҳокимини ҳозиргидек тайинлаган маъқулми ёки уни овоз бериш орқали сайлаганми?"
options_41 = ["Тайинланса яхши","Сайланса яхши","Менга фарқи йўқ","Жавоб беришга қийналаман"]
question_41 = radio_button_question(major_frame, label_41_row, options_41, text_41, 4)

#
# parliament section
#

def radio_button_question(frame_name, label_row, options, text, has_other):
    label = tk.Label(frame_name, text=text)
    label.grid(row=label_row, column=0, columnspan=4, padx=10, pady=30)
    variable = tk.IntVar(frame_name)
    for idx, option in enumerate(options):
        button = tk.Radiobutton(frame_name, text=option, value=idx+1, variable=variable)
        button.grid(row=label_row+idx+1, column=2, padx=10, pady=15, sticky = "w") #####################
    
    if has_other:
        offset = len(options) + 1
        entry = tk.Entry(frame_name, width=100)
        entry.grid(row=label_row+offset+1, column=0, columnspan=4, padx=10, pady=15)
        entry.configure(state=tk.DISABLED)
        button = tk.Button(
            frame_name, text="   Бошқа    ",
            command=lambda: entry.configure(state=tk.NORMAL))
        button.grid(row=label_row+offset, column=2, sticky = "w")
    
    if has_other:
        return (variable, entry)
    else:
        return variable

# Question 42
parliament_frame = tk.LabelFrame(inside_frame, borderwidth=10, highlightthickness=0, padx=10, pady=10)
parliament_frame.pack(fill=tk.BOTH, expand=tk.YES)
label_42_row = 1
text_42 = "42. Ўзбекистон Республикаси Олий Мажлис Қонунчилик палатасининг амалдаги таркибининг фаолиятини қандай баҳолайсиз?"
options_42 = [1, 2, 3, 4, 5, 6, 7]
question_42 = radio_button_question(parliament_frame, label_42_row, options_42, text_42, False)

# Question 43
label_43_row = 9
text_43 = "43. Агар Олий Мажлис Қонунчилик палатаси сайловлари кейинги якшанба куни бўлиб ўтса, сиз қайси партияга овоз берган бўлардингиз?"
options_43 = [
    "1. Ўзбекистон Либерал-демократик партияси",
    "2. “Миллий тикланиш” демократик партияси",
    "3. Ўзбекистон Халқ демократик партияси",
    "4. “Адолат” социал-демократик партияси",
    "5. Экология партияси",
    "6. Ҳеч қайси учун/ҳаммасига қарши",
    "7. Бюллетенни йиртаман",
    "8.Сайловга бормиман",
    "9. Жавоб беришга қийналаман",
    "10. Рад этиш"
    ]
results_43 = radio_button_question(parliament_frame, label_43_row, options_43, text_43, True)







text = text_43
frame_name = parliament_frame
label_row = label_43_row
has_other = False








def checkbox_question(frame_name, label_row, options, text, has_other=False):
    results = []
    label = tk.Label(frame_name, text=text)
    label.grid(row=label_row, column=0, columnspan=10)    
    offset = 1
    for idx, option in enumerate(options):
        result = tk.IntVar()
        check_box = tk.Checkbutton(frame_name, text=option, variable=result)
        check_box.grid(row=label_row+offset, column=0, columnspan=7)
        results.append(result)
        offset += 1
    
    # taking care of 'Other'
    if has_other:
        entry = tk.Entry(frame_name, width=100)
        entry.grid(row=label_row+offset+1, column=0, columnspan=10, padx=10, pady=30)
        entry.configure(state=tk.DISABLED)
        button = tk.Button(
            frame_name, text="   Бошқа    ",
            command=lambda: entry.configure(state=tk.NORMAL))
        button.grid(row=label_row+offset, column=0, columnspan=7)
        results.append(entry)
    return results

def radio_button_question(frame_name, label_row, options, text, num_options):
    label = tk.Label(frame_name, text=text)
    label.grid(row=label_row, column=0, padx=10, pady=0, columnspan=num_options)
    variable = tk.IntVar(frame_name)
    for idx, option in enumerate(options):
        button = tk.Radiobutton(frame_name, text=option, value=idx+1, variable=variable)
        button.grid(row=label_row + 1, column=idx, padx=10, pady=30) #####################

    return variable


# clicked = tk.StringVar()
# dropdown_15 = tk.OptionMenu(welfare_frame, clicked, *options_15)
# dropdown_15.config(width=100)
# dropdown_15.set("")
# dropdown_15.grid(row=19, column=0, columnspan=8)



util.main()
controller.main()
root.mainloop()
