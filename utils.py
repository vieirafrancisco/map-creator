import tkinter
from tkinter import filedialog

tkinter.Tk().withdraw()  # prevents an empty tkinter window from appearing

import pygame as pg


def open_file_from_explorer() -> str:
    file_path = filedialog.askopenfile(filetypes=[(".png", ".jpg")]).name
    return file_path


def write_text(
    text: str,
    surface: object,
    position: tuple,
    color: tuple = (255, 255, 255),
    font_name: str = "Comic Sans MS",
    font_size: int = 16,
    antialising: bool = True,
) -> object:
    my_font = pg.font.SysFont(font_name, font_size)
    text_surface = my_font.render(text, antialising, color)
    surface.blit(text_surface, position)

    return text_surface


def print_callback():
    print("yeyy")
