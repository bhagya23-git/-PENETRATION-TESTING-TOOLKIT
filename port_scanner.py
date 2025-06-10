# port_scanner.py
import socket
import tkinter as tk
from tkinter import scrolledtext

def scan_ports(target, output):
    output.delete(1.0, tk.END)
    output.insert(tk.END, f"Scanning {target}...\n")
    ports = [21, 22, 23, 80, 443, 3306, 8080]
    open_count = 0

    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                output.insert(tk.END, f"Port {port} is OPEN\n")
                open_count += 1
            sock.close()
        except Exception as e:
            output.insert(tk.END, f"Error on port {port}: {e}\n")

    output.insert(tk.END, f"\nScan complete. {open_count} open ports found.\n")

def show_port_scanner():
    window = tk.Toplevel()
    window.title("Port Scanner")
    window.geometry("500x400")
    window.configure(bg="#2d3436")

    tk.Label(window, text="Enter Target IP:", bg="#2d3436", fg="white", font=("Helvetica", 12)).pack(pady=5)
    ip_entry = tk.Entry(window, width=40, font=("Helvetica", 12))
    ip_entry.pack(pady=5)

    output = scrolledtext.ScrolledText(window, width=60, height=15, font=("Consolas", 10))
    output.pack(pady=10)

    tk.Button(window, text="Start Scan", command=lambda: scan_ports_gui(ip_entry.get(), output),
              bg="#27ae60", fg="white", activebackground="#1e8449",
              font=("Helvetica", 12, "bold")).pack(pady=5)
