import tkinter as tk
from tkinter import ttk

class HomeTheaterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Домашний кинотеатр")
        self.root.geometry("600x400")
        self.root.configure(bg='#2E1A47')

        self.create_widgets()

    def create_widgets(self):
        # Заголовок
        title_label = tk.Label(self.root, text="Домашний кинотеатр", font=('Helvetica', 20), bg='#2E1A47', fg='white')
        title_label.pack(pady=10)

        # Выбор фильма
        movie_label = tk.Label(self.root, text="Выберите фильм:", font=('Helvetica', 12), bg='#2E1A47', fg='white')
        movie_label.pack(pady=5)

        movies = ["Фильм 1", "Фильм 2", "Фильм 3"]
        movie_combobox = ttk.Combobox(self.root, values=movies)
        movie_combobox.pack(pady=5)

        # Выбор звуковой системы
        audio_label = tk.Label(self.root, text="Выберите звуковую систему:", font=('Helvetica', 12), bg='#2E1A47', fg='white')
        audio_label.pack(pady=5)

        audio_systems = ["Dolby Atmos", "DTS:X", "Stereo"]
        audio_combobox = ttk.Combobox(self.root, values=audio_systems)
        audio_combobox.pack(pady=5)

        # Кнопка запуска воспроизведения
        play_button = tk.Button(self.root, text="Начать воспроизведение", command=self.start_playback, bg='#654EA3', fg='white')
        play_button.pack(pady=20)

    def start_playback(self):
        # Здесь вы можете добавить код для запуска воспроизведения выбранного фильма
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = HomeTheaterApp(root)
    root.mainloop()
