import customtkinter
from PIL import Image
from utility.messagebox import MessageBox
from PyPDF2 import PdfFileMerger, PdfFileReader


class pdfToPdfs:
    def __init__(self, tab, height, width):
        self.file_paths = []
        self.tab = tab

        self.text_box = customtkinter.CTkTextbox(
            master=tab, height=height - 200, width=width - 250
        )
        self.text_box.pack()

        frame = customtkinter.CTkFrame(
            master=tab, width=width - 250, fg_color="transparent"
        )
        frame.pack()

        add_button = customtkinter.CTkButton(
            master=frame, text="Add PDF", command=self.open_file
        )
        save_button = customtkinter.CTkButton(
            master=frame, text="Merge PDF", command=self.save_file
        )

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
        current_file_paths = customtkinter.filedialog.askopenfiles(
            mode="r", filetypes=[("PDF Files", "*.pdf;")], defaultextension=".pdf"
        )

        # update file_path (total)
        self.file_paths.extend(current_file_paths)

        # update textbox
        for file_path in current_file_paths:
            self.text_box.insert(index=customtkinter.END, text=f"{file_path.name}\n")

    # clears file_paths array used to merge and save pdf
    def clear(self):
        self.file_paths.clear()
        self.text_box.delete("1.0", "end")

    def save_file(self):
        # if no files are selected, show no files selected message box
        if not self.file_paths or len(self.file_paths) < 2:
            MessageBox(self.tab, "Atleast 2 files need to be selected").show_message()
            return

        # if files are selected, ask user where to save the new file
        save_path = customtkinter.filedialog.asksaveasfilename(
            defaultextension=".pdf", filetypes=[("PDf Files", "*.pdf;")]
        )

        # if user doesn't select the directory
        if not save_path:
            MessageBox(self.tab, "File was not saved").show_dir_message()

        else:
            try:
                merger = PdfFileMerger()
                for pdf in self.file_paths:
                    merger.append(pdf.name)
                merger.write(save_path)
                MessageBox(self.tab, "Save Successful").success_message()

            except:
                MessageBox(self.tab, "Unable to write").error_message()
