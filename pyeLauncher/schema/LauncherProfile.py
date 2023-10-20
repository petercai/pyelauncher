#!/usr/bin/env python

#
# Generated Thu Nov 26 23:14:46 2009 by generateDS.py version 1.19a.
#

import sys
import getopt
from xml.dom import minidom
from xml.dom import Node
str_lower = str.lower
#
# User methods
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.

try:
    from generatedssuper import GeneratedsSuper
except ImportError as exp:

    class GeneratedsSuper(object):
        def format_string(self, input_data, input_name=''):
            return input_data
        def format_integer(self, input_data, input_name=''):
            return '%d' % input_data
        def format_float(self, input_data, input_name=''):
            return '%f' % input_data
        def format_double(self, input_data, input_name=''):
            return '%e' % input_data
        def format_boolean(self, input_data, input_name=''):
            return '%s' % input_data


#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Globals
#

ExternalEncoding = 'Cp1252'

#
# Support/utility functions.
#

def showIndent(outfile, level):
    for idx in range(level):
        outfile.write('    ')

def quote_xml(inStr):
    s1 = (isinstance(inStr, str) and inStr or
          '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1

def quote_attrib(inStr):
    s1 = (isinstance(inStr, str) and inStr or '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return s1

def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, outfile, level, name, namespace):
        if self.category == MixedContainer.CategoryText:
            outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(outfile, level, namespace,name)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' % (self.name, self.value, self.name))
    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write('MixedContainer(%d, %d, "%s", "%s"),\n' % \
                (self.category, self.content_type, self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write('MixedContainer(%d, %d, "%s", "%s"),\n' % \
                (self.category, self.content_type, self.name, self.value))
        else:    # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write('MixedContainer(%d, %d, "%s",\n' % \
                (self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


class MemberSpec_(object):
    def __init__(self, name='', data_type='', container=0):
        self.name = name
        self.data_type = data_type
        self.container = container
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_data_type(self, data_type): self.data_type = data_type
    def get_data_type_chain(self): return self.data_type
    def get_data_type(self):
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return 'xs:string'
        else:
            return self.data_type
    def set_container(self, container): self.container = container
    def get_container(self): return self.container

def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)

#
# Data representation classes.
#

class LaunchConfigs(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, version=None, Config=None):
        self.version = _cast(None, version)
        if Config is None:
            self.Config = []
        else:
            self.Config = Config
    def factory(*args_, **kwargs_):
        if LaunchConfigs.subclass:
            return LaunchConfigs.subclass(*args_, **kwargs_)
        else:
            return LaunchConfigs(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Config(self): return self.Config
    def set_Config(self, Config): self.Config = Config
    def add_Config(self, value): self.Config.append(value)
    def insert_Config(self, index, value): self.Config[index] = value
    def get_version(self): return self.version
    def set_version(self, version): self.version = version
    def validate_VersionType(self, value):
        # Validate type VersionType, a restriction on xs:token.
        pass
    def export(self, outfile, level, namespace_='', name_='LaunchConfigs', namespacedef_=''):
        showIndent(outfile, level)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        self.exportAttributes(outfile, level, namespace_, name_='LaunchConfigs')
        if self.hasContent_():
            outfile.write('>\n')
            self.exportChildren(outfile, level + 1, namespace_, name_)
            showIndent(outfile, level)
            outfile.write('</%s%s>\n' % (namespace_, name_))
        else:
            outfile.write('/>\n')
    def exportAttributes(self, outfile, level, namespace_='', name_='LaunchConfigs'):
        outfile.write(' version=%s' % (quote_attrib(self.version), ))
    def exportChildren(self, outfile, level, namespace_='', name_='LaunchConfigs'):
        for Config_ in self.Config:
            Config_.export(outfile, level, namespace_, name_='Config')
    def hasContent_(self):
        if (
            self.Config
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='LaunchConfigs'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        if self.version is not None:
            showIndent(outfile, level)
            outfile.write('version = "%s",\n' % (self.version,))
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Config=[\n')
        level += 1
        for Config in self.Config:
            showIndent(outfile, level)
            outfile.write('model_.Config(\n')
            Config.exportLiteral(outfile, level, name_='Config')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        if attrs.get('version'):
            self.version = attrs.get('version').value
            self.validate_VersionType(self.version)    # validate type VersionType
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'Config':
            obj_ = ConfigType.factory()
            obj_.build(child_)
            self.Config.append(obj_)
# end class LaunchConfigs


class ConfigType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, TaskbarName=None, XmsUnits=None, VMLoc=None, Name=None, EclipseArgs=None, ShowSplash=None, Refresh=None, Xms=None, EclipseLoc=None, Xmx=None, Clean=None, VMArgs=None, WorkspaceLoc=None, XmxUnits=None, Description=None, valueOf_=''):
        self.TaskbarName = _cast(None, TaskbarName)
        self.XmsUnits = _cast(None, XmsUnits)
        self.VMLoc = _cast(None, VMLoc)
        self.Name = _cast(None, Name)
        self.EclipseArgs = _cast(None, EclipseArgs)
        self.ShowSplash = _cast(bool, ShowSplash)
        self.Refresh = _cast(bool, Refresh)
        self.Xms = _cast(None, Xms)
        self.EclipseLoc = _cast(None, EclipseLoc)
        self.Xmx = _cast(None, Xmx)
        self.Clean = _cast(bool, Clean)
        self.VMArgs = _cast(None, VMArgs)
        self.WorkspaceLoc = _cast(None, WorkspaceLoc)
        self.XmxUnits = _cast(None, XmxUnits)
        self.Description = _cast(None, Description)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if ConfigType.subclass:
            return ConfigType.subclass(*args_, **kwargs_)
        else:
            return ConfigType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_TaskbarName(self): return self.TaskbarName
    def set_TaskbarName(self, TaskbarName): self.TaskbarName = TaskbarName
    def validate_NameType(self, value):
        # Validate type NameType, a restriction on xs:string.
        pass
    def get_XmsUnits(self): return self.XmsUnits
    def set_XmsUnits(self, XmsUnits): self.XmsUnits = XmsUnits
    def validate_UnitsType(self, value):
        # Validate type UnitsType, a restriction on xs:string.
        pass
    def get_VMLoc(self): return self.VMLoc
    def set_VMLoc(self, VMLoc): self.VMLoc = VMLoc
    def validate_PathnameType(self, value):
        # Validate type PathnameType, a restriction on xs:token.
        pass
    def get_Name(self): return self.Name
    def set_Name(self, Name): self.Name = Name
    def get_EclipseArgs(self): return self.EclipseArgs
    def set_EclipseArgs(self, EclipseArgs): self.EclipseArgs = EclipseArgs
    def validate_ArgsType(self, value):
        # Validate type ArgsType, a restriction on xs:string.
        pass
    def get_ShowSplash(self): return self.ShowSplash
    def set_ShowSplash(self, ShowSplash): self.ShowSplash = ShowSplash
    def get_Refresh(self): return self.Refresh
    def set_Refresh(self, Refresh): self.Refresh = Refresh
    def get_Xms(self): return self.Xms
    def set_Xms(self, Xms): self.Xms = Xms
    def validate_XmsType(self, value):
        # Validate type XmsType, a restriction on xs:unsignedInt.
        pass
    def get_EclipseLoc(self): return self.EclipseLoc
    def set_EclipseLoc(self, EclipseLoc): self.EclipseLoc = EclipseLoc
    def get_Xmx(self): return self.Xmx
    def set_Xmx(self, Xmx): self.Xmx = Xmx
    def validate_XmxType(self, value):
        # Validate type XmxType, a restriction on xs:unsignedInt.
        pass
    def get_Clean(self): return self.Clean
    def set_Clean(self, Clean): self.Clean = Clean
    def get_VMArgs(self): return self.VMArgs
    def set_VMArgs(self, VMArgs): self.VMArgs = VMArgs
    def get_WorkspaceLoc(self): return self.WorkspaceLoc
    def set_WorkspaceLoc(self, WorkspaceLoc): self.WorkspaceLoc = WorkspaceLoc
    def get_XmxUnits(self): return self.XmxUnits
    def set_XmxUnits(self, XmxUnits): self.XmxUnits = XmxUnits
    def get_Description(self): return self.Description
    def set_Description(self, Description): self.Description = Description
    def validate_DescType(self, value):
        # Validate type DescType, a restriction on xs:string.
        pass
    def getValueOf_(self): return self.valueOf_
    def setValueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def export(self, outfile, level, namespace_='', name_='ConfigType', namespacedef_=''):
        showIndent(outfile, level)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        self.exportAttributes(outfile, level, namespace_, name_='ConfigType')
        if self.hasContent_():
            outfile.write('>')
            self.exportChildren(outfile, level + 1, namespace_, name_)
            outfile.write('</%s%s>\n' % (namespace_, name_))
        else:
            outfile.write('/>\n')
    def exportAttributes(self, outfile, level, namespace_='', name_='ConfigType'):
        if self.TaskbarName is not None:
            outfile.write(' TaskbarName=%s' % (quote_attrib(self.TaskbarName), ))
        if self.XmsUnits is not None:
            outfile.write(' XmsUnits=%s' % (quote_attrib(self.XmsUnits), ))
        if self.VMLoc is not None:
            outfile.write(' VMLoc=%s' % (quote_attrib(self.VMLoc), ))
        outfile.write(' Name=%s' % (quote_attrib(self.Name), ))
        if self.EclipseArgs is not None:
            outfile.write(' EclipseArgs=%s' % (quote_attrib(self.EclipseArgs), ))
        if self.ShowSplash is not None:
            outfile.write(' ShowSplash="%s"' % self.format_boolean(str_lower(str(self.ShowSplash)), input_name='ShowSplash'))
        if self.Refresh is not None:
            outfile.write(' Refresh="%s"' % self.format_boolean(str_lower(str(self.Refresh)), input_name='Refresh'))
        if self.Xms is not None:
            outfile.write(' Xms=%s' % (quote_attrib(self.Xms), ))
        outfile.write(' EclipseLoc=%s' % (quote_attrib(self.EclipseLoc), ))
        if self.Xmx is not None:
            outfile.write(' Xmx=%s' % (quote_attrib(self.Xmx), ))
        if self.Clean is not None:
            outfile.write(' Clean="%s"' % self.format_boolean(str_lower(str(self.Clean)), input_name='Clean'))
        if self.VMArgs is not None:
            outfile.write(' VMArgs=%s' % (quote_attrib(self.VMArgs), ))
        outfile.write(' WorkspaceLoc=%s' % (quote_attrib(self.WorkspaceLoc), ))
        if self.XmxUnits is not None:
            outfile.write(' XmxUnits=%s' % (quote_attrib(self.XmxUnits), ))
        if self.Description is not None:
            outfile.write(' Description=%s' % (quote_attrib(self.Description), ))
    def exportChildren(self, outfile, level, namespace_='', name_='ConfigType'):
        if self.valueOf_.find('![CDATA') > -1:
            value=quote_xml('%s' % self.valueOf_)
            value=value.replace('![CDATA','<![CDATA')
            value=value.replace(']]',']]>')
            outfile.write(value)
        else:
            outfile.write(quote_xml('%s' % self.valueOf_))
    def hasContent_(self):
        if (
            self.valueOf_
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='ConfigType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, name_):
        if self.TaskbarName is not None:
            showIndent(outfile, level)
            outfile.write('TaskbarName = "%s",\n' % (self.TaskbarName,))
        if self.XmsUnits is not None:
            showIndent(outfile, level)
            outfile.write('XmsUnits = "%s",\n' % (self.XmsUnits,))
        if self.VMLoc is not None:
            showIndent(outfile, level)
            outfile.write('VMLoc = "%s",\n' % (self.VMLoc,))
        if self.Name is not None:
            showIndent(outfile, level)
            outfile.write('Name = "%s",\n' % (self.Name,))
        if self.EclipseArgs is not None:
            showIndent(outfile, level)
            outfile.write('EclipseArgs = "%s",\n' % (self.EclipseArgs,))
        if self.ShowSplash is not None:
            showIndent(outfile, level)
            outfile.write('ShowSplash = %s,\n' % (self.ShowSplash,))
        if self.Refresh is not None:
            showIndent(outfile, level)
            outfile.write('Refresh = %s,\n' % (self.Refresh,))
        if self.Xms is not None:
            showIndent(outfile, level)
            outfile.write('Xms = %s,\n' % (self.Xms,))
        if self.EclipseLoc is not None:
            showIndent(outfile, level)
            outfile.write('EclipseLoc = "%s",\n' % (self.EclipseLoc,))
        if self.Xmx is not None:
            showIndent(outfile, level)
            outfile.write('Xmx = %s,\n' % (self.Xmx,))
        if self.Clean is not None:
            showIndent(outfile, level)
            outfile.write('Clean = %s,\n' % (self.Clean,))
        if self.VMArgs is not None:
            showIndent(outfile, level)
            outfile.write('VMArgs = "%s",\n' % (self.VMArgs,))
        if self.WorkspaceLoc is not None:
            showIndent(outfile, level)
            outfile.write('WorkspaceLoc = "%s",\n' % (self.WorkspaceLoc,))
        if self.XmxUnits is not None:
            showIndent(outfile, level)
            outfile.write('XmxUnits = "%s",\n' % (self.XmxUnits,))
        if self.Description is not None:
            showIndent(outfile, level)
            outfile.write('Description = "%s",\n' % (self.Description,))
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('valueOf_ = "%s",\n' % (self.valueOf_,))
    def build(self, node_):
        attrs = node_.attributes
        self.buildAttributes(attrs)
        self.valueOf_ = ''
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildAttributes(self, attrs):
        if attrs.get('TaskbarName'):
            self.TaskbarName = attrs.get('TaskbarName').value
            self.validate_NameType(self.TaskbarName)    # validate type NameType
        if attrs.get('XmsUnits'):
            self.XmsUnits = attrs.get('XmsUnits').value
            self.validate_UnitsType(self.XmsUnits)    # validate type UnitsType
        if attrs.get('VMLoc'):
            self.VMLoc = attrs.get('VMLoc').value
            self.validate_PathnameType(self.VMLoc)    # validate type PathnameType
        if attrs.get('Name'):
            self.Name = attrs.get('Name').value
            self.validate_NameType(self.Name)    # validate type NameType
        if attrs.get('EclipseArgs'):
            self.EclipseArgs = attrs.get('EclipseArgs').value
            self.validate_ArgsType(self.EclipseArgs)    # validate type ArgsType
        if attrs.get('ShowSplash'):
            if attrs.get('ShowSplash').value in ('true', '1'):
                self.ShowSplash = True
            elif attrs.get('ShowSplash').value in ('false', '0'):
                self.ShowSplash = False
            else:
                raise ValueError('Bad boolean attribute (ShowSplash)')
        if attrs.get('Refresh'):
            if attrs.get('Refresh').value in ('true', '1'):
                self.Refresh = True
            elif attrs.get('Refresh').value in ('false', '0'):
                self.Refresh = False
            else:
                raise ValueError('Bad boolean attribute (Refresh)')
        if attrs.get('Xms'):
            self.Xms = attrs.get('Xms').value
            self.validate_XmsType(self.Xms)    # validate type XmsType
        if attrs.get('EclipseLoc'):
            self.EclipseLoc = attrs.get('EclipseLoc').value
            self.validate_PathnameType(self.EclipseLoc)    # validate type PathnameType
        if attrs.get('Xmx'):
            self.Xmx = attrs.get('Xmx').value
            self.validate_XmxType(self.Xmx)    # validate type XmxType
        if attrs.get('Clean'):
            if attrs.get('Clean').value in ('true', '1'):
                self.Clean = True
            elif attrs.get('Clean').value in ('false', '0'):
                self.Clean = False
            else:
                raise ValueError('Bad boolean attribute (Clean)')
        if attrs.get('VMArgs'):
            self.VMArgs = attrs.get('VMArgs').value
            self.validate_ArgsType(self.VMArgs)    # validate type ArgsType
        if attrs.get('WorkspaceLoc'):
            self.WorkspaceLoc = attrs.get('WorkspaceLoc').value
            self.validate_PathnameType(self.WorkspaceLoc)    # validate type PathnameType
        if attrs.get('XmxUnits'):
            self.XmxUnits = attrs.get('XmxUnits').value
            self.validate_UnitsType(self.XmxUnits)    # validate type UnitsType
        if attrs.get('Description'):
            self.Description = attrs.get('Description').value
            self.validate_DescType(self.Description)    # validate type DescType
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.TEXT_NODE:
            self.valueOf_ += child_.nodeValue
        elif child_.nodeType == Node.CDATA_SECTION_NODE:
            self.valueOf_ += '![CDATA['+child_.nodeValue+']]'
# end class ConfigType


USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""

def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def parse(inFileName):
    doc = minidom.parse(inFileName)
    rootNode = doc.documentElement
    rootObj = LaunchConfigs.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_="LaunchConfigs", 
        namespacedef_='')
    return rootObj


def parseString(inString):
    doc = minidom.parseString(inString)
    rootNode = doc.documentElement
    rootObj = LaunchConfigs.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_="LaunchConfigs",
        namespacedef_='')
    return rootObj


def parseLiteral(inFileName):
    doc = minidom.parse(inFileName)
    rootNode = doc.documentElement
    rootObj = LaunchConfigs.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('from LauncherProfile import *\n\n')
    sys.stdout.write('rootObj = LaunchConfigs(\n')
    rootObj.exportLiteral(sys.stdout, 0, name_="LaunchConfigs")
    sys.stdout.write(')\n')
    return rootObj


def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()

