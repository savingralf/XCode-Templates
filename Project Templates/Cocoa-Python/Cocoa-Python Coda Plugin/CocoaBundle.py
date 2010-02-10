#
#  �PROJECTNAMEASIDENTIFIER�.py
#  �PROJECTNAME�
#
#  Created by �FULLUSERNAME� on �DATE�.
#  Copyright �ORGANIZATIONNAME� �YEAR�. All rights reserved.
#

import objc
from Foundation import NSObject, NSImage, NSAttributedString, NSBundle
from AppKit import NSApp, NSNibOwner

class �PROJECTNAMEASIDENTIFIER�(NSObject, objc.protocolNamed('CodaPlugIn')):
    def name(self):
        return '�PROJECTNAME�'

    def initWithPlugInController_bundle_(self, controller, bundle):
        self = super(�PROJECTNAMEASIDENTIFIER�, self).init()
        if self is not None:
            bundle.loadNibFile_externalNameTable_withZone_('�PROJECTNAMEASIDENTIFIER�', 
                                                           {NSNibOwner: self}, None)
            controller.registerActionWithTitle_target_selector_('About �PROJECTNAME�', 
                                                                self, 'showAboutPlugin:')
        return self

    @objc.IBAction
    def showAboutPlugin_(self, sender):
        icon = None
        info = objc.currentBundle().infoDictionary()
        if 'CFBundleIconFile' in info:
            icon_file = info['CFBundleIconFile']
            icon_path = objc.currentBundle().pathForImageResource_(icon_file)
            if icon_path is not None:
                icon = NSImage.alloc().initWithContentsOfFile_(icon_path)
        if icon is None:
            icon = NSImage.imageNamed_('NSApplicationIcon')
        options = {'Credits': NSAttributedString.alloc().initWithString_('�FULLUSERNAME�'),
                   'ApplicationName': self.name(),
                   'ApplicationIcon': icon,
                   'ApplicationVersion': info['CFBundleShortVersionString'],
                   'Version': 'Coda %s' % NSBundle.mainBundle().infoDictionary()['CFBundleShortVersionString']}
        NSApp.orderFrontStandardAboutPanelWithOptions_(options)