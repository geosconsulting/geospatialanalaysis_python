from Tkinter import *
from wx.lib.masked import combobox

class Application(Frame):
    def funzioneSaluto(self):
        print("hi there, everyone!")

    def createWidgets(self):
        
        self.chiudiFinestra = Button(self)
        self.chiudiFinestra["text"] = "Esci"
        self.chiudiFinestra["fg"]   = "red"
        self.chiudiFinestra["command"] =  self.quit
        self.chiudiFinestra.pack({"side": "left"})

        self.saluta = Button(self)
        self.saluta["text"] = "Saluta",
        self.saluta["command"] = self.funzioneSaluto
        self.saluta.pack({"side": "left"})
        

    def __init__(self, master=None):
        Frame.__init__(self, master)        
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.master.title('La Finestrella')
app.master.minsize(200, 60)
app.master.maxsize(300, 120)
app.mainloop()
root.destroy()
