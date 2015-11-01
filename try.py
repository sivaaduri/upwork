from PyQt4 import QtCore, QtGui
import sys

class Text_Screen(QtGui.QTextEdit):
	def __init__(self):
		super(Text_Screen,self).__init__()
		self.acceptRichText=True
		self.canPaste=True	
	def changeEvent(self,ev):
		pass
		
	def LineWrapMode(self):
		pass
		
		
		
		
class Example(QtGui.QMainWindow):
	def __init__(self):
		super(Example,self).__init__()
		self.resize(700,500)
		#self.center()
		self.setWindowTitle('Example')
		self.initUI()
		
		
	def initUI(self):
		self.text=Text_Screen()
		self.control = QtGui.QWidget()
		self.layout1=QtGui.QGridLayout()
		label1=QtGui.QLabel("Max Char")
		text1=QtGui.QLineEdit()
		check1=QtGui.QCheckBox()
		layout2=QtGui.QHBoxLayout()
		layout2.addWidget(check1)
		layout2.addWidget(text1)
		self.layout1.addWidget(label1,0,0)
		self.layout1.addLayout(layout2,0,1)
		self.control.setLayout(self.layout1)
		
		label2=QtGui.QLabel("2nd option")
		text2=QtGui.QLineEdit()
		check2=QtGui.QCheckBox()
		layout3=QtGui.QHBoxLayout()
		layout3.addWidget(check2)
		layout3.addWidget(text2)
		self.layout1.addWidget(label2,1,0)
		self.layout1.addLayout(layout3,1,1)
		self.control.setLayout(self.layout1)
		
		label2=QtGui.QLabel("3rd option")
		text2=QtGui.QLineEdit()
		check2=QtGui.QCheckBox()
		layout4=QtGui.QHBoxLayout()
		layout4.addWidget(check2)
		layout4.addWidget(text2)
		self.layout1.addWidget(label2,2,0)
		self.layout1.addLayout(layout4,2,1)
		self.control.setLayout(self.layout1)
		
		self.widget=QtGui.QWidget()
		self.setCentralWidget(self.widget)
		self.layout=QtGui.QGridLayout()
		self.layout.addWidget(self.control,0,0)
		self.layout.addWidget(self.text,0,1)
		self.widget.setLayout(self.layout)
		self.text.setTabStopWidth(33)
		self.createActions()
		
		
		
	def createActions(self):
		self.newAction = QtGui.QAction(QtGui.QIcon("icons/new.png"),"New",self)
		self.newAction.setShortcut("Ctrl+N")
		self.newAction.setStatusTip("Create a new document from scratch.")
		#self.newAction.triggered.connect(self.new)

		self.openAction = QtGui.QAction(QtGui.QIcon("icons/open.png"),"Open file",self)
		self.openAction.setStatusTip("Open existing document")
		self.openAction.setShortcut("Ctrl+O")
		#self.openAction.triggered.connect(self.open)

		self.saveAction = QtGui.QAction(QtGui.QIcon("icons/save.png"),"Save",self)
		self.saveAction.setStatusTip("Save document")
		self.saveAction.setShortcut("Ctrl+S")
		#self.saveAction.triggered.connect(self.save)

		self.printAction = QtGui.QAction(QtGui.QIcon("icons/print.png"),"Print document",self)
		self.printAction.setStatusTip("Print document")
		self.printAction.setShortcut("Ctrl+P")
		#self.printAction.triggered.connect(self.printHandler)

		self.previewAction = QtGui.QAction(QtGui.QIcon("icons/preview.png"),"Page view",self)
		self.previewAction.setStatusTip("Preview page before printing")
		self.previewAction.setShortcut("Ctrl+Shift+P")
		#self.previewAction.triggered.connect(self.preview)

		self.findAction = QtGui.QAction(QtGui.QIcon("icons/find.png"),"Find and replace",self)
		self.findAction.setStatusTip("Find and replace words in your document")
		self.findAction.setShortcut("Ctrl+F")
		#self.findAction.triggered.connect(find.Find(self).show)

		self.cutAction = QtGui.QAction(QtGui.QIcon("icons/cut.png"),"Cut to clipboard",self)
		self.cutAction.setStatusTip("Delete and copy text to clipboard")
		self.cutAction.setShortcut("Ctrl+X")
		#self.cutAction.triggered.connect(self.text.cut)

		self.copyAction = QtGui.QAction(QtGui.QIcon("icons/copy.png"),"Copy to clipboard",self)
		self.copyAction.setStatusTip("Copy text to clipboard")
		self.copyAction.setShortcut("Ctrl+C")
		#self.copyAction.triggered.connect(self.text.copy)

		self.pasteAction = QtGui.QAction(QtGui.QIcon("icons/paste.png"),"Paste from clipboard",self)
		self.pasteAction.setStatusTip("Paste text from clipboard")
		self.pasteAction.setShortcut("Ctrl+V")
		#self.pasteAction.triggered.connect(self.text.paste)

		self.undoAction = QtGui.QAction(QtGui.QIcon("icons/undo.png"),"Undo last action",self)
		self.undoAction.setStatusTip("Undo last action")
		self.undoAction.setShortcut("Ctrl+Z")
		#self.undoAction.triggered.connect(self.text.undo)

		self.redoAction = QtGui.QAction(QtGui.QIcon("icons/redo.png"),"Redo last undone thing",self)
		self.redoAction.setStatusTip("Redo last undone thing")
		self.redoAction.setShortcut("Ctrl+Y")
		#self.redoAction.triggered.connect(self.text.redo)

		dateTimeAction = QtGui.QAction(QtGui.QIcon("icons/calender.png"),"Insert current date/time",self)
		dateTimeAction.setStatusTip("Insert current date/time")
		dateTimeAction.setShortcut("Ctrl+D")
		#dateTimeAction.triggered.connect(datetime.DateTime(self).show)

		wordCountAction = QtGui.QAction(QtGui.QIcon("icons/count.png"),"See word/symbol count",self)
		wordCountAction.setStatusTip("See word/symbol count")
		wordCountAction.setShortcut("Ctrl+W")
		#wordCountAction.triggered.connect(self.wordCount)

		tableAction = QtGui.QAction(QtGui.QIcon("icons/table.png"),"Insert table",self)
		tableAction.setStatusTip("Insert table")
		tableAction.setShortcut("Ctrl+T")
		#tableAction.triggered.connect(table.Table(self).show)

		imageAction = QtGui.QAction(QtGui.QIcon("icons/image.png"),"Insert image",self)
		imageAction.setStatusTip("Insert image")
		imageAction.setShortcut("Ctrl+Shift+I")
		#imageAction.triggered.connect(self.insertImage)

		bulletAction = QtGui.QAction(QtGui.QIcon("icons/bullet.png"),"Insert bullet List",self)
		bulletAction.setStatusTip("Insert bullet list")
		bulletAction.setShortcut("Ctrl+Shift+B")
		#bulletAction.triggered.connect(self.bulletList)

		numberedAction = QtGui.QAction(QtGui.QIcon("icons/number.png"),"Insert numbered List",self)
		numberedAction.setStatusTip("Insert numbered list")
		numberedAction.setShortcut("Ctrl+Shift+L")
		#numberedAction.triggered.connect(self.numberList)

		self.toolbar = self.addToolBar("Options")

		self.toolbar.addAction(self.newAction)
		self.toolbar.addAction(self.openAction)
		self.toolbar.addAction(self.saveAction)

		self.toolbar.addSeparator()

		self.toolbar.addAction(self.printAction)
		self.toolbar.addAction(self.previewAction)

		self.toolbar.addSeparator()

		self.toolbar.addAction(self.cutAction)
		self.toolbar.addAction(self.copyAction)
		self.toolbar.addAction(self.pasteAction)
		self.toolbar.addAction(self.undoAction)
		self.toolbar.addAction(self.redoAction)

		self.toolbar.addSeparator()

		self.toolbar.addAction(self.findAction)
		self.toolbar.addAction(dateTimeAction)
		self.toolbar.addAction(wordCountAction)
		self.toolbar.addAction(tableAction)
		self.toolbar.addAction(imageAction)

		self.toolbar.addSeparator()

		self.toolbar.addAction(bulletAction)
		self.toolbar.addAction(numberedAction)

		self.addToolBarBreak()
		
		
		
		
				
def main():
    app = QtGui.QApplication(sys.argv)

    main = Example()
    main.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
