#!/Users/colflah/Documents/src/dataScrapingWebsite/venv/bin/python3

import tkinter
from bs4 import BeautifulSoup
import requests, time

url = "http://www.nytimes.com/"


r = requests.get(url)  # make an HTTP request
r_html = r.text 

soup = BeautifulSoup(r_html, "html.parser")

class simplegui_tk(tkinter.Tk):
	def __init__(self,parent):
		tkinter.Tk.__init__(self,parent)
		self.parent = parent
		self.initialize()


	def initialize(self):
		self.grid()

		self.intro = tkinter.StringVar()
		self.intro.set("This program will search NYTimes.com article titles for keywords.")
		label = tkinter.Label(self,textvariable=self.intro,anchor="w",fg="black",bg="white")
		label.grid(column=0,row=0,columnspan=3,stick='EW')

		self.entryVar = tkinter.StringVar()
		self.entry = tkinter.Entry(self,textvariable=self.entryVar)
		self.entry.grid(column=0,row=1,stick='EW')

		button = tkinter.Button(self,text=u"Search",command=self.OnButtonClick)
		button.grid(column=1,row=1)
		
		self.results = tkinter.StringVar()
		self.results.set("")
		label = tkinter.Label(self,textvariable=self.results,anchor="w",fg="black",bg="white",wraplength=300,justify="left")
		label.grid(column=0,row=2,columnspan=3,stick='EW')

		self.grid_columnconfigure(0,weight=1)
		self.resizable(True,False)

	def OnButtonClick(self):
		keyword = self.entryVar.get()
		"""call code based on self.entryVar.get() and run self.entryVar.set("") """
		index = 0
		for item in soup.find_all("h2"):
			try:
				if "story-heading" in item["class"]:
					storyTitle = item.text # very likely to be a story title
					keywordAllCase = [keyword.upper(), keyword.lower(), keyword.title()]
					if any(word in storyTitle for word in keywordAllCase):
						if self.results.get() == "":
							self.results.set("Result "+str(index)+": "+storyTitle)
							index = index + 1
						else:
							self.results.set(self.results.get()+",\nResult "+str(index)+": "+storyTitle)
							index = index + 1
			except KeyError:
				pass
if __name__=="__main__":
	app = simplegui_tk(None)
	app.title("Search NYTIMES.com")
	app.mainloop()


