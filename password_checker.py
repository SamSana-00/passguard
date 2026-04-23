import re
import math

def check_strength(password):
    # Common password blacklist
    common_passwords = [
        "password", "password123", "123456", "123456789", "qwerty",
        "abc123", "letmein", "monkey", "1234567", "dragon",
        "111111", "baseball", "iloveyou", "master", "sunshine",
        "ashley", "bailey", "passw0rd", "shadow", "superman",
        "michael", "football", "welcome", "admin", "login"
    ]
    
    if password.lower() in common_passwords:
        return 0, "COMPROMISED 💀", "instantly", [
            "This is one of the most common passwords in the world!",
            "Hackers try these first — change it immediately"
        ]
    score = 0
    feedback = []

    # Rule checks
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Too short — use at least 8 characters")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add at least one UPPERCASE letter")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter")

    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Add at least one number")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Add at least one special character (!@#$ etc)")

    # Strength label
    if score <= 2:
        strength = "WEAK 🔴"
    elif score == 3:
        strength = "MEDIUM 🟡"
    elif score == 4:
        strength = "STRONG 🟢"
    else:
        strength = "VERY STRONG 💪"

    # Crack time estimation
    charset = 0
    if re.search(r'[a-z]', password): charset += 26
    if re.search(r'[A-Z]', password): charset += 26
    if re.search(r'[0-9]', password): charset += 10
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password): charset += 32

    combinations = charset ** len(password)
    guesses_per_second = 1_000_000_000  # 1 billion guesses/sec
    seconds = combinations / guesses_per_second
    crack_time = format_crack_time(seconds)

    return score, strength, crack_time, feedback


def format_crack_time(seconds):
    if seconds < 1:
        return "instantly"
    elif seconds < 60:
        return f"{int(seconds)} seconds"
    elif seconds < 3600:
        return f"{int(seconds/60)} minutes"
    elif seconds < 86400:
        return f"{int(seconds/3600)} hours"
    elif seconds < 31536000:
        return f"{int(seconds/86400)} days"
    elif seconds < 3.154e+9:
        return f"{int(seconds/31536000)} years"
    else:
        return "centuries 🔒"


# --- Run it ---
import tkinter as tk

def update_display(*args):
    password = entry.get()
    score, strength, crack_time, feedback = check_strength(password)

    # Strength bar color
    colors = {0: "#e74c3c", 1: "#e74c3c", 2: "#e67e22", 
              3: "#f1c40f", 4: "#2ecc71", 5: "#27ae60"}
    color = colors.get(score, "#e74c3c")

    # Update strength bar width
    bar_width = max(10, (score / 5) * 380)
    canvas.coords(bar, 10, 5, bar_width, 30)
    canvas.itemconfig(bar, fill=color)

    # Update labels
    strength_label.config(text=f"Strength: {strength}", fg=color)
    crack_label.config(text=f"⏱ Crack time: {crack_time}")
    score_label.config(text=f"Score: {score}/5")

    # Update suggestions
    suggestions_text.config(state="normal")
    suggestions_text.delete("1.0", tk.END)
    if feedback:
        for tip in feedback:
            suggestions_text.insert(tk.END, f"→ {tip}\n")
    else:
        suggestions_text.insert(tk.END, "✅ Great password!")
    suggestions_text.config(state="disabled")

# --- Build the window ---
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("420x380")
root.configure(bg="#1e1e2e")
root.resizable(False, False)

# Title
tk.Label(root, text="🔐 Password Strength Checker",
         font=("Helvetica", 14, "bold"),
         bg="#1e1e2e", fg="white").pack(pady=15)

# Password entry
entry = tk.Entry(root, font=("Courier", 14), show="•",
                 width=28, bg="#2d2d44", fg="white",
                 insertbackground="white", relief="flat",
                 bd=8)
entry.pack(pady=5)
# Show/Hide toggle
def toggle_password():
    if entry.cget("show") == "•":
        entry.config(show="")
        toggle_btn.config(text="🙈 Hide")
    else:
        entry.config(show="•")
        toggle_btn.config(text="👁 Show")

toggle_btn = tk.Button(root, text="👁 Show", command=toggle_password,
                       bg="#2d2d44", fg="#aaaaaa",
                       relief="flat", font=("Helvetica", 9),
                       cursor="hand2")
toggle_btn.pack()
entry.bind("<KeyRelease>", update_display)

# Strength bar
canvas = tk.Canvas(root, width=400, height=40,
                   bg="#2d2d44", highlightthickness=0)
canvas.pack(pady=8)
bar = canvas.create_rectangle(10, 5, 10, 30, fill="#e74c3c", outline="")

# Labels
strength_label = tk.Label(root, text="Strength: —",
                           font=("Helvetica", 13, "bold"),
                           bg="#1e1e2e", fg="white")
strength_label.pack()

score_label = tk.Label(root, text="Score: 0/5",
                        font=("Helvetica", 10),
                        bg="#1e1e2e", fg="#aaaaaa")
score_label.pack()

crack_label = tk.Label(root, text="⏱ Crack time: —",
                        font=("Helvetica", 10),
                        bg="#1e1e2e", fg="#aaaaaa")
crack_label.pack(pady=3)

# Suggestions box
tk.Label(root, text="Suggestions:",
         font=("Helvetica", 10, "bold"),
         bg="#1e1e2e", fg="#aaaaaa").pack()

suggestions_text = tk.Text(root, height=5, width=46,
                            font=("Courier", 9),
                            bg="#2d2d44", fg="#f0f0f0",
                            relief="flat", bd=6,
                            state="disabled")
suggestions_text.pack(pady=5)

root.mainloop()