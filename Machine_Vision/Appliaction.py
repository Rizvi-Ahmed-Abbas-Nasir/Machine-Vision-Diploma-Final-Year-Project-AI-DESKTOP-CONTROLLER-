import threading
import tkinter
import tkinter.messagebox
import PIL
import customtkinter
import DesktopControllerApplication

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class ToplevelWindow0(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("600x500")

        ImageHome0 = customtkinter.CTkImage(dark_image=PIL.Image.open("Assets\ImgOfMe.png"), size=(150, 160))

        self.label0 = customtkinter.CTkLabel(self, text="DEVELOPER PROFILE: ",   font=customtkinter.CTkFont(family="IBM Plex Sans", size=20))
        self.label0.place(x=40, y=20)

        self.Frame0Img0 = customtkinter.CTkLabel(self,
                                                 text=" ",
                                                 image=ImageHome0,
                                                 font=customtkinter.CTkFont(family="IBM Plex Sans", size=25),
                                                 fg_color="white",
                                                 corner_radius=5)
        self.Frame0Img0.place(x=50, y=90)

        self.label1 = customtkinter.CTkLabel(self, text="Name: Rizvi Ahmed Abbas ",
                                            font=customtkinter.CTkFont(family="IBM Plex Sans", size=18))
        self.label1.place(x=280, y=90)
        self.label1 = customtkinter.CTkLabel(self, text="Age: 20 ",
                                             font=customtkinter.CTkFont(family="IBM Plex Sans", size=15))
        self.label1.place(x=280, y=120)
        self.label1 = customtkinter.CTkLabel(self, text="Engineer: Software Engineering",
                                             font=customtkinter.CTkFont(family="IBM Plex Sans", size=15))
        self.label1.place(x=280, y=150)
        self.label1 = customtkinter.CTkLabel(self, text="Domain: Full-Stack Web Development,",
                                             font=customtkinter.CTkFont(family="IBM Plex Sans", size=15))
        self.label1.place(x=280, y=180)
        self.label1 = customtkinter.CTkLabel(self, text="Mobile Developments, AI&ML",
                                             font=customtkinter.CTkFont(family="IBM Plex Sans", size=15))
        self.label1.place(x=280, y=200)


        self.textbox = customtkinter.CTkTextbox(self, width=500, height=150)
        self.textbox.grid(row=0, column=1, padx=(50, 0), pady=(300, 0), sticky="nsew")
        self.textbox.insert("0.0",
                            "About MySelf\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, "
                                                       "sed diam nonumy eirmod tempor invidunt ut labore et dolore "
                                                       "magna aliquyam erat, sed diam voluptua.\n\n")
        self.textbox.configure(state="disabled")  # configure textbox to be read-only



class ToplevelWindow1(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("600x500")

        ImageHome0 = customtkinter.CTkImage(dark_image=PIL.Image.open("Assets\ImgOfMe.png"), size=(150, 160))

        self.label0 = customtkinter.CTkLabel(self, text="DEVELOPER PROFILE: ",
                                             font=customtkinter.CTkFont(family="IBM Plex Sans", size=20))
        self.label0.place(x=40, y=20)

        self.Frame0Img0 = customtkinter.CTkLabel(self,
                                                 text=" ",
                                                 image=ImageHome0,
                                                 font=customtkinter.CTkFont(family="IBM Plex Sans", size=25),
                                                 fg_color="white",
                                                 corner_radius=5)
        self.Frame0Img0.place(x=50, y=90)

        self.label1 = customtkinter.CTkLabel(self, text="Name: Rizvi Ahmed Abbas ",
                                             font=customtkinter.CTkFont(family="IBM Plex Sans", size=18))
        self.label1.place(x=280, y=90)
        self.label1 = customtkinter.CTkLabel(self, text="Age: 20 ",
                                             font=customtkinter.CTkFont(family="IBM Plex Sans", size=15))
        self.label1.place(x=280, y=120)
        self.label1 = customtkinter.CTkLabel(self, text="Engineer: Software Engineering",
                                             font=customtkinter.CTkFont(family="IBM Plex Sans", size=15))
        self.label1.place(x=280, y=150)
        self.label1 = customtkinter.CTkLabel(self, text="Domain: Full-Stack Web Development,",
                                             font=customtkinter.CTkFont(family="IBM Plex Sans", size=15))
        self.label1.place(x=280, y=180)
        self.label1 = customtkinter.CTkLabel(self, text="Mobile Developments, AI & ML",
                                             font=customtkinter.CTkFont(family="IBM Plex Sans", size=15))
        self.label1.place(x=280, y=200)

        self.textbox = customtkinter.CTkTextbox(self, width=500, height=150)
        self.textbox.grid(row=0, column=1, padx=(50, 0), pady=(300, 0), sticky="nsew")
        self.textbox.insert("0.0",
                            "About MySelf\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, "
                                                 "sed diam nonumy eirmod tempor invidunt ut labore et dolore "
                                                 "magna aliquyam erat, sed diam voluptua.\n\n")
        self.textbox.configure(state="disabled")  # configure textbox to be read-only


class ToplevelWindow2(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("600x500")

        ImageHome0 = customtkinter.CTkImage(dark_image=PIL.Image.open("Assets\ImgOfMe.png"), size=(150, 160))


        self.label0 = customtkinter.CTkLabel(self, text="DEVELOPER PROFILE: ",
                                             font=customtkinter.CTkFont(family="IBM Plex Sans", size=20))
        self.label0.place(x=40, y=20)

        self.Frame0Img0 = customtkinter.CTkLabel(self,
                                                 text=" ",
                                                 image=ImageHome0,
                                                 font=customtkinter.CTkFont(family="IBM Plex Sans", size=25),
                                                 fg_color="white",
                                                 corner_radius=5)
        self.Frame0Img0.place(x=50, y=90)

        self.label1 = customtkinter.CTkLabel(self, text="Name: Rizvi Ahmed Abbas ",
                                             font=customtkinter.CTkFont(family="IBM Plex Sans", size=18))
        self.label1.place(x=280, y=90)
        self.label1 = customtkinter.CTkLabel(self, text="Age: 20 ",
                                             font=customtkinter.CTkFont(family="IBM Plex Sans", size=15))
        self.label1.place(x=280, y=120)
        self.label1 = customtkinter.CTkLabel(self, text="Engineer: Software Engineering",
                                             font=customtkinter.CTkFont(family="IBM Plex Sans", size=15))
        self.label1.place(x=280, y=150)
        self.label1 = customtkinter.CTkLabel(self, text="Domain: Full-Stack Web Development,",
                                             font=customtkinter.CTkFont(family="IBM Plex Sans", size=15))
        self.label1.place(x=280, y=180)
        self.label1 = customtkinter.CTkLabel(self, text="Mobile Developments, AI&ML",
                                             font=customtkinter.CTkFont(family="IBM Plex Sans", size=15))
        self.label1.place(x=280, y=200)

        self.textbox = customtkinter.CTkTextbox(self, width=500, height=150)
        self.textbox.grid(row=0, column=1, padx=(50, 0), pady=(300, 0), sticky="nsew")
        self.textbox.insert("0.0",
                            "About MySelf\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, "
                                                 "sed diam nonumy eirmod tempor invidunt ut labore et dolore "
                                                 "magna aliquyam erat, sed diam voluptua.\n\n")
        self.textbox.configure(state="disabled")  # configure textbox to be read-only


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.toplevel_window0 = None
        self.toplevel_window1 = None
        self.toplevel_window2 = None
        self.title("AI Machine Vision")
        self.geometry(f"{1100}x{580}")
        # Icon for TopLevel Window
        # self.after(201, lambda: self.iconbitmap("logo2.png"))

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # images
        ImageHome0 = customtkinter.CTkImage(dark_image=PIL.Image.open("Assets\AIExapmple.png"), size=(350, 280))
        ImageHome1 = customtkinter.CTkImage(dark_image=PIL.Image.open("Assets\VT.png"), size=(350, 240))
        ImageHome2 = customtkinter.CTkImage(dark_image=PIL.Image.open("Assets\VirtualK.jpg"), size=(350, 280))
        ImageHome3 = customtkinter.CTkImage(dark_image=PIL.Image.open("Assets\Presentation.png"), size=(350, 240))

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Developers",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.open_toplevel0,
                                                        text="Rizvi Ahmed Abbas")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.open_toplevel1,
                                                        text="Saad Shaikh Mujab")
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.open_toplevel2,
                                                        text="Ubaid Mukadam")
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                                       values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                               values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # TabsView
        self.Pages = customtkinter.CTkTabview(self, width=895, height=565,
                                              fg_color=("#bdbdc1", "#29292a"),
                                              corner_radius=15)  # 262628 alternate Color
        self.Pages.add(" Home ")
        self.Pages.add(" Desktop Controller ")
        self.Pages.add(" Trainer ")
        self.Pages.add(" VirtualKeyboard ")
        self.Pages.add(" Presentation Controller ")
        self.Pages.place(x=190, y=3)
        self.Pages._segmented_button.grid(sticky="W")

        # TextBox Home
        self.textbox = customtkinter.CTkTextbox(self.Pages.tab(" Home "), width=350, height=240)
        self.textbox.grid(row=0, column=1, padx=(500, 0), pady=(20, 0), sticky="nsew")
        self.textbox.insert("0.0",
                            "About This Project\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, "
                                                       "sed diam nonumy eirmod tempor invidunt ut labore et dolore "
                                                       "magna aliquyam erat, sed diam voluptua.\n\n")
        self.textbox.configure(state="disabled")  # configure textbox to be read-only

        # Labels Home Page
        self.HomeLabel0 = customtkinter.CTkLabel(self.Pages.tab(" Home "), text="AI ",
                                                 font=customtkinter.CTkFont(family="IBM Plex Sans", size=90),
                                                 fg_color="white", text_color="black", corner_radius=10)
        self.HomeLabel0.place(x=50, y=46)

        self.HomeLabel1 = customtkinter.CTkLabel(self.Pages.tab(" Home "), text=" Machine Vision",
                                                 font=customtkinter.CTkFont(family="IBM Plex Sans", size=30),
                                                 corner_radius=10)
        self.HomeLabel1.place(x=155, y=78)

        self.HomeLabel2 = customtkinter.CTkLabel(self.Pages.tab(" Home "), text=" Diploma Final Year Project.",
                                                 font=customtkinter.CTkFont(family="IBM Plex Sans", size=40),
                                                 corner_radius=0)
        self.HomeLabel2.place(x=5, y=300)

        self.HomeLabel3 = customtkinter.CTkLabel(self.Pages.tab(" Home "),
                                                 text="All Artificial Intelligence(AI) Computer Vision program "
                                                      "are Integrated in one Application. ",
                                                 font=customtkinter.CTkFont(family="IBM Plex Sans", size=19),
                                                 corner_radius=0)
        self.HomeLabel3.place(x=15, y=360)

        self.HomeLabel3 = customtkinter.CTkLabel(self.Pages.tab(" Home "),
                                                 text="Different AI Program Such as Desktop Controller, Virtual "
                                                      "Keyboard, "
                                                      "AI Trainer, Presentation Controller Can be Operate With",
                                                 font=customtkinter.CTkFont(family="IBM Plex Sans", size=15),
                                                 corner_radius=0)
        self.HomeLabel3.place(x=15, y=387)
        self.HomeLabel4 = customtkinter.CTkLabel(self.Pages.tab(" Home "),
                                                 text="This Application, This App is Very User Friendly and easily "
                                                      "Understood by the User "
                                                      ",User can Start Different Modules of AI",
                                                 font=customtkinter.CTkFont(family="IBM Plex Sans", size=15),
                                                 corner_radius=0)
        self.HomeLabel4.place(x=15, y=410)
        self.HomeLabel5 = customtkinter.CTkLabel(self.Pages.tab(" Home "),
                                                 text="Machine Vision "
                                                      "Appliaction(Progarms).",
                                                 font=customtkinter.CTkFont(family="IBM Plex Sans", size=15),
                                                 corner_radius=0)
        self.HomeLabel5.place(x=15, y=430)
        ################################Home###########################

        # Label Desktop
        self.HomeLabel5 = customtkinter.CTkLabel(self.Pages.tab(" Desktop Controller "),
                                                 text="Desktop Controller",
                                                 font=customtkinter.CTkFont(family="IBM Plex Sans", size=27),
                                                 corner_radius=0)
        self.HomeLabel5.place(x=20, y=5)

        # Image Desktop
        self.HomeLabel5 = customtkinter.CTkLabel(self.Pages.tab(" Desktop Controller "),
                                                 text=" ",
                                                 image=ImageHome0,
                                                 font=customtkinter.CTkFont(family="IBM Plex Sans", size=25),
                                                 corner_radius=0)
        self.HomeLabel5.place(x=20, y=90)

        # Desktop Pages
        self.button_1 = customtkinter.CTkButton(self.Pages.tab(" Desktop Controller "),
                                                corner_radius=100,
                                                text="Start",
                                                command=self.open_DestopControllerApp)
        self.button_1.place(x=110, y=400)

        # TextBox Desktop
        self.textbox = customtkinter.CTkTextbox(self.Pages.tab(" Desktop Controller "), width=350, height=240)
        self.textbox.grid(row=0, column=1, padx=(500, 0), pady=(20, 0), sticky="nsew")
        self.textbox.insert("0.0",
                            "About This Project\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, "
                                                       "sed diam nonumy eirmod tempor invidunt ut labore et dolore "
                                                       "magna aliquyam erat, sed diam voluptua.\n\n")
        self.textbox.configure(state="disabled")  # configure textbox to be read-only
        ################Desktop#####################

        # Label Trainer
        self.HomeLabel5 = customtkinter.CTkLabel(self.Pages.tab(" Trainer "),
                                                 text="Trainer",
                                                 font=customtkinter.CTkFont(family="IBM Plex Sans", size=27),
                                                 corner_radius=0)
        self.HomeLabel5.place(x=20, y=5)

        # Image Trainer
        self.HomeLabel5 = customtkinter.CTkLabel(self.Pages.tab(" Trainer "),
                                                 text=" ",
                                                 image=ImageHome1,
                                                 font=customtkinter.CTkFont(family="IBM Plex Sans", size=25),
                                                 corner_radius=0)
        self.HomeLabel5.place(x=20, y=90)

        # Desktop Trainer
        self.button_1 = customtkinter.CTkButton(self.Pages.tab(" Trainer "),
                                                corner_radius=100,
                                                text="Start",
                                                command=self.open_DestopControllerApp)
        self.button_1.place(x=110, y=400)

        # TextBox Trainer
        self.textbox = customtkinter.CTkTextbox(self.Pages.tab(" Trainer "), width=350, height=240)
        self.textbox = customtkinter.CTkTextbox(self.Pages.tab(" Trainer "), width=350, height=240)
        self.textbox.grid(row=0, column=1, padx=(500, 0), pady=(20, 0), sticky="nsew")
        self.textbox.insert("0.0",
                            "About This Project\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, "
                                                       "sed diam nonumy eirmod tempor invidunt ut labore et dolore "
                                                       "magna aliquyam erat, sed diam voluptua.\n\n")
        self.textbox.configure(state="disabled")  # configure textbox to be read-only
        ####################Trainer################

        # Label VirtualKeyboard
        self.HomeLabel5 = customtkinter.CTkLabel(self.Pages.tab(" VirtualKeyboard "),
                                                 text="VirtualKeyboard",
                                                 font=customtkinter.CTkFont(family="IBM Plex Sans", size=27),
                                                 corner_radius=0)
        self.HomeLabel5.place(x=20, y=5)

        # Image VirtualKeyboard
        self.HomeLabel5 = customtkinter.CTkLabel(self.Pages.tab(" VirtualKeyboard "),
                                                 text=" ",
                                                 image=ImageHome2,
                                                 font=customtkinter.CTkFont(family="IBM Plex Sans", size=25),
                                                 corner_radius=0)
        self.HomeLabel5.place(x=20, y=90)

        # Desktop VirtualKeyboard
        self.button_1 = customtkinter.CTkButton(self.Pages.tab(" VirtualKeyboard "),
                                                corner_radius=100,
                                                text="Start",
                                                command=self.open_DestopControllerApp)
        self.button_1.place(x=110, y=400)

        # TextBox VirtualKeyboard
        self.textbox = customtkinter.CTkTextbox(self.Pages.tab(" VirtualKeyboard "), width=350, height=240)
        self.textbox = customtkinter.CTkTextbox(self.Pages.tab(" VirtualKeyboard "), width=350, height=240)
        self.textbox.grid(row=0, column=1, padx=(500, 0), pady=(20, 0), sticky="nsew")
        self.textbox.insert("0.0",
                            "About This Project\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, "
                                                       "sed diam nonumy eirmod tempor invidunt ut labore et dolore "
                                                       "magna aliquyam erat, sed diam voluptua.\n\n")
        self.textbox.configure(state="disabled")  # configure textbox to be read-only
        #############VirtualKeyboard##########

        # Label Presentation Controller
        self.HomeLabel5 = customtkinter.CTkLabel(self.Pages.tab(" Presentation Controller "),
                                                 text="Presentation Controller",
                                                 font=customtkinter.CTkFont(family="IBM Plex Sans", size=27),
                                                 corner_radius=0)
        self.HomeLabel5.place(x=20, y=5)

        # Image Presentation Controller
        self.HomeLabel5 = customtkinter.CTkLabel(self.Pages.tab(" Presentation Controller "),
                                                 text=" ",
                                                 image=ImageHome3,
                                                 font=customtkinter.CTkFont(family="IBM Plex Sans", size=25),
                                                 corner_radius=0)
        self.HomeLabel5.place(x=20, y=90)

        # Desktop Presentation Controller
        self.button_1 = customtkinter.CTkButton(self.Pages.tab(" Presentation Controller "),
                                                corner_radius=100,
                                                text="Start",
                                                command=self.open_DestopControllerApp)
        self.button_1.place(x=110, y=400)

        # TextBox Presentation Controller
        self.textbox = customtkinter.CTkTextbox(self.Pages.tab(" Presentation Controller "), width=350, height=240)
        self.textbox = customtkinter.CTkTextbox(self.Pages.tab(" Presentation Controller "), width=350, height=240)
        self.textbox.grid(row=0, column=1, padx=(500, 0), pady=(20, 0), sticky="nsew")
        self.textbox.insert("0.0",
                            "About This Project\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, "
                                                       "sed diam nonumy eirmod tempor invidunt ut labore et dolore "
                                                       "magna aliquyam erat, sed diam voluptua.\n\n")
        self.textbox.configure(state="disabled")  # configure textbox to be read-only

    #######Presentation Controller##########

    # Methods
    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

    def open_toplevel0(self):
        if self.toplevel_window0 is None or not self.toplevel_window0.winfo_exists():
            self.toplevel_window0 = ToplevelWindow0(self)  # create window if its None or destroyed
            self.toplevel_window0.grab_set()

    def open_toplevel1(self):
        if self.toplevel_window1 is None or not self.toplevel_window1.winfo_exists():
            self.toplevel_window1 = ToplevelWindow1(self)  # create window if its None or destroyed
            self.toplevel_window1.grab_set()

    def open_toplevel2(self):
        if self.toplevel_window2 is None or not self.toplevel_window2.winfo_exists():
            self.toplevel_window2 = ToplevelWindow2(self)  # create window if its None or destroyed
            self.toplevel_window2.grab_set()

    def open_DestopControllerApp(self):
        g = DesktopControllerApplication.main()
        t = threading.Thread(target=g.start)
        t.start()


if __name__ == "__main__":
    app = App()
    app.mainloop()
