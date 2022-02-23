# imports
from imports import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(
    ChromeDriverManager().install(), options=chrome_options)

# Color and fonts
dcolor = '#111111'
frameColor = '#222222'
widFont = 'helvetica bold'

# Basic buildup
root = tk.Tk()
root.geometry('800x600')
root.configure(background=dcolor)
root.resizable(0, 0)
root.title('Pg Searcher')


# Menu Bar
def onOpen():
    global chosendir
    chosendir = filedialog.askopenfilename(
        initialdir="/", title="Open file", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))


def onSave():
    global savedfiles
    savedfiles = filedialog.asksaveasfilename(initialdir="/", title="Save as",
                                              filetypes=(("Text files", "*.txt"), ("All files", "*.*")))


menubar = tk.Menu()
filemenu = tk.Menu(menubar, tearoff=0)
filemenuHelp = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=onOpen)
filemenu.add_command(label="Save", command=onSave)
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Help", menu=filemenuHelp)
filemenuHelp.add_command(label="Help")
filemenuHelp.add_command(label="About")
root.config(menu=menubar)


# Frame, labels, entries
vert1 = Frame(root, bg=frameColor, height=400, width=500)
vert1.place(relx=0.50, rely=0.50, anchor='center')
vert1.grid_columnconfigure((0), weight=1)
vert1.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
vert1.grid_propagate(False)

Label1 = Label(vert1, text="Your query", height=2, fg='white',
               bg=frameColor, font=(widFont, 15))
Label2 = Label(vert1, text="The amount of pages you want to search",
               height=2, fg='white', bg=frameColor, font=(widFont, 15))


Entry1 = Entry(vert1, width=40, font=(widFont, 15))
Entry2 = Entry(vert1, width=40, font=(widFont, 15))


Label1.grid(row=0, column=0, padx=5)
Entry1.grid(row=1, column=0, padx=5)
Label2.grid(row=2, column=0, padx=5)
Entry2.grid(row=3, column=0, padx=5)


def getInput():
    global inp1, inp2
    inp1 = Entry1.get()
    inp2 = int(Entry2.get())

    for page in range(1, inp2):
        url = "http://www.google.com/search?q=" + \
            inp1 + "&start=" + str((inp2 - 1) * 10)
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        search = soup.find_all('div', class_="yuRUbf")
        for h in search:
            print((h.a.get('href')), file=open(chosendir, 'a'))


# Button
submitButton = Button(vert1, width=10, text='Submit',
                      font=(widFont, 15), command=getInput)
submitButton.grid(row=4, column=0, pady=5)


# Mainloop
root.mainloop()
