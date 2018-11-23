from modules import *
import functions 

class Application:
    def __init__(self, master):
        self.frmMaster = Frame()
        self.frmMaster.pack()

        self.frmFiltes = Frame(self.frmMaster)
        self.frmFiltes.pack(side="right", padx="10", pady="10")

        self.frmImages = Frame(self.frmMaster)
        self.frmImages.pack(side="left", padx="10", pady="10")

        self.frmOptions = Frame(self.frmMaster)
        self.frmOptions.pack(side="bottom", padx="10", pady="10")

        self.lblImageOriginal = Label(self.frmMaster)
        self.lblImageOriginal.pack(side="left", fill="both", expand="no", padx="10", pady="10")

        self.lblImageOutput = Label(self.frmMaster)
        self.lblImageOutput.pack(side="right", fill="both", expand="no", padx="10", pady="10")

        self.lblTextOutputAnswer = Label(self.frmMaster, borderwidth=2, relief="solid")
        self.lblTextOutputAnswer.pack(side="bottom", fill="both", expand="no", padx="10", pady="10")

        self.lblTextOutputAnswerText = Label(self.frmMaster, text="Answer:")
        self.lblTextOutputAnswerText.pack(side="bottom", fill="both", expand="no", padx="10", pady="10")

        self.lblTextOutputExpected = Label(self.frmMaster, borderwidth=2, relief="solid")
        self.lblTextOutputExpected.pack(side="bottom", fill="both", expand="no", padx="10", pady="10")

        self.lblTextOutputExpectedText = Label(self.frmMaster, text="Expected:")
        self.lblTextOutputExpectedText.pack(side="bottom", fill="both", expand="no", padx="10", pady="10")

        self.btnImageSelect = Button(self.frmOptions, text="Select an image", command= lambda: (functions.selectImage(self),		self.btnImageSelect.configure(state = DISABLED)))
        self.btnImageSelect.pack(side="left", fill="both", expand="no", padx="10", pady="10") 

        self.btnSolveImage = Button(self.frmOptions, text="Solve", command= lambda: (functions.showResult()))
        self.btnSolveImage.pack(side="left", fill="both", expand="no", padx="10", pady="10") 

        self.btnThreshold = Button(self.frmFiltes, text="Threshold", command = lambda : functions.applyThresholdImage())
        self.btnThreshold.pack(side="top", fill="both", expand="no", padx="10", pady="10")

        self.btnTeste01 = Button(self.frmFiltes, text="Solve From Letters", command = lambda : functions.solveFromLetters())
        self.btnTeste01.pack(side="top", fill="both", expand="no", padx="10", pady="10")

        self.btnTeste02 = Button(self.frmFiltes, text="teste02")
        self.btnTeste02.pack(side="top", fill="both", expand="no", padx="10", pady="10")

        self.btnTeste03 = Button(self.frmFiltes, text="teste03")
        self.btnTeste03.pack(side="top", fill="both", expand="no", padx="10", pady="10")

        self.btnTeste04 = Button(self.frmFiltes, text="teste04")
        self.btnTeste04.pack(side="top", fill="both", expand="yes", padx="10", pady="10")

root = Tk()
root.title("TayCaptha")

Application(root)
root.mainloop()