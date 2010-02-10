#
#  �PROJECTNAMEASIDENTIFIER�Document.py
#  �PROJECTNAME�
#
#  Created by �FULLUSERNAME� on �DATE�.
#  Copyright �ORGANIZATIONNAME� �YEAR�. All rights reserved.
#

from Foundation import *
from AppKit import *

class �PROJECTNAMEASIDENTIFIER�Document(NSDocument):
    def init(self):
        self = super(�PROJECTNAMEASIDENTIFIER�Document, self).init()
        # initialization code
        return self
        
    def windowNibName(self):
        return u"�PROJECTNAMEASIDENTIFIER�Document"
    
    def windowControllerDidLoadNib_(self, aController):
        super(�PROJECTNAMEASIDENTIFIER�Document, self).windowControllerDidLoadNib_(aController)

    def dataOfType_error_(self, typeName, outError):
        return None, NSError.errorWithDomain_code_userInfo_(NSOSStatusErrorDomain, -4, None) # -4 is unimpErr from CarbonCore
    
    def readFromData_ofType_error_(self, data, typeName, outError):
        return NO, NSError.errorWithDomain_code_userInfo_(NSOSStatusErrorDomain, -4, None) # -4 is unimpErr from CarbonCore
