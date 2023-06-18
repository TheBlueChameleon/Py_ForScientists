# ============================================================================ #
# dependencies

import numpy as np

import scipy.optimize as sco
import scipy.fft      as scf

import csv

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# ============================================================================ #
# definition of widgets layout

# ---------------------------------------------------------------------------- #
# the main window and its four compartments; globals

root = tk.Tk()
root.title("Data Analyzer")
root.geometry("800x600")

# ---------------------------------------------------------------------------- #
# frames

frameTopL = tk.Frame(root)
frameTopL.grid(row=0, column=0, sticky="NSWE")

frameBtmL = tk.Frame(root)
frameBtmL.grid(row=1, column=0, sticky="NSWE")

frameTopR = tk.Frame(root)
frameTopR.grid(row=0, column=1, sticky="NSWE")

frameBtmR = tk.Frame(root)
frameBtmR.grid(row=1, column=1, sticky="NSWE")

# ---------------------------------------------------------------------------- #
# buttons, text boxes

btns = dict()
txts = dict()

# ============================================================================ #
# global variables

# ---------------------------------------------------------------------------- #
# fit type data

fitNames = ("polynomial of degree", "exponential", "logarithmic", "sinoidal", "gaussian")
fitType = tk.IntVar()

polyDegree = tk.IntVar()
polyDegree.set(1)

paramCount = {
    0 : None,   # polynomial
    1 : 4,      # exponential
    2 : 4,      # logarithmic
    3 : 4,      # sinoidal
    4 : 4       # gaussian
}

currentFitParams = {
    "Label" : "Fit",
    "Color" : "#000000FF",
    "Coeffs" : [],
}
fits = []

fitFunctions = [
    lambda x, *params    : np.polynomial.Polynomial(params)(x),
    lambda x, a, b, c, d : a * np.exp( b * (x - c)   ) + d,
    lambda x, a, b, c, d : a * np.log( b * (x - c)   ) + d,
    lambda x, a, b, c, d : a * np.sin( b * (x - c)   ) + d,
    lambda x, a, b, c, d : a * np.exp(-b * (x - c)**2) + d
]

def setCurrentFitParams () :
    global currentFitParams
    
    currentFitParams["Label"] = fitNames[fitType.get()]
    if fitType.get() == 0 : 
        currentFitParams["Label"] += " " + str(polyDegree.get())
    
    N = paramCount[fitType.get()]
    if N == None :
        N = polyDegree.get() + 1
    currentFitParams["Coeffs"] = [1 for i in range(N)]
    
setCurrentFitParams()

# ---------------------------------------------------------------------------- #
# plot data

realDataFig = plt.figure(figsize=(5,3))
fourierDFig = plt.figure(figsize=(5,3))

realDataFig.suptitle("Data and Fits")
realDataPlt = realDataFig.add_subplot()
fourierDFig.suptitle("Fourier Space")
fourierDPlt = fourierDFig.add_subplot()

realDataOriginal       = [[], []]           # list[0]: X-coordinates; list[1]: Y-coordinates
realDataReconstruction = [[], []]           # inverse Fourier transform of the quenched spectrum
fourierDOriginal       = [[], []]
fourierDQuenched       = [[], []]

flagUseReconstruction = False               # only if parts of the Fourier spectrum have been quenched, plot/use the reconstructed data

# ============================================================================ #
# main window definitions

# ---------------------------------------------------------------------------- #
# upper left compartment: fit controls

for i, ft in enumerate(fitNames) :
    tk.Radiobutton(
        frameTopL,
        text=ft,
        var=fitType,
        value=i,
        command=setCurrentFitParams
    ).grid(
        row=i, column=0,
        sticky="W"
    )

tk.Spinbox(
    frameTopL,
    textvar=polyDegree,
    from_=0, to=9,
    width=4,
    wrap=True,
    command=setCurrentFitParams
).grid(
    row=0, column=1,
    sticky="WE"
)

for i, lbl in enumerate(("Load Data", "Clear Data", "Add Fit", "Set Fit Parameters")) :
    btns[lbl] = tk.Button(
        frameTopL,
        text=lbl,
    )
    btns[lbl].grid(
        row=i, column=2,
        sticky="WE"
    )

lstFits = tk.Listbox(
    frameTopL,
    height=8
)
lstFits.grid(
    row=5, column=0,
    rowspan=3,
    columnspan=2,
    sticky="NSWE"
)

