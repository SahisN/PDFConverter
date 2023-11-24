import os


def main():
    try:
        os.system("pip install customtkinter")
        os.system("pip install CTkMessagebox")
        os.system("pip install Pillow")
        os.system("pip install PyPDF2")
        os.system("pip install reportlab")
        os.system("pip install tk")
        print("All requirements are satisfied")
    except:
        print("Some requirements are not satisfied. Please check dependencies.txt")

    input("Press any button to continue...")


if __name__ == "__main__":
    main()
