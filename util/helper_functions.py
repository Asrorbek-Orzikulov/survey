import tkinter as tk
import util
import os
import xlsxwriter


def is_digit(input_string, action_type):
    if action_type == '1':  # insertion
        if not input_string.isdigit():
            return False
    return True


def is_cyrillic(input_string, action_type):
    if action_type == '1':
        if input_string not in util.ALPHABET:
            return False
    return True


def is_properly_filled(input_widgets):
    interviewer_id, mahalla_id, survey_id = input_widgets[0][0]
    if any(
        (len(interviewer_id.get()) != 4,
         len(mahalla_id.get()) != 2,
         len(survey_id.get()) != 2)
    ):
        return False

    # early stopping conditions
    if any(
        input_widgets[2][0].get() == 2,
        input_widgets[4][0].get() == 3,
        int(input_widgets[6][0].get()) < 18
    ):
        return True




def clear_data(input_widgets):
    for widgets, state in input_widgets:
        if isinstance(widgets, list):
            for widget in widgets:
                if isinstance(widget, tk.Entry) and state == "hidden":
                    widget.delete(0, tk.END)
                    widget.insert(0, "")
                    widget.configure(state=tk.DISABLED)
                elif isinstance(widget, tk.Entry):
                    widget.delete(0, tk.END)
                    widget.insert(0, "")
                elif isinstance(widget, tk.IntVar) or isinstance(widget, tk.Checkbutton):
                    widget.set(0)
                else:
                    raise ValueError(str(widget.get()) + str(type(widget)))
        elif isinstance(widgets, tk.IntVar):
            widgets.set(0)
        elif isinstance(widgets, tk.Entry):
            widgets.delete(0, tk.END)
            widgets.insert(0, "")
        else:
            raise ValueError(str(widgets.get()) + str(type(widgets)))


def save_data(input_widgets):
    if not is_properly_filled(input_widgets):
        return

    input_info = []
    for widgets, state in input_widgets:
        if isinstance(widgets, list):
            for widget in widgets:
                input_info.append(widget.get())
        else:
            input_info.append(widgets.get())

    if not os.path.isdir("Database"):
        os.mkdir("Database")

    try:
        os.chdir("Database")
        start_str = ""
        for entry in input_widgets[0][0]:
            start_str += entry.get() + "-"

        file_exists = True
        count = 0
        while file_exists:
            if os.path.isfile(start_str + f"{count}.xlsx"):
                count += 1
            else:
                name = start_str + f"{count}"
                file_exists = False

        with xlsxwriter.Workbook(f"{name}.xlsx") as workbook:
            worksheet = workbook.add_worksheet()
            worksheet.write_row(0, 0, util.COLUMN_NAMES)
            worksheet.write_row(1, 0, input_info)

        os.chdir("..")
    except Exception as error:
        util.log('error', str(error))


def entry_clicked(radio_var, entry):
    radio_var.set(0)
    entry.configure(state=tk.NORMAL)


def radio_button_question(frame_name, label_row, options, text, has_other=False):
    label = tk.Label(frame_name, text=text)
    label.grid(row=label_row, column=0, columnspan=3, padx=10, pady=30)
    label.config(font=("Arial", 12))
    variable = tk.IntVar(frame_name)
    for idx, option in enumerate(options):
        button = tk.Radiobutton(frame_name, text=option, value=idx+1, variable=variable)
        button.configure(font=("Arial", 12))
        button.grid(row=label_row+idx+1, column=1, padx=10, pady=5, sticky="w")

    if has_other:
        offset = len(options) + 1
        entry = tk.Entry(frame_name, width=100, validate="key")
        entry.configure(validatecommand=(entry.register(is_cyrillic),'%S','%d'))
        entry.grid(row=label_row+offset+1, column=0, columnspan=3, padx=10, pady=15)
        entry.configure(state=tk.DISABLED, font=("Arial", 12))
        other_button = tk.Button(
            frame_name, text="   Бошқа    ", font=("Arial", 12),
            command=lambda: entry_clicked(variable, entry))
        other_button.grid(row=label_row+offset, column=1, sticky="w", pady=5)
        return [variable, entry]

    return variable


def checkbox_question(frame_name, label_row, options, text, has_other=False):
    results = []
    label = tk.Label(frame_name, text=text)
    label.grid(row=label_row, column=0, columnspan=3, padx=10, pady=30)
    label.config(font=("Arial", 12))
    offset = 1
    for idx, option in enumerate(options):
        result = tk.IntVar()
        check_box = tk.Checkbutton(frame_name, text=option, variable=result, font=("Arial", 12))
        check_box.grid(row=label_row+offset, column=1, padx=10, pady=5, sticky="w")
        results.append(result)
        offset += 1

    # taking care of 'Other'
    if has_other:
        entry = tk.Entry(frame_name, width=100, validate="key", font=("Arial", 12))
        entry.configure(validatecommand=(entry.register(is_cyrillic),'%S','%d'))
        entry.grid(row=label_row+offset+1, column=0, columnspan=3, padx=10, pady=30)
        entry.configure(state=tk.DISABLED)
        button = tk.Button(
            frame_name, text="   Бошқа    ", font=("Arial", 12),
            command=lambda: entry.configure(state=tk.NORMAL))
        button.grid(row=label_row+offset, column=1, padx=10, pady=5, sticky="w")
        results.append(entry)
    return results


def inputting_questions(frame_name, label_row, num_options, text, has_difficult):
    results = []
    label = tk.Label(frame_name, text=text)
    label.grid(row=label_row, column=0, columnspan=3, padx=10, pady=30)
    label.config(font=("Arial", 12))
    for idx in range(1, num_options+1):
        entry = tk.Entry(frame_name, width=100, validate="key", font=("Arial", 12))
        entry.configure(validatecommand=(entry.register(is_cyrillic),'%S','%d'))
        entry.grid(row=label_row+idx, column=0, columnspan=3, padx=10, pady=10)
        results.append(entry)

    if has_difficult:
        is_difficult = tk.IntVar()
        check_box = tk.Checkbutton(frame_name, text="Жавоб беришга қийналаман", variable=is_difficult)
        check_box.configure(font=("Arial", 12))
        check_box.grid(row=label_row+num_options+1, column=1, padx=10, pady=5, sticky="w")
        results.append(is_difficult)
    return results