for i, lbl in enumerate(("Remove Fit", "Adjust Fit", "View Fit Data")) :
    btns[lbl] = tk.Button(
        frameTopL,
        text=lbl
    )
    btns[lbl].grid(
        row=i+5, column=2,
        sticky="WE"
    )

# ---------------------------------------------------------------------------- #
# lower left compartment: Fourier Space controls

for i, lbl in enumerate(("from", "to")) :
    tk.Label(
        frameBtmL,
        text=lbl
    ).grid(
        row=0, column=2*i
    )
    
    txts[lbl] = tk.Entry(
        frameBtmL,
        width=10
    )
    txts[lbl].grid(
        row=0, column=2*i+1
    )

lbl = "Quench"
btns[lbl] = tk.Button(
    frameBtmL,
    text=lbl
)
btns[lbl].grid(
    row=0, column=4,
    sticky="WE"
)

lstQuench = tk.Listbox(
    frameBtmL,
    height=8
)
lstQuench.grid(
    row=1, column=0,
    rowspan=3,
    columnspan=4,
    sticky="NSWE"
)

for i, lbl in enumerate(("Remove Quench",)) :
    btns[lbl] = tk.Button(
        frameBtmL,
        text=lbl,
    )
    btns[lbl].grid(
        row=i+1, column=4,
        sticky="WE"
    )

# ---------------------------------------------------------------------------- #
# right compartments: data and fit plot, fourierD space plot

realDataCvs = FigureCanvasTkAgg(realDataFig, master=frameTopR)
fourierDCvs = FigureCanvasTkAgg(fourierDFig , master=frameBtmR)

realDataCvs.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
fourierDCvs.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# ============================================================================ #
# generic procs

def updatePlots () :
    realDataPlt.cla()
    fourierDPlt.cla()
    
    realDataPlt.plot(  *realDataOriginal                                 , label="original data", color="#AAAAAAFF" if flagUseReconstruction else "#0000AAFF")
    fourierDPlt.plot(  fourierDOriginal[0], np.abs(fourierDOriginal[1])  , label="original data", color="#AAAAAAFF" if flagUseReconstruction else "#0000AAFF")
    
    for fit in fits :
        realDataPlt.plot( realDataOriginal[0], fit["YData"], label=fit["Label"], color=fit["Color"] )
    
    if flagUseReconstruction :
        realDataPlt.plot(*realDataReconstruction                         , label="quenched data", color="#0000AAFF")
        fourierDPlt.plot(fourierDQuenched[0], np.abs(fourierDQuenched[1]), label="quenched data", color="#0000AAFF")
    
    realDataPlt.legend()
    fourierDPlt.legend()
    
    realDataCvs.draw()
    fourierDCvs.draw()

# ---------------------------------------------------------------------------- #

def loadFile(filename) :
    callback_ResetData(False)
    
    with open(filename, "r") as hFile :
        rdr = csv.reader(hFile, delimiter=",")
        
        for line in rdr :
            realDataOriginal[0].append(float(line[0]))
            realDataOriginal[1].append(float(line[1]))
        
    realDataOriginal[0] = np.array(realDataOriginal[0])
    realDataOriginal[1] = np.array(realDataOriginal[1])
    
    fourierDOriginal[0] = np.arange( len(realDataOriginal[0]) )
    fourierDOriginal[1] = scf.fft(realDataOriginal[1])
    
    updatePlots()

# ---------------------------------------------------------------------------- #

def doQuenches () :
    global flagUseReconstruction
    
    if lstQuench.size() :
        flagUseReconstruction = True
        
        fourierDQuenched[0] = fourierDOriginal[0]
        fourierDQuenched[1] = fourierDOriginal[1].copy()
        
        for lineID in range(lstQuench.size()) :
            line = lstQuench.get(lineID)
            lower, upper = line.split(" to ")
            lower = int(lower)
            upper = int(upper)
            
            for i in range(lower, upper) :
                fourierDQuenched[1][i] = 0
        
        realDataReconstruction[0] = realDataOriginal[0]
        realDataReconstruction[1] = scf.ifft(fourierDQuenched[1]).real
        
    else :
        flagUseReconstruction = False
    
    updatePlots()
    

# ============================================================================ #
# button callbacks and assignment, real data compartment

# ---------------------------------------------------------------------------- #
# Clear Data

def callback_ResetData(update = True) :
    global realDataOriginal
    global realDataReconstruction
    global fourierDOriginal
    global fourierDQuenched
    global fits
    
    realDataOriginal       = [[], []]
    realDataReconstruction = [[], []]
    fourierDOriginal       = [[], []]
    fourierDQuenched       = [[], []]
    
    fits = []
    
    lstFits  .delete(0, tk.END)
    lstQuench.delete(0, tk.END)
    
    if update : updatePlots()

