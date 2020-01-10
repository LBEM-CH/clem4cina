# #!/usr/local/bin/python3

# run on OSX:
# xcode-select --install
# brew install tcl-tk
# brew uninstall python
# brew install python --with-tcl-tk
# pip install --upgrade pip
# pip install matplotlib
# pip install numpy

import tkinter 
from tkinter import ttk
from tkinter import *
import numpy as np
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import tkinter.simpledialog



class Adder(ttk.Frame):
    """The adders gui and functions."""
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.init_gui()
        self.counter = 1
        self.counter1 = 1
        self.pos = []
        self.pos1 = []
        

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

    def lm2em_5p(self):

        lm1 = np.array(self.LM1_entry.get().split(',')).astype(np.float).reshape((1,2))
        lm2 = np.array(self.LM2_entry.get().split(',')).astype(np.float).reshape((1,2))
        lm3 = np.array(self.LM3_entry.get().split(',')).astype(np.float).reshape((1,2))
        lm4 = np.array(self.LM4_entry.get().split(',')).astype(np.float).reshape((1,2))
        lm5 = np.array(self.LM5_entry.get().split(',')).astype(np.float).reshape((1,2))
        lm = np.array([lm1, lm2, lm3, lm4, lm5])


        all_coordinates = np.empty([1,2], dtype = float)
        x_result = np.empty([1,2], dtype = float)

        for x in lm:

            print("Input LM coordinates: ",x)
            lm = x - LM_off
            x_result = np.matmul(lm,x_lm2em) + EM_off
            all_coordinates = np.vstack((all_coordinates, x_result))
            final_coordinates = all_coordinates[1:,:]

            if len(final_coordinates) == 5:
                self.result_label['text'] = final_coordinates
                print("Output EM coordinates: ",self.result_label['text'])   
       
 

    def em2lm_5p(self) : 
        
        em1 = np.array(self.EM1_entry.get().split(',')).astype(np.float).reshape((1,2))
        em2 = np.array(self.EM2_entry.get().split(',')).astype(np.float).reshape((1,2))
        em3 = np.array(self.EM3_entry.get().split(',')).astype(np.float).reshape((1,2))
        em4 = np.array(self.EM4_entry.get().split(',')).astype(np.float).reshape((1,2))
        em5 = np.array(self.EM5_entry.get().split(',')).astype(np.float).reshape((1,2))
        em = np.array([em1, em2, em3, em4, em5])

        all_coordinates = np.empty([1,2], dtype = float)
        x_result = np.empty([1,2], dtype = float)

        for x in em:

            print("Input LM coordinates: ",x)
            em = x - EM_off
            x_result = np.matmul(em,x_em2lm) + LM_off
            all_coordinates = np.vstack((all_coordinates, x_result))
            final_coordinates = all_coordinates[1:,:]

            if len(final_coordinates) == 5:
                self.result_label['text'] = final_coordinates
                print("Output EM coordinates: ",self.result_label['text'])   

            

    def em2lm(self):
        global invx
        em = np.array(self.EM_entry.get().split(',')).astype(np.float).reshape((1,2))
        print("Input EM coordinates: ",em)
        em = em - EM_off
        self.result_label['text'] = np.matmul(em,x_em2lm) + LM_off
        print("Output LM coordinates: ",self.result_label['text'])

    def clear_text_LM(self):
        self.lm1_entry.delete(0, 'end')
        self.lm2_entry.delete(0, 'end')
        self.lm3_entry.delete(0, 'end')
        self.LM1_entry.delete(0, 'end')
        self.LM2_entry.delete(0, 'end')
        self.LM3_entry.delete(0, 'end')
        self.LM4_entry.delete(0, 'end')
        self.LM5_entry.delete(0, 'end')

    def clear_text_EM(self):
        self.em1_entry.delete(0, 'end')
        self.em2_entry.delete(0, 'end')
        self.em3_entry.delete(0, 'end')
        self.EM1_entry.delete(0, 'end')
        self.EM2_entry.delete(0, 'end')
        self.EM3_entry.delete(0, 'end')
        self.EM4_entry.delete(0, 'end')
        self.EM5_entry.delete(0, 'end')


    def save(self):
       
        f = asksaveasfilename(defaultextension= ".txt")

        if f is None:
            return

        LM1 = self.LM1_entry.get()
        LM2 = self.LM2_entry.get()
        LM3 = self.LM3_entry.get()
        LM4 = self.LM4_entry.get()
        LM5 = self.LM5_entry.get()
        LM = np.array([LM1, LM2, LM3, LM4, LM5])

        with open(f, "w+") as file:
            for x in LM:
                file.write(x)
                file.write("\n")
            

    def load_previous(self):

        f = askopenfilename(defaultextension= ".txt")

        LM1 = self.LM1_entry.delete(0, 'end')
        LM2 = self.LM2_entry.delete(0, 'end')
        LM3 = self.LM3_entry.delete(0, 'end')
        LM4 = self.LM4_entry.delete(0, 'end')
        LM5 = self.LM5_entry.delete(0, 'end')
        LM = np.array([LM1, LM2, LM3, LM4, LM5])
        text = []

        with open(f, "r") as file:
            array = []
            for line in file:
                line = line.strip('\n')
                array.append(line)
            
        self.LM1_entry.insert(0, array[0])
        self.LM2_entry.insert(0, array[1])
        self.LM3_entry.insert(0, array[2])
        self.LM4_entry.insert(0, array[3])
        self.LM5_entry.insert(0, array[4])  

    

    #def get_coord(self, event):
     #   global coords
     #   coords = "{0},{1}".format(event.x, event.y)
      #  print(coords)


    def load_image(self):

        global preview
        global image
        global canvas

        preview = Toplevel()

        button1 = ttk.Button(preview, text = "Control points", command = self.choose3cp)
        button1.pack(side='top', anchor = 'n')

        button2 = ttk.Button(preview, text = "5 ROIs", command = self.choose5ROI)
        button2.pack(side='top', anchor = 's')

        #preview.bind("<Button-1>", self.get_coord)

        preview.geometry('1000x900')
        canvas = Canvas(preview,cursor="plus", width=900,height=900)
        canvas.pack()
        canvas.config(scrollregion=canvas.bbox(ALL))

        file_name=askopenfilename(filetypes=[('TIF FILES', '.tif')])
        pilImage = Image.open(file_name)  
        pilImage.thumbnail((900,900), Image.ANTIALIAS)

        image = ImageTk.PhotoImage(pilImage)
        imagesprite = canvas.create_image(0,0,image=image, anchor="nw")


    def choose3cp(self):

        tkinter.messagebox.showinfo("Instructions", "Click control points: \n" 
                                            "1) LM1 \n"
                                            "2) LM2 \n"
                                            "3) LM3\n"
                                            "4) click to press enter")

        canvas.bind("<Button-1>", self.imgClick3p)
        canvas.delete("numbers_cp")

    def imgClick3p(self, event):

        lm1 = self.lm1_entry.delete(0, 'end')
        lm2 = self.lm2_entry.delete(0, 'end')
        lm3 = self.lm3_entry.delete(0, 'end')
        lm = np.array([lm1, lm2, lm3])



        if self.counter < 4:
            x = canvas.canvasx(event.x)
            y = canvas.canvasy(event.y)
            text_id = canvas.create_text(x,y, text= self.counter, font=("calibri", 12), fill="red2", tag="numbers_cp")
            self.pos.append("{0},{1}".format(event.x, event.y))
            self.counter += 1

        else :
            self.lm1_entry.insert(0, (self.pos[0]))
            self.lm2_entry.insert(0, (self.pos[1]))
            self.lm3_entry.insert(0, (self.pos[2]))
            

            canvas.unbind("<Button 1>")
            self.counter = 1
            self.pos.clear()

       
    def choose5ROI(self):

        tkinter.messagebox.showinfo("Instructions", "Click ROI points: \n" 
                                            "1) LM1 \n"
                                            "2) LM2 \n"
                                            "3) LM3 \n"
                                            "4) LM4 \n"
                                            "5) LM5 \n"
                                            "6) click to press enter")

        canvas.bind("<Button-1>", self.imgClick5p)
        canvas.delete("numbers_roi")


    def imgClick5p(self, event):

        
        LM1 = self.LM1_entry.delete(0, 'end')
        LM2 = self.LM2_entry.delete(0, 'end')
        LM3 = self.LM3_entry.delete(0, 'end')
        LM4 = self.LM4_entry.delete(0, 'end')
        LM5 = self.LM5_entry.delete(0, 'end')

        if self.counter1 < 6:
            x = canvas.canvasx(event.x)
            y = canvas.canvasy(event.y)
            text_id = canvas.create_text(x,y, text= self.counter1, font=("calibri", 12), fill="darkgreen", tag="numbers_roi")
            self.pos1.append("{0},{1}".format(event.x, event.y)) 
            self.counter1 += 1

        else :
            self.LM1_entry.insert(0, (self.pos1[0]))
            self.LM2_entry.insert(0, (self.pos1[1]))
            self.LM3_entry.insert(0, (self.pos1[2]))             
            self.LM4_entry.insert(0, (self.pos1[3]))
            self.LM5_entry.insert(0, (self.pos1[4]))

            canvas.unbind("<Button 1>")
            self.counter1 = 1
            self.pos1.clear()

            
        
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

        ttk.Label(self, text='LM1').grid(column=0, row=1,
                sticky='w')

        self.LM1_entry = ttk.Entry(self, width=10)
        self.LM1_entry.grid(column=1, row = 1)

        ttk.Label(self, text='LM2').grid(column=0, row=2,
                sticky='w')

        self.LM2_entry = ttk.Entry(self, width=10)
        self.LM2_entry.grid(column=1, row = 2)


        ttk.Label(self, text='LM3').grid(column=0, row=3,
                sticky='w')

        self.LM3_entry = ttk.Entry(self, width=10)
        self.LM3_entry.grid(column=1, row = 3)


        ttk.Label(self, text='LM4').grid(column=0, row=4,
                sticky='w')

        self.LM4_entry = ttk.Entry(self, width=10)
        self.LM4_entry.grid(column=1, row = 4)


        ttk.Label(self, text='LM5').grid(column=0, row=5,
                sticky='w')

        self.LM5_entry = ttk.Entry(self, width=10)
        self.LM5_entry.grid(column=1, row = 5)




        ttk.Label(self, text='EM1').grid(column=2, row=1,
                sticky='w')

        self.EM1_entry = ttk.Entry(self, width=10)
        self.EM1_entry.grid(column=3, row=1)

        ttk.Label(self, text='EM2').grid(column=2, row=2,
                sticky='w')

        self.EM2_entry = ttk.Entry(self, width=10)
        self.EM2_entry.grid(column=3, row = 2)


        ttk.Label(self, text='EM3').grid(column=2, row=3,
                sticky='w')

        self.EM3_entry = ttk.Entry(self, width=10)
        self.EM3_entry.grid(column=3, row = 3)


        ttk.Label(self, text='EM4').grid(column=2, row=4,
                sticky='w')

        self.EM4_entry = ttk.Entry(self, width=10)
        self.EM4_entry.grid(column=3, row = 4)


        ttk.Label(self, text='EM5').grid(column=2, row=5,
                sticky='w')

        self.EM5_entry = ttk.Entry(self, width=10)
        self.EM5_entry.grid(column=3, row = 5)



        self.calc_button = ttk.Button(self, text='LM->EM',
                command=self.lm2em_5p)
        self.calc_button.grid(column=0, row=6, columnspan=2)

        self.calc_button = ttk.Button(self, text='LM<-EM',
                command=self.em2lm_5p)
        self.calc_button.grid(column=2, row=6, columnspan=2)

        self.result_frame = ttk.LabelFrame(self, text='Result',
                height=100)
        self.result_frame.grid(column=0, row=7, columnspan=4, sticky='nesw')

