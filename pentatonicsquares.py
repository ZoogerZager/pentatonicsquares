from pygame import midi
from tkinter import *
from tkinter import ttk

class pentatonicsquares:

    midi.init()
    player = midi.Output(0)
    player.set_instrument(10, 1) # Glockenspiel
    player.set_instrument(11, 2) # Music Box
    player.set_instrument(12, 3) # Vibraphone
    player.set_instrument(13, 4) # Marimba
    midi_codes = [52, 54, 56, 59, 61, 64]

    def __init__(self, master):

        self.master = master
        self._createGUI()
        self.master.protocol('WM_DELETE_WINDOW', self._safe_close)

    def _createGUI(self):

        self.master.title('Pentatonic Squares')
        self.master.resizable(False, False)

        # Menu Configuration
        self.menubar = Menu(self.master)
        self.master.config(menu = self.menubar)
        self.file = Menu(self.menubar)
        self.scales = Menu(self.menubar)
        self.help = Menu(self.menubar)
        self.menubar.add_cascade(menu=self.file, label='File')
        self.menubar.add_cascade(menu=self.scales, label='Scales')
        self.menubar.add_cascade(menu=self.help, label='Help')
        self.file.add_command(label='Quit', command=self._safe_close)
        self.scales.add_command(label='Go Major', command=self.go_major)
        self.scales.add_command(label='Go Minor', command=self.go_minor)
        self.help.add_command(label='LOL, no', command=lambda: None)

        self.frame_main = ttk.Frame(self.master)
        self.frame_main.pack(side=TOP)

        self.notes = [100, 102, 107, 109]

        green = Frame(self.frame_main, width=400, height=400, background='#56B949')
        green.bind('<Button-1>', self.green_press)
        green.bind('<Button-2>', self.green_press)
        green.bind('<Button-3>', self.green_press)
        green.grid(row=0, column=0)
        red = Frame(self.frame_main, width=400, height=400, background='#EE4035')
        red.bind('<Button-1>', self.red_press)
        red.bind('<Button-2>', self.red_press)
        red.bind('<Button-3>', self.red_press)
        red.grid(row=0, column=1)
        blue = Frame(self.frame_main, width=400, height=400, background='#30499B')
        blue.bind('<Button-1>', self.blue_press)
        blue.bind('<Button-2>', self.blue_press)
        blue.bind('<Button-3>', self.blue_press)
        blue.grid(row=1, column=0)
        orange = Frame(self.frame_main, width=400, height=400, background='#F0A32F')
        orange.bind('<Button-1>', self.orange_press)
        orange.bind('<Button-2>', self.orange_press)
        orange.bind('<Button-3>', self.orange_press)
        orange.grid(row=1, column=1)

    def green_press(self, event):
        self.player.note_on(self.notes[0] - self.calc_note(event.y), self.calc_velocity(event.x), event.num)

    def red_press(self, event):
        self.player.note_on(self.notes[1] - self.calc_note(event.y), self.calc_velocity_right(event.x), event.num)

    def blue_press(self, event):
        self.player.note_on(self.notes[2] - self.calc_note(event.y), self.calc_velocity(event.x), event.num)

    def orange_press(self, event):
        self.player.note_on(self.notes[3] - self.calc_note(event.y), self.calc_velocity_right(event.x), event.num)

    def four_press(self, event):
        print('heyo')

    def calc_velocity(self, x_pos):
        return round(127 * (x_pos / 400))

    def calc_velocity_right(self, x_pos):
        return 127 - round(127 * (x_pos / 400))

    def calc_note(self, y_pos):
        return 12 * round(4 * (y_pos) / 400)

    def go_major(self):
        self.notes = [100, 104, 107, 109]

    def go_minor(self):
        self.notes = [100, 103, 107, 110]

    def _safe_close(self):
        self.player.close()
        self.master.destroy()

def main():

    root = Tk()
    app = pentatonicsquares(root)
    root.mainloop()

if __name__ == '__main__': main()
