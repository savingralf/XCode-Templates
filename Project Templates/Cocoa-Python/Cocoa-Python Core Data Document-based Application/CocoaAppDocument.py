#
#  �PROJECTNAMEASIDENTIFIER�Document.py
#  �PROJECTNAME�
#
#  Created by �FULLUSERNAME� on �DATE�.
#  Copyright �ORGANIZATIONNAME� �YEAR�. All rights reserved.
#

from Foundation import *
from CoreData import *
from AppKit import *

class �PROJECTNAMEASIDENTIFIER�Document(NSPersistentDocument):
    def init(self):
        self = super(�PROJECTNAMEASIDENTIFIER�Document, self).init()
        # initialization code
        return self
        
    def windowNibName(self):
        return u"�PROJECTNAMEASIDENTIFIER�Document"
    
    def windowControllerDidLoadNib_(self, aController):
        super(�PROJECTNAMEASIDENTIFIER�Document, self).windowControllerDidLoadNib_(aController)
        # user interface preparation code
