# vim reimagined - by Jackson McDonald - v4!
# version 4 is the latest version of the project

import tkinter as tk
from tkinter import font  # for font selection
from tkinter import filedialog  # for saving the file
import time  # for getting the time for a time function
from tkinter import simpledialog, messagebox  # for finding / replacing words


# https://www.geeksforgeeks.org/python-gui-tkinter/ - list of useful tkinter tools

# version 4 - find and replace update is here!

# bold / italics were sadly removed in version 1 as they were deemed useless. RIP...
# pack() is responsible for putting the buttons / windows on the GUI

def fonts():
    # uses the systems fonts and stores it in this list
    # https://stackoverflow.com/questions/39614027/list-available-font-families-in-tkinter
    available_fonts = list(font.families())

    # new window for font selection
    font_window = tk.Toplevel(root)
    font_window.title("Font Selector")
    # size can be expanded if more buttons are added
    font_window.geometry("300x450")
    # store selected font
    selected_font = tk.StringVar()

    # title above button
    font_label = tk.Label(font_window, text="Select font")
    font_label.pack()
    font_dropdown = tk.OptionMenu(font_window, selected_font, *available_fonts, )  # * to format the list
    font_dropdown.pack()

    # fill the list with a range of numbers
    available_sizes = [str(i) for i in range(8, 31)]

    # store selected size
    selected_size = tk.StringVar()

    # title above button
    size_label = tk.Label(font_window, text="Select Size:")
    size_label.pack()
    # drop down displays sizes formatted
    size_dropdown = tk.OptionMenu(font_window, selected_size, *available_sizes)
    size_dropdown.pack()

    # fill list with these colors, more can be added later
    available_colors = ["green", "red", "blue", "yellow", "cyan", "magenta", "white", "black"]
    selected_color = tk.StringVar()  # store selected color
    color_label = tk.Label(font_window, text="Select Color:")
    color_label.pack()
    # drop down displays colors formatted
    color_dropdown = tk.OptionMenu(font_window, selected_color, *available_colors)
    color_dropdown.pack()

    # buttons within "Font"
    # all buttons padded with (pady=10)
    apply_font = tk.Button(font_window, text="Apply Font",
                           command=lambda: text_box.config(font=(selected_font.get() if selected_font.get()
                                                                 else "Times New Roman", selected_size.get()
                                                                 if selected_size.get() else 12)))  # set default values
    apply_font.pack(pady=10)

    resize_text = tk.Button(font_window, text="Apply Size",
                            command=lambda: text_box.config(font=(
                                selected_font.get() if selected_font.get() else "Times New Roman", (selected_size.get())
                                if selected_size.get() else 12)))  # set default values
    resize_text.pack(pady=10)
    apply_color = tk.Button(font_window, text="Apply Color",
                            command=lambda: text_box.config(
                                fg=selected_color.get() if selected_color.get() else "Black", font=(
                                    selected_font.get() if selected_font.get() else "Times New Roman",
                                    (selected_size.get())
                                    if selected_size.get() else 12,)))  # set default values
    apply_color.pack(pady=10)

    reset_button = tk.Button(font_window, text="Reset Settings",
                             command=lambda: text_box.config(insertbackground="black",
                                                             bg="white", fg="black", font=("Times New Roman", 12,)))
    # resets cursor color, background color, text color, font, and font size
    reset_button.pack(pady=10)

    dark_mode = tk.Button(font_window, text="Dark Mode",
                          command=lambda: text_box.config(
                              insertbackground=selected_color.get() if selected_color.get() else "white", bg="black",
                              fg=selected_color.get()
                              if selected_color.get() else "White", font=(
                                  selected_font.get() if selected_font.get() else "Times New Roman",
                                  (selected_size.get())
                                  if selected_size.get() else 12,)))  # set default values)
    dark_mode.pack(pady=10)

    light_mode = tk.Button(font_window, text="Light Mode",
                           command=lambda: text_box.config(
                               insertbackground=selected_color.get() if selected_color.get() else "black", bg="white",
                               fg=selected_color.get()
                               if selected_color.get() else "black", font=(
                                   selected_font.get() if selected_font.get() else "Times New Roman",
                                   (selected_size.get())
                                   if selected_size.get() else 12,)))  # set default values)
    light_mode.pack(pady=10)


def save_the_file():
    # thank you https://www.youtube.com/watch?v=Klp2Q462chU for file logic
    # open the file menu
    file = filedialog.asksaveasfile(defaultextension=".txt",  # set a default file extension.
                                    filetypes=[("Text Files", "*.txt")])
    # get all the user's text stored as a string
    file_text = str(text_box.get(1.0, tk.END))
    # write ot the file
    file.write(file_text)
    # close the file
    file.close()


def file_manager():
    font_window = tk.Toplevel(root)
    font_window.title("File Manager")
    font_window.geometry("300x300")

    # buttons with in "File"
    # save file, saves file if they already have a name, else prompt save as
    save_file = tk.Button(font_window, text="Save as", command=save_the_file)
    save_file.pack(pady=10)


