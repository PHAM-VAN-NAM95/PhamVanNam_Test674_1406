import tkinter as tk
from tkinter import messagebox
import rsa

class RSAApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RSA Cipher - Pham Van Nam")
        self.root.geometry("500x500")

        self.public_key, self.private_key = None, None

        tk.Label(root, text="BÀI KIỂM TRA: MÃ HÓA RSA", font=("Arial", 14, "bold")).pack(pady=10)

        # Nút tạo khóa
        tk.Button(root, text="1. Tạo Khóa RSA (Generate Keys)", command=self.generate_keys, bg="yellow").pack(pady=5)

        tk.Label(root, text="Văn bản gốc (Plaintext):").pack()
        self.txt_input = tk.Text(root, height=3, width=50)
        self.txt_input.pack(pady=5)

        # Nút mã hóa
        tk.Button(root, text="2. Mã hóa (Encrypt)", command=self.encrypt_text, bg="lightblue").pack(pady=5)

        tk.Label(root, text="Văn bản mã hóa (Ciphertext - Hex):").pack()
        self.txt_cipher = tk.Text(root, height=4, width=50)
        self.txt_cipher.pack(pady=5)

        # Nút giải mã
        tk.Button(root, text="3. Giải mã (Decrypt)", command=self.decrypt_text, bg="lightgreen").pack(pady=5)

        tk.Label(root, text="Kết quả giải mã (Decrypted):").pack()
        self.txt_output = tk.Text(root, height=3, width=50)
        self.txt_output.pack(pady=5)

    def generate_keys(self):
        try:
            # Tạo cặp khóa 512-bit
            self.public_key, self.private_key = rsa.newkeys(512)
            messagebox.showinfo("Thành công", "Đã tạo cặp khóa RSA thành công!")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    def encrypt_text(self):
        if not self.public_key:
            messagebox.showwarning("Cảnh báo", "Vui lòng bấm 'Tạo Khóa RSA' trước!")
            return
        text = self.txt_input.get("1.0", tk.END).strip()
        if not text:
            return
        try:
            # Mã hóa và chuyển sang dạng Hex để dễ hiển thị trên UI
            ciphertext = rsa.encrypt(text.encode('utf-8'), self.public_key)
            self.txt_cipher.delete("1.0", tk.END)
            self.txt_cipher.insert(tk.END, ciphertext.hex())
        except Exception as e:
            messagebox.showerror("Lỗi mã hóa", str(e))

    def decrypt_text(self):
        if not self.private_key:
            messagebox.showwarning("Cảnh báo", "Chưa có khóa private để giải mã!")
            return
        hex_cipher = self.txt_cipher.get("1.0", tk.END).strip()
        if not hex_cipher:
            return
        try:
            # Chuyển từ Hex về Bytes và giải mã
            ciphertext = bytes.fromhex(hex_cipher)
            decrypted = rsa.decrypt(ciphertext, self.private_key)
            self.txt_output.delete("1.0", tk.END)
            self.txt_output.insert(tk.END, decrypted.decode('utf-8'))
        except Exception as e:
            messagebox.showerror("Lỗi giải mã", "Dữ liệu bị sai lệch!\n" + str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = RSAApp(root)
    root.mainloop()