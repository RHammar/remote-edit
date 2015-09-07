import sublime, sublime_plugin, os

#host='sts@exploratory9-avhs2.vhslab.rnd.axis.com'
# host='sts@DebianAVHS'
host = None
def plugin_loaded():
  s = sublime.load_settings('remote-edit.sublime-settings')
  s.add_on_change('readsettings', update_settings)
  update_settings()

def update_settings():
    print("update_settings")
    global host
    s = sublime.load_settings('remote-edit.sublime-settings')
    host = s.get('host')

class RemoteEdit(sublime_plugin.EventListener):
    def on_post_save(self, view):
        remote = {"/home/rickardh/repos/avhsportal/avhs/webgui": "/usr/bin/scp '$1' "+ host +":'~/current/web/webgui/$2'",
                  "/home/rickardh/repos/avhsportal/avhs/portal": "/usr/bin/scp '$1' "+ host +":'~/current/$2'",
                  "/home/rickardh/repos/avhsportal/avhs/portal/apps/helpers": "/usr/bin/scp '$1' "+ host +":'~/current/bin/$2'",
                  "/home/rickardh/repos/webgrind":               "/usr/bin/scp '$1' "+ host +":'~/current/web/webgrind/$2'"}
                  # "/home/rickardh/script/explorer.html": "/usr/bin/scp '$1' sts@DebianAVHS:'~/current/web/webgui/$2'"}

        for dirname, target in remote.items():
            if view.file_name().startswith(dirname):
                target = target.replace("$1", view.file_name())
                target = target.replace("$2", view.file_name()[len(dirname):])

                print("remote edit: " + target)
                os.system(target + " &")
