# 🔐 PassGuard — Password Strength Checker

A cybersecurity tool that analyzes password strength in real time, estimates crack time, and generates secure passwords.

🔗 **Live Demo**: [your-username.github.io/passguard](https://your-username.github.io/passguard)

---

## Features

- **Real-time strength analysis** — live color bar updates as you type
- **Crack time estimation** — shows how long it would take to brute-force your password
- **Common password blacklist** — flags the top 25 most-used passwords instantly
- **Smart suggestions** — tells you exactly what to improve
- **Password generator** — customizable length, uppercase, lowercase, numbers, symbols
- **Show/Hide toggle** — for safe input
- **100% client-side** — no password is ever sent to a server

---

## Screenshots

> *(Add screenshots of your app here after deploying)*

---

## How It Works

The strength scoring is based on 5 rules:
1. Length ≥ 8 characters
2. Length ≥ 12 characters (bonus)
3. Contains uppercase letters (A-Z)
4. Contains numbers (0-9)
5. Contains special characters (!@#$ etc.)

Crack time is estimated using:
```
combinations = charset_size ^ password_length
crack_time   = combinations / 1,000,000,000 (guesses per second)
```

---

## Tech Stack

- Python (core logic — `password_checker.py`)
- HTML / CSS / Vanilla JavaScript (web interface)
- Tkinter (desktop GUI version)

---

## Files

| File | Description |
|------|-------------|
| `index.html` | Web version — deploy this on GitHub Pages |
| `password_checker.py` | Python terminal + GUI version |
| `README.md` | This file |

---

## How to Run Locally

**Web version:**
Just open `index.html` in any browser. No installation needed.

**Python version:**
```bash
python password_checker.py
```

---

## Deploying to GitHub Pages (Free Hosting)

1. Create a new repository on GitHub named `passguard`
2. Upload `index.html` and `README.md`
3. Go to **Settings → Pages**
4. Under Source, select **main branch → / (root)**
5. Click Save — your site will be live at `https://your-username.github.io/passguard`

---

## What I Learned

- Password security fundamentals (entropy, charset size, brute-force estimation)
- Python scripting with `re` and `tkinter`
- Building real-time interactive web tools with vanilla JavaScript
- Cybersecurity concepts from IBM SkillsBuild program

---

## Certificate

This project was built as part of the **IBM SkillsBuild Cybersecurity Fundamentals** course, completed on March 25, 2026.

Verified badge: [View on Credly](https://www.credly.com/badges/815628ec-7e81-48d5-b2b6-95f19ca15c34)

---

## Author

**Samreen Sana**  
Sree Chaitanya College of Engineering, Karimnagar, Telangana  
[LinkedIn](https://linkedin.com/in/your-profile) · [GitHub](https://github.com/your-username)

---

*Built with curiosity and a lot of Ctrl+Z.*
