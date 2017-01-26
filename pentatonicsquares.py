from pygame import midi
from tkinter import *
from tkinter import ttk

class pentatonicsquares:

    midi.init()
    player = midi.Output(0)
    player.set_instrument(10, 1) # Tubular Bells
    player.set_instrument(11, 2)
    player.set_instrument(12, 3)
    player.set_instrument(13, 4)
    midi_codes = [52, 54, 56, 59, 61, 64]

    def __init__(self, master):

        self.master = master
        self._createGUI()
        self.master.protocol('WM_DELETE_WINDOW', self._safe_close)

    def _createGUI(self):

        self.master.title('Pentatonic Squares')
        self.master.resizable(False, False)

        self.frame_input = ttk.Frame(self.master)
        self.frame_input.pack(side=TOP)

        self.notes = [40, 42, 47, 49]

        green = Frame(self.frame_input, width=400, height=400, background='#56B949')
        green.bind('<Button-1>', self.green_press)
        green.bind('<Button-2>', self.green_press_two)
        green.bind('<Button-3>', self.green_press_three)
        green.grid(row=0, column=0)
        red = Frame(self.frame_input, width=400, height=400, background='#EE4035')
        red.bind('<Button-1>', self.red_press)
        red.bind('<Button-2>', self.red_press_two)
        red.bind('<Button-3>', self.red_press_three)
        red.grid(row=0, column=1)
        blue = Frame(self.frame_input, width=400, height=400, background='#30499B')
        blue.bind('<Button-1>', self.blue_press)
        blue.bind('<Button-2>', self.blue_press_two)
        blue.bind('<Button-3>', self.blue_press_three)
        blue.grid(row=1, column=0)
        orange = Frame(self.frame_input, width=400, height=400, background='#F0A32F')
        orange.bind('<Button-1>', self.orange_press)
        orange.bind('<Button-2>', self.orange_press_two)
        orange.bind('<Button-3>', self.orange_press_three)
        orange.grid(row=1, column=1)


    def green_press(self, event):
        self.player.note_on(self.calc_note(event.y) + self.notes[0], self.calc_velocity(event.x), 1)

    def red_press(self, event):
        self.player.note_on(self.calc_note(event.y) + self.notes[1], self.calc_velocity(event.x), 1)

    def blue_press(self, event):
        self.player.note_on(self.calc_note(event.y) + self.notes[2], self.calc_velocity(event.x), 1)

    def orange_press(self, event):
        self.player.note_on(self.calc_note(event.y) + self.notes[3], self.calc_velocity(event.x), 1)

    def green_press_two(self, event):
        self.player.note_on(self.calc_note(event.y) + self.notes[0], self.calc_velocity(event.x), 2)

    def red_press_two(self, event):
        self.player.note_on(self.calc_note(event.y) + self.notes[1], self.calc_velocity(event.x), 2)

    def blue_press_two(self, event):
        self.player.note_on(self.calc_note(event.y) + self.notes[2], self.calc_velocity(event.x), 2)

    def orange_press_two(self, event):
        self.player.note_on(self.calc_note(event.y) + self.notes[3], self.calc_velocity(event.x), 2)

    def green_press_three(self, event):
        self.player.note_on(self.calc_note(event.y) + self.notes[0], self.calc_velocity(event.x), 3)

    def red_press_three(self, event):
        self.player.note_on(self.calc_note(event.y) + self.notes[1], self.calc_velocity(event.x), 3)

    def blue_press_three(self, event):
        self.player.note_on(self.calc_note(event.y) + self.notes[2], self.calc_velocity(event.x), 3)

    def orange_press_three(self, event):
        self.player.note_on(self.calc_note(event.y) + self.notes[3], self.calc_velocity(event.x), 3)

    def calc_velocity(self, x_pos):
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
