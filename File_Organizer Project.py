import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# --- FILE CATEGORIES ---
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z"],
    "Programs": [".exe", ".msi"],
    "Scripts": [".py", ".js", ".java", ".cpp", ".c"],
    "Others": []  # Anything not matching above goes here
}

def create_folder(path):
    """Create folder if it doesn't exist."""
    if not os.path.exists(path):
        os.makedirs(path)

def get_category(file_ext):
    """Return the category name based on file extension."""
    for category, extensions in FILE_TYPES.items():
        if file_ext.lower() in extensions:
            return category
    return "Others"

def organize_files(folder_path):
    """Organize files in the selected folder."""
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            category = get_category(ext)
            category_folder = os.path.join(folder_path, category)

            create_folder(category_folder)
            new_path = os.path.join(category_folder, filename)

            shutil.move(file_path, new_path)
            print(f"Moved: {filename} → {category}/")

def choose_folder():
    folder_path = filedialog.askdirectory(title="Select Folder to Organize")
    if folder_path:
        organize_files(folder_path)
        messagebox.showinfo("Success", "✅ Files have been organized successfully!")

# --- GUI SETUP ---
root = tk.Tk()
root.title("File Organizer")
root.geometry("350x200")
root.config(bg="#f4f4f4")

label = tk.Label(root, text="Select a folder to organize:", font=("Arial", 12), bg="#f4f4f4")
label.pack(pady=20)

btn = tk.Button(root, text="Choose Folder", command=choose_folder, font=("Arial", 12), bg="#4CAF50", fg="white", width=15)
btn.pack(pady=10)

root.mainloop()
