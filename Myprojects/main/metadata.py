# main.py - Full GUI Application
import datetime
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
from PIL import Image as PilImage
from exif import Image as ExifImage
import json
import os
from typing import List

# === Custom Data Structure ===
class MetadataTag:
    def __init__(self, name: str, value, group: str):
        self.name = name
        self.value = str(value)[:100]  # truncate for display
        self.group = group

    def is_sensitive(self) -> bool:
        sensitive_groups = ["GPSInfo", "Image"]
        return any(g in self.group for g in sensitive_groups)

# === Core Logic ===
class MetadataExtractor:
    def extract(self, filepath: str) -> List[MetadataTag]:
        try:
            with open(filepath, "rb") as f:
                img = ExifImage(f)
            if not img.has_exif:
                return []
            tags = []
            for tag in img.list_all():
                try:
                    val = getattr(img, tag)
                    group = "GPSInfo" if "gps" in tag.lower() else "Exif" if any(x in tag.lower() for x in ["exif", "date"]) else "Image"
                    tags.append(MetadataTag(tag, val, group))
                except:
                    pass
            return tags
        except Exception as e:
            print(f"Error: {e}")
            return []

# === GUI Application ===
class ForensicsTool(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Network Forensics - Image Metadata Tool v1.0 by Sandip")
        self.geometry("1250x720")
        self.configure(bg="#0a0a0a")
        self.current_path = None
        self.tags = []

        # Styling
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background="#1e1e1e", foreground="#00ff9d", fieldbackground="#1e1e1e")
        style.configure("TButton", padding=6)

        # Title
        tk.Label(self, text="NETWORK FORENSICS IMAGE METADATA TOOL", bg="#0a0a0a", fg="#00ff9d", font=("Consolas", 16, "bold")).pack(pady=10)

        # Buttons frame
        btn_frame = tk.Frame(self, bg="#0a0a0a")
        btn_frame.pack(pady=5)
        ttk.Button(btn_frame, text="Select Single Image", command=self.load_single).grid(row=0, column=0, padx=5)
        ttk.Button(btn_frame, text="Select Folder (Batch)", command=self.load_folder).grid(row=0, column=1, padx=5)
        ttk.Button(btn_frame, text="Sanitize & Save Cleaned Image", command=self.sanitize).grid(row=0, column=2, padx=5)
        ttk.Button(btn_frame, text="Export JSON Report", command=self.export_report).grid(row=0, column=3, padx=5)

        # Table
        self.tree = ttk.Treeview(self, columns=("Tag", "Value", "Group"), show="headings", height=15)
        self.tree.heading("Tag", text="Tag")
        self.tree.heading("Value", text="Value")
        self.tree.heading("Group", text="Group")
        self.tree.column("Tag", width=250)
        self.tree.column("Value", width=400)
        self.tree.column("Group", width=150)
        self.tree.pack(pady=10, padx=20, fill="both", expand=True)

        # Risk panel
        self.risk_frame = tk.Frame(self, bg="#1e1e1e")
        self.risk_frame.pack(fill="x", padx=20, pady=5)
        self.risk_label = tk.Label(self.risk_frame, text="Risk Score: Not analysed", bg="#1e1e1e", fg="white", font=("Consolas", 12, "bold"))
        self.risk_label.pack(pady=8)

        # Log
        self.log = scrolledtext.ScrolledText(self, height=6, bg="#0a0a0a", fg="#00ff9d", font=("Consolas", 10))
        self.log.pack(fill="x", padx=20, pady=10)

        self.log.insert(tk.END, "Tool ready. Select an image to begin forensic analysis.\n")

    def log_message(self, msg):
        now = datetime.datetime.now().strftime('%H:%M:%S')
        self.log.insert(tk.END, f"[{now}] {msg}\n")
        self.log.see(tk.END)

    def load_single(self):
        path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.tif *.tiff")])
        if path:
            self.current_path = path
            self.process_image()

    def load_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.log_message(f"Batch processing folder: {folder}")
            # Simple batch demo - process first 5 images
            for file in os.listdir(folder)[:5]:
                if file.lower().endswith((".jpg", ".jpeg", ".tif", ".tiff")):
                    self.current_path = os.path.join(folder, file)
                    self.process_image()
                    break  # demo only

    def process_image(self):
        self.tree.delete(*self.tree.get_children())
        extractor = MetadataExtractor()
        self.tags = extractor.extract(self.current_path)
        for tag in self.tags:
            self.tree.insert("", "end", values=(tag.name, tag.value, tag.group))

        gps_present = any("gps" in t.name.lower() for t in self.tags)
        risk_text = "HIGH - Location leak possible (GPS detected)" if gps_present else "LOW - No immediate privacy risk"
        self.risk_label.config(text=f"Risk Score: {risk_text}", foreground="#ff4444" if gps_present else "#00ff9d")
        self.log_message(f"Extraction complete. {len(self.tags)} tags found from {os.path.basename(self.current_path)}")

    def sanitize(self):
        if not self.current_path or not self.tags:
            messagebox.showwarning("Warning", "No image loaded")
            return
        try:
            with open(self.current_path, "rb") as f:
                img = ExifImage(f)
            sensitive = ["gps_latitude", "gps_longitude", "gps_altitude", "make", "model", "serial", "software"]
            for tag in sensitive:
                if hasattr(img, tag):
                    delattr(img, tag)
            new_path = self.current_path.replace(".", "_SANITIZED.")
            with open(new_path, "wb") as f:
                f.write(img.get_file())
            messagebox.showinfo("Success", f"Cleaned image saved:\n{new_path}\nSensitive metadata removed.")
            self.log_message("Sanitisation completed - GPS and device info removed.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def export_report(self):
        if not self.tags:
            messagebox.showwarning("Warning", "No data to export")
            return
        data = {
            "filename": os.path.basename(self.current_path),
            "risk_level": self.risk_label.cget("text"),
            "extracted_at": datetime.datetime.now().isoformat(),
            "tags": [{"name": t.name, "value": t.value, "group": t.group} for t in self.tags]
        }
        save_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON", "*.json")])
        if save_path:
            with open(save_path, "w") as f:
                json.dump(data, f, indent=4)
            messagebox.showinfo("Exported", f"Forensic report saved:\n{save_path}")

if __name__ == "__main__":
    app = ForensicsTool()
    app.mainloop()