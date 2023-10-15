from Tab import Tab
from AppConfigs import *


class AIVisionMachineHome(Tab):

    def __init__(self, tab_view):
        button = self._create_button(tab_view, image=IMAGES[AI_VISION_MACHINE], border_width=0)
        frame = self._create_frame(tab_view)

        super().__init__(AI_VISION_MACHINE, button, frame, tab_view)

        self._init_content(body_text="We are harnessing the power of Python technology to seamlessly integrate AI "
                                     "into various modules, making it accessible and user-friendly through a "
                                     "graphical desktop application. This innovative approach offers numerous "
                                     "advantages, such as enabling sign language interpretation for enhanced "
                                     "communication and learning, replacing traditional mouse and keyboard inputs "
                                     "with intuitive hand gestures for PC interaction, recording and analyzing user "
                                     "workout data, and facilitating hands-free presentations using natural hand "
                                     "gestures, eliminating the need for additional assistance. This integration "
                                     "holds the potential to greatly benefit a wide range of users.",
                           images=[AI_VISION_MACHINE])


class DesktopMouseInputTab(Tab):

    def __init__(self, tab_view, command):
        button = self._create_button(tab_view, image=IMAGES[DESKTOP_MOUSE_INPUT])
        frame = self._create_frame(tab_view)

        super().__init__(DESKTOP_MOUSE_INPUT, button, frame, tab_view)
        self._init_content(body_text="In this module, AI interprets hand gestures based on a predefined dataset. This "
                                     "functionality replaces the traditional use of a mouse and keyboard. These "
                                     "gestures are capable of manipulating the cursor and virtual keyboard, "
                                     "providing an intuitive and hands-free desktop navigation experience.",
            images=[self.name], Start=command)


class DesktopKeyboardInputTab(Tab):

    def __init__(self, tab_view, command):
        button = self._create_button(tab_view, image=IMAGES[DESKTOP_KEYBOARD_INPUT])
        frame = self._create_frame(tab_view)

        super().__init__(DESKTOP_KEYBOARD_INPUT, button, frame, tab_view)
        self._init_content(body_text="In this module, AI interprets hand gestures based on a predefined dataset. This "
                                     "functionality replaces the traditional use of a mouse and keyboard. These "
                                     "gestures are capable of manipulating the cursor and virtual keyboard, "
                                     "providing an intuitive and hands-free desktop navigation experience.",
            images=[self.name], Start=command)
