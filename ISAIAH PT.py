from tkinter import Tk, Entry, Button, Label, StringVar

window = Tk()
window.geometry("500x300")
window.title("Emoji converter")

entry_txt = Entry(window, width=20)
entry_txt.pack(pady = 20)

result = StringVar()

result_label = Label(window, textvariable=result)
result_label.pack(pady = 20) 

emojis = {
    "happy": "😊",

    "sad": "😒",

    "excited": "😃",

    "tongue sticking out": "😛",

    "wink": "😉",

    "bored": "😐",

    "confused": "😕",

    "surprised": "😯",

    "cool": "😎",

    "angel": "😇",

    "love": "❤️",

    "angry": "😠",

    "in love": "😍",

    "shy": "😳",

    "laughing": "😂"

}




























search_btn = Button(window, text="Convert", command=lambda: search(entry_txt.get()))
search_btn.pack()

window2_btn = Button(window, text="Open converter", command=newWindow)
window2_btn.pack()

window.mainloop()
