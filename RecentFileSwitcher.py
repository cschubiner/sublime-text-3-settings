import sublime
import sublime_plugin
import os
import time

class CONSTANT:
  prefix = 'recent_file_switcher: '
  timestamp = prefix + 'timestamp'
  file_info = prefix + 'file_info'

# generate quick view for open files based on timestamp and file name
# configure short-cut like { "keys": ["super+e"], "command": "recent_file_switcher" }
class RecentFileSwitcherCommand(sublime_plugin.WindowCommand):

  def run(self):
    self.open_views = []
    self.window = sublime.active_window()

    for view in self.window.views():
      self.open_views.append((view, self.get_timestamp(view), self.get_file_info(view)))

    # sort view based on last timestamp
    self.open_views.sort(key=lambda view: (-view[1]))
    self.open_views.pop(0)

    open_files = []
    for view in self.open_views:
      open_files.append(view[2])

    self.window.show_quick_panel(open_files, self.view_selected, False, -1)

  def get_timestamp(self, view):
    timestamp = view.settings().get(CONSTANT.timestamp, None)
    if timestamp: return timestamp

    file_name = view.file_name()
    if file_name:
      try:
        timestamp = os.path.getmtime(file_name)
      except:
        timestamp = 0
    else:
      timestamp = time.time()

    view.settings().set(CONSTANT.timestamp, timestamp)
    return timestamp

  def get_file_info(self, view):
    file_info = view.settings().get(CONSTANT.file_info, None)
    if file_info: return file_info

    file_name = view.file_name()
    if file_name:
      base_name = os.path.basename(file_name)
      dir_name = None
      for folder in self.window.folders():
        if os.path.commonprefix([folder, file_name]) == folder:
          dir_name = os.path.relpath(file_name, folder)
      if not dir_name: dir_name = os.path.dirname(file_name)
    else:
      base_name = 'untitled'
      dir_name = 'untitled'

    file_info = [base_name, dir_name]
    view.settings().set(CONSTANT.file_info, file_info)
    return file_info


  def view_selected(self, selected):
    if selected >= 0:
      self.window.focus_view(self.open_views[selected][0])

    return selected

# event listener to record activation time and auto-save after lost focus
class ViewEventListener(sublime_plugin.EventListener):

  def on_activated(self, view):
    view.settings().set(CONSTANT.timestamp, time.time())

  def on_deactivated_async(self, view):
    if view.is_dirty() and view.file_name():
      view.run_command('save')
