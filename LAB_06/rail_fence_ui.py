import tkinter as tk
from tkinter import messagebox

# --- CÁC HÀM XỬ LÝ RAIL FENCE ---
def encryptRailFence(text, key):
    if key <= 1: return text
    rail = [''] * key
    row, direction = 0, 1
    for char in text:
        rail[row] += char
        if row == 0: direction = 1
        elif row == key - 1: direction = -1
        row += direction
    return ''.join(rail)

def decryptRailFence(cipher, key):
    if key <= 1: return cipher
    rail = [['\n' for _ in range(len(cipher))] for _ in range(key)]
    dir_down = None
    row, col = 0, 0
    # Đánh dấu vị trí
    for i in range(len(cipher)):
        if row == 0: dir_down = True
        if row == key - 1: dir_down = False
        rail[row][col] = '*'
        col += 1
        if dir_down: row += 1
        else: row -= 1
    # Điền ký tự vào
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1
    # Đọc kết quả
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0: dir_down = True
        if row == key - 1: dir_down = False
        if rail[row][col] != '*':
            result.append(rail[row][col])
            col += 1
        if dir_down: row += 1
        else: row -= 1
    return "".join(result)

# --- XỬ LÝ GIAO DIỆN (UI) ---
def handle_encrypt():
    text = txt_input.get("1.0", tk.END).strip()
    try:
        key = int(entry_key.get())
        encrypted = encryptRailFence(text, key)
        txt_output.delete("1.0", tk.END)
        txt_output.insert(tk.END, encrypted)
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập khóa (Key) là một số nguyên dương!")

def handle_decrypt():
    text = txt_input.get("1.0", tk.END).strip()
    try:
        key = int(entry_key.get())
        decrypted = decryptRailFence(text, key)
        txt_output.delete("1.0", tk.END)
        txt_output.insert(tk.END, decrypted)
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập khóa (Key) là một số nguyên dương!")

# --- TẠO CỬA SỔ WINDOWS ---
root = tk.Tk()
root.title("Rail Fence Cipher - Pham Van Nam")
root.geometry("450x350")

tk.Label(root, text="BÀI KIỂM TRA: RAIL FENCE CIPHER", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(root, text="Nhập văn bản (Plaintext/Ciphertext):").pack()
txt_input = tk.Text(root, height=4, width=50)
txt_input.pack(pady=5)

frame_key = tk.Frame(root)
frame_key.pack(pady=5)
tk.Label(frame_key, text="Khóa K (số dòng):").pack(side=tk.LEFT)
entry_key = tk.Entry(frame_key, width=10)
entry_key.pack(side=tk.LEFT, padx=5)

frame_btns = tk.Frame(root)
frame_btns.pack(pady=10)
tk.Button(frame_btns, text="Mã Hoá (Encrypt)", command=handle_encrypt, bg="lightblue").pack(side=tk.LEFT, padx=10)
tk.Button(frame_btns, text="Giải Mã (Decrypt)", command=handle_decrypt, bg="lightgreen").pack(side=tk.LEFT, padx=10)

tk.Label(root, text="Kết quả (Output):").pack()
txt_output = tk.Text(root, height=4, width=50)
txt_output.pack(pady=5)

root.mainloop()