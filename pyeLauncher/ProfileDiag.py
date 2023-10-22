#Boa:Dialog:ProfileDialog

import wx
from wx.lib.anchors import LayoutAnchors
import wx.lib.stattext
import wx.lib.intctrl
import wx.lib.filebrowsebutton
from schema.LauncherProfile import ConfigType

def create(parent):
    return ProfileDialog(parent)

[wxID_PROFILEDIALOG, wxID_PROFILEDIALOGBUTTONCANCEL, 
 wxID_PROFILEDIALOGBUTTONECLIPSELOCATION, wxID_PROFILEDIALOGBUTTONOK, 
 wxID_PROFILEDIALOGBUTTONWORKSPACE, wxID_PROFILEDIALOGCBCLEANCACHE, 
 wxID_PROFILEDIALOGCBREFRESH, wxID_PROFILEDIALOGCBSHOWSPLASH, 
 wxID_PROFILEDIALOGFILEBROWSEJVM, wxID_PROFILEDIALOGGENERALINFOBOX, 
 wxID_PROFILEDIALOGGENSTATICTEXT1, wxID_PROFILEDIALOGGENSTATICTEXT2, 
 wxID_PROFILEDIALOGINTCTRLINITMEM, wxID_PROFILEDIALOGINTCTRLMAXMEM, 
 wxID_PROFILEDIALOGSTATICBOX1, wxID_PROFILEDIALOGSTATICBOX2, 
 wxID_PROFILEDIALOGSTATICTEXT1, wxID_PROFILEDIALOGSTATICTEXT2, 
 wxID_PROFILEDIALOGSTATICTEXT3, wxID_PROFILEDIALOGSTATICTEXT4, 
 wxID_PROFILEDIALOGSTATICTEXT5, wxID_PROFILEDIALOGTEXTECLIPSEARGS, 
 wxID_PROFILEDIALOGTEXTECLIPSELOCATION, wxID_PROFILEDIALOGTEXTNAME, 
 wxID_PROFILEDIALOGTEXTVMARGS, wxID_PROFILEDIALOGTEXTWORKSPACE, 
 wxID_PROFILEDIALOGTXTECLIPSENULL, wxID_PROFILEDIALOGTXTNAMENULL, 
 wxID_PROFILEDIALOGTXTWORKSPACENULL, 
] = [wx.NewId() for _init_ctrls in range(29)]

