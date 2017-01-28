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
        'Distortion Guitar', 'Guitar Harmonics', 'Acoustic Bass',
        'Electric Bass (finger)', 'Electric Bass (pick)', 'Fretless Bass',
        'Slap Bass 1', 'Slap Bass 2', 'Synth Bass 1', 'Synth Bass 2', 'Violin',
        'Viola', 'Cello', 'Contrabass', 'Tremolo Strings', 'Pizzicato Strings',
        'Orchestral Harp', 'Timpani', 'String Ensemble 1', 'String Ensemble 2',
        'Synth Strings 1', 'Synth Strings 2', 'Choir Aahs', 'Choir Oohs',
        'Synth Voice', 'Orchestra Hit', 'Trumpet', 'Trombone', 'Tuba', 'Muted Trumpet',
        'French Horn', 'Brass Section', 'Synth Brass 1', 'Synth Brass 2',
        'Soprano Sax', 'Alto Sax', 'Tenor Sax', 'Baritone Sax', 'Oboe', 'English Horn',
        'Bassoon', 'Clarinet', 'Piccolo', 'Flute', 'Recorder', 'Pan Flute',
        'Blown Bottle', 'Shakuhachi', 'Whistle', 'Ocarina', 'Lead 1 (square)',
        'Lead 2 (sawtooth)', 'Lead 3 (calliope)', 'Lead 4 (chiff)', 'Lead 5 (charang)',
        'Lead 6 (voice)', 'Lead 7 (fifths)', 'Lead 8 (bass + lead)', 'Pad 1 (new age)',
        'Pad 2 (warm)', 'Pad 3 (polysynth)', 'Pad 4 (choir)', 'Pad 5 (bowed)',
        'Pad 6 (metallic)', 'Pad 7 (halo)', 'Pad 8 (sweep)', 'FX 1 (rain)',
        'FX 2 (soundtrack)', 'FX 3 (crystal)', 'FX 4 (atmosphere)', 'FX 5 (brightness)',
        'FX 6 (goblins)', 'FX 7 (echoes)', 'FX 8 (sci-fi)', 'Sitar', 'Banjo',
        'Shamisen', 'Koto', 'Kalimba', 'Bag pipe', 'Fiddle', 'Shanai', 'Tinkle Bell',
        'Agogo', 'Steel Drums', 'Woodblock', 'Taiko Drum', 'Melodic Tom', 'Synth Drum',
        'Reverse Cymbal', 'Guitar Fret Noise', 'Breath Noise', 'Seashore', 'Bird Tweet',
        'Telephone Ring', 'Helicopter', 'Applause', 'Gunshot']

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

        self.bass_menu = Menu(self.menubar)
        self.instruments.add_cascade(menu=self.bass_menu, label='Bass')
        for bass in self.instrument_list[32:40]:
            self.bass_menu.add_command(label=bass, command=lambda i=bass: self.select_instrument(i))

        self.strings_menu = Menu(self.menubar)
        self.instruments.add_cascade(menu=self.strings_menu, label='Strings')
        for string in self.instrument_list[40:48]:
            self.strings_menu.add_command(label=string, command=lambda i=string: self.select_instrument(i))

        self.ensemble_menu = Menu(self.menubar)
        self.instruments.add_cascade(menu=self.ensemble_menu, label='Ensemble')
        for ensemble in self.instrument_list[48:56]:
            self.ensemble_menu.add_command(label=ensemble, command=lambda i=ensemble: self.select_instrument(i))

        self.brass_menu = Menu(self.menubar)
        self.instruments.add_cascade(menu=self.brass_menu, label='Brass')
        for brass in self.instrument_list[56:64]:
            self.brass_menu.add_command(label=brass, command=lambda i=brass: self.select_instrument(i))

        self.reed_menu = Menu(self.menubar)
        self.instruments.add_cascade(menu=self.reed_menu, label='Reed')
        for reed in self.instrument_list[64:72]:
            self.reed_menu.add_command(label=reed, command=lambda i=reed: self.select_instrument(i))

        self.pipe_menu = Menu(self.menubar)
        self.instruments.add_cascade(menu=self.pipe_menu, label='Pipe')
        for pipe in self.instrument_list[72:80]:
            self.pipe_menu.add_command(label=pipe, command=lambda i=pipe: self.select_instrument(i))

        self.synth_lead_menu = Menu(self.menubar)
        self.instruments.add_cascade(menu=self.synth_lead_menu, label='Synth Lead')
        for synth in self.instrument_list[80:88]:
            self.synth_lead_menu.add_command(label=synth, command=lambda i=synth: self.select_instrument(i))

        self.synth_pad_menu = Menu(self.menubar)
        self.instruments.add_cascade(menu=self.synth_pad_menu, label='Synth Pad')
        for synth in self.instrument_list[88:96]:
            self.synth_pad_menu.add_command(label=synth, command=lambda i=synth: self.select_instrument(i))

        self.synth_effects_menu = Menu(self.menubar)
        self.instruments.add_cascade(menu=self.synth_effects_menu, label='Synth Effects')
        for synth in self.instrument_list[96:104]:
            self.synth_effects_menu.add_command(label=synth, command=lambda i=synth: self.select_instrument(i))

        self.world_menu = Menu(self.menubar)
        self.instruments.add_cascade(menu=self.world_menu, label='World')
        for world in self.instrument_list[104:112]:
            self.world_menu.add_command(label=world, command=lambda i=world: self.select_instrument(i))

        self.percussion_menu = Menu(self.menubar)
        self.instruments.add_cascade(menu=self.percussion_menu, label='Percussion')
        for perc in self.instrument_list[112:120]:
            self.percussion_menu.add_command(label=perc, command=lambda i=perc: self.select_instrument(i))

        self.sound_effects_menu = Menu(self.menubar)
        self.instruments.add_cascade(menu=self.sound_effects_menu, label='Sound Effects')
        for sound in self.instrument_list[120:128]:
            self.sound_effects_menu.add_command(label=sound, command=lambda i=sound: self.select_instrument(i))

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
            green.bind(mouse_button, lambda event, i=0: self.play_note(event, color=i))
            red.bind(mouse_button, lambda event, i=1: self.play_note(event, color=i))
            blue.bind(mouse_button, lambda event, i=2: self.play_note(event, color=i))
            orange.bind(mouse_button, lambda event, i=3: self.play_note(event, color=i))

    def play_note(self, event, color):
        if color in [0, 2]:
            self.player.note_on(self.notes[color] - self.calc_note(event.y), self.calc_velocity(event.x), event.num)
        if color in [1, 3]:
            self.player.note_on(self.notes[color] - self.calc_note(event.y), self.calc_velocity_right(event.x), event.num)

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
        self.player.set_instrument(self.instrument_list.index(instrument), 1)

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
    app = pentatonicsquares(root)
    root.mainloop()

if __name__ == '__main__': main()
