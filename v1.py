import tkinter as tk
import tkinter.ttk as ttk


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


class TextScrollCombo(tk.Frame):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

    # ensure a consistent GUI size
        self.grid_propagate(False)
    # implement stretchability
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    # create a Text widget
        self.txt = tk.Text(self, wrap=tk.WORD)
        self.txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

    # create a Scrollbar and associate it with txt
        scrollb = tk.Scrollbar(self, command=self.txt.yview)
        scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = scrollb.set


# window
main_window = tk.Tk()
main_window.title('Spongebob mock generator')
main_window.config(bg='#444444')

# Text + Scrollbar combo
combo = TextScrollCombo(main_window)
combo.pack(fill="both", expand=True, side=tk.BOTTOM)
combo.config(width=400, height=300)
combo.txt.config(font=("consolas", 10), undo=True, wrap='word', bg='black', fg='white')
combo.txt.config(borderwidth=3, relief="sunken", insertbackground='white')


def entry_focus_in(*args):
    if user_entry.get() == default_entry_text:
        textEntry.set('')
        user_entry.configure(fg='white')


def entry_focus_out(*args):
    if user_entry.get() == '':
        textEntry.set(default_entry_text)
        user_entry.configure(fg='#777777')


# Text Entry
default_entry_text = 'Enter text here...'
textEntry = tk.StringVar()
textEntry.set(default_entry_text)
user_entry = tk.Entry(main_window, width=50, bg='black', fg='#777777', insertbackground='white', textvariable=textEntry)
user_entry.pack(side=tk.TOP)
user_entry.bind("<FocusIn>", entry_focus_in)
user_entry.bind("<FocusOut>", entry_focus_out)


def generate_button_clicked():
    # scramble Entry and insert to text widget
    if user_entry.get() == '':
        return
    combo.txt.insert(tk.INSERT, (scrambler(user_entry.get())))
    combo.txt.insert(tk.INSERT, '\n')


# Button
generate_button = tk.Button(main_window, text='Generate', command=generate_button_clicked, bg='black', fg='white')
generate_button.pack(side=tk.TOP, pady=5)

# Style
style = ttk.Style()
style.theme_use('clam')


main_window.mainloop()