btns["Clear Data"]["command"] = callback_ResetData

# ---------------------------------------------------------------------------- #
# Load Data

def callback_Load() :
    filename = filedialog.askopenfilename(
        filetypes=[
            ("CSV files", "*.csv"),
            ("Text files", "*.txt"),
            ("Any files", "*")
        ]
    )
    
    if len(filename) > 0 :
        callback_ResetData(False)
        loadFile(filename)
    
btns["Load Data"]["command"] = callback_Load

# ---------------------------------------------------------------------------- #
# Add Fit

def callback_AddFit () :
    useX =                                                         realDataOriginal[0]
    useY = realDataReconstruction[1] if flagUseReconstruction else realDataOriginal[1]
    firstGuess = currentFitParams["Coeffs"]
    
    if len(useX) == 0 :
        messagebox.showerror(
            "No Data",
            "No data for fit – load a data file first."
        )
        return
    
    
    popt, pcov = sco.curve_fit(fitFunctions[fitType.get()], useX, useY, p0=firstGuess)
    
    if (pcov == np.inf).any() :
        messagebox.showerror(
            "Failed to fit",
            "Could not find a fit with given settings. Try adjusting the initial parameters."
        )
        return
    
    lstFits.insert(tk.END, currentFitParams["Label"])
    fits.append( currentFitParams.copy() )
    fits[-1]["Coeffs"] = popt
    fits[-1]["Covar"]  = pcov
    fits[-1]["YData"]  = fitFunctions[fitType.get()](useX, *popt)
    
    updatePlots()

btns["Add Fit"]["command"] = callback_AddFit

# ---------------------------------------------------------------------------- #
# Set Fit Parameters

