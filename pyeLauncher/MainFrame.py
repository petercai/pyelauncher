#Boa:Frame:AppFrame
from xml.dom import minidom

import wx
from wx.lib.anchors import LayoutAnchors
from ProfileDiag import ProfileDialog
from schema.LauncherProfile import LaunchConfigs
from schema.LauncherProfile import ConfigType
import sys
import copy

def create(parent):
    return AppFrame(parent)

[wxID_APPFRAME, wxID_APPFRAMEBTNCOPYPROFILE, wxID_APPFRAMEBTNDELETEPROFILE, 
 wxID_APPFRAMEBTNEDITPROFILE, wxID_APPFRAMEBTNNEWPROFILE, 
 wxID_APPFRAMEBTNRUNPROFILE, wxID_APPFRAMELSTPROFILES, wxID_APPFRAMEMAINPANEL, 
 wxID_APPFRAMEMAINSTATUSBAR, 
] = [wx.NewId() for _init_ctrls in range(9)]

[wxID_APPFRAMEFILEMENUACTION_NEW, wxID_APPFRAMEFILEMENUACTION_RUN, 
] = [wx.NewId() for _init_coll_fileMenu_Items in range(2)]

[wxID_APPFRAMEEDITMENUACTION_COPY, wxID_APPFRAMEEDITMENUACTION_EDIT, 
] = [wx.NewId() for _init_coll_editMenu_Items in range(2)]

[wxID_APPFRAMEMAINTOOLBARACTION_NEW] = [wx.NewId() for _init_coll_mainToolBar_Tools in range(1)]

[wxID_APPFRAMEHELPMENUACTION_ABOUT] = [wx.NewId() for _init_coll_helpMenu_Items in range(1)]

