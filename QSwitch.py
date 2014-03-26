# encoding: utf-8

import os
import sublime
import sublime_plugin  

class QSwitchCommand(sublime_plugin.TextCommand):  
    def run(self, view, *args):  
        
        filename = self.view.file_name()

        if filename:
            s = filename.split('/')
            fs = s[-1].split('.')

            path = '/'.join(s[:-1])+'/'

            if fs[-2] == 'tpl':
                f = '.'.join(fs[:-2])+'.'+fs[-1]
            else:
                f = '.'.join(fs[:-1])+'.tpl.'+fs[-1]

            filename = path+f

            if os.path.exists(filename):
                sublime.active_window().open_file(filename)