import sublime, sublime_plugin




class runhtmlCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		name = str(self.view.window().active_view().file_name())
		print(name)
		
		if name == None:
			sublime.message_dialog("This file does not have a name.")
			return

		try:
			htmlExtension = ".html"
			if name[len(name) - len(htmlExtension):] != htmlExtension and name[len(name) - len(htmlExtension):] != htmlExtension.upper():
				ans = sublime.ok_cancel_dialog("This file name does not end with an HTML extension.", "Run anyway")
				if ans == False:
					return
		except:
			ans = sublime.message_dialog("This file name does not end with an HTML extension.",  "Run anyway")
			if ans == False:
				return

		from subprocess import call
		call(['firefox '+name], shell=True)
