# zip_brute_forcer.py
import zipfile
import tkinter as tk
from tkinter import filedialog, scrolledtext

def brute_force_zip(zip_path, wordlist_path, output):
    output.delete(1.0, tk.END)
    output.insert(tk.END, f"Starting brute-force...\n")
    try:
        with zipfile.ZipFile(zip_path, 'r') as zf:
            with open(wordlist_path, 'r') as file:
                for line in file:
                    password = line.strip()
                    output.insert(tk.END, f"Trying: {password}\n")
                    try:
                        zf.extractall(pwd=bytes(password, 'utf-8'))
                        output.insert(tk.END, f"\nPassword found: {password}\n")
                        return
                    except:
                        continue
            output.insert(tk.END, "\nPassword not found in wordlist.\n")
    except Exception as e:
        output.insert(tk.END, f"[ERROR] {str(e)}")

def show_zip_cracker():
    window = tk.Toplevel()
    window.title("ZIP Brute Forcer")
    window.geometry("600x500")
    window.configure(bg="#2d3436")

    zip_path = tk.StringVar()
    wordlist_path = tk.StringVar()

    tk.Label(window, text="Select ZIP File:", bg="#2d3436", fg="white", font=("Helvetica", 12)).pack(pady=3)
    tk.Entry(window, textvariable=zip_path, width=50).pack(pady=3)
    tk.Button(window, text="Browse ZIP", command=lambda: zip_path.set(filedialog.askopenfilename(filetypes=[("ZIP files", "*.zip")])),
              bg="#f39c12", fg="white", activebackground="#d68910",
              font=("Helvetica", 10, "bold")).pack(pady=3)

    tk.Label(window, text="Select Wordlist File:", bg="#2d3436", fg="white", font=("Helvetica", 12)).pack(pady=3)
    tk.Entry(window, textvariable=wordlist_path, width=50).pack(pady=3)
    tk.Button(window, text="Browse Wordlist", command=lambda: wordlist_path.set(filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])),
              bg="#e67e22", fg="white", activebackground="#ca6f1e",
              font=("Helvetica", 10, "bold")).pack(pady=3)

    output = scrolledtext.ScrolledText(window, width=70, height=15, font=("Consolas", 10))
    output.pack(pady=10)

    tk.Button(window, text="Start Brute Force", command=lambda: brute_force_zip(zip_path.get(), wordlist_path.get(), output),
              bg="#27ae60", fg="white", activebackground="#1e8449",
              font=("Helvetica", 12, "bold")).pack(pady=5)
