import sublime_plugin

class SingleLastSelectionCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    view = self.view
    if len(view.sel()):
      last = view.sel()[-1]
      view.sel().clear()
      view.sel().add(last)
