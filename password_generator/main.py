from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
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
password_entry = Entry(width=entries_width)
password_entry.grid(row=3, column=1, columnspan=2)

# Buttons
buttons_width = 30
generate_password_button = Button(text="Generate Password", width=buttons_width)
generate_password_button.grid(row=4, column=1)
add_button = Button(text="Add", width=buttons_width)
add_button.grid(row=5, column=1, columnspan=2)


window.mainloop()
