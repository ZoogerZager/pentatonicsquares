import midi_instruments
import webbrowser
from pygame import midi
from tkinter import *
from tkinter import ttk


class tetratonicsquares:

    midi.init()
    player = midi.Output(0)
    player.set_instrument(10, 1) # Glockenspiel
    player.set_instrument(11, 2) # Music Box
    player.set_instrument(12, 3) # Vibraphone

    scale_dict = {'Default': [100, 102, 107, 109], 'Major': [100, 104, 107, 109],
                  'Major 7': [100, 104, 107, 111], 'Minor': [100, 103, 107, 110],
                  'Insen': [100, 101, 105, 110], 'Dim 7': [100, 103, 106, 109]}
    notes = scale_dict['Default']
    default_click = 1 # Mouse Button 1

    def __init__(self, master):

        self.master = master
        self._createGUI()
        self.master.protocol('WM_DELETE_WINDOW', self._safe_close)

    def _createGUI(self):

        self.master.title('Tetratonic Squares')
        self.master.resizable(False, False)

        # Menu Configuration
        self.menubar = Menu(self.master)
        self.master.config(menu=self.menubar)

        # File
        self.file = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(menu=self.file, label='File')
        self.file.add_command(label='Reset', command=self.reset)
        self.file.add_command(label='Quit', command=self._safe_close)

        self.buttons = Menu(self.menubar)
        self.menubar.add_cascade(menu=self.buttons, label='Buttons')
        self.buttons.add_radiobutton(label='Left Click', command=lambda: self.set_click(1))
        self.buttons.add_radiobutton(label='Right Click', command=lambda: self.set_click(3))
        self.buttons.add_radiobutton(label='Middle Click', command=lambda: self.set_click(2))

        # Instruments
        self.instrument_dict = midi_instruments.instruments
        self.instruments = Menu(self.menubar)
        self.menubar.add_cascade(menu=self.instruments, label='Instruments')

        for family, instrument_list in self.instrument_dict.items():
            menu = Menu(self.menubar)
            self.instruments.add_cascade(menu=menu, label=family)
            for instrument in instrument_list:
                menu.add_command(label=instrument,
                command=lambda f=family, i=instrument: self.select_instrument(f, i))

        # Scales
        self.scales = Menu(self.menubar)
        self.menubar.add_cascade(menu=self.scales, label='Scales')
        for name, scale in self.scale_dict.items():
            self.scales.add_command(label=name, command= lambda s=scale: self.set_scale(s))
        self.scales.add_separator()
        self.second, self.third, self.fourth = (IntVar(), IntVar(), IntVar())
        self.scales.add_command(label='Define Custom Scale', command=self.custom_scale)

        # About
        self.about = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(menu=self.about, label='About')
        self.about.add_command(label='README', command=self.open_readme)

        # GUI
        self.frame_main = ttk.Frame(self.master)
        self.frame_main.pack(side=TOP)
        self.green = Frame(self.frame_main, width=400, height=400, background='#56B949')
        self.green.grid(row=0, column=0)
        self.red = Frame(self.frame_main, width=400, height=400, background='#EE4035')
        self.red.grid(row=0, column=1)
        self.blue = Frame(self.frame_main, width=400, height=400, background='#30499B')
        self.blue.grid(row=1, column=0)
        self.orange = Frame(self.frame_main, width=400, height=400, background='#F0A32F')
        self.orange.grid(row=1, column=1)

        # Key Bindings
        for mouse_button in ['<Button-1>', '<Button-2>', '<Button-3>']:
            self.green.bind(mouse_button, lambda event, i=0: self.play_note(event, note=i))
            self.red.bind(mouse_button, lambda event, i=1: self.play_note(event, note=i))
            self.blue.bind(mouse_button, lambda event, i=2: self.play_note(event, note=i))
            self.orange.bind(mouse_button, lambda event, i=3: self.play_note(event, note=i))

    def play_note(self, event, note):
        if note in [0, 1]:
            note_code = self.notes[note] - self.calc_note(event.y)
        if note in [2, 3]:
            note_code = self.notes[note] - 48 + self.calc_note(event.y)
        if note in [0, 2]:
            self.player.note_on(note_code, self.calc_velocity(event.x), event.num)
        if note in [1, 3]:
            self.player.note_on(note_code, self.calc_velocity_right(event.x), event.num)

    def calc_velocity(self, x_pos):
        return round(127 * (x_pos / 400))

    def calc_velocity_right(self, x_pos):
        return 127 - round(127 * (x_pos / 400))

    def calc_note(self, y_pos):
        return 12 * round(4 * (y_pos) / 400)

    def set_scale(self, scale):
        self.notes = scale

    def set_custom_scale(self):
        self.notes = [100, 100 + self.second.get(), 100 + self.third.get(), 100 + self.fourth.get()]

    def custom_scale(self):
        popup = Toplevel(self.master, background='#83DE84', width=100, height=100, padx=10, pady=15)
        popup.title('Define Custom Scale')
        Spinbox(popup, values=('Root'), width=7).grid(row=0, column=0)
        Spinbox(popup, from_=0, to=11, width=7, textvariable=self.second, command=self.set_custom_scale).grid(row=0, column=1)
        Spinbox(popup, from_=0, to=11, width=7, textvariable=self.third, command=self.set_custom_scale).grid(row=0, column=2)
        Spinbox(popup, from_=0, to=11, width=7, textvariable=self.fourth, command=self.set_custom_scale).grid(row=0, column=3)
        Label(popup, text='Notes are measured in half steps above the Root', pady=10, background='#83DE84').grid(row=1, column=0, columnspan=4)

    def select_instrument(self, family, instrument):
        midi_code = ((list(self.instrument_dict.keys())).index(family) * 8
                    + self.instrument_dict[family].index(instrument))
        self.player.set_instrument(midi_code, self.default_click)

    def set_click(self, button):
        self.default_click = button

    def reset(self):
        self.player.close()
        self.notes = scale_dict['Default']
        self.player = midi.Output(0)
        self.player.set_instrument(10, 1)
        self.player.set_instrument(11, 2)
        self.player.set_instrument(12, 3)

    def open_readme(self):
        webbrowser.open('https://github.com/joemarchese/tetratonicsquares/blob/master/README.md')

    def _safe_close(self):
        self.player.close()
        self.master.destroy()

def main():

    root = Tk()
    app = tetratonicsquares(root)
    root.mainloop()

if __name__ == '__main__': main()
