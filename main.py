from src.data_loader import load_data
from ui.main_ui import menu

movies, data = load_data()
menu(movies, data)
