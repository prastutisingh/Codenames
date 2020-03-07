import tkinter as tk
from functools import partial
import sys

def main():
    window = tk.Tk()
    window.title('Codenames Data Collector')
    window.geometry("1600x300")

    def close():
        window.destroy()
        sys.exit(0)

    window.protocol("WM_DELETE_WINDOW", close)

    var = tk.StringVar()
    entry_var = tk.StringVar()

    try:
        current_count = len(open('data.txt').readlines())
    except FileNotFoundError:
        current_count = 0
        print('Thanks for doing this!')

    with open('data.txt', 'a+') as answers:
        with open('examples.txt', 'r') as examples:
            should_close = tk.BooleanVar()

            # write chosen clue to answers file when button is clicked
            def btn_click(num, item):
                answers.write(num + '.')
                answers.write(item.strip() + '\n')
                var.set(item.strip())

            def close_click():
                should_close.set(True)
                var.set("")

            def entry(num, entry_var):
                answers.write(num + '.')
                answers.write(entry_var.get() + '\n')
                e.delete(0, 'end')
                var.set(entry_var.get())

            def pass_click(num):
                answers.write(num + '.')
                answers.write('No good clues' + '\n')
                var.set(item.strip())

            count = 1
            for line in examples:
                if count <= current_count:
                    count += 1
                    pass
                else:
                    input_line = line.split('.')
                    num = input_line[0]
                    full_list = input_line[1].strip('\n').split(',')
                    good = full_list[:2]
                    clues = full_list[2:]

                    top_frame = tk.Frame(window)
                    top_frame.pack()
                    bottom_frame = tk.Frame(window)
                    bottom_frame.pack(side='bottom')

                    # Quit button
                    tk.Button(top_frame, text='QUIT', fg='red3', font=('Helvetica Bold', 16), relief='raised',
                              padx=5, pady=5, command=close_click).grid(row=0, column=0, columnspan=1)

                    # Good words
                    tk.Label(top_frame, text='Good words:', font=('Helvetica', 16)).grid(row=1, column=4)
                    tk.Label(top_frame, text=', '.join(good), fg='forestgreen', font=('Helvetica', 16)).grid(row=2, column=4)

                    # Entry box
                    e = tk.Entry(top_frame, textvariable=entry_var)
                    e.grid(row=3, column=4, padx=5, pady=20)
                    tk.Button(top_frame, text='Enter', fg='DodgerBlue3', font=('Helvetica Bold', 16), relief='raised',
                              padx=10, pady=2, command=partial(entry, num, entry_var)).grid(row=3, column=5)

                    # Clue buttons
                    clue_buttons = []
                    for i, item in enumerate(clues[:5]):
                        clue_buttons.append(tk.Button(bottom_frame, text=item, fg='blue4', font=('Helvetica', 16),
                                                      padx=20, pady=8, command=partial(btn_click, num, item)))
                        clue_buttons[-1].grid(row=1, column=i)

                    clue_buttons_2 = []
                    for i, item in enumerate(clues[5:10]):
                        clue_buttons_2.append(tk.Button(bottom_frame, text=item, fg='blue4', font=('Helvetica', 16),
                                                        padx=20, pady=8, command=partial(btn_click, num, item)))
                        clue_buttons_2[-1].grid(row=2, column=i)

                    # Pass button
                    tk.Button(bottom_frame, text='PASS', fg='DodgerBlue3', font=('Helvetica Bold', 16), relief='raised',
                              padx=10, pady=5, command=partial(pass_click, num)).grid(row=4, column=4, columnspan=2)

                    # wait for click
                    window.wait_variable(var)

                    if should_close.get():
                        break

                    # clear things out
                    top_frame.destroy()
                    bottom_frame.destroy()

                    count += 1

if __name__ == '__main__':
    main()