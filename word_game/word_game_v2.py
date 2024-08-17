import random
import requests
import tkinter as tk

### INITIALIZATION ###

url = "https://raw.githubusercontent.com/coleridge113/myProjects/main/word_game/words.txt"
page = requests.get(url)
words = []
word = ''
for char in page.text:
    if char.isalpha():
        word += char
    else:
        if word.isalpha():
            words.append(word)
        word = ''


def random_word():
    global WORD, KNOWN_WORDS
    WORD = random.choice(words)
    if WORD not in KNOWN_WORDS:
        return WORD
    else:
        return random_word()

KNOWN_WORDS = []
WORD = random_word()
#WORD = 'bears'
CORRECT_LETTERS = set(WORD)
GUESSED_LETTERS = set()

### END OF INITIALIZATION ###

### START OF BACKEND ###

def intro():
    print(f"\nHello {player_name}! Let's play a word-guessing game.")
    print("You can guess the letters of the word, and if you guess correctly, they will be displayed.\n")


def outro():
    print(f"\nThe word is '{WORD}'")
    print(f"Congratulations, {player_name}! You've completed the game.")


def display_word():
    word = ""
    for letter in WORD:
        if letter in GUESSED_LETTERS:
            #print(letter, end=" ")
            word += letter + " "*3
        else:
            #print("_", end=
            word += "_" + " "*3
    return word.rstrip()


def validate_input(letter):
    if letter in WORD and len(letter) == 1:
        GUESSED_LETTERS.add(letter)
        display_var.set(display_word())
    else:
        global lives
        lives -= 1
        lives_var.set(str(lives))

### END OF BACKEND ###

### START OF FRONTEND ###

root = tk.Tk()

# Window size settings
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root_width = 1000
root_height = 600
root.geometry(f"{root_width}x{root_height}+{int((screen_width/2)-(root_width/2))}+{int((screen_height/2)-(root_height/2))}") # Open window in middle of screen regardless of window size or monitor size
root.title("Word Game")

# Global settings
fontstyle = "Small Fonts"

# Top section
top_frame = tk.Frame(root)
top_frame.columnconfigure(index=(0,1), weight=1)
top_frame.rowconfigure(index=(0,1), weight=1)
top_frame.pack(fill="both")

# Player name section

player_name = tk.StringVar()
player_name_frame = tk.Frame(top_frame)
player_name_frame.grid(row=0, column=0, sticky="w")

tk.Label(player_name_frame, text="Player name: ", font=(fontstyle,12,)).pack(side="left")
player_name_entry = tk.Entry(player_name_frame, textvariable=player_name)
player_name_entry.pack(side="left")

def enter_name():
    if player_name.get().isalpha():
        player_name.set(player_name.get())
        hide()

def hide():
    player_name_entry.pack_forget()
    player_name_btn.pack_forget()
    player_name_label.pack(side="left")
    player_name_edit.pack(side="left", padx=(40,0))

def edit():
    player_name_label.pack_forget()
    player_name_entry.pack(side="left")
    player_name_btn.pack(side="left")
    player_name_edit.pack_forget()


player_name_btn = tk.Button(player_name_frame, text="Enter", command=enter_name)
player_name_btn.pack(side="left")
player_name_label = tk.Label(player_name_frame, textvariable=player_name, font=(fontstyle,12))
player_name_edit = tk.Button(player_name_frame, text="Edit", command=edit)

# Restart button
def restart():
    global KNOWN_WORDS, GUESSED_LETTERS, CORRECT_LETTERS, words, lives
    lives = 5
    lives_var.set(str(lives))

    words = KNOWN_WORDS
    KNOWN_WORDS = []
    print(KNOWN_WORDS)
    GUESSED_LETTERS = set()
    known_words_var.set(', '.join(KNOWN_WORDS))
    display_var.set(display_word())



restart_btn = tk.Button(top_frame, text="Restart", command=restart)
restart_btn.grid(row=0, column=1, sticky="ne")

# Lives section
lives_var = tk.StringVar()
lives = 5
lives_var.set(str(lives))
lives_frame = tk.Frame(top_frame)
lives_frame.grid(row=1, column=0, sticky="w")
lives_label= tk.Label(lives_frame, text="Lives: ", font=(fontstyle, 12))
lives_label.pack(side="left")
lives_count = tk.Label(lives_frame, textvariable=lives_var, font=(fontstyle,12))
lives_count.pack(side="left")


# Display section
display_var = tk.StringVar()
display_var.set(display_word())
tk.Label(root, textvariable=display_var, font=(fontstyle, 32, "bold",), borderwidth=1, relief="solid", bg="white").pack(padx=100, pady=(100,50), ipady=50, fill="both")


# Answer entry section
entry_var = tk.StringVar()
res_var = tk.StringVar()
entry_frame = tk.Frame(root, borderwidth=1, relief="solid", )
entry_frame.columnconfigure(index=(0,1), weight=1)
entry_frame.rowconfigure(index=0, weight=1)
entry_frame.pack()
entry = tk.Entry(entry_frame, textvariable=entry_var)
entry.grid(row=0, column=0,sticky='nsw')
entry.focus()
def submit(event=None):
    print("Get!")
    validate_input(entry_var.get())
    entry_var.set("")
    if lives <= 0 or CORRECT_LETTERS == GUESSED_LETTERS:
        if words == KNOWN_WORDS:
            restart()
        play_again()

tk.Button(entry_frame, text="Submit", command=submit).grid(row=0, column=1,)
#root.bind('<Enter>', submit)

# Reveal button section
nxt_rev_frame = tk.Frame(root)
nxt_rev_frame.pack(pady=(10,0))

def reveal():
    global CORRECT_LETTERS, GUESSED_LETTERS
    if CORRECT_LETTERS == GUESSED_LETTERS:
        play_again()
    for letter in CORRECT_LETTERS:
        if letter not in GUESSED_LETTERS:
            GUESSED_LETTERS.add(letter)
            print(GUESSED_LETTERS)
            print(f"'{letter}' added!")
            display_var.set(display_word())
            break
        else:
            print("None to add")
tk.Button(nxt_rev_frame, text="Reveal", command=reveal).pack(side="left", padx=(0,5))


# Play again section

def play_again():
    global WORD, CORRECT_LETTERS, GUESSED_LETTERS, lives
    lives = 5
    lives_var.set(str(lives))
    KNOWN_WORDS.append(WORD)
    known_words_var.set(', '.join(KNOWN_WORDS))
    if len(words) != len(KNOWN_WORDS):
        WORD = random_word()
        CORRECT_LETTERS = set(WORD)
        GUESSED_LETTERS = set()
        display_var.set(display_word())
    else:
        print("No more words!")
        restart()

next_word_btn = tk.Button(nxt_rev_frame, text="Next Word", command=play_again)
next_word_btn.pack(side="left")


# Known words section
known_words_var = tk.StringVar()
known_frame = tk.Frame(root)
known_frame.pack(pady=(60,0))
tk.Label(known_frame, textvariable=known_words_var, font=(fontstyle,12)).pack()





### END OF FRONTEND ###


if __name__ == "__main__":
    root.mainloop()