def callback_SetFitParameters () :
    dlg = tk.Toplevel()
    dlg.title("Set Fit Parameters")
    
    framesDlg = []
    for i in range(4) :
        framesDlg.append(tk.Frame(dlg))
        framesDlg[-1].pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    
    tk.Label(framesDlg[0], text="Label").pack(side=tk.LEFT)
    txtLabel = tk.Entry(framesDlg[0])
    txtLabel.insert(0, currentFitParams["Label"])
    txtLabel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    
    tk.Label(framesDlg[1], text="Color").pack(side=tk.LEFT)
    txtColor = tk.Entry(framesDlg[1])
    txtColor.insert(0, currentFitParams["Color"])
    txtColor.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    
    N = paramCount[ fitType.get() ]
    if N == None :
        N = polyDegree.get() + 1
    
    txtCoeffs = []
    for i in range(N) :
        tk.Label(framesDlg[2], text=chr(i + 97)).grid(row = i % 5, column = (i // 5) * 2)
        txtCoeffs.append(tk.Entry(
            framesDlg[2],
        ))
        txtCoeffs[-1].insert(0, str(currentFitParams["Coeffs"][i]))
        txtCoeffs[-1].grid(row = i % 5, column = (i // 5) * 2 + 1)
    
    # ........................................................................ #
    def callback_SetFitParametersOK () :
        global currentFitParams
        
        for i, box in enumerate(txtCoeffs) :
            try :
                currentFitParams["Coeffs"][i] = float(box.get())
                
            except ValueError :
                messagebox.showerror(
                    "Invalid Parameter",
                    "Invalid Parameter for " + chr(i + 97) + ":\n'" + box.get() + "'"
                )
                return
        currentFitParams["Label"] = txtLabel.get()
        currentFitParams["Color"] = txtColor.get()
        
        dlg.destroy()
    # ........................................................................ #
    
    tk.Button(
        framesDlg[3],
        text="ok",
        command = callback_SetFitParametersOK
    ).pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    tk.Button(
        framesDlg[3],
        text="cancel",
        command = lambda : dlg.destroy()
    ).pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    
    dlg.grab_set()
    dlg.mainloop()


btns["Set Fit Parameters"]["command"] = callback_SetFitParameters

# ============================================================================ #
# button callbacks and assignment, fit compartment

# ---------------------------------------------------------------------------- #
# Remove Fit

def callback_RemoveFit () :
    if len( lstFits.curselection() ) == 0 :
        messagebox.showerror(
            "No Fit Selected",
            "No Fit Selected"
        )
        return
    
    ID = lstFits.curselection()[0]
    
    lstFits.delete(ID)
    fits.pop(ID)
    
    updatePlots()

btns["Remove Fit"]["command"] = callback_RemoveFit

# ---------------------------------------------------------------------------- #
# Adjust Fit

def callback_AdjustFit () :
    if len( lstFits.curselection() ) == 0 :
        messagebox.showerror(
            "No Fit Selected",
            "No Fit Selected"
        )
        return
    
    ID = lstFits.curselection()[0]
    
    # ........................................................................ #
    
    dlg = tk.Toplevel()
    dlg.title("Adjust Fit Settings")
    
    framesDlg = []
    for i in range(3) :
        framesDlg.append(tk.Frame(dlg))
        framesDlg[-1].pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    
    tk.Label(framesDlg[0], text="Label").pack(side=tk.LEFT)
    txtLabel = tk.Entry(framesDlg[0])
    txtLabel.insert(0, fits[ID]["Label"])
    txtLabel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    
    tk.Label(framesDlg[1], text="Color").pack(side=tk.LEFT)
    txtColor = tk.Entry(framesDlg[1])
    txtColor.insert(0, fits[ID]["Color"])
    txtColor.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    
    # ........................................................................ #
    
    def callback_AdjustFitOK () :
        global fits
        
        fits[ID]["Label"] = txtLabel.get()
        fits[ID]["Color"] = txtColor.get()
        
        dlg.destroy()
        
        updatePlots()
    
    # ........................................................................ #
    
    tk.Button(
        framesDlg[2],
        text="ok",
        command = callback_AdjustFitOK
    ).pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    tk.Button(
        framesDlg[2],
        text="cancel",
        command = lambda : dlg.destroy()
    ).pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    
    # ........................................................................ #
    
    dlg.grab_set()
    dlg.mainloop()
    

btns["Adjust Fit"]["command"] = callback_AdjustFit

# ---------------------------------------------------------------------------- #
# View Fit Data

def callback_ViewFitData () :
    if len( lstFits.curselection() ) == 0 :
        messagebox.showerror(
            "No Fit Selected",
            "No Fit Selected"
        )
        return
    
    ID = lstFits.curselection()[0]
    
    # ........................................................................ #
    
    dlg = tk.Toplevel()
    dlg.title("View Fit Data")
    
    for i, lbl in enumerate(("Label", "Color", "Coeffs")) :
        tk.Label(
            dlg,
            text = lbl
        ).grid(
            row=i, column=0
        )
        
        tk.Label(
            dlg,
            text = fits[ID][lbl]
        ).grid(
            row=i, column=1
        )
    
    tk.Label(
        dlg,
        text = "Covariance Matrix"
    ).grid(
        row=3, column=0,
        columnspan=2
    )
    
    tk.Label(
        dlg,
        text = fits[ID]["Covar"]
    ).grid(
        row=4, column=0,
        columnspan=2
    )
    
    tk.Button(
        dlg,
        text="OK",
        command = lambda : dlg.destroy()
    ).grid(
        row=5, column=0,
        columnspan=2
    )
    
    # ........................................................................ #
    
    dlg.grab_set()
    dlg.mainloop()

btns["View Fit Data"]["command"] = callback_ViewFitData

# ============================================================================ #
# button callbacks and assignment, Fourier compartment

# ---------------------------------------------------------------------------- #
# Quench

def callback_Quench () :
    rangetext = txts["from"].get() + " to " + txts["to"].get()
    
    try :
        lower = int(txts["from"].get())
        upper = int(txts["to"]  .get())
    except ValueError :
        messagebox.showerror(
            "Invalid Range",
            "Invalid Range:\n" + rangetext
        )
        return
    
    lower, upper = sorted([lower, upper])
    
    N = len(fourierDOriginal[0])
    if (lower < 0) or (upper < 0) or (lower > N) or (upper > N) :
        messagebox.showerror(
            "Invalid Range",
            "Invalid Range:\n" + rangetext
        )
        return
    
    lstQuench.insert(tk.END, rangetext)
    doQuenches()
    
btns["Quench"]["command"] = callback_Quench

# ---------------------------------------------------------------------------- #
# Remove Quench

def callback_RemoveQuench () :
    if len(lstQuench.curselection()) == 0 :
        return
    
    ID = lstQuench.curselection()[0]
    lstQuench.delete(ID)
    doQuenches()

btns["Remove Quench"]["command"] = callback_RemoveQuench

# ============================================================================ #
# go live!

root.mainloop()
