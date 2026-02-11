import tkinter as tk
from tkinter import messagebox, filedialog
import random
import datetime
from threading import Thread
import time
from PIL import ImageGrab
import pygame

# -----------------------------
# Compatibility Logic
# -----------------------------
def calculate_compatibility(name1, name2, bday1, bday2):
    random.seed(name1 + name2)
    name_score = (sum(ord(c) for c in name1.lower()) + sum(ord(c) for c in name2.lower())) % 100
    bday_diff = abs((bday1 - bday2).days)
    date_factor = 100 - (bday_diff % 50)
    magic_factor = random.randint(60, 100)
    return int((name_score + date_factor + magic_factor) / 3)

def message_for_score(score):
    if score > 90:
        return "💞 Perfect match! You two are soulmates!"
    elif score > 75:
        return "❤️ Strong chemistry! Love is in the air."
    elif score > 60:
        return "💖 You’re great together! Keep that spark alive."
    elif score > 40:
        return "💫 Some ups and downs, but love always finds a way!"
    else:
        return "💔 Opposites attract... maybe 😉"

# -----------------------------
# Floating Hearts Animation
# -----------------------------
def float_hearts(canvas):
    hearts = []
    for _ in range(10):
        x = random.randint(0, 400)
        y = random.randint(300, 400)
        heart = canvas.create_text(x, y, text="❤️", font=("Arial", 14))
        hearts.append(heart)

    while True:
        for heart in hearts:
            canvas.move(heart, 0, -1)
            _, y = canvas.coords(heart)
            if y < -10:
                canvas.coords(heart, random.randint(0, 400), 400)
        time.sleep(0.05)

# -----------------------------
# Background Music
# -----------------------------
def play_music():
    pygame.mixer.init()
    try:
        pygame.mixer.music.load("love_song.mp3")
        pygame.mixer.music.play(-1)
    except:
        print("🎵 Music file not found (add love_song.mp3).")

# -----------------------------
# Screenshot Function
# -----------------------------
def save_result_as_image():
    x = root.winfo_rootx()
    y = root.winfo_rooty()
    w = root.winfo_width()
    h = root.winfo_height()
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png")])
    if file_path:
        ImageGrab.grab(bbox=(x, y, x + w, y + h)).save(file_path)
        messagebox.showinfo("Saved!", "💖 Screenshot saved successfully!")

