import tkinter as tk
import util
import os
import xlsxwriter

def save_data():
    column_names = ["Name", "Lives in Region", "District/City Name",
                    "District or City", "Gender", "Age"]
    # input_widgets = [entry_1, region, entry_3, place, gender, entry_6]
    # input_info = [widget.get() for widget in input_widgets]

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

def is_digit(input_string, action_type):
    if action_type == '1': #insert
        if not input_string.isdigit():
            return False
    return True

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
            command=lambda: entry.configure(state=tk.NORMAL))
        other_button.grid(row=label_row+offset, column=1, sticky="w", pady=5)
        return entry

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
