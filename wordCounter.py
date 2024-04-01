import tkinter as tk

def wordCounter(sentence):
    flag = False
    w_count = 0
    for i in sentence:

        if i.isalnum() or i in ('-', '_'):
            if not flag:
                w_count += 1
                flag = True
        else:
            flag = False
    return w_count

def count_display(even =None):
    text = text_area.get("1.0", "end-1c")
    word_count = wordCounter(text)
    result.config(text=f"------Word Counter------\nWord Count : {word_count} Character Count : {len(text)}")

def clear():
    text_area.delete("1.0", "end")
    result.config(text="------Word Counter------\nEnter Your Text Below")

if __name__ == '__main__':
    window = tk.Tk()
    window.title("Word Counter")
    window.geometry("700x500")

    text_frame = tk.Frame(window, bd=2, relief=tk.SOLID, highlightbackground="blue", highlightthickness=1)
    text_frame.pack(pady=10)

    result = tk.Label(window, text="------Word Counter------\nEnter Your Text Below", font=("Consolas", 14))
    result.pack()

    text_area = tk.Text(window, wrap= "word", width= 55, height= 16, font=("Consolas", 14))
    text_area.pack(pady= 10)
    text_area.bind("<KeyRelease>", count_display)

    button = tk.Button(window, text="clear", font=("Consolas", 14), command=clear)
    button.pack()

    window.mainloop()