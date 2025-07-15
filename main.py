import tkinter as tk
from chambre_renderer import render_chambre

def launch_app():
    render_chambre()

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Optimiseur de chambre")
    root.geometry("300x200")

    label = tk.Label(root, text="Optimisation des meubles")
    label.pack(pady=10)

    btn = tk.Button(root, text="Placer automatiquement", command=launch_app)
    btn.pack(pady=20)

    root.mainloop()
