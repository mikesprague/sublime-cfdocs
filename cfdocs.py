# Written by Mike Sprague (mikesprague@gmail.com)
# based on Search DevDocs Plugin by Vitor Britto (code@vitorbritto.com.br / vitorbritto.com.br)

import sublime
import sublime_plugin

import subprocess
import webbrowser


def SearchFor(text):
    url = 'http://cfdocs.org/' + text.replace(' ', '%20')
    webbrowser.open_new_tab(url)


class CfDocsSearchSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
            # if the user didn't select anything, search the currently highlighted word
            if selection.empty():
                text = self.view.word(selection)

            text = self.view.substr(selection)
            SearchFor(text)


class CfDocsSearchFromInputCommand(sublime_plugin.WindowCommand):
    def run(self):
        # Get the search item
        self.window.show_input_panel('Search CFDocs for', '',
            self.on_done, self.on_change, self.on_cancel)

    def on_done(self, input):
        SearchFor(input)

    def on_change(self, input):
        pass

    def on_cancel(self):
        pass
