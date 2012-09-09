#!/usr/bin/python
# -*- coding: utf-8 -*-

"""

This is the main module for the Word Tag program. 
Author: David Wong <davidwong.xc@gmail.com>
License: 3-clause BSD license

"""

from __future__ import absolute_import
from __future__ import unicode_literals

import threading
import collections
import os
import csv

import wx
import nltk

from word_tag.gui_windows import *
from word_tag.business import tag_text

class MainWindow(wx.Frame):
    """Main window for the application."""
     
    _tagged_text = ""
    _counter_tags = collections.Counter()
    
    def __init__(self, *args, **kwargs):
        """
        __init__ creates the GUI, loads resources for tagging, creates menus,
        and binds events. 
        
        """
        
        super(MainWindow, self).__init__(*args, **kwargs)
        self.load_resources = threading.Thread(target=self.load_resource)
        self.load_resources.start()
        self.panel = wx.Panel(self)
        self.create_interior_ui()
        self.create_menus()
        self.bind_events()
        self.Show()
        
    
    def load_resource(self):
        """Loads the resource needed for part of speech tagging."""
        
        #Load resource using the NLTK protocol. nltk.load() searches for the resource URL in the directories specified by nltk.data.path
        nltk.load('taggers/maxent_treebank_pos_tagger/english.pickle')    
    
    def create_results_box(self):
        """Creates the boxes that show the counts for each part of speech.
            Also creates some of the option buttons related to the results 
            display."""
        
        self.create_title_options()
        self.create_sub_grids()     
        self.create_result_labels()
        self.create_result_boxes()  
        self.add_to_grid_sizers()
        
        self.results_sizer.Add(self.grid1_sizer, proportion=1, flag=wx.EXPAND)
        self.results_sizer.Add(self.grid2_sizer, proportion=1, flag=wx.EXPAND)
        self.results_sizer.Add(self.grid3_sizer, proportion=1, flag=wx.EXPAND)
        self.results_sizer.Add(self.grid4_sizer, proportion=1, flag=wx.EXPAND)
    
    def create_title_options(self):
        """Creates result titles and radio button options for showing counts as totals
        or averages per sentence."""
        
        self.title_sizer = wx.FlexGridSizer(rows=1, cols=3, vgap=0, hgap=8)
        self.results_title = wx.StaticText(self.panel, label="Results: ")
        self.rb_totalcounts = wx.RadioButton(self.panel, label="Total Counts", style=wx.RB_GROUP)
        self.rb_averages_persentence = wx.RadioButton(self.panel, label="Averages per Sentence")
        self.title_sizer.Add(self.results_title, proportion=1)
        self.title_sizer.Add(self.rb_totalcounts, proportion=1)
        self.title_sizer.Add(self.rb_averages_persentence, proportion=1)    
    
    def create_sub_grids(self):
        """Creates the grid sizers for the results boxes."""
        
        self.results_sizer = wx.FlexGridSizer(rows=1, cols=4, vgap=0, hgap=40)
        self.grid1_sizer = wx.FlexGridSizer(rows=5, cols=2, vgap=10, hgap=5)
        self.grid2_sizer = wx.FlexGridSizer(rows=5, cols=2, vgap=10, hgap=5)
        self.grid3_sizer = wx.FlexGridSizer(rows=5, cols=2, vgap=10, hgap=5)
        self.grid4_sizer = wx.FlexGridSizer(rows=5, cols=2, vgap=10, hgap=5)
    
    
    def create_result_labels(self):
        
        self.adjectives_label = wx.StaticText(self.panel, label="Adjective")
        self.adverbs_label = wx.StaticText(self.panel, label="Adverb")
        self.conjunctions_label = wx.StaticText(self.panel, label="Coordinating Conjunction")
        self.determiners_label = wx.StaticText(self.panel, label="Determiner")
        self.modal_verb_label = wx.StaticText(self.panel, label="Modal Verb")
        
        self.noun_label = wx.StaticText(self.panel, label="Noun")
        self.preposition_label = wx.StaticText(self.panel, label="Preposition or Subordinating Conjunction")
        self.pronoun_label = wx.StaticText(self.panel, label="Pronoun")
        self.proper_noun_label = wx.StaticText(self.panel, label="Proper Noun")
        self.verb_base_label = wx.StaticText(self.panel, label="Verb, base form")
        
        self.verb_gerund_label = wx.StaticText(self.panel, label="Verb, gerund or past participle")
        self.verb_nonthird_label = wx.StaticText(self.panel, label="Verb, non-3rd person singular present")
        self.verb_pastpar_label = wx.StaticText(self.panel, label="Verb, past participle")
        self.verb_past_label = wx.StaticText(self.panel, label="Verb, past tense")
        self.verb_third_label = wx.StaticText(self.panel, label="Verb, 3rd person singular present")
        self.Wh_determiner_label = wx.StaticText(self.panel, label="Wh-determiner")
        self.words_label = wx.StaticText(self.panel, label="Words")
        self.sentences_label = wx.StaticText(self.panel, label="Sentences")
    
    def create_result_boxes(self):
        """Creates the result boxes where counts are displayed."""
        
        self.adjectives_box = wx.TextCtrl(self.panel, size=(50, -1))
        self.adverbs_box = wx.TextCtrl(self.panel, size=(50, -1))
        self.conjunctions_box = wx.TextCtrl(self.panel, size=(50, -1))
        self.determiners_box = wx.TextCtrl(self.panel, size=(50, -1))
        self.modal_verb_box = wx.TextCtrl(self.panel, size=(50, -1))
        self.noun_box = wx.TextCtrl(self.panel, size=(50, -1))
        self.preposition_box = wx.TextCtrl(self.panel, size=(50, -1))
        self.pronoun_box = wx.TextCtrl(self.panel, size=(50, -1))
        self.proper_noun_box = wx.TextCtrl(self.panel, size=(50, -1))
        self.verb_base_box = wx.TextCtrl(self.panel, size=(50, -1))
        self.verb_gerund_box = wx.TextCtrl(self.panel, size=(50, -1))
        self.verb_pastpar_box = wx.TextCtrl(self.panel, size=(50, -1))
        self.verb_past_box = wx.TextCtrl(self.panel, size=(50, -1))
        self.verb_nonthird_box = wx.TextCtrl(self.panel, size=(50, -1))
        self.verb_third_box = wx.TextCtrl(self.panel, size=(50, -1))
        self.Wh_deteminer_box = wx.TextCtrl(self.panel, size=(50, -1))
        self.words_box = wx.TextCtrl(self.panel, size=(50, -1))
        self.sentences_box = wx.TextCtrl(self.panel, size=(50, -1))
   
    def add_to_grid_sizers(self):
        """Adds labels and results boxes to grid sizers."""
        
        for label, box in [(self.adjectives_label, self.adjectives_box), 
                           (self.adverbs_label, self.adverbs_box), (self.conjunctions_label, self.conjunctions_box), 
                           (self.determiners_label, self.determiners_box), (self.modal_verb_label, self.modal_verb_box)]:
            self.grid1_sizer.Add(label, proportion=1, flag=wx.EXPAND|wx.TOP, border=3)
            self.grid1_sizer.Add(box, proportion=1, flag=wx.EXPAND)
            
        for label, box in [(self.noun_label, self.noun_box), 
                           (self.preposition_label, self.preposition_box),(self.pronoun_label, self.pronoun_box), 
                           (self.proper_noun_label, self.proper_noun_box), (self.verb_base_label, self.verb_base_box)]:
            self.grid2_sizer.Add(label, proportion=1, flag=wx.EXPAND|wx.TOP, border=3)
            self.grid2_sizer.Add(box, proportion=1, flag=wx.EXPAND)
            
        for label, box in [(self.verb_gerund_label, self.verb_gerund_box),  (self.verb_nonthird_label, self.verb_nonthird_box),
                           (self.verb_pastpar_label, self.verb_pastpar_box), (self.verb_past_label, self.verb_past_box), 
                           (self.verb_third_label, self.verb_third_box)]:
            self.grid3_sizer.Add(label, proportion=1, flag=wx.EXPAND|wx.TOP, border=3)
            self.grid3_sizer.Add(box, proportion=1, flag=wx.EXPAND)
            
        
        for label, box in [(self.Wh_determiner_label, self.Wh_deteminer_box), (self.words_label, self.words_box),
                           (self.sentences_label, self.sentences_box)]:
            self.grid4_sizer.Add(label, proportion=1, flag=wx.EXPAND|wx.TOP, border=3)
            self.grid4_sizer.Add(box, proportion=1, flag=wx.EXPAND)
        
    def create_interior_ui(self):
        
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        h_sizer1 = wx.BoxSizer(wx.HORIZONTAL)
        v_sizer1 = wx.BoxSizer(wx.VERTICAL)
        bttn_sizer = wx.FlexGridSizer(rows=1, cols=3, vgap=0, hgap=25)
        
        self.textbox_main = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE)
        h_sizer1.Add(self.textbox_main, proportion=1, flag=wx.EXPAND|wx.ALIGN_TOP|wx.RIGHT|wx.LEFT|wx.TOP, border=20)
        main_sizer.Add(h_sizer1, proportion=1, flag=wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND)
        
        self.tag_text_bttn = wx.Button(self.panel, label="Tag Text")
        self.tagset_details_bttn = wx.Button(self.panel, label="Tagset Details")
        self.full_results_bttn = wx.Button(self.panel, label="Full Results")
        
        
        bttn_sizer.Add(self.tag_text_bttn, proportion=1)
        bttn_sizer.Add(self.tagset_details_bttn, proportion=1)
        bttn_sizer.Add(self.full_results_bttn, proportion=1)
        
        v_sizer1.Add(bttn_sizer, proportion=0.2, flag=wx.ALIGN_LEFT|wx.EXPAND|wx.LEFT|wx.TOP|wx.BOTTOM, border=10)
        
        self.create_results_box()
        v_sizer1.Add(self.title_sizer, proportion=0.2, flag=wx.EXPAND|wx.ALL, border=12)
        v_sizer1.Add(self.results_sizer, proportion=0.6, flag=wx.EXPAND|wx.ALL, border=10)
        main_sizer.Add(v_sizer1, proportion=1, flag=wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND|wx.ALL, border=20)
        
        self.panel.SetSizer(main_sizer)
        self.Centre()
        
    def create_menus(self):
        
        self.menubar = wx.MenuBar()
        self.create_file_menu()
        self.create_edit_menu()
        self.create_help_menu()
            
        self.menubar.Append(self.file_menu, '&File')
        self.menubar.Append(self.edit_menu, '&Edit')
        self.menubar.Append(self.help_menu, '&Help')
        self.SetMenuBar(self.menubar)
    
    def create_file_menu(self):
        
        self.file_menu = wx.Menu()
        self.file_item_load = wx.MenuItem(self.file_menu, wx.ID_ANY, "Load text from file")
        self.file_item_save_to_text = wx.MenuItem(self.file_menu, wx.ID_SAVE, "Save results to a text file")
        self.file_item_save_to_csv = wx.MenuItem(self.file_menu, wx.ID_ANY, "Save results to a csv file")
        self.file_item_exit = wx.MenuItem(self.file_menu, wx.ID_EXIT, "Exit", "Exit Application")
        self.file_menu.AppendItem(self.file_item_load)
        self.file_menu.AppendItem(self.file_item_save_to_text)
        self.file_menu.AppendItem(self.file_item_save_to_csv)
        self.file_menu.AppendSeparator()
        self.file_menu.AppendItem(self.file_item_exit)
         
         
    def create_edit_menu(self):
        
        self.edit_menu = wx.Menu()
        self.edit_item_cut = wx.MenuItem(self.edit_menu, wx.ID_CUT, "Cut")
        self.edit_item_copy = wx.MenuItem(self.edit_menu, wx.ID_COPY, "Copy")
        self.edit_item_paste = wx.MenuItem(self.edit_menu, wx.ID_PASTE, "Paste")
        self.edit_item_delete = wx.MenuItem(self.edit_menu, wx.ID_DELETE, "Delete")
        self.edit_item_clear_textbox = wx.MenuItem(self.edit_menu, wx.ID_ANY, "Clear Textbox")
        self.edit_item_select_all = wx.MenuItem(self.edit_menu, wx.ID_SELECTALL, "Select All")
        for item in [self.edit_item_cut, self.edit_item_copy, self.edit_item_paste, self.edit_item_delete]:
            self.edit_menu.AppendItem(item)
            
        self.edit_menu.AppendSeparator()
        self.edit_menu.AppendItem(self.edit_item_clear_textbox)
        self.edit_menu.AppendItem(self.edit_item_select_all)         
        
    def create_help_menu(self):
        
        self.help_menu = wx.Menu()
        self.help_item_view_help = wx.MenuItem(self.help_menu, wx.ID_HELP, "View Help")
        self.help_item_about = wx.MenuItem(self.help_menu, wx.ID_ABOUT, "About Word Tag")
        
        self.help_menu.AppendItem(self.help_item_view_help)
        self.help_menu.AppendItem(self.help_item_about)
         
    def bind_events(self):
        
        self.tag_text_bttn.Bind(wx.EVT_BUTTON, self.set_results)
        self.tagset_details_bttn.Bind(wx.EVT_BUTTON, self.show_tagswindow)
        self.full_results_bttn.Bind(wx.EVT_BUTTON, self.show_fullresults)
        
        self.bind_filemenu_events()
        self.bind_editmenu_events()
        self.bind_helpmenu_events()
         
    def bind_filemenu_events(self):
        
        self.Bind(wx.EVT_MENU, self.on_exit, id=wx.ID_EXIT)
        self.Bind(wx.EVT_MENU, self.on_load, id=self.file_item_load.GetId())
        self.Bind(wx.EVT_MENU, self.on_save_to_text, id=wx.ID_SAVE)
        self.Bind(wx.EVT_MENU, self.on_save_to_csv, id=self.file_item_save_to_csv.GetId())
        
        
    def bind_editmenu_events(self):
        
        self.Bind(wx.EVT_MENU, self.on_cut, id=wx.ID_CUT)
        self.Bind(wx.EVT_MENU, self.on_copy, id=wx.ID_COPY)
        self.Bind(wx.EVT_MENU, self.on_paste, id=wx.ID_PASTE)
        self.Bind(wx.EVT_MENU, self.on_delete, id=wx.ID_DELETE)
        self.Bind(wx.EVT_MENU, self.on_clear_textbox, id=self.edit_item_clear_textbox.GetId())
        self.Bind(wx.EVT_MENU, self.on_select_all, id=wx.ID_SELECTALL)
    
    def bind_helpmenu_events(self):
        
        self.Bind(wx.EVT_MENU, self.on_view_help, id=wx.ID_HELP)
        self.Bind(wx.EVT_MENU, self.on_about, id=wx.ID_ABOUT)
          
            
            
    def set_results(self, evt):
        
        MainWindow._tagged_text, MainWindow._counter_tags = tag_text(text=self.textbox_main.GetValue(),
                                                                     use_averages=self.rb_averages_persentence.GetValue())
        self.textbox_main.ChangeValue(MainWindow._tagged_text)
        self.set_resultbox(MainWindow._counter_tags)
        if hasattr(MainWindow, "fullresults_window"):
            self.fullresults_window.set_results(MainWindow._counter_tags)
        else:
            self.fullresults_window = FullResultsWindow(MainWindow._counter_tags, parent=self, title="Full Results")
                                                        
        
        
                
    def set_resultbox(self, counter_tags):
        """
        Shows results in the results boxes. Some parts of speech are counted together.
        For example, adjectives, comparative adjectives, and superlative adjectives are
        counted together under Adjectives.
        """
        
        self.adjectives_box.ChangeValue("%g" % (counter_tags['JJ'] + counter_tags['JJR'] + counter_tags['JJS']))
        self.adverbs_box.ChangeValue("%g" % (counter_tags['RB'] + counter_tags['RBR'] + counter_tags['RBS'] + counter_tags['WRB']))
        self.conjunctions_box.ChangeValue("%g" % counter_tags['CC'])
        self.determiners_box.ChangeValue("%g" % counter_tags['DT'])
        self.modal_verb_box.ChangeValue("%g" % counter_tags['MD'])
        self.noun_box.ChangeValue("%g" % (counter_tags['NN'] + counter_tags['NNS']))
        self.preposition_box.ChangeValue("%g" % counter_tags['IN'])
        self.pronoun_box.ChangeValue("%g" % (counter_tags['PRP'] + counter_tags['PRP$'] + counter_tags['WP'] + counter_tags['WP$']))
        self.proper_noun_box.ChangeValue("%g" % (counter_tags['NNP'] + counter_tags['NNPS']))
        self.verb_base_box.ChangeValue("%g" % counter_tags['VB'])
        self.verb_gerund_box.ChangeValue("%g" % counter_tags['VBG'])
        self.verb_nonthird_box.ChangeValue("%g" % counter_tags['VBP'])
        self.verb_pastpar_box.ChangeValue("%g" % counter_tags['VBN'])
        self.verb_past_box.ChangeValue("%g" % counter_tags['VBD'])
        self.verb_third_box.ChangeValue("%g" % counter_tags['VBZ'])
        self.Wh_deteminer_box.ChangeValue("%g" % counter_tags['WDT'])
        self.words_box.ChangeValue("%g" % counter_tags['words'])
        self.sentences_box.ChangeValue("%g" % counter_tags['sentences'])
        
    def show_tagswindow(self, evt):
        
        self.tag_window = TagsetWindow(self, title="Tagset Details", size=(400, 400))
        self.tag_window.show_tagset()
        
    
    def show_fullresults(self, evt):
        """Shows the full results window, which includes all parts of speech
        in the Penn Treebank tagset.""" 
        
        if hasattr(MainWindow, "fullresults_window"):
            pass
        else:
            self.fullresults_window = FullResultsWindow(MainWindow._counter_tags, parent=self, title="Full Results")
        self.fullresults_window.Center()
        self.fullresults_window.Show()
        self.fullresults_window.Raise()
        
        
    def on_exit(self, evt):
        
        self.Close()
    
    def on_load(self, evt):
        
        file_dialog = FileDialog(self)
        file_dialog.prompt_for_file()
        file_name = file_dialog.get_file_name()
        is_success = self.textbox_main.LoadFile(file_name)
        if is_success:
            pass
        else:
            load_fail_dialog = wx.MessageDialog(parent=self, message="The file could not be loaded", style=wx.OK)
            load_fail_dialog.ShowModal() 
    
    def on_save_to_text(self, evt): 
        
        file_dialog = FileDialog(self)
        file_dialog.prompt_for_file(".txt")
        file_name = file_dialog.get_file_name()
        txt_file = open(file_name, 'a')
        wordclass_list = sorted(FullResultsWindow.tags_dict.iterkeys())
        for i in wordclass_list:
            try:
                txt_file.write(' '.join([i, FullResultsWindow.tags_dict[i], str(self._counter_tags[FullResultsWindow.tags_dict[i]]), "\n"]))
            except IOError:
                write_fail_dialog = wx.MessageDialog(parent=self, message="Could not write to the file", style=wx.OK)
                write_fail_dialog.ShowModal()
        
        txt_file.close()  
             
    
    def on_save_to_csv(self, evt):
        
        file_dialog = FileDialog(self)
        file_dialog.prompt_for_file(".csv")
        file_name = file_dialog.get_file_name()
        csv_file = open(file_name, 'a')
        csv_writer = csv.writer(csv_file)
        wordclass_list = sorted(FullResultsWindow.tags_dict.iterkeys())
        for i in wordclass_list:
            try:
                csv_writer.writerow((i, FullResultsWindow.tags_dict[i], str(self._counter_tags[FullResultsWindow.tags_dict[i]])))
            except IOError:
                write_fail_dialog = wx.MessageDialog(parent=self, message="Could not write to the file", style=wx.OK)
                write_fail_dialog.ShowModal()
        
        csv_file.close()
        
                
        
             
    def on_cut(self, evt):
        textbox = self.FindFocus()
        if wx.TheClipboard.Open():
            textbox.Cut()
        else:
            error_dialog = wx.MessageDialog(parent=self, message="Error: Unable to open the clipboard", style=wx.OK)
            error_dialog.ShowModal()
       
    
    def on_copy(self, evt):
        textbox = self.FindFocus()
        if wx.TheClipboard.Open():
            textbox.Copy()
        else:
            error_dialog = wx.MessageDialog(parent=self, message="Error: Unable to open the clipboard", style=wx.OK)
            error_dialog.ShowModal()
            
    
    def on_paste(self, evt):
        textbox = self.FindFocus()
        if wx.TheClipboard.Open():
            textbox.Paste()
        else:
            error_dialog = wx.MessageDialog(parent=self, message="Error: Unable to open the clipboard", style=wx.OK)
            error_dialog.ShowModal()
    
    def on_delete(self, evt):
        textbox = self.FindFocus()
        textbox.Cut()
        wx.TheClipboard.Clear()
    
    def on_clear_textbox(self, evt):
        self.textbox_main.Clear()
    
    def on_select_all(self, evt):
        textbox = self.FindFocus()
        textbox.SelectAll()
        
    def on_view_help(self, evt):
        self.help_window = HelpWindow(self, title="Help", size=(400, 400))
        self.help_window.show_help()
         
    def on_about(self, evt):
        description = """\nWord Tag is a part of speech tagging program that uses the NLTK library. It has features for\
 counting the number of words in each part of speech category in a body of text, saving results\
 to a text or CSV file, and loading text from a file."""
        
        program_license = """\nWord Tag is free software and licensed under the BSD license. Word Tag is distributed without any warranty, express or implied.\
 See the BSD License for more details."""
        
        about_dialog = AboutDialog(name='Word Tag', version='1.0', description=description, program_license=program_license, copy_right="(c) 2012 David Wong", developers=['David Wong'])
        about_dialog.show_about() 
         
             
def startapp():
    """Starts the main loop of the application."""
    app = wx.App(False)
    MainWindow(parent=None, title="Word Tag", size=(1200, 700))
    app.MainLoop() 
    
    
if __name__ == '__main__':
    startapp()
   
