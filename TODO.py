#the to do list

from tkinter import *
from PIL import Image, ImageTk
#from tkinter import ttk



class Todo :

    def __init__(self, root, bg, main_text, text) :

        self.root = root
        self.bg = bg
        self.main_text = main_text
        self.text = text
        self.root.title("TO-DO LIST")
        self.root.geometry("1280x760")
        self.root.iconbitmap("icone.png")
        
        def add() : #To add a task.

            content = self.text.get(1.0, END)
            self.main_text.insert(END, content)
            
            with open ("donnees\\fichiers.txt", "a") as fichier :

                fichier.write(content)
                fichier.seek(0)

            self.text.delete(1.0, END)

        def delete() : #To delete a task.

            delete_t = self.main_text.curselection()
            look = self.main_text.get(delete_t)

            with open ("donnees\\fichiers.txt", "r+") as file :

                lines = file.readlines()
                file.seek(0)

                for line in lines :

                    item = str(look)

                    if item not in line :

                        file.write(line)

                    file.truncate()

            self.main_text.delete(delete_t)

        def complete() : #To mark a task as completed

            with open ("donnees\\fichiers.txt", "r+") as monfichier :

                lines = monfichier.readlines()
                monfichier.seek(0)

                item = ""

                for line in lines :

                    line = item
                    monfichier.write(item)
                    monfichier.truncate()

            self.main_text.delete(0, END)

        def credits_() :

            self.label_b = Label(self.root, image = self.bg)
            self.label_b.place(x = 0, y = 0)

            self.label = Label(self.root, text = "Made by Lula Jonathan", font = "ariel, 20 italic bold", width = 20, bd = 5, bg = "blue", fg = "white")
            self.label.place(x = 500, y = 350)

            self.button_back = Button(self.root, text = "Back", font = "ariel, 20 bold", width = 10, bd = 5, bg = "blue", fg = "white", command = view_1)
            self.button_back.place(x = 40, y = 690)
        
        def view_2() : 

            #self.root.configure(bg = "white")

            self.label_b = Label(self.root, image = self.bg)
            self.label_b.place(x = 0, y = 0)
            
            self.label = Label(self.root, text = "TO-DO LIST", font = "ariel, 25 bold", width = 64, bd = 5, bg = "blue", fg = "white")
            #self.label.pack(side = 'top', fill = BOTH)
            self.label.place(x = 0, y =0)

            self.label_1 = Label(self.root, text = "Add a task", font = "ariel, 20 bold", width = 26, bd = 5, bg = "blue", fg = "white")
            self.label_1.place(x = 40, y = 100)

            self.label_2 = Label(self.root, text = "Your tasks", font = "ariel, 20 bold", width = 29, bd = 5, bg = "blue", fg = "white")
            self.label_2.place(x = 700, y = 100)

            self.main_text = Listbox(self.root, height = 15, bd = 8, width = 33, font = "ariel, 20")
            self.main_text.place(x = 700, y = 150)

            self.text = Text(self.root, bd = 5, height = 2, width = 30, font = "ariel, 20")
            self.text.place(x = 40, y = 150)
        
            
            self.button_add = Button(self.root, text = "Add task", font = "ariel, 20 bold", width = 10, bd = 5, bg = "blue", fg = "white", command = add)
            self.button_add.place(x = 40, y = 250)

            self.button_delete = Button(self.root, text = "Delete task", font = "ariel, 20 bold", width = 10, bd = 5, bg = "blue", fg = "white", command = delete)
            self.button_delete.place(x = 40, y = 350)

            self.button_complete = Button(self.root, text = "List completed", font = "ariel, 20 bold", width = 15, bd = 5, bg = "blue", fg = "white", command = complete)
            self.button_complete.place(x = 40, y = 450)

            self.button_back = Button(self.root, text = "Back", font = "ariel, 20 bold", width = 10, bd = 5, bg = "blue", fg = "white", command = view_1)
            self.button_back.place(x = 40, y = 690)

            with open ("donnees\\fichiers.txt", "r") as mfichier :

                read = mfichier.readlines()

            for i in read :

               ready = i.split()
               self.main_text.insert(END, ready)

        def view_1() :
            
            self.label_b = Label(self.root, image = self.bg)
            self.label_b.place(x = 0, y = 0)

            self.label_1 = Label(self.root, text = "Welcome", font = "ariel, 30 bold", width = 15, bd = 5, bg = "blue", fg = "white")
            self.label_1.place(x = 450, y = 30)

            self.button_start = Button(self.root, text = "Get start", font = "ariel, 20 bold", width = 10, bd = 5, bg = "blue", fg = "white", command = view_2)
            self.button_start.place(x = 550, y = 450)

            self.button_credits = Button(self.root, text = "Credits", font = "ariel, 20 bold", width = 10, bd = 5, bg = "blue", fg = "white", command = credits_)
            self.button_credits.place(x = 40, y = 690)

        view_1()
        


def main() :

    root = Tk()
    bg = Image.open("icone.png")
    main_text = Listbox()
    text = Text()

    resize_bg = bg.resize((1280, 760))
    final_bg = ImageTk.PhotoImage(resize_bg)
    
    fenetre = Todo(root, final_bg, main_text, text)
    root.mainloop()
