from tkinter import *



class Window:
    def __init__(self,title="Grand window",icon=None,resizable=(False,False),width,height,location_x,location_y):
        self.root = Tk()
        self.root.title(title)
        self.root.iconbitmap(icon)
        self.root.resizable(resizable[0],resizable[1])

        self.root.width = width
        self.root.height = height
        self.root.location_x = location_x
        self.root.location_y = location_y

        self.root.size = self.root.width + "x" + self.root.height
        self.root.location = "+" + self.root.location_x + "+" + self.root.location_y

        if icon:
            self.root.iconbitmap(icon)

        self.root.geometry(self.root.size + self.root.location)





window = Tk()
window.title("Graund window")
window.iconbitmap("tomatos_logo_32.ico")

window.resizable(True,True)

window_width = "400"
window_height = "200"
window_location_x = "400"
window_location_y = "200"

window_size = window_width+"x"+window_height
window_location ="+"+window_location_x+"+"+window_location_y

window.geometry(window_size+window_location)

window.mainloop()






if __name__ == '__main__':
    #print_hi('PyCharm')
    print("start")
