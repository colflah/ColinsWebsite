import tkinter, random


class simplegui_tk(tkinter.Tk):
	def __init__(self,parent):
		tkinter.Tk.__init__(self,parent)
		self.parent = parent
		self.initialize()




	def initialize(self):
		self.grid()
	
		self.intro = tkinter.StringVar()
		self.intro.set("In this program, you can play Tic - Tac - Toe.\nPick who is X and who is O")
		label = tkinter.Label(self,textvariable=self.intro,anchor="w",fg="black",bg="white")
		label.grid(column=0,row=0,columnspan=2,stick='EW')

		self.intro = tkinter.StringVar()
		self.intro.set(" X =")
		label = tkinter.Label(self,textvariable=self.intro,fg="black",bg="white")
		label.grid(column=0,row=1,columnspan=1,stick='EW')

		self.pickPlayerOneName = tkinter.StringVar()
		self.pickPlayerOne = tkinter.Entry(self,textvariable=self.pickPlayerOneName)
		self.pickPlayerOne.grid(column=1,row=1,columnspan=2,stick='EW')

		self.intro = tkinter.StringVar()
		self.intro.set(" O =")
		label = tkinter.Label(self,textvariable=self.intro,fg="black",bg="white")
		label.grid(column=0,row=2,columnspan=1,stick='EW')

		self.pickPlayerTwoName = tkinter.StringVar()
		self.pickPlayerTwo = tkinter.Entry(self,textvariable=self.pickPlayerTwoName)
		self.pickPlayerTwo.grid(column=1,row=2,stick='EW')

		self.start = tkinter.Button(self,text=u"Start",command=self.startGame)
		self.start.grid(column=0,row=3, columnspan=2)

		self.grid_columnconfigure(0,weight=1)
		self.resizable(False,False)	

	def startGame(self):
		self.playerTwoName = self.pickPlayerTwoName.get()
		self.playerOneName = self.pickPlayerOneName.get()
		
		for widget in self.winfo_children():
			widget.destroy()

		self.button1 = tkinter.Button(self,text=u" ",command=lambda: self.OnButtonClick(self.button1), padx = 20, pady=20)
		self.button1.grid(column=1,row=1)

		self.button2 = tkinter.Button(self,text=u" ",command=lambda: self.OnButtonClick(self.button2), padx = 20, pady=20)
		self.button2.grid(column=1,row=2)

		self.button3 = tkinter.Button(self,text=u" ",command=lambda: self.OnButtonClick(self.button3), padx = 20, pady=20)
		self.button3.grid(column=1,row=3)

		self.button4 = tkinter.Button(self,text=u" ",command=lambda: self.OnButtonClick(self.button4), padx = 20, pady=20)
		self.button4.grid(column=2,row=1)

		self.button5 = tkinter.Button(self,text=u" ",command=lambda: self.OnButtonClick(self.button5), padx = 20, pady=20)
		self.button5.grid(column=2,row=2)

		self.button6 = tkinter.Button(self,text=u" ",command=lambda: self.OnButtonClick(self.button6), padx = 20, pady=20)
		self.button6.grid(column=2,row=3)

		self.button7 = tkinter.Button(self,text=u" ",command=lambda: self.OnButtonClick(self.button7), padx = 20, pady=20)
		self.button7.grid(column=3,row=1)

		self.button8 = tkinter.Button(self,text=u" ",command=lambda: self.OnButtonClick(self.button8), padx = 20, pady=20)
		self.button8.grid(column=3,row=2)

		self.button9 = tkinter.Button(self,text=u" ",command=lambda: self.OnButtonClick(self.button9), padx = 20, pady=20)
		self.button9.grid(column=3,row=3)

		self.turn = tkinter.StringVar()

		firstplayer = random.randint(0,1)
		if firstplayer == 0:
			self.turn.set("Player O must go first.")
			self.currentPlayer = "O"
		else:
			self.turn.set("Player X must go first.")
			self.currentPlayer = "X" 

		label = tkinter.Label(self,textvariable=self.turn,anchor="w",fg="black",bg="white")
		label.grid(column=0,row=4,columnspan=3,stick='EW')

		self.grid_columnconfigure(0,weight=1)
		self.resizable(False,False)

	def OnButtonClick(self, btn):
		if btn['text']==" " and self.currentPlayer == "O":
			btn['text'] = "O"
			self.currentPlayer = "X"
			self.turn.set("Player X's turn.")
		elif btn['text']==" " and self.currentPlayer == "X":
			btn['text'] = "X"
			self.currentPlayer = "O"
			self.turn.set("Player O's turn.")
		self.checkForWin()

	def checkForWin(self):
		if self.button1['text']=="X" and self.button2['text']=="X" and self.button3['text']=="X":
			self.winner = self.playerOneName
			self.endGame()
		if self.button1['text']=="O" and self.button2['text']=="O" and self.button3['text']=="O":
			self.winner = self.playerTwoName
			self.endGame() 
		if self.button4['text']=="X" and self.button5['text']=="X" and self.button6['text']=="X":
			self.winner = self.playerOneName
			self.endGame() 
		if self.button4['text']=="O" and self.button5['text']=="O" and self.button6['text']=="O":
			self.winner = self.playerTwoName
			self.endGame()
		if self.button7['text']=="X" and self.button8['text']=="X" and self.button9['text']=="X":
			self.winner = self.playerOneName
			self.endGame()
		if self.button7['text']=="O" and self.button8['text']=="O" and self.button9['text']=="O":
			self.winner = self.playerTwoName
			self.endGame()

		if self.button1['text']=="X" and self.button4['text']=="X" and self.button7['text']=="X":
			self.winner = self.playerOneName
			self.endGame()
		if self.button1['text']=="O" and self.button4['text']=="O" and self.button7['text']=="O":
			self.winner = self.playerTwoName
			self.endGame()
		if self.button2['text']=="X" and self.button5['text']=="X" and self.button8['text']=="X":
			self.winner = self.playerOneName
			self.endGame()
		if self.button2['text']=="O" and self.button5['text']=="O" and self.button8['text']=="O":
			self.winner = self.playerTwoName
			self.endGame()
		if self.button3['text']=="X" and self.button6['text']=="X" and self.button9['text']=="X":
			self.winner = self.playerOneName
			self.endGame()
		if self.button3['text']=="O" and self.button6['text']=="O" and self.button9['text']=="O":
			self.winner = self.playerTwoName
			self.endGame()

		if self.button1['text']=="X" and self.button5['text']=="X" and self.button9['text']=="X":
			self.winner = self.playerOneName
			self.endGame()
		if self.button1['text']=="O" and self.button5['text']=="O" and self.button9['text']=="O":
			self.winner = self.playerTwoName
			self.endGame()
		if self.button3['text']=="X" and self.button5['text']=="X" and self.button7['text']=="X":
			self.winner = self.playerOneName
			self.endGame()
		if self.button3['text']=="O" and self.button5['text']=="O" and self.button7['text']=="O":
			self.winner = self.playerTwoName
			self.endGame()
		# If winner is found, set self.winner to winner letter and then run self.endGame()

	def endGame(self):
		for widget in self.winfo_children():
			widget.destroy()
		self.endText = tkinter.StringVar()



		self.endText.set("Player "+self.winner+" is the winner!\nPress button to play again.")
		label = tkinter.Label(self,textvariable=self.endText,anchor="w",fg="black",bg="white")
		label.grid(column=0,row=0,columnspan=3,stick='EW')

		self.button9 = tkinter.Button(self,text=u"Replay",command=self.restart, padx = 20, pady=20)
		self.button9.grid(column=0,row=1)
	
	def restart(self):
		for widget in self.winfo_children():
			widget.destroy()
		self.initialize()

if __name__=="__main__":
	app = simplegui_tk(None)
	app.title("my graphical user interface (gui)")
	app.mainloop()