def clock():
    # this function gets the time
    # a - weekday, b - month literal, d - day of month, I - hour in 12-hour format, M - minute,
    # p - AM / PM, Y - year
    text_box.insert(tk.INSERT,
                    time.strftime("%a %b %d %I:%M %p %Y "))  # insert is used to write directly to the textbox


def new_window():
    # currently this function is in demo
    # later it will open a new instance of the program
    new_root = tk.Toplevel(root)
    new_root.title("vim - New File")
    new_root.geometry("400x400")
    new_root.resizable(True, True)

    text_box2 = tk.Text(new_root)
    text_box2.config(font=("Times New Roman", 12))
    text_box2.pack(fill=tk.BOTH, expand=True)
    # remove this field when it is no longer a demo
    text_box2.insert(tk.INSERT, "This feature is currently a demo \n"
                                "it does not contain all features")


def find_word():
    find_words = simpledialog.askstring("Find", "Enter text to find:")
    if find_words:
        start_index = "1.0"
        found = False
        count = -1  # start count at -1 because it will increment when loop starts
        while True:
            # search the word in the text box
            start_index = text_box.search(find_words, start_index, stopindex=tk.END)
            count += 1
            if not start_index:
                break
            end_index = f"{start_index}+{len(find_words)}c"
            text_box.tag_add("highlight", start_index, end_index)
            # highlight the words yellow
            text_box.tag_configure("highlight", background="yellow")
            start_index = end_index
            found = True

        if not found:
            # when a word is not found replace is not prompted
            messagebox.showinfo("Not Found", f"'Cannot find {find_words}'.")
        else:
            # display the word that was found and how many instances were found
            messagebox.showinfo("Found", f"'{find_words} {count}' found.")
            replace_words = simpledialog.askstring("Replace", "Enter text to replace:")
            if find_words and replace_words:
                content = text_box.get('1.0', tk.END)  # get all text
                updated_content = content.replace(find_words, replace_words)
                text_box.delete('1.0', tk.END)  # delete text
                text_box.insert('1.0', updated_content)  # replace text with updated word
            # remove the highlight from the words
            text_box.tag_configure("highlight", background="")


root = tk.Tk()
root.title("vim")
root.geometry("400x400")  # notepad's dimensions - roughly
root.resizable(True, True)

button_frame = tk.Frame(root)  # frame for all top buttons
button_frame.pack(fill=tk.X, padx=10, pady=10)  # pack the button frame at the top buttons will be stored here

font_button = tk.Button(button_frame, text="Font", command=fonts)  # call the fonts function
font_button.pack(side=tk.LEFT, padx=5)  # place the button on the left side

file_button = tk.Button(button_frame, text="File", command=file_manager)  # call the file function
file_button.pack(side=tk.LEFT, padx=5)  # place the button on the left side

time_button = tk.Button(button_frame, text="Time", command=clock)  # call the file function
time_button.pack(side=tk.LEFT, padx=5)

plus_button = tk.Button(button_frame, text="+", command=new_window)
plus_button.pack(side=tk.LEFT, padx=5)

find_and_replace_label = tk.Button(button_frame, text="Find", command=find_word)
find_and_replace_label.pack(side=tk.LEFT, padx=5)

word_count_frame = tk.Frame(root)  # frame for word count label and char count label
word_count_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=5)  # pack the word count frame at the bottom

word_count_label = tk.Label(word_count_frame, text="Word count: 0", anchor="w")  # position this west
word_count_label.pack(fill=tk.X)

char_count_label = tk.Label(word_count_frame, text="Characters: 0", anchor="w")  # position this west
char_count_label.pack(fill=tk.X)

# while text box appears before word count label it has to be created after
# https://stackoverflow.com/questions/61171160/how-do-i-stop-text-from-cutting-off-in-the-tkinter-text-widget-in-python-3-7
# wrap=tk.WORD tabs words down instead of cutting them off if they exceed the box size
text_box = tk.Text(root, wrap=tk.WORD)
text_box.config(font=("Times New Roman", 12))  # default font and size if no fonds are applied
text_box.pack(fill=tk.BOTH, expand=True)  # pack the text box


def word_counter():
    data = text_box.get("1.0", tk.END)  # grab all the text in the text box
    words = data.split()  # split by whitespace
    word_count = len(words)
    char_count = len(data) - 1  # subtract one because data starts at 1
    word_count_label.config(text=f"{word_count} words")  # word count is written over the label
    char_count_label.config(text=f"{char_count} characters")


# current constraint of this is that the time function does not get counted
text_box.bind("<KeyRelease>", lambda event: word_counter())  # the even happens when user presses a key

root.mainloop()  # this runs the entire code

# project notes
# high priority
# words per minute counter

# low priority:
# add more file extensions for users



# ideas
# built in calculator would be nice
# highlighted font manipulation
