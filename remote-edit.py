import sublime, sublime_plugin, os

host = None
path_mapping = None
def plugin_loaded():
  s = sublime.load_settings('remote-edit.sublime-settings')
  s.add_on_change('readsettings', update_settings)
  update_settings()

def update_settings():
    global host, path_mapping
    s = sublime.load_settings('remote-edit.sublime-settings')
    host = s.get('host')
    path_mapping = s.get('path_mapping')
    # print(repr(path_mapping))

class RemoteEdit(sublime_plugin.EventListener):
    def on_post_save(self, view):

        copy = {}
        for local,remote in path_mapping.items():
            copy[local] = "/usr/bin/scp '$1' "+ host +":'" + remote + "$2'"

        # print(repr(copy))
        for dirname, target in copy.items():
            if view.file_name().startswith(dirname):
                print(len(dirname))
                target = target.replace("$1", view.file_name())
                target = target.replace("$2", view.file_name()[len(dirname):])

                print("remote edit: " + target)
                os.system(target + " &")
