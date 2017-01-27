from pygame import midi
from tkinter import *
from tkinter import ttk

class pentatonicsquares:

    midi.init()
    player = midi.Output(0)
    player.set_instrument(10, 1) # Glockenspiel
    player.set_instrument(11, 2) # Music Box
    player.set_instrument(12, 3) # Vibraphone
    notes = [100, 102, 107, 109]

    def __init__(self, master):

        self.master = master
        self._createGUI()
        self.master.protocol('WM_DELETE_WINDOW', self._safe_close)

    def _createGUI(self):

        self.master.title('Pentatonic Squares')
        self.master.resizable(False, False)

        # Menu Configuration
        self.menubar = Menu(self.master)
        self.master.config(menu=self.menubar)

        # File
        self.file = Menu(self.menubar)
        self.menubar.add_cascade(menu=self.file, label='File')
        self.file.add_command(label='Reset', command=self.reset)
        self.file.add_command(label='Quit', command=self._safe_close)

        # Instruments
        self.instrument_list = ['Acoustic Grand Piano', 'Bright Acoustic Piano',
        'Electric Grand Piano', 'Honky-tonk Piano', 'Electric Piano 1',
        'Electric Piano 2', 'Harpsichord', 'Clavi', 'Celesta', 'Glockenspiel',
        'Music Box', 'Vibraphone', 'Marimba', 'Xylophone', 'Tubular Bells',
        'Dulcimer', 'Drawbar Organ', 'Percussive Organ', 'Rock Organ',
        'Church Organ', 'Reed Organ', 'Accordion', 'Harmonica', 'Tango Accordion',
        'Acoustic Guitar (nylon)', 'Acoustic Guitar (steel)', 'Electric Guitar (jazz)',
        'Electric Guitar (clean)', 'Electric Guitar (muted)', 'Overdriven Guitar',
        'Distortion Guitar', 'Guitar Harmonics']

        self.instruments = Menu(self.menubar)
        self.menubar.add_cascade(menu=self.instruments, label='Instruments')

        self.piano_menu = Menu(self.menubar)
        self.instruments.add_cascade(menu=self.piano_menu, label='Piano')
        for piano in self.instrument_list[0:8]:
            self.piano_menu.add_command(label=piano, command=lambda i=piano: self.select_instrument(i))

        self.chrom_percussion = Menu(self.menubar)
        self.instruments.add_cascade(menu=self.chrom_percussion, label='Chromatic Percussion')
        for chrom_per in self.instrument_list[8:16]:
            self.chrom_percussion.add_command(label=chrom_per, command=lambda i=chrom_per: self.select_instrument(i))

        self.organ_menu = Menu(self.menubar)
        self.instruments.add_cascade(menu=self.organ_menu, label='Organ')
        for organ in self.instrument_list[16:24]:
            self.organ_menu.add_command(label=organ, command=lambda i=organ: self.select_instrument(i))

        self.guitar_menu = Menu(self.menubar)
        self.instruments.add_cascade(menu=self.guitar_menu, label='Guitar')
        for guitar in self.instrument_list[24:32]:
            self.guitar_menu.add_command(label=guitar, command=lambda i=guitar: self.select_instrument(i))

        # Scales
        self.scales = Menu(self.menubar)
        self.menubar.add_cascade(menu=self.scales, label='Scales')
        self.scales.add_command(label='Major (R M3 P5 M6)', command=self.go_major)
        self.scales.add_command(label='Minor (R m3 P5 m7)', command=self.go_minor)

        # Help
        self.help = Menu(self.menubar)
        self.menubar.add_cascade(menu=self.help, label='Help')
        self.help.add_command(label='LOL, no', command=lambda: None)

        # GUI
        self.frame_main = ttk.Frame(self.master)
        self.frame_main.pack(side=TOP)
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

    def select_instrument(self, instrument):
        self.player.set_instrument(self.instrument_list.index(instrument) + 1, 1)

    def reset(self):
        self.player.close()
        self.player = midi.Output(0)
        self.player.set_instrument(10, 1)
        self.player.set_instrument(11, 2)
        self.player.set_instrument(12, 3)
        self.midi_codes = [52, 54, 56, 59, 61, 64]

    def _safe_close(self):
        self.player.close()
        self.master.destroy()

def main():

    root = Tk()
    app = pentatonicsquares(root)
    root.mainloop()

if __name__ == '__main__': main()
