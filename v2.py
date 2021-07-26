# v2.1 - Scramble during input.
# v2.2 - minor cosmetic changes
import tkinter as tk
from tkinter.scrolledtext import ScrolledText


def scrambler(user_input):
    counter = 0
    lst = []
    # Alternate between small and big letters, skipping non-alphabetic characters.
    for character in user_input:
        if not character.isalpha():
            lst.append(character)
            continue
        if counter % 2 == 0:
            counter += 1
            lst.append(character.lower())
        else:
            counter += 1
            lst.append(character.upper())

    return ''.join(lst)


def get_stringvar(event):
    # Get text from txt1, scramble and return result to txt2.
    SV.set(scroll_txt1.get("1.0", tk.END))
    scroll_txt2.replace("1.0", tk.END, scrambler(SV.get()))


# Window
window = tk.Tk()
window.title('Spongebob mock generator v2.2')
window.geometry('550x550')
window.resizable(False, False)
window.configure(bg='#333333')
# Write Label
lbl = tk.Label(window, text='Write here:', bg='#333333', fg='white')
lbl.pack()
SV = tk.StringVar()
# Scr.txt1
scroll_txt1 = ScrolledText(window, height=10, bg='#777777', fg='white')
scroll_txt1.pack()
scroll_txt1.bind('<KeyRelease>', get_stringvar)
# copy label
lbl2 = tk.Label(window, text=scrambler('copy here:'), bg='#333333', fg='yellow')
lbl2.pack()
# Scr.txt2
scroll_txt2 = ScrolledText(window, height=10, bg='#777777', fg='yellow1')
scroll_txt2.pack()
# # Image
# sponge_image = tk.PhotoImage(file=(file_path)) #replace (file_path) with image path.
# lbl3 = tk.Label(image=sponge_image, bg='#333333')
# lbl3.pack()
window.mainloop()
