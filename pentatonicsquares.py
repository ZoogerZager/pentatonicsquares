from pygame import midi
from tkinter import *
from tkinter import ttk

class pentatonicsquares:

    midi.init()
    player = midi.Output(0)
    player.set_instrument(15, 1) # Tubular Bells
    midi_codes = [52, 54, 56, 59, 61, 64]

    def __init__(self, master):

        self.master = master
        self._createGUI()
        self.master.protocol('WM_DELETE_WINDOW', self._safe_close)

    def _createGUI(self):

        self.master.title('Pentatonic Squares')
        self.master.resizable(False, False)

        self.frame_input = ttk.Frame(self.master)
        self.frame_input.pack(side= TOP)

        green = Frame(self.frame_input, width=400, height=400, background='#56B949')
        green.bind('<Button-1>', self.green_press)
        green.grid(row=0, column=0)
        red = Frame(self.frame_input, width=400, height=400, background='#EE4035')
        red.bind('<Button-1>', self.red_press)
        red.grid(row=0, column=1)
        blue = Frame(self.frame_input, width=400, height=400, background='#30499B')
        blue.bind('<Button-1>', self.blue_press)
        blue.grid(row=1, column=0)
        orange = Frame(self.frame_input, width=400, height=400, background='#F0A32F')
        orange.bind('<Button-1>', self.orange_press)
        orange.grid(row=1, column=1)

    def green_press(self, event):
        self.player.note_on(self.calc_note(event.y) + 40, self.calc_volume(event.x), 1)
        print('Green!', event.x, event.y)

    def red_press(self, event):
        self.player.note_on(self.calc_note(event.y) + 42, self.calc_volume(event.x), 1)
        print('Red!', event.x, event.y)

    def blue_press(self, event):
        self.player.note_on(self.calc_note(event.y) + 47, self.calc_volume(event.x), 1)
        print('Blue!', event.x, event.y)

    def orange_press(self, event):
        self.player.note_on(self.calc_note(event.y) + 49, self.calc_volume(event.x), 1)
        print('Orange!', event.x, event.y)

    def calc_volume(self, x_pos):
        return round(127 * (x_pos / 400))

    def calc_note(self, y_pos):
        return 12 * round(4 * (y_pos) / 400)

    def _safe_close(self):
        self.player.close()
        self.master.destroy()

def main():

    root = Tk()
    app = pentatonicsquares(root)
    root.mainloop()

if __name__ == '__main__': main()
