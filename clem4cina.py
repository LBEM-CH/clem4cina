#!/usr/local/bin/python3


import tkinter
from tkinter import ttk
import numpy as np


class Adder(ttk.Frame):
    """The adders gui and functions."""
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.init_gui()

    def on_quit(self):
        """Exits program."""
        quit()

    def prepareLM2EM(self):
        """Calculates the affine transform from the control points."""

        global x_lm2em
        global LM_off
        global EM_off

        lm1 = np.array(self.lm1_entry.get().split(',')).astype(np.float)
        lm2 = np.array(self.lm2_entry.get().split(',')).astype(np.float)
        lm3 = np.array(self.lm3_entry.get().split(',')).astype(np.float)
        em1 = np.array(self.em1_entry.get().split(',')).astype(np.float)
        em2 = np.array(self.em2_entry.get().split(',')).astype(np.float)
        em3 = np.array(self.em3_entry.get().split(',')).astype(np.float)

        LM = np.array([lm1, lm2, lm3])
        EM = np.array([em1, em2, em3])
        LM_off = LM.mean(axis=0)
        EM_off = EM.mean(axis=0)
        LM = LM - LM_off
        EM = EM - EM_off
        x_lm2em = np.linalg.lstsq(LM, EM)[0]

        print("LM2EM Matrix: ",x_lm2em)
        print("LM offset   : ",LM_off)
        print("EM offset   : ",EM_off)

        self.answer_lm2em_label['text'] = x_lm2em

    def prepareEM2LM(self):
        """Calculates the affine transform from the control points."""

        global x_em2lm
        global LM_off
        global EM_off

        lm1 = np.array(self.lm1_entry.get().split(',')).astype(np.float)
        lm2 = np.array(self.lm2_entry.get().split(',')).astype(np.float)
        lm3 = np.array(self.lm3_entry.get().split(',')).astype(np.float)
        em1 = np.array(self.em1_entry.get().split(',')).astype(np.float)
        em2 = np.array(self.em2_entry.get().split(',')).astype(np.float)
        em3 = np.array(self.em3_entry.get().split(',')).astype(np.float)

# TODO: The program should be able to save the last values into some text file, and read that upon startup as default values.

        LM = np.array([lm1, lm2, lm3])
        EM = np.array([em1, em2, em3])
        LM_off = LM.mean(axis=0)
        EM_off = EM.mean(axis=0)
        LM = LM - LM_off
        EM = EM - EM_off
        x_em2lm = np.linalg.lstsq(EM, LM)[0]

        print("EM2LM Matrix: ",x_em2lm)
        print("LM offset   : ",LM_off)
        print("EM offset   : ",EM_off)
        self.answer_em2lm_label['text'] = x_em2lm

    def lm2em(self):
        lm = np.array(self.LM_entry.get().split(',')).astype(np.float).reshape((1,2))
        print("Input LM coordinates: ",lm)
        lm = lm - LM_off
        self.result_label['text'] = np.matmul(lm,x_lm2em) + EM_off
        print("Output EM coordinates: ",self.result_label['text'])

    def em2lm(self):
        global invx
        em = np.array(self.EM_entry.get().split(',')).astype(np.float).reshape((1,2))
        print("Input EM coordinates: ",em)
        em = em - EM_off
        self.result_label['text'] = np.matmul(em,x_em2lm) + LM_off
        print("Output LM coordinates: ",self.result_label['text'])

    def init_gui(self):
        """Builds GUI."""
        self.root.title('CLEM4CINA')
        self.root.option_add('*tearOff', 'FALSE')

        self.grid(column=0, row=0, sticky='nsew')

        self.menubar = tkinter.Menu(self.root)

        self.menu_file = tkinter.Menu(self.menubar)
        self.menu_file.add_command(label='Exit', command=self.on_quit)

        self.menu_edit = tkinter.Menu(self.menubar)

        self.menubar.add_cascade(menu=self.menu_file, label='File')
#         self.menubar.add_cascade(menu=self.menu_edit, label='Edit')

        self.root.config(menu=self.menubar)

