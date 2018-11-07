from modules import *

def selectImage(self):
        path = filedialog.askopenfilename()
        image = cv2.imread(path)
        #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = np.asarray(image)
        image = ImageTk.PhotoImage(file=path)

        self.frmImageOriginal = Label(self.frmMaster)
        self.frmImageOriginal.image = image
        self.frmImageOriginal.configure(image = image)
        self.frmImageOriginal.pack(side = "bottom", fill = "both", expand = "yes")
        self.btnImageSelect.configure(state = DISABLED)

def applyThresholdImage(self):
    image = self.frmImageOriginal.cget('image')
    filters.thresholdImage(image)