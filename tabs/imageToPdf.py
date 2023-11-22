from tkinter import *
import customtkinter
from PIL import Image


class imageToPdf:
    def __init__(self, tab, height, width):
        self.text_box = customtkinter.CTkTextbox(
            master=tab,
            height=height - 200,
            width=width - 250,
        )
        self.text_box.pack()

        frame = customtkinter.CTkFrame(
            master=tab, width=width - 250, fg_color="transparent"
        )
        frame.pack()

        add_button = customtkinter.CTkButton(
            master=frame, text="Add File", command=self.open_file
        )
        save_button = customtkinter.CTkButton(master=frame, text="Convert To PDF")

        delete_img = customtkinter.CTkImage(
            dark_image=Image.open("./assets/trash.png"),
            size=(30, 30),
        )
        image_button = customtkinter.CTkButton(
            frame,
            image=delete_img,
            text="",
            width=30,
            height=30,
            hover_color="#78291a",
            command=self.clear,
        )

        add_button.place(x=80, y=15)
        save_button.place(x=230, y=15)
        image_button.place(x=405, y=10)

    def open_file(self):
        # self.text_box.insert(index=INSERT, text="hello\n")
        file_paths = customtkinter.filedialog.askopenfiles(
            mode="r",
            filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")],
            defaultextension=".jpg",
        )

        # update textbox
        for file_path in file_paths:
            self.text_box.insert(index=END, text=f"{file_path.name}\n")

    # clears file_paths array used to merge and save images
    def clear(self):
        # self.file_paths.clear()
        self.text_box.delete("1.0", "end")
