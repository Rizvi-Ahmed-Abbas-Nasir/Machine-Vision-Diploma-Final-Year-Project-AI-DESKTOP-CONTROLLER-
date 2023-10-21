import customtkinter as ck
import PIL.Image

# (light, dark)
WIN_BG = ("#F9F9F9", "#222831")
FRAME_BG = ("#EAF6F6", "#393E46")
FRAME_BORDER_BG = ("#79A8A1", FRAME_BG[1])

BUTTON_TEXT_BG = ("black", "white")
BTN_BG = ("#C8E6E6", "#0F4C75")
BTN_HOVER_BG = ("#70C8DD", "#396B8D")
BTN_BORDER_BG = ("#68A8A8", "white")
BTN_HOVER_BORDER_BG = (BTN_BORDER_BG[0], "#FFFFFF")

TAB_BUTTONS_FRAME_BG = ("#FFFFFF", FRAME_BG[1])
TAB_BTN_WIDTH = 64
TAB_BTN_NORMAL_BG = "transparent"
TAB_BTN_SELECTED_BG = BTN_BG
TAB_BTN_HOVER_BG = (BTN_HOVER_BG[0], "#696969")
TAB_BTN_DISABLE_BG = TAB_BTN_HOVER_BG
TAB_BTN_BORDER_BG = ("#68A8A8", TAB_BUTTONS_FRAME_BG[1])
TAB_HOVER_BTN_BORDER_BG = BTN_HOVER_BORDER_BG
TAB_BTN_FRAME_BG = ("#79A8A1", "#31363E")

FONTS = {}
STYLES = {}
IMAGES = {}

ICON_SIZE = (48, 48)
LOGO_SIZE = (220, 220)

WIN_HEIGHT = 720
WIN_WIDTH = 1280

SIDE_FRAME_WIDTH = 300
SIDE_FRAME_PADDING = 25

TAB_VIEW_PADDING = 12

AI_VISION_MACHINE = "AI Vision Machine"
DESKTOP_MOUSE_INPUT = "Desktop Mouse Input"
DESKTOP_KEYBOARD_INPUT = "Desktop Keyboard Input"
WORKOUT_TRAINER = "Workout Trainer"
SIGN_LANGUAGE_READER = "Sign Language Reader"
PRESENTATION_CONTROLLER = "Presentation Controller"

IMAGE = "image"
ICON = "icon"


def load_configs():
    global FONTS
    load_fonts(**{"JetBrains Mono": [16, 24, 32], "Verdana": [14, 18]})

    load_images(ImageConfig(AI_VISION_MACHINE, IMAGE, LOGO_SIZE, False),
                ImageConfig(AI_VISION_MACHINE, ICON, ICON_SIZE),
                ImageConfig(DESKTOP_MOUSE_INPUT, ICON, ICON_SIZE),
                ImageConfig(WORKOUT_TRAINER, ICON, ICON_SIZE),
                ImageConfig(DESKTOP_KEYBOARD_INPUT, ICON, ICON_SIZE),
                ImageConfig(PRESENTATION_CONTROLLER, ICON, ICON_SIZE),
                ImageConfig(SIGN_LANGUAGE_READER, ICON, ICON_SIZE),

                ImageConfig(DESKTOP_MOUSE_INPUT, IMAGE, (300, 300), False),
                ImageConfig(DESKTOP_MOUSE_INPUT + "2", IMAGE, (300, 300), False),
                ImageConfig(WORKOUT_TRAINER, IMAGE, (426, 258), False),
                ImageConfig(DESKTOP_KEYBOARD_INPUT, IMAGE, (384, 216), False),
                ImageConfig(SIGN_LANGUAGE_READER, IMAGE, (488, 576)),
                ImageConfig(PRESENTATION_CONTROLLER, IMAGE, (467, 263), False))


def load_fonts(**kwargs):
    for name, values in kwargs.items():
        for size in values:
            FONTS.update({f"{name}_{size}": ck.CTkFont(family=name, size=size)})


def load_images(*images):
    for img in images:
        light = "_light"
        dark = "_dark"

        if not img.is_appearance_supported:
            light = dark = ""

        newImg = ck.CTkImage(light_image=PIL.Image.open(f"Assets/{img.file}_{img.name}{light}.png"),
                             dark_image=PIL.Image.open(f"Assets/{img.file}_{img.name}{dark}.png"))

        if img.size is not None:
            newImg.configure(size=img.size)

        IMAGES.update({f"{img.name}{img.file}": newImg})


class ImageConfig:

    def __init__(self, name, file, size=None, is_appearance_supported=True):
        self.name = name
        self.file = file
        self.size = size
        self.is_appearance_supported = is_appearance_supported
