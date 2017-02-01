from collections import OrderedDict
from pygame import midi
from tkinter import *
from tkinter import ttk

class tetratonicsquares:

    midi.init()
    player = midi.Output(0)
    player.set_instrument(10, 1) # Glockenspiel
    player.set_instrument(11, 2) # Music Box
    player.set_instrument(12, 3) # Vibraphone
    notes = [100, 102, 107, 109]
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
        self.file = Menu(self.menubar)
        self.menubar.add_cascade(menu=self.file, label='File')
        self.file.add_command(label='Reset', command=self.reset)
        self.file.add_command(label='Quit', command=self._safe_close)

        self.buttons = Menu(self.menubar)
        self.menubar.add_cascade(menu=self.buttons, label='Buttons')
        self.buttons.add_radiobutton(label='Left Click', command=lambda: self.set_click(1))
        self.buttons.add_radiobutton(label='Right Click', command=lambda: self.set_click(3))
        self.buttons.add_radiobutton(label='Middle Click', command=lambda: self.set_click(2))

        # Instruments
        self.instrument_dict = OrderedDict()
        self.instrument_dict['Piano'] = ['Acoustic Grand Piano', 'Bright Acoustic Piano','Electric Grand Piano', 'Honky-tonk Piano', 'Electric Piano 1','Electric Piano 2', 'Harpsichord', 'Clavi',]
        self.instrument_dict['Chromatic Percussion'] = ['Celesta', 'Glockenspiel', 'Music Box', 'Vibraphone', 'Marimba', 'Xylophone', 'Tubular Bells', 'Dulcimer']
        self.instrument_dict['Organ'] = ['Drawbar Organ', 'Percussive Organ', 'Rock Organ', 'Church Organ', 'Reed Organ', 'Accordion', 'Harmonica', 'Tango Accordion']
        self.instrument_dict['Guitar'] = ['Acoustic Guitar (nylon)', 'Acoustic Guitar (steel)', 'Electric Guitar (jazz)', 'Electric Guitar (clean)', 'Electric Guitar (muted)', 'Overdriven Guitar', 'Distortion Guitar', 'Guitar Harmonics']
        self.instrument_dict['Bass'] = ['Acoustic Bass', 'Electric Bass (finger)', 'Electric Bass (pick)', 'Fretless Bass', 'Slap Bass 1', 'Slap Bass 2', 'Synth Bass 1', 'Synth Bass 2']
        self.instrument_dict['Strings'] = ['Violin', 'Viola', 'Cello', 'Contrabass', 'Tremolo Strings', 'Pizzicato Strings', 'Orchestral Harp', 'Timpani']
        self.instrument_dict['Ensemble'] = ['String Ensemble 1', 'String Ensemble 2', 'Synth Strings 1', 'Synth Strings 2', 'Choir Aahs', 'Choir Oohs', 'Synth Voice', 'Orchestra Hit']
        self.instrument_dict['Brass'] = ['Trumpet', 'Trombone', 'Tuba', 'Muted Trumpet', 'French Horn', 'Brass Section', 'Synth Brass 1', 'Synth Brass 2']
        self.instrument_dict['Reed'] = ['Soprano Sax', 'Alto Sax', 'Tenor Sax', 'Baritone Sax', 'Oboe', 'English Horn', 'Bassoon', 'Clarinet']
        self.instrument_dict['Pipe'] = ['Piccolo', 'Flute', 'Recorder', 'Pan Flute', 'Blown Bottle', 'Shakuhachi', 'Whistle', 'Ocarina']
        self.instrument_dict['Synth Lead'] = ['Lead 1 (square)', 'Lead 2 (sawtooth)', 'Lead 3 (calliope)', 'Lead 4 (chiff)', 'Lead 5 (charang)', 'Lead 6 (voice)', 'Lead 7 (fifths)', 'Lead 8 (bass + lead)']
        self.instrument_dict['Synth Pad'] = ['Pad 1 (new age)', 'Pad 2 (warm)', 'Pad 3 (polysynth)', 'Pad 4 (choir)', 'Pad 5 (bowed)', 'Pad 6 (metallic)', 'Pad 7 (halo)', 'Pad 8 (sweep)']
        self.instrument_dict['Synth Effects'] = ['FX 1 (rain)', 'FX 2 (soundtrack)', 'FX 3 (crystal)', 'FX 4 (atmosphere)', 'FX 5 (brightness)', 'FX 6 (goblins)', 'FX 7 (echoes)', 'FX 8 (sci-fi)']
        self.instrument_dict['World'] = ['Sitar', 'Banjo', 'Shamisen', 'Koto', 'Kalimba', 'Bag pipe', 'Fiddle', 'Shanai']
        self.instrument_dict['Percussion'] = ['Tinkle Bell', 'Agogo', 'Steel Drums', 'Woodblock', 'Taiko Drum', 'Melodic Tom', 'Synth Drum', 'Reverse Cymbal']
        self.instrument_dict['Sound Effects'] = ['Guitar Fret Noise', 'Breath Noise', 'Seashore', 'Bird Tweet', 'Telephone Ring', 'Helicopter', 'Applause', 'Gunshot']

        self.instruments = Menu(self.menubar)
        self.menubar.add_cascade(menu=self.instruments, label='Instruments')

        for family, instrument_list in self.instrument_dict.items():
            menu = Menu(self.menubar)
            self.instruments.add_cascade(menu=menu, label=family)
            for instrument in instrument_list:
                menu.add_command(label=instrument, command=lambda f=family, i=instrument: self.select_instrument(f, i))

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
        green.grid(row=0, column=0)
        red = Frame(self.frame_main, width=400, height=400, background='#EE4035')
        red.grid(row=0, column=1)
        blue = Frame(self.frame_main, width=400, height=400, background='#30499B')
        blue.grid(row=1, column=0)
        orange = Frame(self.frame_main, width=400, height=400, background='#F0A32F')
        orange.grid(row=1, column=1)

        # Key Bindings
        for mouse_button in ['<Button-1>', '<Button-2>', '<Button-3>']:
            green.bind(mouse_button, lambda event, i=0: self.play_note(event, note=i))
            red.bind(mouse_button, lambda event, i=1: self.play_note(event, note=i))
            blue.bind(mouse_button, lambda event, i=2: self.play_note(event, note=i))
            orange.bind(mouse_button, lambda event, i=3: self.play_note(event, note=i))

    def play_note(self, event, note):
        if note in [0, 2]:
            self.player.note_on(self.notes[note] - self.calc_note(event.y),
                                self.calc_velocity(event.x), event.num)
        if note in [1, 3]:
            self.player.note_on(self.notes[note] - self.calc_note(event.y),
                                self.calc_velocity_right(event.x), event.num)

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

    def select_instrument(self, family, instrument):
        midi_code = ((list(self.instrument_dict.keys())).index(family) * 8
                    + self.instrument_dict[family].index(instrument))
        self.player.set_instrument(midi_code, self.default_click)

    def set_click(self, button):
        self.default_click = button

    def reset(self):
        self.player.close()
        self.player = midi.Output(0)
        self.player.set_instrument(10, 1)
        self.player.set_instrument(11, 2)
        self.player.set_instrument(12, 3)

    def _safe_close(self):
        self.player.close()
        self.master.destroy()

def main():

    root = Tk()
    app = tetratonicsquares(root)
    root.mainloop()

if __name__ == '__main__': main()
