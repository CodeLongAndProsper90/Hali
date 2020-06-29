
#!/usr/bin/python3
import gi.repository
from parse import get_pkg_attr
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2','4.0')
from gi.repository import Gtk, WebKit2, Gdk, GdkPixbuf, GLib
import parse
from sys import exit
import time
import os
import re

"""
A simple web browser.
Based off of:
https://brobin.me/blog/2014/07/how-to-make-your-own-web-browser-in-python/
Created 11/28/19 (Thanksgiving!)
assets/nexttab.png, assets/tabback.png Icon made by Flatpik from www.flaticon.com
assets/close.png made by Vectors Market from www.flaticon.com
assets/loading.png Icons made by Pixel perfect from www.flaticon.com
"""
class browser_win():


            #  End auto-run code!
  def path(self,relative):
    return os.path.join(
        os.environ.get("_MEIPASS2",os.path.abspath(".")),relative
      )
  def load_page(self, widget): #Handles loading of http and https webpages. Search_web handles google queires
    self.loadimg.show()
    address = self.address_bar.get_text()
    self.window.set_title(f'Loading: {address}')

    
    if bool(self.url.match(address)):              
      self.webview.load_uri(address)
    else:   
        self.search_web(address)
    GLib.timeout_add(1000, lambda w: self.loadimg.hide() , lambda : print('', end=''))
    self.loadimg.hide()
  def change_title(self, widget, frame, title):
    self.window.set_title(title)
  def change_url(self, widget, frame):
    uri = frame.get_uri()
    self.address_bar.set_text(uri)

  def go_back(self, widget):
    self.webview.go_back()

  def go_forward(self, widget):
    self.webview.go_forward()

  def refresh_page(self, widget):
    self.webview.reload()
  def go_home(self, widget):
    try:
      self.homeloc = get_pkg_attr('home: ','config')
      print(self.homeloc)
    except:
      self.homeloc='https://google.com'
      self.address_bar.set_text(self.homeloc)
      self.load_page(widget)

  def search_web(self, widget): #Queries google.com for the string in the addressbar

    address = self.address_bar.get_text()
    address = get_pkg_attr('search: ', 'config') + address.replace(' ', '%20') 
    self.webview.load_uri(address)
  def close(self,widget): 
    addr = self.address_bar.get_text()
    parse.set_pkg_attr('last: ',addr,'config')
    Gtk.main_quit()
    exit()
  def process_keypress(self, widget, event):
    ctrl = (event.state & Gdk.ModifierType.CONTROL_MASK)
    if ctrl and event.keyval == Gdk.KEY_L:
      self.address_bar.grab_focus()
  def __init__(self):
      self.url = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    # create window
      self.window = Gtk.Window()
      self.window.connect('destroy', self.close)
      self.window.set_default_size(360, 600)
      self.window.set_icon_from_file(self.path('assets/halibut2.png'))
      # Create navigation bar
      self.navigation_bar = Gtk.HBox()

      self.backimg = Gtk.Image.new_from_file("assets/back.png") #Make back icon
      self.back = Gtk.ToolButton() # Make back button
      self.back.set_icon_widget(self.backimg) # Bind the two

      #  make the foward button
      self.fowardimg = Gtk.Image.new_from_file("assets/foward.png")
      self.forward = Gtk.ToolButton()
      self.forward.set_icon_widget(self.fowardimg)

      #  Make the reload button
      self.refreshimg = Gtk.Image.new_from_file("assets/reload.png")
      self.refresh = Gtk.ToolButton()
      self.refresh.set_icon_widget(self.refreshimg)

      #  Make the home button 
      self.homeimg =  Gtk.Image.new_from_file("assets/home.png")
      self.home = Gtk.ToolButton()
      self.home.set_icon_widget(self.homeimg)

      #  Make the search button
      self.searchimg = Gtk.Image.new_from_file("assets/search.png")
      self.search = Gtk.ToolButton()
      self.search.set_icon_widget(self.searchimg)

      # self.nexttabimg = Gtk.Image.new_from_file("assets/nexttab.png")
      # self.nexttab = Gtk.ToolButton()
      # self.nexttab.set_icon_widget(self.nexttabimg)

      #This is the "tab back" button img

      # self.lasttabimg = Gtk.Image.new_from_file("assets/tabback.png")
      # self.lasttab = Gtk.ToolButton()
      # self.lasttab.set_icon_widget(self.lasttabimg)


      # self.closetabimg = Gtk.Image.new_from_file('assets/close.png')
      # self.closetab = Gtk.ToolButton()
    # self.closetab.set_icon_widget(self.closetabimg)

      pixbufAn = GdkPixbuf.PixbufAnimation.new_from_file("assets/loading.gif")
      self.loadimg = Gtk.Image()
      self.loadimg.set_from_animation(pixbufAn)
      #  Make the address bar that you type the url in

      self.tablbl = Gtk.Label()
      self.address_bar = Gtk.Entry()
      self.spinner = Gtk.Spinner()
      self.address_bar.set_property("width-request", 100) # Define default sive

      #  Connect the buttons to their respective functions
      self.back.connect('clicked', self.go_back) # Go back a page
      self.forward.connect('clicked', self.go_forward) # go foward a page
      self.refresh.connect('clicked', self.refresh_page) # Reload page
      self.home.connect('clicked', self.go_home) # GO to home page
      self.search.connect('clicked',self.search_web) # search the text ing the uri bar on google.com
      # self.nexttab.connect('clicked', self.next_tab) # go to the next tab
      # self.lasttab.connect('clicked', self.back_tab) # go back a tab
      # self.closetab.connect('clicked', self.close_tab)
      self.address_bar.connect('activate', self.load_page)
      self.window.connect('key-press-event', self.process_keypress) 
      #  load the buttons into the app
      # The False, False, 0 make the images work, but I don't why.
      # I suspect black magic...
      self.navigation_bar.pack_start(self.back, False, False,  0)
      self.navigation_bar.pack_start(self.forward, False, False, 0)
      self.navigation_bar.pack_start(self.refresh, False, False, 0)
      self.navigation_bar.pack_start(self.home, False, False, 0)
      self.navigation_bar.pack_start(self.search, False, False, 0)
      self.navigation_bar.pack_start(self.address_bar, False, False, 0)
      self.navigation_bar.pack_start(self.spinner, False, False, 0)



      # self.navigation_bar.pack_start(self.closetab, False, False, 0)

      # self.navigation_bar.pack_start(self.nexttab, False, False, 0)

      self.navigation_bar.pack_start(self.tablbl, False, False, 0)
      self.navigation_bar.pack_start(self.loadimg, False, False, 0)

      # Create view for webpage
      self.view = Gtk.ScrolledWindow()
      self.webview = WebKit2.WebView()
      self.go_home(None)
      last_page=parse.get_pkg_attr('last: ','config')
      self.webview.load_uri(last_page)
      # self.webview.connect('title-changed', self.change_title)
      # self.webview.connect('load-committed', self.change_url)
      #  self.webview.connect('download-requested', self.download_requested)
      #  self.webview.connect('mime-type-policy-decision-requested', self.policy_decision_requested)
      self.view.add(self.webview)
      # Add everything and initialize
      self.container = Gtk.VBox()
      self.container.pack_start(self.navigation_bar, False,False,0)
      self.container.pack_start(self.view, True, True, 0)

      self.window.add(self.container)
      self.window.set_default_size(800,600)
      self.tabs = []
      self.pos=0
      self.window.show_all()
      self.loadimg.hide()

      try:
        Gtk.main()
      except KeyboardInterrupt or EOFError:

        addr = self.address_bar.get_text()
        parse.set_pkg_attr('last: ',addr,'config')
        Gtk.main_quit()
        exit()
  
wow = browser_win()
