import tkinter as tk
import random as rd
import string


def generate_password(length, no_of_passwords):
    passwords = []
    characters = string.ascii_letters + string.digits + string.punctuation
    for _ in range(no_of_passwords):
        password = ''.join(rd.choice(characters) for _ in range(length))
        passwords.append(password)
    return passwords


def generate_and_display_passwords(event=None):
    try:
        length = int(length_entry.get().strip())
        no_of_passwords = int(no_of_passwords_entry.get().strip())
        passwords = generate_password(length, no_of_passwords)
        password_text.config(state='normal')
        password_text.delete(1.0, tk.END)
        for password in passwords:
            password_text.insert(tk.END, password + '\n')
        password_text.config(state='disabled')
        errors.config(text="")
    except ValueError:
        errors.config(text="Please enter valid values for password length and number of passwords.")


def main():
    global length_entry, no_of_passwords_entry, password_text, errors
    window = tk.Tk()
    window.title("Password Generator")
    window.geometry("700x500")

    input_frame = tk.Frame(window)
    input_frame.pack(pady=20)

    length_label = tk.Label(input_frame, text="Enter Password Length:", font=("Consolas", 14))
    length_label.grid(row=0, column=0, padx=10)

    length_entry = tk.Entry(input_frame, width=10, font=("Consolas", 14))
    length_entry.grid(row=0, column=1, padx=10)
    length_entry.bind("<KeyRelease>", generate_and_display_passwords)

    no_of_passwords_label = tk.Label(input_frame, text="Number of Passwords:", font=("Consolas", 14))
    no_of_passwords_label.grid(row=1, column=0, padx=10)

    no_of_passwords_entry = tk.Entry(input_frame, width=10, font=("Consolas", 14))
    no_of_passwords_entry.grid(row=1, column=1, padx=10)
    no_of_passwords_entry.bind("<KeyRelease>", generate_and_display_passwords)

    display_frame = tk.Frame(window)
    display_frame.pack(pady=20)

    passwords_label = tk.Label(display_frame, text="Generated Passwords", font=("Consolas", 14))
    passwords_label.pack()

    password_text = tk.Text(display_frame, width=50, height=15, font=("Consolas", 12))
    password_text.pack()
    password_text.config(state='disabled')

    errors = tk.Label(display_frame, font=("Consolas", 12))
    errors.pack()

    window.mainloop()


if __name__ == "__main__":
    main()