# -----------------------------
# Main Love Calculator UI
# -----------------------------
def launch_main_screen():
    start_frame.destroy()

    # Title
    title = tk.Label(root, text="💞 Love Compatibility AI 💞", font=("Comic Sans MS", 18, "bold"), fg="#ff4d6d", bg="#fff0f5")
    title.pack(pady=10)

    # Canvas for floating hearts
    canvas = tk.Canvas(root, width=400, height=100, bg="#fff0f5", highlightthickness=0)
    canvas.pack()
    Thread(target=float_hearts, args=(canvas,), daemon=True).start()

    frame = tk.Frame(root, bg="#fff0f5")
    frame.pack(pady=20)

    # Inputs
    tk.Label(frame, text="Your Name:", font=("Arial", 12), bg="#fff0f5").grid(row=0, column=0, sticky="w", padx=5, pady=5)
    entry_name1 = tk.Entry(frame, width=25, font=("Arial", 12))
    entry_name1.grid(row=0, column=1, pady=5)

    tk.Label(frame, text="Your Birthday (YYYY-MM-DD):", font=("Arial", 12), bg="#fff0f5").grid(row=1, column=0, sticky="w", padx=5, pady=5)
    entry_bday1 = tk.Entry(frame, width=25, font=("Arial", 12))
    entry_bday1.grid(row=1, column=1, pady=5)

    tk.Label(frame, text="Partner's Name:", font=("Arial", 12), bg="#fff0f5").grid(row=2, column=0, sticky="w", padx=5, pady=5)
    entry_name2 = tk.Entry(frame, width=25, font=("Arial", 12))
    entry_name2.grid(row=2, column=1, pady=5)

    tk.Label(frame, text="Partner's Birthday (YYYY-MM-DD):", font=("Arial", 12), bg="#fff0f5").grid(row=3, column=0, sticky="w", padx=5, pady=5)
    entry_bday2 = tk.Entry(frame, width=25, font=("Arial", 12))
    entry_bday2.grid(row=3, column=1, pady=5)

    # Result labels
    result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#fff0f5", fg="#d63384")
    result_label.pack(pady=10)
    message_label = tk.Label(root, text="", font=("Arial", 12), bg="#fff0f5", wraplength=350, justify="center")
    message_label.pack(pady=5)

    # Calculate button
    def calculate_love():
        name1 = entry_name1.get().strip()
        name2 = entry_name2.get().strip()
        bday1 = entry_bday1.get().strip()
        bday2 = entry_bday2.get().strip()
        if not (name1 and name2 and bday1 and bday2):
            messagebox.showerror("Error", "Please fill in all fields!")
            return
        try:
            b1 = datetime.datetime.strptime(bday1, "%Y-%m-%d").date()
            b2 = datetime.datetime.strptime(bday2, "%Y-%m-%d").date()
        except ValueError:
            messagebox.showerror("Error", "Use YYYY-MM-DD for dates.")
            return
        score = calculate_compatibility(name1, name2, b1, b2)
        result_label.config(text=f"💌 Compatibility Score: {score}%")
        message_label.config(text=message_for_score(score))

    btn_calc = tk.Button(root, text="💖 Calculate Love 💖", font=("Arial", 14, "bold"), bg="#ff4d6d", fg="white",
                         padx=20, pady=10, borderwidth=0, command=calculate_love)
    btn_calc.pack(pady=15)

    btn_save = tk.Button(root, text="📸 Save Result as Image", font=("Arial", 11, "bold"), bg="#ff80a6", fg="white",
                         padx=10, pady=5, borderwidth=0, command=save_result_as_image)
    btn_save.pack(pady=5)

    footer = tk.Label(root, text="Created with ❤️ by You", font=("Arial", 10, "italic"), bg="#fff0f5", fg="#888")
    footer.pack(side="bottom", pady=5)

# -----------------------------
# Fade-In Animation
# -----------------------------
def fade_in(widget):
    for alpha in range(0, 100, 5):
        widget.attributes("-alpha", alpha / 100)
        time.sleep(0.05)

# -----------------------------
# Start Screen
# -----------------------------
def show_start_screen():
    global start_frame
    start_frame = tk.Frame(root, bg="#fff0f5")
    start_frame.pack(fill="both", expand=True)

    tk.Label(start_frame, text="💘 Love Compatibility AI 💘",
             font=("Comic Sans MS", 22, "bold"), fg="#ff4d6d", bg="#fff0f5").pack(pady=100)

    tk.Label(start_frame, text="Made with ❤️ by Motsamai for My Love 💞",
         font=("Arial", 12, "italic"), bg="#fff0f5", fg="#ff4d6d").pack(pady=10)

    tk.Label(start_frame, text="A fun romantic app to test your love 💞",
             font=("Arial", 12), bg="#fff0f5", fg="#555").pack(pady=10)

    btn_start = tk.Button(start_frame, text="Start ❤️", font=("Arial", 14, "bold"),
                          bg="#ff4d6d", fg="white", padx=20, pady=10, borderwidth=0,
                          command=lambda: Thread(target=fade_and_launch).start())
    btn_start.pack(pady=20)

def fade_and_launch():
    for i in range(100, 0, -5):
        root.attributes("-alpha", i / 100)
        time.sleep(0.03)
    launch_main_screen()
    for i in range(0, 100, 5):
        root.attributes("-alpha", i / 100)
        time.sleep(0.03)

# -----------------------------
# Main App Window
# -----------------------------
root = tk.Tk()
root.title("💘 Love Compatibility AI 💘")
root.geometry("430x560")
root.configure(bg="#fff0f5")
root.resizable(False, False)

Thread(target=play_music, daemon=True).start()
show_start_screen()
root.mainloop()
