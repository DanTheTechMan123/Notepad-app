#these 2 imports allow me to make a gui and access files
import tkinter as tk
import os

#this sets up the application window
window = tk.Tk()
window.title("Word processing")
window.configure(width=500, height=400)

#these next 4 functions are activated by the button
def save():
    #another function that opens a text file, puts information in, and then saves
    def action():
        #I get the text from the textbox
        fin = textentry.get("1.0","end")
        input = text.get()
        #I open the text file with an intention to write
        f = open(input+".txt", "w+")
        f.write(fin)
        #closes text file and closes popup window
        f.close()
        popup.destroy()
    #this is a popup window that allows you to enter a filename to save
    popup = tk.Tk()
    popup.title("Save as")
    popup.configure(width=100,height=100)
    lab = tk.Label(popup, text="Enter txt file name:")
    lab.pack()
    text = tk.Entry(popup)
    text.pack()
    but = tk.Button(popup, text="Submit",command=action)
    but.pack()
    popup.mainloop()

def opens():
    #another function that opens a text file and reads information
    def action():
        input = text.get()
        f = os.path.isfile(input + ".txt")
        #checks if filename exists
        if f == True:
            file = open(input+".txt", "r+")
            textentry.delete(1.0,"end")
            textentry.insert(1.0,file.read())
            popup.destroy()
        else:
            text.delete(0, "end")
            text.insert(0, "That file doesn't exist.")
    #popup window
    popup = tk.Tk()
    popup.title("Open")
    popup.configure(width=100, height=100)
    lab = tk.Label(popup, text="Enter txt file name:")
    lab.pack()
    text = tk.Entry(popup)
    text.pack()
    but = tk.Button(popup, text="Submit", command=action)
    but.pack()
    #I don't terminate this time incase of wrond filename
    popup.mainloop()

def words():
    string = textentry.get("1.0", "end")
    if string == "":
        label2['text'] = "Words: 0"
    else:
        #splits the string into an array of words that are space split
        lis = string.split(" ")
        #the length of this list determines the # of words
        length = len(lis)
        label2['text'] = "Words: " + str(length)

def rep_o():
    string = textentry.get("1.0","end")
    f = find.get()
    r = replace.get()
    #gets the number of times the string you want to find appears in the text
    count = string.count(f)
    if count == 0:
        find.delete(0, "end")
        find.insert(0, "No instances were found")
    else:
        #replaces all instances of the finding string with the replace
        string = string.replace(f, r, 1) #does it once
        textentry.delete(1.0,"end")
        textentry.insert(1.0,string)

def rep():
    string = textentry.get("1.0","end")
    f = find.get()
    r = replace.get()
    count = string.count(f)
    if count == 0:
        find.delete(0, "end")
        find.insert(0, "No instances were found")
    else:
        string = string.replace(f, r) #does all at once
        textentry.delete(1.0,"end")
        textentry.insert(1.0,string)
    
#This is a text widget from the import
label = tk.Label(window, text="Word processing")
label.pack(pady = 10) #gives you y coordinate spacing

#Button widget from the import
button = tk.Button(window,text="Save", command=save) #calls on above functions
button.pack(side="top", pady = 10)

button2 = tk.Button(window,text="Open", command=opens)
button2.pack(side="top", pady= 10)

#text field widget from import
textentry = tk.Text(window,  bg="white")
textentry.pack(side="left", padx=10, pady = 10)


button4 = tk.Button(window, text = "Replace one", command=rep_o)
button4.pack(side="bottom", pady = 10, padx = 10)

button5 = tk.Button(window, text = "Replace all", command=rep)
button5.pack(side="bottom", pady=10, padx = 10)

#text input widget from import
replace = tk.Entry(window)
replace.pack(side="bottom", pady=10, padx = 10)

label4 = tk.Label(window, text="Replace with: ")
label4.pack(side="bottom", pady=10, padx = 10)

find = tk.Entry(window)
find.pack(side="bottom", pady=10, padx = 10)

label3 = tk.Label(window, text="Find instances of: ")
label3.pack(side="bottom", pady=10, padx = 10)

la = tk.Label(window, text="Find and replace")
la.pack(side="bottom", pady=10, padx = 10)


button3 = tk.Button(window,text="Get word count", command=words)
button3.pack(side="bottom", pady=10, padx = 10)

label2 = tk.Label(window, text="Words: ")
label2.pack(side="bottom", pady=10, padx = 10)


window.mainloop() #this makes the window run all of these commands
#as long as the window is open
