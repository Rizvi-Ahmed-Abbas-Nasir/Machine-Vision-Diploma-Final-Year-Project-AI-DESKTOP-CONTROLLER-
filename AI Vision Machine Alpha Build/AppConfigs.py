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
IMAGE_SIZE = (300, 300)
LOGO_SIZE = (240, 240)

WIN_HEIGHT = 720
WIN_WIDTH = 1280

SIDE_FRAME_WIDTH = 300
SIDE_FRAME_PADDING = 25

TAB_VIEW_PADDING = 12

AI_VISION_MACHINE = "AI Vision Machine"
DESKTOP_MOUSE_INPUT = "Desktop Mouse Input"
DESKTOP_KEYBOARD_INPUT = "Desktop Keyboard Input"
WORKOUT_TRAINER = "Workout Trainer"


def load_configs():
    global FONTS
    load_fonts(**{"JetBrains Mono": [16, 24, 32], "Verdana": [14, 18]})
    load_images(AI_VISION_MACHINE, DESKTOP_MOUSE_INPUT, WORKOUT_TRAINER, DESKTOP_KEYBOARD_INPUT,
                "ppt", "sign_lang_letter", "sign_lang_word",
                size=ICON_SIZE, file="icon", is_appearance_supported=True)
    load_images(DESKTOP_MOUSE_INPUT, DESKTOP_KEYBOARD_INPUT, size=IMAGE_SIZE, file="image")
    load_images(AI_VISION_MACHINE, size=LOGO_SIZE, file="image")
    # load_icons(AI_VISION_MACHINE, f"{AI_VISION_MACHINE}_normal", size=LOGO_SIZE)


def load_fonts(**kwargs):
    for name, values in kwargs.items():
        for size in values:
            FONTS.update({f"{name}_{size}": ck.CTkFont(family=name, size=size)})


def load_images(*icons, size=None, file, is_appearance_supported=False):
    light = "_light"
    dark = "_dark"
    if not is_appearance_supported:
        dark = light = ""

    for name in icons:

        image = ck.CTkImage(light_image=PIL.Image.open(f"Assets/{file}_{name}{light}.png"),
                            dark_image=PIL.Image.open(f"Assets/{file}_{name}{dark}.png"))
        if size is not None:
            image.configure(size=size)

        if list(IMAGES.keys()).__contains__(name):
            IMAGES.update({f"{name}_{file}": image})
            continue

        IMAGES.update({name: image})