#----------------------------------------------------------------------

        # Labels that remain constant throughout execution.
        ttk.Label(self, text='LM coordinates').grid(column=0, row=0,
                columnspan=2)

        ttk.Label(self, text='EM coordinates').grid(column=2, row=0,
                columnspan=2)

        ttk.Label(self, text='LM').grid(column=0, row=1,
                sticky='w')

        self.LM_entry = ttk.Entry(self, width=10)
        self.LM_entry.grid(column=1, row = 1)

        ttk.Label(self, text='EM').grid(column=2, row=1,
                sticky='w')

        self.EM_entry = ttk.Entry(self, width=10)
        self.EM_entry.grid(column=3, row=1)

        self.calc_button = ttk.Button(self, text='LM->EM',
                command=self.lm2em)
        self.calc_button.grid(column=0, row=2, columnspan=2)

        self.calc_button = ttk.Button(self, text='LM<-EM',
                command=self.em2lm)
        self.calc_button.grid(column=2, row=2, columnspan=2)

        self.result_frame = ttk.LabelFrame(self, text='Result',
                height=100)
        self.result_frame.grid(column=0, row=3, columnspan=4, sticky='nesw')

# TODO:  Result should be put out with three post-comma digits only.  Double brackets are not needed.

        self.result_label = ttk.Label(self.result_frame, text='')
        self.result_label.grid(column=0, row=0)

#----------------------------------------------------------------------

        ttk.Label(self, text='Control points').grid(column=0, row=4,
                columnspan=4)

        ttk.Label(self, text='LM1').grid(column=0, row=5,
                sticky='w')
        self.lm1_entry = ttk.Entry(self, width=10)
        self.lm1_entry.grid(column=1, row = 5)

        ttk.Label(self, text='EM1').grid(column=2, row=5,
                sticky='w')
        self.em1_entry = ttk.Entry(self, width=10)
        self.em1_entry.grid(column=3, row=5)

        ttk.Label(self, text='LM2').grid(column=0, row=6,
                sticky='w')
        self.lm2_entry = ttk.Entry(self, width=10)
        self.lm2_entry.grid(column=1, row = 6)

        ttk.Label(self, text='EM2').grid(column=2, row=6,
                sticky='w')
        self.em2_entry = ttk.Entry(self, width=10)
        self.em2_entry.grid(column=3, row=6)

        ttk.Label(self, text='LM3').grid(column=0, row=9,
                sticky='w')
        self.lm3_entry = ttk.Entry(self, width=10)
        self.lm3_entry.grid(column=1, row = 9)

        ttk.Label(self, text='EM3').grid(column=2, row=9,
                sticky='w')
        self.em3_entry = ttk.Entry(self, width=10)
        self.em3_entry.grid(column=3, row=9)

#----------------------------------------------------------------------

        self.calc_button = ttk.Button(self, text='Prepare LM2EM',
                command=self.prepareLM2EM)
        self.calc_button.grid(column=0, row=10, columnspan=2)

        self.answer_lm2em_frame = ttk.LabelFrame(self, text='Transform',
                height=100)
        self.answer_lm2em_frame.grid(column=0, row=11, columnspan=2, sticky='nesw')

        self.answer_lm2em_label = ttk.Label(self.answer_lm2em_frame, text='')
        self.answer_lm2em_label.grid(column=0, row=0)

        self.calc_button = ttk.Button(self, text='Prepare EM2LM',
                command=self.prepareEM2LM)
        self.calc_button.grid(column=2, row=10, columnspan=2)

        self.answer_em2lm_frame = ttk.LabelFrame(self, text='Transform',
                height=100)
        self.answer_em2lm_frame.grid(column=2, row=11, columnspan=2, sticky='nesw')

        self.answer_em2lm_label = ttk.Label(self.answer_em2lm_frame, text='')
        self.answer_em2lm_label.grid(column=1, row=0)

# TODO:  Offset should also be put out here.

#         ttk.Separator(self, orient='horizontal').grid(column=0,
#                 row=3, columnspan=4, sticky='ew')

        # Labels that remain constant throughout execution.

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

#----------------------------------------------------------------------
#----------------------------------------------------------------------
#----------------------------------------------------------------------


if __name__ == '__main__':
    root = tkinter.Tk()
    Adder(root)
    root.mainloop()
