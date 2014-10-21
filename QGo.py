# encoding: utf-8

import os
import sublime
import sublime_plugin
from copy import copy

def getfiles(path):
    files = os.listdir(path)

    results_files = []
    for f in files:
        f = os.path.join(path, f)
        if os.path.isdir(f):
            results_files += getfiles(f)
        else:
            results_files.append(f)

    return results_files


class QGoCommand(sublime_plugin.TextCommand):
    def run(self, view, *args):

        filename = self.view.file_name()

        if filename:
            s = filename.split('/')
            fs = s[-1].split('.')

            original = copy(fs)
            original = '.'.join(original)

            fs = fs[:-1]
            if fs[-1] == 'tpl':
                fs = fs[:-1]
            fs = '.'.join(fs)

            files = []
            pastas = sublime.active_window().folders()
            for p in pastas:
                files += getfiles(p)

            self.results = filter(lambda f: fs in f and original not in f, files)

            self.results_clean = [f.split('/')[-2:] for f in self.results]

            self.view.window().show_quick_panel(self.results_clean, self.insert_link)

    def insert_link(self, choice):
        if(choice != -1):
            sublime.active_window().open_file(self.results[choice])





