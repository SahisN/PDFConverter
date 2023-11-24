from tkinter import *
import customtkinter
from PIL import Image
from utility.messagebox import MessageBox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from utility.file_manager_handler import FileManagerHandler


class imageToPdf:
    def __init__(self, tab, height, width):
        self.file_paths = []
        self.tab = tab
        self.text_box = customtkinter.CTkTextbox(
            master=tab,
            state="disable",
            height=height - 200,
            width=width - 250,
        )
        self.text_box.pack()

        frame = customtkinter.CTkFrame(
            master=tab, width=width - 250, fg_color="transparent"
        )
        frame.pack()

        add_button = customtkinter.CTkButton(
            master=frame, text="Add Files", command=self.open_file
        )
        save_button = customtkinter.CTkButton(
            master=frame, text="Convert To PDF", command=self.save_file
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
        # only collects current selected file path
        current_file_paths = customtkinter.filedialog.askopenfiles(
            mode="r",
            filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")],
            defaultextension=".jpg",
        )

        # update file_path (collects all the file paths)
        self.file_paths.extend(current_file_paths)

        # update textbox
        self.text_box.configure(state="normal")
        for file_path in current_file_paths:
            self.text_box.insert(index=END, text=f"{file_path.name}\n")
        self.text_box.configure(state="disable")

    # clears file_paths array used to merge and save images
    def clear(self):
        self.text_box.configure(state="normal")
        self.file_paths.clear()
        self.text_box.delete("1.0", "end")
        self.text_box.configure(state="disable")

    def save_file(self):
        # if no image file are selected, prompt user to select a image file
        if not self.file_paths:
            MessageBox(
                master=self.tab, message="Atleast 1 image file needs to be selected"
            ).show_message()
            return

        # if there is atleast 1 image file,
        # then prompt user to select the location and file name
        save_path = customtkinter.filedialog.asksaveasfilename(
            defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf;")]
        )

        # if user press cancel, then show message
        if not save_path:
            MessageBox(self.tab, "File was not saved").show_dir_message()

        else:
            try:
                # Create a PDF document
                pdf_canvas = canvas.Canvas(save_path, pagesize=letter)

                # use for loop to iterate thru indivual image
                for image_path in self.file_paths:
                    # open the image using Pillow (PIL)
                    image = Image.open(image_path.name)

                    # Set the dimension of the PDF to match the current image
                    pdf_canvas.setPageSize((image.width, image.height))

                    # Draw the image on the PDF
                    pdf_canvas.drawInlineImage(
                        image, 0, 0, width=image.width, height=image.height
                    )

                    # Add a new page for the next image
                    pdf_canvas.showPage()

                # Save the pdf
                pdf_canvas.save()

                # notify user that file has been saved
                msg = MessageBox(
                    self.tab, message=f"Save Successful at {save_path}"
                ).success_message()

                print(save_path)

                # if user request to reveal the recently saved file
                if msg.get() == "Take me there":
                    FileManagerHandler(save_path)

            except:
                MessageBox(self.tab, message="Unable to write").error_message()
