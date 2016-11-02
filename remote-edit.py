import sublime, sublime_plugin, os

hosts = None
path_mapping = None
def plugin_loaded():
  s = sublime.load_settings('remote-edit.sublime-settings')
  s.add_on_change('readsettings', update_settings)
  update_settings()

def update_settings():
    global hosts, path_mapping
    s = sublime.load_settings('remote-edit.sublime-settings')
    hosts = s.get('hosts')
    path_mapping = s.get('path_mapping')
    # print(repr(path_mapping))

class RemoteEdit(sublime_plugin.EventListener):
    def on_post_save(self, view):

        print(hosts)
        for host in hosts:
            copy = {}
            # print('##############', host, '##############')

            for local,remote in path_mapping.items():
                copy[local] = "/usr/bin/scp '$1' "+ host +":'" + remote + "$2'"

            # print(repr(copy))
            for dirname, target in copy.items():
                if view.file_name().startswith(dirname):
                    target = target.replace("$1", view.file_name())
                    target = target.replace("$2", view.file_name()[len(dirname):])

                    print("remote edit: " + target)
                    os.system(target + " &")
