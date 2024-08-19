import re, pyperclip
import tkinter as tk


class Extractor:
    def __init__(self):
        self.matches = list()
        self.text = pyperclip.copy("")

    def extract_mobile_num(self, text):
        """Returns a list of mobile numbers (Philippine format)."""
        phoneRegex = re.compile(r"""(
            ((\()?(\+)?63(\))?|0)       # Country code
            (9\d{2})                    # Network provider code
            (\s|-|\.)?                  # Separator
            (\d{3})                     # Three mid numbers
            (\s|-|\.)?                  # Separator
            (\d{4})                     # Last four digits
            )""", re.VERBOSE)

        extracted_mobile_numbers = phoneRegex.findall(text)
        for num in extracted_mobile_numbers:
            if len(num[0]) >= 11:
                self.matches.append(num[0])

    def extract_email(self, text):
        """Returns a list of email addresses."""
        emailRegex = re.compile(r"""(
                [a-zA-Z0-9._%+-]+      # username
                @                      # @ symbol
                [a-zA-Z0-9.-]+         # domain name
                (\.[a-zA-Z]{2,4})      # dot-something
                )""", re.VERBOSE)

        extracted_emails = emailRegex.findall(text)
        for email in extracted_emails:
            self.matches.append(email[0])


def extract_from_clipboard():
    ex = Extractor()

    while not ex.text:
        ex.text = pyperclip.paste()

        if ex.text:
            ex.extract_mobile_num(ex.text)
            ex.extract_email(ex.text)

        if ex.matches:
            print("\nFound numbers/emails:\n")
            print("\n".join(ex.matches))
    return ex.matches


class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        self.root.title("Number/Email Extractor")

        # Main text body widget
        self.text = tk.Text(self.root, width=35 , height=20, background="white",)
        self.text.pack()

        # Button frame
        self.btn_frame = tk.Frame(self.root)
        self.btn_frame.pack()

        # Redo button
        self.redo_btn = tk.Button(self.btn_frame, text="Copy", command=self.redo)
        self.redo_btn.pack(side="left", padx=(0,5))

        # Clear button
        self.clear_btn = tk.Button(self.btn_frame, text="Clear", command=self.clear)
        self.clear_btn.pack(side="left")

        self.root.mainloop()


    def pop_up(self, matches):
        if matches:
            copied_text = '\n\n'.join(matches)
            self.text.insert(index=1.0, chars=copied_text)
            self.text.pack()

        else:
            print("No matches")

    def clear(self):
        self.text.delete(1.0, tk.END)
        self.text.pack()

    def redo(self):
        self.clear()
        self.pop_up(extract_from_clipboard())



if __name__ == "__main__":
    win = Window()


