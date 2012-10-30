#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: David Wong <davidwong.xc@gmail.com>
License: 3 clause BSD license

This module contains classes for most of the windows used in the Word Tag program.

"""
 
from __future__ import absolute_import
from __future__ import unicode_literals

import os

import wx
import wx.html

class TagsetWindow(wx.Frame):
    """Shows details about the Penn Treebank tagset."""
    
    def __init__(self, *args, **kwargs):
        super(TagsetWindow, self).__init__(*args, **kwargs)
        self.html_window = wx.html.HtmlWindow(self, style=wx.html.HW_SCROLLBAR_AUTO)
        
    def show_tagset(self):
        tagset_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static", "tagset.html") 
        if self.html_window.LoadPage(tagset_path):
            self.Center()
            self.Show()
            self.Raise()
        else:
            self.html_window.AppendToPage("<p>The local file containing the tagset details could not be loaded.<br />" \
                                          "<br />The text-tagger application uses the default tagger provided by the Natural Language Toolkit (NLTK) library. " \
                                          "The NLTK default tagger uses the Penn Treebank tag set. " \
                                          "Tagset details can be found at www.anc.org/OANC/penn.html.<br />" \
                                          "<br />The Results section groups some parts of speech together. For example, 'JJ' (adjective), " \
                                          "'JJR' (adjective, comparative), and 'JJS' (adjective, superlative), are all counted together under the Adjective category. " \
                                          "For specific results, click the Full Results button. </p>")
            self.Center()
            self.Show()
            self.Raise()
        
class HelpWindow(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(HelpWindow, self).__init__(*args, **kwargs)
        self.html_window = wx.html.HtmlWindow(self, style=wx.html.HW_SCROLLBAR_AUTO)    
    
    def show_help(self):
        help_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static", "help.html")
        if self.html_window.LoadPage(help_path):
            self.Center()
            self.Show()
            self.Raise()
            
        
class FullResultsWindow(wx.Frame):
    tags_dict = dict({'Coordinating Conjunction': 'CC', 'Cardinal Number': 'CD', 'Determiner': 'DT',
                      'Existential there': 'EX', 'Foreign Word': 'FW', 'Preposition or Subordinating Conjunction': 'IN',
                      'Adjective': 'JJ', 'Adjective, comparative': 'JJR', 'Adjective, superlative': 'JJS',
                      'List item marker': 'LS', 'Modal': 'MD', 'Noun, singular or mass': 'NN', 'Noun, plural': 'NNS',
                      'Proper noun, singular': 'NNPS', 'Proper noun, plural': 'NNPS', 'Predeterminer': 'PDT', 'Possessive ending': 'POS',
                      'Personal pronoun': 'PRP', 'Possessive pronoun':'PRP$', 'Adverb': 'RB', 'Adverb, comparative': 'RBR',
                      'Adverb, superlative': 'RBS', 'Particle': 'RP', 'Symbol': 'SYM', 'To': 'TO', 'Interjection': 'UH',
                      'Verb, base form': 'VB', 'Verb, past tense': 'VBD', 'Verb, gerund or present participle': 'VBG', 'VBN': 'Verb, past participle',
                      'Verb, non-3rd person singular present': 'VBP', 'Verb, 3rd person singular present': 'VBZ', 'Wh-determiner': 'WDT', 'Wh-pronoun': 'WP',
                      'Possessive wh-pronoun': 'WP$', 'Wh-adverb': 'WRB'})
    
    def __init__(self, counter_tags, *args, **kwargs):
        super(FullResultsWindow, self).__init__(*args, **kwargs)
        self.window = wx.ScrolledWindow(self)
        self.fullresults_sizer = wx.FlexGridSizer(rows=38, cols=2, vgap=3, hgap=5)
        self.set_results(counter_tags)
        self.window.SetSizer(self.fullresults_sizer)
        self.window.SetScrollRate(5, 5)
        
    
    def set_results(self, counter_tags):
        self.fullresults_sizer.Clear(deleteWindows=True)
        wordclass_list = sorted(FullResultsWindow.tags_dict.iterkeys())
        for i in wordclass_list:
            self.fullresults_sizer.Add(wx.StaticText(self.window, label=' '.join([i, FullResultsWindow.tags_dict[i]])))
            self.fullresults_sizer.Add(wx.StaticText(self.window, label="%g" % counter_tags[FullResultsWindow.tags_dict[i]]))
        self.fullresults_sizer.Add(wx.StaticText(self.window, label='Words'))
        self.fullresults_sizer.Add(wx.StaticText(self.window, label="%g" % counter_tags['words']))
        self.fullresults_sizer.Add(wx.StaticText(self.window, label='Sentences'))
        self.fullresults_sizer.Add(wx.StaticText(self.window, label="%g" % counter_tags['sentences']))
        
            
class FileDialog(object):
    def __init__(self, parent_window):
        self.filename = ''
        self.dirname = ''
        self.full_path_to_file = ''
        self.parent_window = parent_window
        self.dialog = wx.FileDialog(self.parent_window, "Choose a file", self.dirname, self.filename, "*.*", wx.FD_FILE_MUST_EXIST)
        
    def prompt_for_file(self, extension=None):
        """Pass a file extension like '.txt' to this function to have it
        only accept files with that extension."""
        
        if self.dialog.ShowModal() == wx.ID_OK:
            self.filename = self.dialog.GetFilename()
            self.dirname = self.dialog.GetDirectory()
            self.full_path_to_file = os.path.join(self.dirname, self.filename)
            
        if extension is not None:
            self.check_extension(self.full_path_to_file, extension)
                
        self.dialog.Destroy()
        
    def get_file_name(self):
        return self.full_path_to_file
    
    def check_extension(self, file_name, extension):
        file_extension = os.path.splitext(file_name)[1]
        if file_extension != extension:
            self.filetype_error_dialog = wx.MessageDialog(self.parent_window, "Please choose a %s file" % extension, "Error", wx.OK | wx.ICON_ERROR)
            self.filetype_error_dialog.ShowModal()    
        
    
class AboutDialog():
    def __init__(self, icon=None, name=None, version=None, description=None,
                 copy_right=None, program_license=None, developers=None):
        """icon should be a jpeg, all other arguments except developers
        should be a string. developers should be a list of strings."""
        
        self.info = wx.AboutDialogInfo()
        if icon:
            self.info.SetIcon(wx.Icon(icon, wx.BITMAP_TYPE_JPEG))
        if name:
            self.info.SetName(name)
        if version:
            self.info.SetVersion(version)
        if description:
            self.info.SetDescription(description)
        if copy_right:
            self.info.SetCopyright(copy_right)
        if program_license:
            self.info.SetCopyright(program_license)
        if developers:
            for developer in developers:
                self.info.AddDeveloper(developer)
                
    def show_about(self):
        wx.AboutBox(self.info)        
        
        
            