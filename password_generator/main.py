from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    is_okay = messagebox.askokcancel(title=website, message=f"These are the entered data:"
                                                            f"\nEmail: {email}"
                                                            f"\nPassword: {password}"
                                                            f"\nDo you want to save?")

    if is_okay:
        with open("saved_passwords.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=35, pady=35)

canvas = Canvas(width=300, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
entries_width = 35
website_entry = Entry(width=entries_width)
website_entry.grid(row=1, column=1, columnspan=2)
email_entry = Entry(width=entries_width)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "Matasem.h97@gmail.com")
password_entry = Entry(width=entries_width)
password_entry.grid(row=3, column=1, columnspan=2)

# Buttons
buttons_width = 30
generate_password_button = Button(text="Generate Password", width=buttons_width)
generate_password_button.grid(row=4, column=1)
add_button = Button(text="Add", width=buttons_width, command=save)
add_button.grid(row=5, column=1, columnspan=2)

window.mainloop()
