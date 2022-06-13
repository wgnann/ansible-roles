import tkinter

class brightController:
    def __init__(self):
        window = tkinter.Tk()
        frame = tkinter.Frame(window)
        frame.pack(padx=10, pady=10)
        label = tkinter.Label(frame, text="Controle de brilho", height=2)
        label.pack()
        self.slider = tkinter.Scale(frame, from_=100, to=255, orient="horizontal", command=self.setBrightness)
        self.slider.set(self.getBrightness())
        self.slider.pack()
        button = tkinter.Button(frame, text="Redefinir")
        button.bind("<Button-1>", self.resetBrightness)
        button.pack()
        window.mainloop()

    def getBrightness(self):
        file = open("/sys/class/backlight/radeon_bl0/brightness", "r")
        brightness = file.read()
        file.close()
        return brightness.strip()

    def setBrightness(self, event):
        brightness = str(self.slider.get())
        file = open("/sys/class/backlight/radeon_bl0/brightness", "w")
        file.write(brightness)
        file.close()

    def resetBrightness(self, event):
        self.slider.set(100)

def main():
    brightController()
main()
