import tkinter as tk
import os
from scss import Compiler

class ScssCompilerNotification:
    def __init__(self, root):
        self.root = root
        self.root.title("SCSS Compiler")
        
        self.notify_label = tk.Label(root, text="")
        self.notify_label.pack(pady=10)
        
        self.compile_btn = tk.Button(root, text="Compile SCSS", command=self.compile_scss)
        self.compile_btn.pack(pady=10)
    
        self.scss_dir = 'scss'  # Use the directory containing your SCSS files
        self.css_dir = 'css'    # Use the directory where you want to output the compiled CSS
    
    def compile_scss(self):
        for scss_file_name in os.listdir(self.scss_dir):
            if scss_file_name.endswith('.scss'):
                scss_file_path = os.path.join(self.scss_dir, scss_file_name)
                css_file_name = scss_file_name.replace('.scss', '.css')  # Fix the method name and replace '.scss' with '.css'
                css_file_path = os.path.join(self.css_dir, css_file_name)
            
                with open(scss_file_path, 'r') as scss_file:
                    scss_code = scss_file.read()
                    
                compiler = Compiler()
                css_code = compiler.compile_string(scss_code)
                
                with open(css_file_path, 'w') as css_file:  # Use 'w' to write, not 'r'
                    css_file.write(css_code)
                    
                self.show_notification(f"Successfully compiled {scss_file_path} to {css_file_path}")
                
    def show_notification(self, message):
        self.notify_label.config(text=message)
        self.root.after(3000, self.clear_notification)
        
    def clear_notification(self):
        self.notify_label.config(text='')

if __name__ == '__main__':
    root = tk.Tk()
    notification_app = ScssCompilerNotification(root)
    root.mainloop()