class AppFrame(wx.Frame):
    def _init_coll_mainMenuBar_Menus(self, parent):
        # generated method, don't edit

        parent.Append(menu=self.fileMenu, title='File')
        parent.Append(menu=self.editMenu, title='Edit')
        parent.Append(menu=self.helpMenu, title='Help')

    def _init_coll_editMenu_Items(self, parent):
        # generated method, don't edit

        parent.Append(helpString='', id=wxID_APPFRAMEEDITMENUACTION_COPY,
              kind=wx.ITEM_NORMAL, item='Copy')
        parent.Append(helpString='', id=wxID_APPFRAMEEDITMENUACTION_EDIT,
              kind=wx.ITEM_NORMAL, item='Edit')

    def _init_coll_helpMenu_Items(self, parent):
        # generated method, don't edit

        parent.Append(helpString='', id=wxID_APPFRAMEHELPMENUACTION_ABOUT,
              kind=wx.ITEM_NORMAL, item='About')

    def _init_coll_fileMenu_Items(self, parent):
        # generated method, don't edit

        parent.Append(helpString='', id=wxID_APPFRAMEFILEMENUACTION_NEW,
              kind=wx.ITEM_NORMAL, item='New...')
        parent.Append(helpString='', id=wxID_APPFRAMEFILEMENUACTION_RUN,
              kind=wx.ITEM_NORMAL, item='Run')
        self.Bind(wx.EVT_MENU, self.OnNewEclipseConfiguration,
              id=wxID_APPFRAMEFILEMENUACTION_NEW)

    def _init_coll_lstProfiles_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT, heading='Name',
              width=150)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT,
              heading='Eclipse', width=85)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT, heading='JVM',
              width=85)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_LEFT,
              heading='Workspace', width=-1)

    def _init_coll_mainStatusBar_Fields(self, parent):
        # generated method, don't edit
        parent.SetFieldsCount(1)

        parent.SetStatusText(text='Ready')

        parent.SetStatusWidths([-1])

    def _init_utils(self):
        # generated method, don't edit
        self.fileMenu = wx.Menu(title='')

        self.editMenu = wx.Menu(title='')

        self.helpMenu = wx.Menu(title='')

        self.mainMenuBar = wx.MenuBar()
        self.mainMenuBar.SetClientSize(wx.Size(117150544, -1))

        self._init_coll_fileMenu_Items(self.fileMenu)
        self._init_coll_editMenu_Items(self.editMenu)
        self._init_coll_helpMenu_Items(self.helpMenu)
        self._init_coll_mainMenuBar_Menus(self.mainMenuBar)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_APPFRAME, name='AppFrame', parent=prnt,
              pos=wx.Point(453, 337), size=wx.Size(485, 314),
              style=wx.DEFAULT_FRAME_STYLE, title='Eclipse Launcher')
        self._init_utils()
        self.SetClientSize(wx.Size(477, 287))
        self.SetMenuBar(self.mainMenuBar)

        self.mainStatusBar = wx.StatusBar(id=wxID_APPFRAMEMAINSTATUSBAR,
              name='mainStatusBar', parent=self, style=0)
        self.mainStatusBar.SetAutoLayout(True)
        self._init_coll_mainStatusBar_Fields(self.mainStatusBar)
        self.SetStatusBar(self.mainStatusBar)

        self.mainPanel = wx.Panel(id=wxID_APPFRAMEMAINPANEL, name='mainPanel',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(477, 248),
              style=wx.TAB_TRAVERSAL)
        self.mainPanel.SetConstraints(LayoutAnchors(self.mainPanel, True, True,
              True, True))
        self.mainPanel.SetAutoLayout(True)
        self.mainPanel.Bind(wx.EVT_SIZE, self.OnMainPanelSize)

        self.btnCopyProfile = wx.Button(id=wxID_APPFRAMEBTNCOPYPROFILE,
              label='Copy', name='btnCopyProfile', parent=self.mainPanel,
              pos=wx.Point(376, 88), size=wx.Size(88, 23), style=0)
        self.btnCopyProfile.Bind(wx.EVT_BUTTON, self.OnBtnCopyProfileButton,
              id=wxID_APPFRAMEBTNCOPYPROFILE)

        self.btnEditProfile = wx.Button(id=wxID_APPFRAMEBTNEDITPROFILE,
              label='Edit', name='btnEditProfile', parent=self.mainPanel,
              pos=wx.Point(376, 120), size=wx.Size(88, 23), style=0)
        self.btnEditProfile.Bind(wx.EVT_BUTTON, self.OnBtnEditProfileButton,
              id=wxID_APPFRAMEBTNEDITPROFILE)

        self.btnDeleteProfile = wx.Button(id=wxID_APPFRAMEBTNDELETEPROFILE,
              label='Delete', name='btnDeleteProfile', parent=self.mainPanel,
              pos=wx.Point(376, 152), size=wx.Size(88, 23), style=0)
        self.btnDeleteProfile.Bind(wx.EVT_BUTTON, self.OnBtnDeleteProfileButton,
              id=wxID_APPFRAMEBTNDELETEPROFILE)

        self.btnRunProfile = wx.Button(id=wxID_APPFRAMEBTNRUNPROFILE,
              label='Run', name='btnRunProfile', parent=self.mainPanel,
              pos=wx.Point(376, 24), size=wx.Size(88, 23), style=0)
        self.btnRunProfile.Bind(wx.EVT_BUTTON, self.OnBtnRunProfileButton,
              id=wxID_APPFRAMEBTNRUNPROFILE)

        self.btnNewProfile = wx.Button(id=wxID_APPFRAMEBTNNEWPROFILE,
              label='New', name='btnNewProfile', parent=self.mainPanel,
              pos=wx.Point(376, 56), size=wx.Size(88, 23), style=0)
        self.btnNewProfile.Bind(wx.EVT_BUTTON, self.OnNewProfile,
              id=wxID_APPFRAMEBTNNEWPROFILE)

        self.lstProfiles = wx.ListView(winid=wxID_APPFRAMELSTPROFILES,
              name='lstProfiles', parent=self.mainPanel, pos=wx.Point(8, 8),
              size=wx.Size(360, 240), style=wx.LC_SINGLE_SEL | wx.LC_REPORT)
        self._init_coll_lstProfiles_Columns(self.lstProfiles)
        self.lstProfiles.Bind(wx.EVT_LEFT_DCLICK, self.OnLstProfilesLeftDclick)
        self.lstProfiles.Bind(wx.EVT_LIST_ITEM_SELECTED,
              self.OnLstProfilesListItemSelected, id=wxID_APPFRAMELSTPROFILES)

    def initInstanceList(self):
        for i, config in enumerate( self._configs ):
            index = self.lstProfiles.InsertItem(i, config.get_TaskbarName())
            self.lstProfiles.SetItem(index, 1, config.get_EclipseLoc())
            self.lstProfiles.SetItem(index, 2, config.get_VMLoc())
            self.lstProfiles.SetItem(index, 3, config.get_WorkspaceLoc())
        
    def __init__(self, parent):
        self._init_ctrls(parent)
        # read profile
        self._configName = "elauncher.xml"
        doc = minidom.parse(self._configName)
        rootNode = doc.documentElement
        self._rootObj = LaunchConfigs.factory()
        self._rootObj.build(rootNode)
        doc = None
        self._configs = self._rootObj.get_Config()
        self.initInstanceList()

    def save(self):
        
        # save configuration file
        fw = open(self._configName, 'w')
        fw.write('<?xml version="1.0" ?>\n')
        self._rootObj.export(fw, 0, name_="LaunchConfigs", namespacedef_='')
        fw.close()


    def saveProfile(self, profile):
        # update UI
        profileName = profile.get_TaskbarName()
        self.lstProfiles.SetStringItem(self.currentItemIndex, 0, profileName)
        self.lstProfiles.SetStringItem(self.currentItemIndex, 1, profile.get_EclipseLoc())
        self.lstProfiles.SetStringItem(self.currentItemIndex, 2, profile.get_VMLoc())
        self.lstProfiles.SetStringItem(self.currentItemIndex, 3, profile.get_WorkspaceLoc())
        self.save()

    def addProfile(self, profile):
        # update UI
        profileName = profile.get_TaskbarName()
        index = self.lstProfiles.InsertStringItem(sys.maxint, profile.get_TaskbarName())
        self.lstProfiles.SetStringItem(index, 1, profile.get_EclipseLoc())
        self.lstProfiles.SetStringItem(index, 2, profile.get_VMLoc())
        self.lstProfiles.SetStringItem(index, 3, profile.get_WorkspaceLoc())
        
        self._rootObj.add_Config(profile);
        
        # save configuration file
        self.save()

        

    def OnNewProfile(self, event):
        # create profile dialog
        newDiag = ProfileDialog(self)
        # set profile
        newDiag.set_Profile(None)
        newDiag.Centre()
        result = newDiag.ShowModal()
        if result == wx.ID_OK :
            # add the profile to the list
            self.addProfile(newDiag.get_Profile())

    def OnLstProfilesLeftDclick(self, event):
        event.Skip()

    def OnMainPanelSize(self, event):
        # align buttons
        self.btnCopyProfile.Position = (self.Size[0]-self.btnCopyProfile.Size[0]-20,self.btnCopyProfile.Position[1])
        self.btnDeleteProfile.Position = (self.Size[0]-self.btnDeleteProfile.Size[0]-20,self.btnDeleteProfile.Position[1])
        self.btnEditProfile.Position = (self.Size[0]-self.btnEditProfile.Size[0]-20, self.btnEditProfile.Position[1])
        self.btnNewProfile.Position = (self.Size[0]-self.btnNewProfile.Size[0]-20, self.btnNewProfile.Position[1])
        self.btnRunProfile.Position = (self.Size[0]-self.btnRunProfile.Size[0]-20, self.btnRunProfile.Position[1])
        
        # resize list view
        self.lstProfiles.Size = (self.btnCopyProfile.Position[0]-20, self.mainPanel.Size[1]-20)
        
        varWidth = (self.lstProfiles.Size[0]-150)/3
        if varWidth > 85 :
            self.lstProfiles.SetColumnWidth(1, varWidth)
            self.lstProfiles.SetColumnWidth(2, varWidth)
            self.lstProfiles.SetColumnWidth(3, varWidth)
            

    def OnNewEclipseConfiguration(self, event):
        event.Skip()

    def OnBtnRunProfileButton(self, event):
        from subprocess import Popen, PIPE
        # "H:\eclipse\Ganymede_RCP\eclipse\eclipse.exe" 
        # -data "H:\workspace\workspace_python" 
        # -name "GanymedeRCP - Python" 
        # -clean -refresh -nosplash
        # -vm "G:\jdk1515\bin\javaw.exe" -vmargs -Xms256M -Xmx512M
        profile = self._configs[self.currentItemIndex]
        workspace = '-data \"%s\"' % (profile.get_WorkspaceLoc())
        taskname = '-name \"%s\"' % (profile.get_TaskbarName())
        optionClean = profile.get_Clean()
        optionRefresh = profile.get_Refresh()
        optionSplash = profile.get_ShowSplash()
        eargs = '%s %s %s %s' % (profile.get_EclipseArgs() or '', 
                           optionClean and '-clean' or '',
                           optionRefresh and '-refresh' or '',
                           not optionSplash  and '-nosplash' or '')
        jvmargs= '-vmargs -Xms%sM -Xmx%sM %s' %(profile.get_Xms(), profile.get_Xmx(), profile.get_VMArgs() or '')
        jvm = '-vm \"%s\" %s' % (profile.get_VMLoc(), jvmargs)
        cmd = '\"%s\" %s %s %s %s' % (profile.get_EclipseLoc(), workspace, taskname, eargs, jvm)  
        Popen(cmd)

    def OnBtnEditProfileButton(self, event):
        profile = self._configs[self.currentItemIndex]
        profileDialog = ProfileDialog(self)
        profileDialog.set_Profile(profile)
        profileDialog.Centre()
        if profileDialog.ShowModal() == wx.ID_OK :
            self.saveProfile(profile)
            

    def OnLstProfilesListItemSelected(self, event):
        self.currentItemIndex = event.m_itemIndex;

    def OnBtnDeleteProfileButton(self, event):
#        self._configs.remove(self.currentItemIndex)
        self.lstProfiles.DeleteItem(self.currentItemIndex)
        del self._configs[self.currentItemIndex]
        self.save()

    def OnBtnCopyProfileButton(self, event):
        copyProfile = copy.deepcopy(self._configs[self.currentItemIndex])
        name = copyProfile.get_TaskbarName()
        copyProfile.set_TaskbarName("Copy of " + name)
        profileDialog = ProfileDialog(self)
        profileDialog.set_Profile(copyProfile)
        profileDialog.Centre()
        if profileDialog.ShowModal() == wx.ID_OK :
            self.addProfile(copyProfile)
