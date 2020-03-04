import tkinter as tk
from functools import partial
import sys

def main():
    window = tk.Tk()
    window.title('Codenames Data Collector')
    window.geometry("1600x320")

    def close():
        window.destroy()
        sys.exit(0)

    window.protocol("WM_DELETE_WINDOW", close)

    var = tk.StringVar()

    try:
        current_count = len(open('data.txt').readlines())
    except FileNotFoundError:
        current_count = 0
        print('Thanks for doing this!')

    with open('data.txt', 'a+') as answers:
        with open('examples.txt', 'r') as examples:
            should_close = tk.BooleanVar()

            # write chosen clue to answers file when button is clicked
            def btn_click(i, item):
                answers.write(str(i - 1) + '.')
                answers.write(item.strip() + '\n')
                var.set(item.strip())

            def close_click():
                should_close.set(True)
                var.set("")

            def pass_click(i):
                answers.write(str(i - 1) + '.')
                answers.write('No good clues' + '\n')
                var.set(item.strip())

            i = 1
            for line in examples:
                if i <= current_count:
                    i += 1
                    pass
                else:
                    input_line = line.split('.')
                    full_list = input_line[1].strip('\n').split(',')
                    good = full_list[:3]
                    clues = full_list[4:]

                    top_frame = tk.Frame(window)
                    top_frame.pack()
                    bottom_frame = tk.Frame(window)
                    bottom_frame.pack(side='bottom')

                    tk.Button(top_frame, text='QUIT', fg='red', font=('Helvetica Bold', 16), padx=10, pady=10,
                              command=close_click).grid(row=1, column=0)

                    tk.Label(top_frame, text='Good words:', font=('Helvetica', 16)).grid(row=1, column=4)
                    tk.Label(top_frame, text=', '.join(good), fg='green', font=('Helvetica', 16)).grid(row=2, column=4)

                    e = tk.Entry(top_frame)
                    e.grid(row=3, column=4)

                    def entry(i):
                        answers.write(str(i - 1) + '.')
                        answers.write(e.get() + '\n')
                        var.set(e.get())

                    tk.Button(top_frame, text='Enter', fg='blue', font=('Helvetica Bold', 16), padx=10, pady=10,
                              command=entry(i)).grid(row=3, column=5)

                    #tk.Button(top_frame, text='PASS', fg='red', font=('Helvetica Bold', 16), padx=10, pady=10,
                    #           command=partial(pass_click, i)).grid(row=3, column=4)

                    clue_buttons = []
                    for i, item in enumerate(clues[:10]):
                        clue_buttons.append(tk.Button(bottom_frame, text=item, fg='blue', font=('Helvetica', 16),
                                                      padx=20, pady=10, command=partial(btn_click, i, item)))
                        clue_buttons[-1].grid(row=4, column=i)

                    clue_buttons_2 = []
                    for i, item in enumerate(clues[10:]):
                        clue_buttons_2.append(tk.Button(bottom_frame, text=item, fg='blue', font=('Helvetica', 16),
                                                        padx=20, pady=10, command=partial(btn_click, i, item)))
                        clue_buttons_2[-1].grid(row=5, column=i)

                    # wait for click
                    window.wait_variable(var)

                    if should_close.get():
                        break

                    # clear things out
                    top_frame.destroy()
                    bottom_frame.destroy()

                    i += 1

if __name__ == '__main__':
    main()