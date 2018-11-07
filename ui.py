from modules import *

class Application:

    def __init__(self, master=None):

        self.frmMaster = Frame()
        self.frmMaster.pack()

        self.frmImageOriginal = None
        
        self.btnImageSelect = Button(self.frmMaster, text="Select an image", command= lambda: funcs.selectImage(self))
        self.btnImageSelect.pack(side="right", fill="both", expand="yes", padx="10", pady="10") 

        self.btnThreshold = Button(self.frmMaster, text="Threshold", command =  lambda: funcs.applyThresholdImage(self))
        self.btnThreshold.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")

        self.sair = Button(self.frmMaster)

        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "10")
        self.sair["width"] = 5
        self.sair["command"] = self.frmMaster.quit
        self.sair.pack(side="bottom", fill="both",
                            expand="yes", padx="10", pady="10")

root = Tk()
Application(root)
root.mainloop()