import tkinter as tk
import util
import os
import xlsxwriter


# survey_structure = [
#     (0, 1),
#     (1, 1),
#     (2, 1),
#     (3, 1),
#     (4, 1),
#     (5, 1),
#     (6, 1),
#     (6.1, 1),
#     (7, 1),
#     (8, 1),
#     (9, 1),
#     (10, 1),
#     (11, 1),
#     (12, 1),
#     (13, 1),
#     (14, 1),
#     (15, 10),
#     (16, 1),
#     (17, 6),
#     (18, 1),
#     (19, 1),
#     (20, 1),
#     (21, 1),
#     (22, 1),
#     (23, 1),
#     (24, 1),
#     (25, 1),
#     (26, 1),
#     (27, 1),
#     (28, 1),
#     (29, 21),
#     (30, 12),
#     (31, 1),
#     (32, 4),
#     (33, 1),
#     (34, 1),
#     (35, 1),
#     (36, 1),
#     (37, 1),
#     (38, 1),
#     (39, 1),
#     (40, 1),
#     (41, 1),
#     (42, 1),
#     (43, 1),
#     (44, 3),
#     (45, 1),
#     (46, 11),
#     (47, 1),
#     (48, 1),
#     (49, 1),
#     (50, 1),
#     (51, 8),
#     (52, 1),
#     (53, 19),
#     (54, 1),
#     (55, 1),
#     (56, 1),
#     (57, 1),
#     (58, 2)
#     ]

# column_names = []
# for question, num_answers in survey_structure:
#     for count in range(1, num_answers+1):
#         if num_answers == 1:
#             column_name = "Q_" + str(question)
#         else:
#             column_name = "Q_" + str(question) + "_" + str(count)
#         column_names.append(column_name)


column_names = [
    'Q_0',
    'Q_1',
    'Q_2',
    'Q_3',
    'Q_4',
    'Q_5',
    'Q_6',
    'Q_7_0',
    'Q_7',
    'Q_8',
    'Q_9',
    'Q_10',
    'Q_11',
    'Q_12',
    'Q_13',
    'Q_14',
    'Q_15_1',
    'Q_15_2',
    'Q_15_3',
    'Q_15_4',
    'Q_15_5',
    'Q_15_6',
    'Q_15_7',
    'Q_15_8',
    'Q_15_9',
    'Q_15_10',
    'Q_16',
    'Q_17_1',
    'Q_17_2',
    'Q_17_3',
    'Q_17_4',
    'Q_17_5',
    'Q_17_6',
    'Q_18',
    'Q_19',
    'Q_20',
    'Q_21',
    'Q_22',
    'Q_23',
    'Q_24',
    'Q_25',
    'Q_26',
    'Q_27',
    'Q_28',
    'Q_29_1',
    'Q_29_2',
    'Q_29_3',
    'Q_29_4',
    'Q_29_5',
    'Q_29_6',
    'Q_29_7',
    'Q_29_8',
    'Q_29_9',
    'Q_29_10',
    'Q_29_11',
    'Q_29_12',
    'Q_29_13',
    'Q_29_14',
    'Q_29_15',
    'Q_29_16',
    'Q_29_17',
    'Q_29_18',
    'Q_29_19',
    'Q_29_20',
    'Q_29_21',
    'Q_30_1',
    'Q_30_2',
    'Q_30_3',
    'Q_30_4',
    'Q_30_5',
    'Q_30_6',
    'Q_30_7',
    'Q_30_8',
    'Q_30_9',
    'Q_30_10',
    'Q_30_11',
    'Q_30_12',
    'Q_31',
    'Q_32_1',
    'Q_32_2',
    'Q_32_3',
    'Q_32_4',
    'Q_33',
    'Q_34',
    'Q_35',
    'Q_36',
    'Q_37',
    'Q_38',
    'Q_39',
    'Q_40',
    'Q_41',
    'Q_42',
    'Q_43',
    'Q_44_1',
    'Q_44_2',
    'Q_44_3',
    'Q_45',
    'Q_46_1',
    'Q_46_2',
    'Q_46_3',
    'Q_46_4',
    'Q_46_5',
    'Q_46_6',
    'Q_46_7',
    'Q_46_8',
    'Q_46_9',
    'Q_46_10',
    'Q_46_11',
    'Q_47',
    'Q_48',
    'Q_49',
    'Q_50',
    'Q_51_1',
    'Q_51_2',
    'Q_51_3',
    'Q_51_4',
    'Q_51_5',
    'Q_51_6',
    'Q_51_7',
    'Q_51_8',
    'Q_52',
    'Q_53_1',
    'Q_53_2',
    'Q_53_3',
    'Q_53_4',
    'Q_53_5',
    'Q_53_6',
    'Q_53_7',
    'Q_53_8',
    'Q_53_9',
    'Q_53_10',
    'Q_53_11',
    'Q_53_12',
    'Q_53_13',
    'Q_53_14',
    'Q_53_15',
    'Q_53_16',
    'Q_53_17',
    'Q_53_18',
    'Q_53_19',
    'Q_54',
    'Q_55',
    'Q_56',
    'Q_57',
    'Q_58_1',
    'Q_58_2'
    ]


