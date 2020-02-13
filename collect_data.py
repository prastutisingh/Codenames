import tkinter as tk
from functools import partial
import sys

def main():
    window = tk.Tk()
    window.title('Codenames Data Collector')
    window.geometry("1200x320")

    def close():
        window.destroy()
        sys.exit(0)

    window.protocol("WM_DELETE_WINDOW", close)

    var = tk.StringVar()

    try:
        current_count = len(open('data_1000_vocab.txt').readlines())
    except FileNotFoundError:
        current_count = 0
        print('Thanks for doing this!')

    with open('data_1000_vocab.txt', 'a+') as answers:
        with open('examples_1000_vocab.txt', 'r') as examples:
            should_close = tk.BooleanVar()

            # write chosen clue to answers file when button is clicked
            def btn_click(i, item):
                answers.write(str(i - 1) + '.')
                answers.write(item.strip() + '\n')
                var.set(item.strip())

            def close_click():
                should_close.set(True)
                var.set("")

            i = 1
            for line in examples:
                if i <= current_count:
                    i += 1
                    pass
                else:
                    input_line = line.split('.')
                    full_list = input_line[1].strip('\n').split(',')
                    good = full_list[:3]
                    bad = full_list[3:9]
                    clues = full_list[9:]

                    top_frame = tk.Frame(window)
                    top_frame.pack()
                    bottom_frame = tk.Frame(window)
                    bottom_frame.pack(side='bottom')

                    tk.Button(top_frame, text='QUIT', fg='red', font=('Helvetica Bold', 16), padx=10, pady=10,
                              command=close_click).pack(side='left', padx=10, pady=25)

                    tk.Label(top_frame, text='Good words:', font=('Helvetica', 16)).pack(pady=25)
                    tk.Label(top_frame, text=', '.join(good), fg='green', font=('Helvetica', 16)).pack()
                    tk.Label(top_frame, text='Bad words:', font=('Helvetica', 16)).pack(pady=25)
                    tk.Label(top_frame, text=', '.join(bad), fg='red', font=('Helvetica', 16)).pack()

                    clue_buttons = []
                    for item in clues:
                        clue_buttons.append(tk.Button(bottom_frame, text=item, fg='blue', font=('Helvetica', 16),
                                                      padx=20, pady=10, command=partial(btn_click, i, item)))
                        clue_buttons[-1].pack(side='left', padx=20, pady=20)

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