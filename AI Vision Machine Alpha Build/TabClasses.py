from Tab import Tab
from AppConfigs import *


class AIVisionMachineHome(Tab):

    def __init__(self, tab_view):
        button = self._create_button(tab_view, image=IMAGES[AI_VISION_MACHINE+ICON], border_width=0)
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

    def __init__(self, tab_view):
        button = self._create_button(tab_view, image=IMAGES[DESKTOP_MOUSE_INPUT+ICON])
        frame = self._create_frame(tab_view)

        super().__init__(DESKTOP_MOUSE_INPUT, button, frame, tab_view)
        self._init_content(body_text="In this module, AI interprets hand gestures based on a predefined dataset. This "
                                     "functionality replaces the traditional use of a mouse. These "
                                     "gestures are capable of manipulating the cursor, providing an intuitive and "
                                     "hands-free desktop navigation experience.",
            images=[self.name, self.name+"2"], Start=self.start_mouse_input)

    def start_mouse_input(self):
        pass


class DesktopKeyboardInputTab(Tab):

    def __init__(self, tab_view):
        button = self._create_button(tab_view, image=IMAGES[DESKTOP_KEYBOARD_INPUT+ICON])
        frame = self._create_frame(tab_view)

        super().__init__(DESKTOP_KEYBOARD_INPUT, button, frame, tab_view)
        self._init_content(body_text="In this module, AI interprets hand gestures based on a predefined dataset. This "
                                     "functionality replaces the traditional use of a keyboard. These "
                                     "gestures are capable of manipulating the virtual keyboard, "
                                     "providing an intuitive and hands-free desktop navigation experience.",
            images=[self.name], Start=self.start_keyboard_input)

    def start_keyboard_input(self):
        pass


class WorkoutTrainerTab(Tab):

    def __init__(self, tab_view):
        button = self._create_button(tab_view, image=IMAGES[WORKOUT_TRAINER+ICON])
        frame = self._create_frame(tab_view)

        super().__init__(WORKOUT_TRAINER, button, frame, tab_view)
        self._init_content(body_text="The Workout Trainer module employs AI to map landmarks on various parts of the "
                                     "user's body, such as arms and legs. It then collects statistical data based on "
                                     "the specific workout exercise being performed. This data is presented to the "
                                     "user, offering real-time feedback and guidance during their workout routine.",
                           images=[self.name], Start=self.start_workout_trainer)

    def start_workout_trainer(self):
        pass


class PresentationControllerTab(Tab):

    def __init__(self, tab_view):
        button = self._create_button(tab_view, image=IMAGES[PRESENTATION_CONTROLLER+ICON])
        frame = self._create_frame(tab_view)

        super().__init__(PRESENTATION_CONTROLLER, button, frame, tab_view)
        self._init_content(body_text="In this module, AI reads hand gestures through the camera screen and interprets "
                                     "them to manipulate PowerPoint (PPT) slides. Users can seamlessly control and "
                                     "present their slides without the need for a third person or constantly "
                                     "returning to their device to change slides or manage the presentation.",
                           images=[self.name], Start=self.start_presentation_controller)

    def start_presentation_controller(self):
        pass


class SignLanguageTab(Tab):

    def __init__(self, tab_view):
        button = self._create_button(tab_view, image=IMAGES[SIGN_LANGUAGE_READER+ICON])
        frame = self._create_frame(tab_view)

        super().__init__(SIGN_LANGUAGE_READER, button, frame, tab_view)
        self._init_content(body_text="Through extensive training, our AI is equipped to interpret hand signs and "
                                     "identify the corresponding letters by analyzing landmarks on the user's "
                                     "fingers. This module aids in bridging the communication gap between sign "
                                     "language users and non-sign language speakers."
                                     "Similarly, this module also reads hand signs and goes a step further by "
                                     "recognizing entire words. Separate datasets are used for each module within "
                                     "this hand sign translation system, enabling accurate and context-aware "
                                     "communication through sign language",
                           images=[self.name],
                           Sign_Language_Letters=self.start_sign_lang_word,
                           Sign_Language_Words=self.start_sign_lang_word())

    def start_sign_lang_letter(self):
        pass

    def start_sign_lang_word(self):
        pass


