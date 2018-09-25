import sublime, sublime_plugin, math

class SurroundWithCommand(sublime_plugin.TextCommand):
	def run(self, edit, action):
		self.edit = edit
		self.language = self.view.settings().get('syntax')

		if action == 'for':
			self.addfor()
		elif action == 'if':
			self.addif()
		elif action == 'ifelse':
			self.addifelse()
		elif action == 'while':
			self.addwhile()
		elif action == 'dowhile':
			self.adddowhile()
		elif action == 'try':
			self.addtry()
		elif action == 'div':
			self.adddiv()

	def addwhile(self):
		if self.language == "Packages/Python/Python.tmLanguage":
			self.insertStuff("while ${1:Condition}:", "", "while :", "", "While-Loop")
		else:			
			self.insertStuff("while (${1:/*Condition*/}) {", "}", "while () {", "}", "While-Loop")
		
	def addfor(self):
		if self.language == "Packages/Python/Python.tmLanguage":
			self.insertStuff("for ${1:/*Condition*/}:", "", "for :", "", "For-Loop")
		else:
			self.insertStuff("for (${1:/*Condition*/}) {", "}", "for () {", "}", "For-Loop")

	def addtry(self):
		if self.language == "Packages/Python/Python.tmLanguage":
			self.insertStuff("try:", "except ${1:Exception}: ${2:Code to Catch}", "try:", "except :", "Try-Except-Clause")
		else:
			self.insertStuff("try {", "} catch (${1:/*Exception*/}) {${2:/*Code to Catch*/}}", "try {", "} catch () {}", "Try-Catch-Clause")

	def adddowhile(self):
		self.insertStuff("do {", "} while (${1:/*Condition*/});", "do {", "} while ();", "Do-While-Loop")
		
	def addif(self):
		if self.language == "Packages/Python/Python.tmLanguage":
			self.insertStuff("if ${1:Condition}:", "", "if :", "", "If-Clause")
		else:
			self.insertStuff("if (${1:/*Condition*/}) {", "}", "if () {", "}", "If-Clause")

	def addifelse(self):
		if self.language == "Packages/Python/Python.tmLanguage":
			self.insertStuff("if ${1:/*Condition*/}:", "else: ${2:/*Else Code*/}", "if :", "else: ", "If-Else-Clause")
		else:
			self.insertStuff("if (${1:/*Condition*/}) {", "} else {${2:/*Else Code*/}}", "if () {", "} else {}", "If-Else-Clause")

	def adddiv(self):
		self.insertStuff("<div id=\"${1:ID}\">", "</div>", "<div>", "</div>", "Div")

	def insertStuff(self, pre, after, preTwo, afterTwo, type):
		sels = self.view.sel()

		nSel = 0
		for sel in sels:
			nSel += 1
		
		for sel in sels:
			if sel.empty():
				continue
			str    	= self.view.substr(sel)
			tab    	= self.insert_start_line(sel)
			if nSel == 1:
				str    	= self.insert_tab_line(str)
				str 	= str.replace('\n'+tab, '\n')
				str    	= pre + '\n\t' + str + '\n' + after
				str    	= self.normalize_line_endings(str)
				self.view.run_command('insert_snippet', {"contents": str})
			else:
				str    	= self.insert_tab_line(str)
				str 	= preTwo + '\n\t' + tab + str + '\n' + tab + afterTwo
				str    	= self.normalize_line_endings(str)
				self.view.replace(self.edit, sel, str)
			sublime.status_message(type + ' added')

	def normalize_line_endings(self, string):
		string = string.replace('\r\n', '\n').replace('\r', '\n')
		line_endings = self.view.settings().get('default_line_ending')
		if line_endings == 'windows':
			string = string.replace('\n', '\r\n')
		elif line_endings == 'mac':
			string = string.replace('\n', '\r')
		return string

	def insert_tab_line(self, string):
		string = string.replace('\r\n', '\n').replace('\r', '\n')
		string = string.replace('\n', '\n\t')
		return string

	def insert_start_line(self, selection):
		start 		= selection.begin()
		(row, col)	= self.view.rowcol(start)
		leftPoint 	= self.view.text_point(row, 0)
		region 		= sublime.Region(leftPoint, start)
		strSpace	= self.view.substr(region)

		string     = '';
		incSpace   = 0
		incTab     = 0
		for s in strSpace:
			if s == '\t':
				incTab	 += 1
			elif s == ' ':
				incSpace += 1
			else:
				incSpace += 1

		tabSize = self.view.settings().get("tab_size")
		rest 	= incSpace % tabSize
		nTab	= (incSpace-rest)/tabSize
		nTab	= math.floor(nTab);
		
		for x in range(0,(incTab+nTab)):
			string += '\t'
		for x in range(0,rest):
			string += ' '

		return string