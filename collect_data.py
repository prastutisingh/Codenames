import tkinter as tk
from functools import partial

answers = open('data_1000_vocab.txt', 'w')

def btn_click(item):
    answers.write(item.strip() + '\n')

def main():
    window = tk.Tk()
    window.title('Codenames Data Collector')
    window.geometry("1200x320")

    file = open('examples_1000_vocab.txt', 'r')

    for line in file:
        full_list = line.strip('\n').split(',')
        good = full_list[:3]
        bad = full_list[3:9]
        clues = full_list[9:]

        top_frame = tk.Frame(window).pack()
        bottom_frame = tk.Frame(window).pack(side='bottom')

        tk.Label(top_frame, text='Good words:', font=('Helvetica', 16)).pack(pady=25)
        tk.Label(top_frame, text=', '.join(good), fg = 'green', font=('Helvetica', 16)).pack()
        tk.Label(top_frame, text='Bad words:', font=('Helvetica', 16)).pack(pady=25)
        tk.Label(top_frame, text=', '.join(bad), fg = 'red', font=('Helvetica', 16)).pack()

        clue_buttons = []
        for item in clues:
            clue_buttons.append(tk.Button(bottom_frame, text=item, fg='blue', font=('Helvetica', 16),
                                          padx=20, command=partial(btn_click, item))
                                .pack(side='left', padx=20))

    window.mainloop()

    file.close()
    answers.close()

if __name__ == '__main__':
    main()