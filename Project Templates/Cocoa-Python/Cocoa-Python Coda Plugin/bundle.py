#
#  bundle.py
#  �PROJECTNAME�
#
#  Created by �FULLUSERNAME� on �DATE�.
#  Copyright �ORGANIZATIONNAME� �YEAR�. All rights reserved.
#

# Update system path for the bundle.
import sys, objc
resource_path = objc.currentBundle().resourcePath()
sys.path.insert(0, resource_path.stringByAppendingPathComponent_('PyObjC'))
sys.path.insert(0, resource_path)

# Import modules containing classes required by the plugin.
import �PROJECTNAMEASIDENTIFIER�
