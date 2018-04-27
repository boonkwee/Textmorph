# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class frmMorph
###########################################################################

class frmMorph (wx.Frame):
    
    def __init__(self, parent):
        wx.Frame.__init__ (self, parent, id = wx.ID_ANY, title = u"Text Morph", pos = wx.DefaultPosition, size = wx.Size(500,300), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL)
        
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(255, 255, 255))
        
        bSizer1 = wx.BoxSizer(wx.VERTICAL)
        
        sbSizer1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Input text"), wx.VERTICAL)
        
        self.txt_input = wx.TextCtrl(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        sbSizer1.Add(self.txt_input, 1, wx.ALL|wx.EXPAND, 5)
        
        
        bSizer1.Add(sbSizer1, 0, wx.EXPAND, 5)
        
        sbSizer2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Processed text"), wx.VERTICAL)
        
        self.txt_processed = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY)
        sbSizer2.Add(self.txt_processed, 1, wx.ALL|wx.EXPAND, 5)
        
        
        bSizer1.Add(sbSizer2, 0, wx.EXPAND, 5)
        
        bSizer2 = wx.BoxSizer(wx.VERTICAL)
        
        bSizer5 = wx.BoxSizer(wx.HORIZONTAL)
        
        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.chk_modify_text_upper = wx.CheckBox(self, wx.ID_ANY, u"Uppercase", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.chk_modify_text_upper, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        
        self.chk_modify_text_lower = wx.CheckBox(self, wx.ID_ANY, u"Lowercase", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.chk_modify_text_lower, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        
        self.chk_modify_text_proper = wx.CheckBox(self, wx.ID_ANY, u"Titlecase", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.chk_modify_text_proper, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        
        
        bSizer5.Add(bSizer4, 0, wx.EXPAND, 5)
        
        bSizer6 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.chk_search_replace = wx.CheckBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer6.Add(self.chk_search_replace, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        
        self.lbl_search_text = wx.StaticText(self, wx.ID_ANY, u"Replace", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_search_text.Wrap(-1)
        bSizer6.Add(self.lbl_search_text, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        
        self.txt_search_text = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt_search_text.Enable(False)
        self.txt_search_text.SetMaxSize(wx.Size(30,-1))
        
        bSizer6.Add(self.txt_search_text, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        
        self.lbl_replace_with = wx.StaticText(self, wx.ID_ANY, u"with", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_replace_with.Wrap(-1)
        bSizer6.Add(self.lbl_replace_with, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        
        self.txt_replace_text = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.txt_replace_text.Enable(False)
        self.txt_replace_text.SetMaxSize(wx.Size(30,-1))
        
        bSizer6.Add(self.txt_replace_text, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        
        
        bSizer5.Add(bSizer6, 1, wx.EXPAND, 5)
        
        
        bSizer2.Add(bSizer5, 1, wx.EXPAND, 5)
        
        
        bSizer1.Add(bSizer2, 0, wx.EXPAND, 5)
        
        bSizer3 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.btnExit = wx.Button(self, wx.ID_ANY, u"Bye", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.btnExit, 0, wx.ALL, 5)
        
        
        bSizer1.Add(bSizer3, 0, wx.ALIGN_RIGHT, 5)
        
        
        self.SetSizer(bSizer1)
        self.Layout()
        self.status_bar = self.CreateStatusBar(2, wx.STB_SIZEGRIP, wx.ID_ANY)
        
        self.Centre(wx.BOTH)
        
        # Connect Events
        self.txt_input.Bind(wx.EVT_TEXT, self.on_input_text_changed)
        self.chk_modify_text_upper.Bind(wx.EVT_CHECKBOX, self.on_toggle_uppercase)
        self.chk_modify_text_lower.Bind(wx.EVT_CHECKBOX, self.on_toggle_lowercase)
        self.chk_modify_text_proper.Bind(wx.EVT_CHECKBOX, self.on_toggle_titlecase)
        self.chk_search_replace.Bind(wx.EVT_CHECKBOX, self.on_toggle_search_replace)
        self.txt_search_text.Bind(wx.EVT_TEXT, self.on_search_text)
        self.txt_replace_text.Bind(wx.EVT_TEXT, self.on_replace_text)
        self.btnExit.Bind(wx.EVT_BUTTON, self.on_close)
    
    def __del__(self):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def on_input_text_changed(self, event):
        event.Skip()
    
    def on_toggle_uppercase(self, event):
        event.Skip()
    
    def on_toggle_lowercase(self, event):
        event.Skip()
    
    def on_toggle_titlecase(self, event):
        event.Skip()
    
    def on_toggle_search_replace(self, event):
        event.Skip()
    
    def on_search_text(self, event):
        event.Skip()
    
    def on_replace_text(self, event):
        event.Skip()
    
    def on_close(self, event):
        event.Skip()
    