def save_data(input_widgets):
    input_info = []
    for widgets in input_widgets:
        if type(widgets) == list:
            for widget in widgets:
                input_info.append(widget.get())
        else:
            input_info.append(widgets.get())

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

    except Exception as error:
        util.log('error', "Could not create an Excel file")
        util.log('error', str(error))
    finally:
        pass
        # root.quit()

def is_digit(input_string, action_type):
    if action_type == '1': #insert
        if not input_string.isdigit():
            return False
    return True


def entry_clicked(radio_var, entry):
    radio_var.set(0)
    entry.configure(state=tk.NORMAL)


def radio_button_question(frame_name, label_row, options, text, has_other=False):
    label = tk.Label(frame_name, text=text)
    label.grid(row=label_row, column=0, columnspan=3, padx=10, pady=30)
    variable = tk.IntVar(frame_name)
    for idx, option in enumerate(options):
        button = tk.Radiobutton(frame_name, text=option, value=idx+1, variable=variable)
        button.grid(row=label_row+idx+1, column=1, padx=10, pady=5, sticky="w") #####################

    if has_other:
        offset = len(options) + 1
        entry = tk.Entry(frame_name, width=100)
        entry.grid(row=label_row+offset+1, column=0, columnspan=3, padx=10, pady=15)
        entry.configure(state=tk.DISABLED)
        other_button = tk.Button(
            frame_name, text="   Бошқа    ",
            command=lambda: entry_clicked(variable, entry))
        other_button.grid(row=label_row+offset, column=1, sticky="w", pady=5)

        if variable.get() == 0 and entry.get() == "":
            return variable
        elif variable.get() == 0 and entry.get() != "":
            return entry
        elif variable.get() != 0:
            return variable
        else:
            raise ValueError("ValueError exception thrown")

    return variable

def checkbox_question(frame_name, label_row, options, text, has_other=False):
    results = []
    label = tk.Label(frame_name, text=text)
    label.grid(row=label_row, column=0, columnspan=3, padx=10, pady=30)
    offset = 1
    for idx, option in enumerate(options):
        result = tk.IntVar()
        check_box = tk.Checkbutton(frame_name, text=option, variable=result)
        check_box.grid(row=label_row+offset, column=1, padx=10, pady=5, sticky="w")
        results.append(result)
        offset += 1

    # taking care of 'Other'
    if has_other:
        entry = tk.Entry(frame_name, width=100)
        entry.grid(row=label_row+offset+1, column=0, columnspan=3, padx=10, pady=30)
        entry.configure(state=tk.DISABLED)
        button = tk.Button(
            frame_name, text="   Бошқа    ",
            command=lambda: entry.configure(state=tk.NORMAL))
        button.grid(row=label_row+offset, column=1, padx=10, pady=5, sticky="w")
        results.append(entry)
    return results

def inputting_questions(frame_name, label_row, num_options, text, has_difficult):
    results = []
    label = tk.Label(frame_name, text=text)
    label.grid(row=label_row, column=0, columnspan=3, padx=10, pady=30)
    for idx in range(1, num_options+1):
        entry = tk.Entry(frame_name, width=100)
        entry.grid(row=label_row+idx, column=0, columnspan=3, padx=10, pady=10)
        results.append(entry)

    if has_difficult:
        is_difficult = tk.IntVar()
        check_box = tk.Checkbutton(frame_name, text="Жавоб беришга қийналаман", variable=is_difficult)
        check_box.grid(row=label_row+num_options+1, column=1, padx=10, pady=5, sticky="w")
        results.append(is_difficult)
    return results