# TODO:  Result should be put out with three post-comma digits only.  Double brackets are not needed.

        self.result_label = ttk.Label(self.result_frame, text='')
        self.result_label.grid(column=0, row=0)

#----------------------------------------------------------------------

        ttk.Label(self, text='Control points').grid(column=0, row=8,
                columnspan=4)

        ttk.Label(self, text='LM1').grid(column=0, row=9,
                sticky='w')
        self.lm1_entry = ttk.Entry(self, width=10)
        self.lm1_entry.grid(column=1, row = 9)

        ttk.Label(self, text='EM1').grid(column=2, row=9,
                sticky='w')
        self.em1_entry = ttk.Entry(self, width=10)
        self.em1_entry.grid(column=3, row=9)

        ttk.Label(self, text='LM2').grid(column=0, row=10,
                sticky='w')
        self.lm2_entry = ttk.Entry(self, width=10)
        self.lm2_entry.grid(column=1, row = 10)

        ttk.Label(self, text='EM2').grid(column=2, row=10,
                sticky='w')
        self.em2_entry = ttk.Entry(self, width=10)
        self.em2_entry.grid(column=3, row=10)

        ttk.Label(self, text='LM3').grid(column=0, row=11,
                sticky='w')
        self.lm3_entry = ttk.Entry(self, width=10)
        self.lm3_entry.grid(column=1, row = 11)

        ttk.Label(self, text='EM3').grid(column=2, row=11,
                sticky='w')
        self.em3_entry = ttk.Entry(self, width=10)
        self.em3_entry.grid(column=3, row=11)

