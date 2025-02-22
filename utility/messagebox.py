from CTkMessagebox import CTkMessagebox


class MessageBox:
    def __init__(
        self,
        master,
        message,
    ):
        self.master = master
        self.width = 400
        self.height = 200
        self.message = message

    # shows messagebox when files are not selected
    def show_message(self):
        CTkMessagebox(
            master=self.master,
            width=self.width,
            height=self.height,
            title="No files selected",
            message=self.message,
            option_1="OK",
        )

    # show messagebox when directory is not selected
    def show_dir_message(self):
        CTkMessagebox(
            master=self.master,
            width=self.width,
            height=self.height,
            title="Directory not selected",
            message=self.message,
            option_1="OK",
            icon="warning",
        )

    # shows when a save is successful
    def success_message(self):
        return CTkMessagebox(
            master=self.master,
            width=self.width,
            height=self.height,
            title="Save Successfull",
            message=self.message,
            option_1="OK",
            option_2="Take me there",
            icon="check",
        )

    # shows when save is failed
    def error_message(self):
        CTkMessagebox(
            master=self.master,
            width=self.width,
            height=self.height,
            title="Save Failed",
            message=self.message,
            option_1="OK",
            icon="cancel",
        )
