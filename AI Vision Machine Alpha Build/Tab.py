from AppConfigs import *


class Tab:

    def __init__(self, name, button, frame, tab_view):
        self.name = name
        self._button = button
        self._frame = frame
        self.normal_config = self.on_normal_config
        self.selected_config = self.on_selected_config
        tab_view.add_tab(self)

    def select(self, tab_view):
        self._button._state = "disabled"
        self.selected_config()
        tab_view.deselect_tabs(self)
        self._frame.pack(fill="both", expand=True)

    def deselect(self):
        self._button._state = "normal"
        self.normal_config()
        self._frame.pack_forget()

    def on_normal_config(self):
        self._button.configure(fg_color=TAB_BTN_NORMAL_BG, border_width=1, border_color=TAB_BTN_BORDER_BG)

    def on_selected_config(self):
        self._button.configure(fg_color=TAB_BTN_SELECTED_BG, border_width=2, border_color=TAB_HOVER_BTN_BORDER_BG)

    def _create_frame(self, master):
        frame = ck.CTkFrame(master, fg_color=FRAME_BG, border_width=2, corner_radius=10, border_color=FRAME_BORDER_BG,
                            width=WIN_WIDTH - SIDE_FRAME_WIDTH - SIDE_FRAME_PADDING * 4,
                            height=WIN_HEIGHT - SIDE_FRAME_PADDING * 6)
        frame.propagate(False)
        return frame

    def _create_button(self, tab_view, image, fg_color=TAB_BTN_NORMAL_BG, hover_color=TAB_BTN_HOVER_BG, text="",
                       corner_radius=10, border_width=2):
        button = ck.CTkButton(tab_view.buttons_frame, text=text, image=image,
                              width=TAB_BTN_WIDTH, compound="bottom", fg_color=fg_color,
                              hover_color=hover_color, corner_radius=corner_radius)
        button.configure(compound="top", border_color=TAB_BTN_BORDER_BG,
                         border_width=border_width, command=lambda tv=tab_view: self.select(tv))
        button.pack(side="left", padx=8, pady=4)

        return button

    def _init_content(self, body_text="", images=None, **action_buttons):
        header_frame = ck.CTkFrame(self._frame, fg_color="transparent", corner_radius=50)
        header_frame.pack(fill="both", padx=10)

        heading_label = ck.CTkLabel(header_frame, text=self.name, font=FONTS["JetBrains Mono_32"])
        heading_label.pack(side="left", fill="y", padx=20, pady=20)

        for text, command in action_buttons.items():
            button = ck.CTkButton(header_frame, text=" ".join(text.split('_')), border_width=1, border_color=BTN_BORDER_BG,
                                  font=FONTS["JetBrains Mono_16"], text_color=BUTTON_TEXT_BG,
                                  fg_color=BTN_BG, hover_color=BTN_HOVER_BG, command=command)
            button.pack(side="top", anchor="e", padx=20, pady=10)

        outer_frame = ck.CTkFrame(self._frame, fg_color="transparent", border_width=2, border_color=WIN_BG)
        outer_frame.propagate(False)
        outer_frame.pack(side="bottom", fill="both", expand=True, padx=16, pady=16)

        scrollable_content_frame = ck.CTkScrollableFrame(outer_frame, fg_color="transparent")
        scrollable_content_frame.pack(fill="both", padx=5, pady=5, expand=True)

        self.body_label = ck.CTkLabel(scrollable_content_frame, text=body_text, font=FONTS["Verdana_18"],
                                      wraplength=outer_frame.cget("width") * 4, justify="left")
        outer_frame.bind("<Configure>", command=self._update_wrap_length)
        self.body_label.pack(side="top", anchor="nw", expand=True, padx=20, pady=20)

        if images is None:
            return

        image_frame = scrollable_content_frame

        if len(images) > 2:
            scrollable_image_frame = ck.CTkScrollableFrame(scrollable_content_frame,
                                                           fg_color="transparent", orientation="horizontal",
                                                           border_width=2, border_color=WIN_BG)
            scrollable_image_frame.pack(fill="both")
            scrollable_image_frame.configure(height=IMAGE_SIZE[1])

            image_frame = scrollable_image_frame

        for image in images:
            image_label = ck.CTkLabel(image_frame, text="", image=IMAGES[image+IMAGE])
            image_label.pack(side="left", fill="both", padx=10, pady=10, expand=True)

    def _update_wrap_length(self, event):
        self.body_label.configure(wraplength=event.width - 350)
