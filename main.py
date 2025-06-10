# main.py
import tkinter as tk
from port_scanner import show_port_scanner
from zip_brute_forcer import show_zip_cracker

def main():
    root = tk.Tk()
    root.title("Penetration Testing Toolkit")
    root.geometry("400x300")
    root.configure(bg="#1e1e2f")

    title = tk.Label(root, text="PenTest Toolkit", font=("Helvetica", 20, "bold"), fg="white", bg="#1e1e2f")
    title.pack(pady=25)

    tk.Button(root, text="Port Scanner", command=show_port_scanner,
              bg="#3498db", fg="white", activebackground="#2980b9",
              font=("Helvetica", 12, "bold"), width=25).pack(pady=10)

    tk.Button(root, text="ZIP Brute Forcer", command=show_zip_cracker,
              bg="#9b59b6", fg="white", activebackground="#8e44ad",
              font=("Helvetica", 12, "bold"), width=25).pack(pady=10)

    tk.Button(root, text="Exit", command=root.destroy,
              bg="#e74c3c", fg="white", activebackground="#c0392b",
              font=("Helvetica", 12, "bold"), width=25).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()