class ProfileDialog(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_PROFILEDIALOG, name='ProfileDialog',
              parent=prnt, pos=wx.Point(512, 306), size=wx.Size(542, 515),
              style=wx.CAPTION, title='Eclipse Runtime')
        self.SetClientSize(wx.Size(534, 488))
        self.Bind(wx.EVT_INIT_DIALOG, self.OnProfileDialogInitDialog)

        self.generalInfoBox = wx.StaticBox(id=wxID_PROFILEDIALOGGENERALINFOBOX,
              label='General Info', name='generalInfoBox', parent=self,
              pos=wx.Point(8, 8), size=wx.Size(512, 64), style=0)

        self.staticBox1 = wx.StaticBox(id=wxID_PROFILEDIALOGSTATICBOX1,
              label='Eclipse Information', name='staticBox1', parent=self,
              pos=wx.Point(8, 80), size=wx.Size(512, 192), style=0)

        self.staticBox2 = wx.StaticBox(id=wxID_PROFILEDIALOGSTATICBOX2,
              label='Java Information', name='staticBox2', parent=self,
              pos=wx.Point(8, 280), size=wx.Size(512, 152), style=0)

        self.staticText2 = wx.StaticText(id=wxID_PROFILEDIALOGSTATICTEXT2,
              label='Name:', name='staticText2', parent=self, pos=wx.Point(40,
              32), size=wx.Size(31, 16), style=0)

        self.textName = wx.TextCtrl(id=wxID_PROFILEDIALOGTEXTNAME,
              name='textName', parent=self, pos=wx.Point(104, 32),
              size=wx.Size(368, 21), style=0, value='')

        self.cbCleanCache = wx.CheckBox(id=wxID_PROFILEDIALOGCBCLEANCACHE,
              label='Clean plugin cache', name='cbCleanCache', parent=self,
              pos=wx.Point(24, 200), size=wx.Size(112, 13), style=0)
        self.cbCleanCache.SetValue(True)
        self.cbCleanCache.Set3StateValue(0)

        self.cbShowSplash = wx.CheckBox(id=wxID_PROFILEDIALOGCBSHOWSPLASH,
              label='Show splash screen', name='cbShowSplash', parent=self,
              pos=wx.Point(144, 200), size=wx.Size(144, 13), style=0)
        self.cbShowSplash.SetValue(False)

        self.cbRefresh = wx.CheckBox(id=wxID_PROFILEDIALOGCBREFRESH,
              label='Refresh worksapce', name='cbRefresh', parent=self,
              pos=wx.Point(336, 200), size=wx.Size(120, 13), style=0)
        self.cbRefresh.SetValue(True)

        self.fileBrowseJVM = wx.lib.filebrowsebutton.FileBrowseButton(buttonText='Browse',
              dialogTitle='Choose a file', fileMask='*.exe',
              id=wxID_PROFILEDIALOGFILEBROWSEJVM, initialValue='',
              labelText='File Entry:', parent=self, pos=wx.Point(16, 296),
              size=wx.Size(496, 48), startDirectory='.', style=wx.TAB_TRAVERSAL,
              toolTip='Type filename or click browse to choose file')
        self.fileBrowseJVM.SetLabel('JVM:')
        self.fileBrowseJVM.SetValue('')
        self.fileBrowseJVM.SetName('fileBrowseJVM')

        self.intCtrlInitMem = wx.lib.intctrl.IntCtrl(allow_long=False,
              allow_none=False, default_color=wx.BLACK,
              id=wxID_PROFILEDIALOGINTCTRLINITMEM, limited=False, max=None,
              min=None, name='intCtrlInitMem', oob_color=wx.RED, parent=self,
              pos=wx.Point(136, 364), size=wx.Size(100, 21), style=0,
              value=256)

        self.intCtrlMaxMem = wx.lib.intctrl.IntCtrl(allow_long=False,
              allow_none=False, default_color=wx.BLACK,
              id=wxID_PROFILEDIALOGINTCTRLMAXMEM, limited=False, max=None,
              min=None, name='intCtrlMaxMem', oob_color=wx.RED, parent=self,
              pos=wx.Point(392, 364), size=wx.Size(104, 21), style=0,
              value=1024)

        self.genStaticText1 = wx.lib.stattext.GenStaticText(ID=wxID_PROFILEDIALOGGENSTATICTEXT1,
              label='Init VM Memory[M]:', name='genStaticText1', parent=self,
              pos=wx.Point(16, 368), size=wx.Size(94, 13), style=0)

        self.genStaticText2 = wx.lib.stattext.GenStaticText(ID=wxID_PROFILEDIALOGGENSTATICTEXT2,
              label='Maximum VM Memory[M]:', name='genStaticText2', parent=self,
              pos=wx.Point(264, 368), size=wx.Size(122, 13), style=0)

        self.staticText1 = wx.StaticText(id=wxID_PROFILEDIALOGSTATICTEXT1,
              label='Workspace:', name='staticText1', parent=self,
              pos=wx.Point(24, 160), size=wx.Size(57, 13), style=0)

        self.textEclipseLocation = wx.TextCtrl(id=wxID_PROFILEDIALOGTEXTECLIPSELOCATION,
              name='textEclipseLocation', parent=self, pos=wx.Point(104, 116),
              size=wx.Size(304, 21), style=wx.TE_READONLY, value='')

        self.buttonEclipseLocation = wx.Button(id=wxID_PROFILEDIALOGBUTTONECLIPSELOCATION,
              label='Browse', name='buttonEclipseLocation', parent=self,
              pos=wx.Point(416, 115), size=wx.Size(75, 23), style=0)
        self.buttonEclipseLocation.Bind(wx.EVT_BUTTON,
              self.OnButtonEclipseLocationButton,
              id=wxID_PROFILEDIALOGBUTTONECLIPSELOCATION)

        self.staticText3 = wx.StaticText(id=wxID_PROFILEDIALOGSTATICTEXT3,
              label='Eclipse: ', name='staticText3', parent=self,
              pos=wx.Point(48, 120), size=wx.Size(39, 13), style=0)

        self.textWorkspace = wx.TextCtrl(id=wxID_PROFILEDIALOGTEXTWORKSPACE,
              name='textWorkspace', parent=self, pos=wx.Point(104, 156),
              size=wx.Size(304, 21), style=wx.TE_READONLY, value='')

        self.buttonWorkspace = wx.Button(id=wxID_PROFILEDIALOGBUTTONWORKSPACE,
              label='Browse', name='buttonWorkspace', parent=self,
              pos=wx.Point(416, 155), size=wx.Size(75, 23), style=0)
        self.buttonWorkspace.Bind(wx.EVT_BUTTON, self.OnButtonWorkspaceButton,
              id=wxID_PROFILEDIALOGBUTTONWORKSPACE)

        self.staticText4 = wx.StaticText(id=wxID_PROFILEDIALOGSTATICTEXT4,
              label='Additional VM args:', name='staticText4', parent=self,
              pos=wx.Point(32, 400), size=wx.Size(92, 13), style=0)

        self.staticText5 = wx.StaticText(id=wxID_PROFILEDIALOGSTATICTEXT5,
              label='Additional Eclipse Args:', name='staticText5', parent=self,
              pos=wx.Point(32, 236), size=wx.Size(111, 13), style=0)

        self.textEclipseArgs = wx.TextCtrl(id=wxID_PROFILEDIALOGTEXTECLIPSEARGS,
              name='textEclipseArgs', parent=self, pos=wx.Point(160, 232),
              size=wx.Size(336, 21), style=0, value='')

        self.textVMArgs = wx.TextCtrl(id=wxID_PROFILEDIALOGTEXTVMARGS,
              name='textVMArgs', parent=self, pos=wx.Point(136, 396),
              size=wx.Size(368, 21), style=0, value='')

        self.buttonOK = wx.Button(id=wxID_PROFILEDIALOGBUTTONOK, label='OK',
              name='buttonOK', parent=self, pos=wx.Point(336, 448),
              size=wx.Size(75, 23), style=0)
        self.buttonOK.Bind(wx.EVT_BUTTON, self.OnButtonOKButton,
              id=wxID_PROFILEDIALOGBUTTONOK)

        self.buttonCancel = wx.Button(id=wxID_PROFILEDIALOGBUTTONCANCEL,
              label='Cancel', name='buttonCancel', parent=self,
              pos=wx.Point(424, 448), size=wx.Size(75, 23), style=0)
        self.buttonCancel.Bind(wx.EVT_BUTTON, self.OnButtonCancelButton,
              id=wxID_PROFILEDIALOGBUTTONCANCEL)

        self.txtEclipseNull = wx.StaticText(id=wxID_PROFILEDIALOGTXTECLIPSENULL,
              label='*', name='txtEclipseNull', parent=self, pos=wx.Point(88,
              120), size=wx.Size(6, 13), style=0)
        self.txtEclipseNull.SetForegroundColour(wx.Colour(255, 0, 0))
        self.txtEclipseNull.SetConstraints(LayoutAnchors(self.txtEclipseNull,
              True, True, False, False))
        self.txtEclipseNull.Show(False)

        self.txtWorkspaceNull = wx.StaticText(id=wxID_PROFILEDIALOGTXTWORKSPACENULL,
              label='*', name='txtWorkspaceNull', parent=self, pos=wx.Point(88,
              160), size=wx.Size(6, 13), style=0)
        self.txtWorkspaceNull.SetForegroundColour(wx.Colour(255, 0, 0))
        self.txtWorkspaceNull.Show(False)

        self.txtNameNull = wx.StaticText(id=wxID_PROFILEDIALOGTXTNAMENULL,
              label='*', name='txtNameNull', parent=self, pos=wx.Point(88, 32),
              size=wx.Size(6, 13), style=0)
        self.txtNameNull.SetForegroundColour(wx.Colour(255, 0, 0))
        self.txtNameNull.Show(False)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def set_Profile(self, profile):
        self._profile = profile

    def get_Profile(self):
        return self._profile

    def OnProfileDialogInitDialog(self, event):
        if self._profile != None :
            name = self._profile.get_TaskbarName()
            self.textName.Value = name
            # file locator
            self.textEclipseLocation.Value = (self._profile.get_EclipseLoc())
            self.textWorkspace.Value = (self._profile.get_WorkspaceLoc())
            self.fileBrowseJVM.SetValue(self._profile.get_VMLoc())
            
            #eclipse settings
            bVal = self._profile.get_Clean()
            if( bVal == None): bVal = False
            self.cbCleanCache.SetValue(bVal)
            bVal = self._profile.get_Refresh()
            if( bVal == None): bVal = False
            self.cbRefresh.SetValue(bVal)
            bVal = self._profile.get_ShowSplash()
            if( bVal == None): bVal = False
            self.cbShowSplash.SetValue(bVal)
            
            eArgs = self._profile.get_EclipseArgs()
            if( eArgs ):
                self.textEclipseArgs.SetValue(eArgs)
            
            # JVM settings
            initVal = self._profile.get_Xms()
            self.intCtrlInitMem.SetValue(int(initVal))
            maxVal = self._profile.get_Xmx()
            self.intCtrlMaxMem.SetValue(int(maxVal))
            vmArgs = self._profile.get_VMArgs()
            if( vmArgs ):
                self.textVMArgs.Value = vmArgs;

    def OnButtonEclipseLocationButton(self, event):
        # Create the dialog. In this case the current directory is forced as the starting
        # directory for the dialog, and no default file name is forced. This can easilly
        # be changed in your program. This is an 'open' dialog, and allows multitple
        # file selections as well.
        #
        # Finally, if the directory is changed in the process of getting files, this
        # dialog is set up to change the current working directory to the path chosen.

        # Define the wildcard to filter executable files (e.g., .exe for Windows, .app for macOS)
        wildcard = "Executable Files (*.exe;*.app)|*.exe;*.app|All Files (*.*)|*.*"

        # Specify the default file (optional)
        default_file = "eclipse.exe"  # Provide the default file name

        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultDir=self.textEclipseLocation.Value, 
            defaultFile="SpringToolSuite4.app",
            wildcard=wildcard,
            style=wx.FD_OPEN
            )

        # Show the dialog and retrieve the user response. If it is the OK response, 
        # process the data.
        if dlg.ShowModal() == wx.ID_OK:
            # This returns a Python list of files that were selected.
            self.textEclipseLocation.Value = dlg.GetPaths()[0]

        # Destroy the dialog. Don't do this until you are done with it!
        # BAD things can happen otherwise!
        dlg.Destroy()


    def OnButtonWorkspaceButton(self, event):
        dlg = wx.DirDialog(self, "Choose a directory:",
                          style=wx.DD_DEFAULT_STYLE
                           | wx.DD_DIR_MUST_EXIST
                           
                           )
        dlg.SetPath(self.textWorkspace.Value)
        # If the user selects OK, then we process the dialog's data.
        # This is done by getting the path data from the dialog - BEFORE
        # we destroy it. 
        if dlg.ShowModal() == wx.ID_OK:
            self.textWorkspace.Value = dlg.GetPath()

        # Only destroy a dialog after you're done with it.
        dlg.Destroy()

    def OnButtonOKButton(self, event):
        self.txtNameNull.Show(False)
        self.txtEclipseNull.Show(False)
        self.txtWorkspaceNull.Show(False)
        
        profileName = self.textName.Value
        eclipseLocation = self.textEclipseLocation.Value
        workspaceLocation =  self.textWorkspace.Value
        
        if profileName == None or len(profileName) == 0 :
            self.txtNameNull.Show(True)
        elif eclipseLocation == None or len(eclipseLocation) == 0:
            self.txtEclipseNull.Show (True)
        elif  workspaceLocation == None or len(workspaceLocation) == 0:
            self.txtWorkspaceNull.Show(True)
        else :  
            # turn off error info
            self.txtNameNull.Show(False)
            self.txtEclipseNull.Show(False)
            self.txtWorkspaceNull.Show(False)
            
            if self._profile == None :
                self._profile = ConfigType()
            
            self._profile.set_TaskbarName(profileName)
            # eclipse
            self._profile.set_EclipseLoc(eclipseLocation)
            self._profile.set_WorkspaceLoc(workspaceLocation)
            # cache clean
            self._profile.set_Clean(self.cbCleanCache.Value)
            # splash 
            self._profile.set_ShowSplash(self.cbShowSplash.Value)
            # refresh
            self._profile.set_Refresh(self.cbRefresh.Value)
            # additional args
            self._profile.set_EclipseArgs(self.textEclipseArgs.Value)
            # java
            self._profile.set_VMLoc(self.fileBrowseJVM.GetValue())
            # maximium
            self._profile.set_Xmx(self.intCtrlMaxMem.Value)
            self._profile.set_Xms(self.intCtrlInitMem.Value)
            self._profile.set_VMArgs(self.textVMArgs.Value)
            
            self.EndModal(wx.ID_OK)

    def OnButtonCancelButton(self, event):
        self.EndModal(wx.ID_CANCEL)