#----------------------------------------------------------------------

        self.calc_button = ttk.Button(self, text='Prepare LM2EM',
                command=self.prepareLM2EM)
        self.calc_button.grid(column=0, row=12, columnspan=2)

        self.answer_lm2em_frame = ttk.LabelFrame(self, text='Transform',
                height=100)
        self.answer_lm2em_frame.grid(column=0, row=13, columnspan=2, sticky='nesw')

        self.answer_lm2em_label = ttk.Label(self.answer_lm2em_frame, text='')
        self.answer_lm2em_label.grid(column=0, row=0)

        self.calc_button = ttk.Button(self, text='Prepare EM2LM',
                command=self.prepareEM2LM)
        self.calc_button.grid(column=2, row=12, columnspan=2)

        self.answer_em2lm_frame = ttk.LabelFrame(self, text='Transform',
                height=100)
        self.answer_em2lm_frame.grid(column=2, row=13, columnspan=2, sticky='nesw')

        self.answer_em2lm_label = ttk.Label(self.answer_em2lm_frame, text='')
        self.answer_em2lm_label.grid(column=1, row=0)
#----------------------------------------------------------------------

        self.calc_button = ttk.Button(self, text='Clear all LM',
                command=self.clear_text_LM)
        self.calc_button.grid(column=0, row=15, columnspan = 2)

        self.calc_button = ttk.Button(self, text='Clear all EM',
                command=self.clear_text_EM)
        self.calc_button.grid(column=2, row=15, columnspan = 2)

        self.calc_button = ttk.Button(self, text='Save ROI as',
                command=self.save)
        self.calc_button.grid(column=0, row=17, columnspan = 2)

        self.calc_button = ttk.Button(self, text='Load ROI', command=self.load_previous)
        self.calc_button.grid(column=2, row=17, columnspan = 2)

        self.calc_button = ttk.Button(self, text='Load image',
                command=self.load_image)
        self.calc_button.grid(column=0, row=18, columnspan = 2)




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
