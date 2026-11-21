from tkinter import *
from tkinter import scrolledtext
from art import logo
import requests

THEME_COLOR = "#252321"
ACCENT_COLOR = "#353433"
TEXT_COLOR = "#D4D4D4"

current_font_size = 16
MIN_FONT_SIZE = 8
MAX_FONT_SIZE = 40


def zoom_in():
    global current_font_size
    if current_font_size < MAX_FONT_SIZE:
        current_font_size += 2
        lyrics_display.config(font=("Courier New", current_font_size))


def zoom_out():
    global current_font_size
    if current_font_size > MIN_FONT_SIZE:
        current_font_size -= 2
        lyrics_display.config(font=("Courier New", current_font_size))


def fetch_lyrics():
    artist_name = artist_entry.get().strip()
    title_name = title_entry.get().strip()

    # clear title entry
    title_entry.delete(0, END)

    # clear output
    lyrics_display.config(state=NORMAL)
    lyrics_display.delete("1.0", END)

    if not artist_name or not title_name:
        lyrics_display.insert(
            END, "Please enter both an artist name and a song title.")
        lyrics_display.config(state=DISABLED)
        return

    end_point = f"https://api.lyrics.ovh/v1/{artist_name}/{title_name}"
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.get(url=end_point, headers=headers, timeout=10)
        song_lyrics = response.json()

        if "lyrics" in song_lyrics:
            header = f"{title_name.title()} by {artist_name.title()}\n"
            divider = "---------------------------------------\n"
            lyrics_display.insert(
                END, header + divider + song_lyrics["lyrics"])
        else:
            lyrics_display.insert(
                END, f"Sorry, no lyrics found for '{title_name.title()}' by {artist_name.title()}.")

    except requests.exceptions.RequestException as e:
        lyrics_display.insert(
            END, f"Network error: Could not connect to the API.\n\nDetails: {e}")

    # lock the text box
    lyrics_display.config(state=DISABLED)


def clear_fields():
    artist_entry.delete(0, END)
    title_entry.delete(0, END)
    lyrics_display.config(state=NORMAL)
    lyrics_display.delete("1.0", END)
    lyrics_display.config(state=DISABLED)
    artist_entry.focus()


# ui setup
window = Tk()
window.title("Lyrify")
window.config(bg=THEME_COLOR, padx=25, pady=25)

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width - 650) // 2
y = (screen_height - 950) // 2

window.geometry(f"650x900+{x}+{y}")

# title header
title_label = Label(
    text=logo,
    font=("Courier New", 15, "bold"),
    justify="left",
    bg=THEME_COLOR,
    fg=TEXT_COLOR
)
title_label.grid(row=0, column=0, columnspan=2, pady=(0, 15))

# artist input
artist_label = Label(
    text="Artist Name:",
    font=("Courier New", 15),
    bg=THEME_COLOR,
    fg=TEXT_COLOR
)
artist_label.grid(row=1, column=0, sticky="w", pady=5)

artist_entry = Entry(width=35, font=("Courier New", 15))
artist_entry.grid(row=1, column=1, sticky="ew", pady=5, padx=(10, 0))
artist_entry.focus()

# song title input
title_label = Label(
    text="Song Title:",
    font=("Courier New", 15),
    bg=THEME_COLOR,
    fg=TEXT_COLOR
)
title_label.grid(row=2, column=0, sticky="w", pady=5)

title_entry = Entry(width=35, font=("Courier New", 15))
title_entry.grid(row=2, column=1, sticky="ew", pady=5, padx=(10, 0))

# buttons frame
button_frame = Frame(bg=THEME_COLOR)
button_frame.grid(row=3, column=0, columnspan=2, pady=15)

search_button = Button(
    button_frame,
    text="Get Lyrics",
    font=("Courier New", 14, "bold"),
    bg=ACCENT_COLOR,
    fg=TEXT_COLOR,
    width=12,
    command=fetch_lyrics
)
search_button.pack(side=LEFT, padx=5)

clear_button = Button(
    button_frame,
    text="Clear / New Search",
    font=("Courier New", 14, "bold"),
    bg=ACCENT_COLOR,
    fg=TEXT_COLOR,
    width=18,
    command=clear_fields
)
clear_button.pack(side=LEFT, padx=5)

zoom_out_button = Button(
    button_frame,
    text="-",
    font=("Courier New", 14, "bold"),
    bg=ACCENT_COLOR,
    fg=TEXT_COLOR,
    width=3,
    command=zoom_out
)
zoom_out_button.pack(side=LEFT, padx=5)

zoom_in_button = Button(
    button_frame,
    text="+",
    font=("Courier New", 14, "bold"),
    bg=ACCENT_COLOR,
    fg=TEXT_COLOR,
    width=3,
    command=zoom_in
)
zoom_in_button.pack(side=LEFT, padx=5)

# scrollable lyrics display text
lyrics_display = scrolledtext.ScrolledText(
    window,
    wrap=WORD,
    width=50,
    height=20,
    font=("Courier New", current_font_size),
    bg=ACCENT_COLOR,
    fg=TEXT_COLOR,
    padx=10,
    pady=10,
    state=DISABLED
)
lyrics_display.grid(row=4, column=0, columnspan=2, sticky="nsew")

# allow window resizing to expand the lyrics box smoothly
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(4, weight=1)

# keyboard shortcuts
window.bind("<Return>", lambda event: fetch_lyrics())
window.bind("<Control-plus>", lambda event: zoom_in())
# handles '+' without holding Shift
window.bind("<Control-equal>", lambda event: zoom_in())
window.bind("<Control-minus>", lambda event: zoom_out())

window.mainloop()
