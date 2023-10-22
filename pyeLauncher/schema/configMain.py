'''
Created on 2009-11-26

@author: peter
'''
from xml.dom import minidom
from LauncherProfile import LaunchConfigs
import sys

def main():
    doc = minidom.parse("../config/elauncher.xml")
    rootNode = doc.documentElement
    rootObj = LaunchConfigs.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    accessData(rootObj)
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_="LaunchConfigs",
        namespacedef_='')
    return rootObj

        
def accessData(root):
    _configs = root.get_Config()
    for config in _configs: 
        _taskbarName = config.get_TaskbarName()
        config.set_TaskbarName(_taskbarName+"_pyext")
        print("Name=" + _taskbarName)


if __name__ == '__main__':
    main()