import wx

APP_EXIT = 1

class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):

        self.count = 5

        self.toolbar = self.CreateToolBar()
        t_undo = self.toolbar.AddTool(wx.ID_UNDO, '', wx.Bitmap('icons/tundo.png'))
        t_redo = self.toolbar.AddTool(wx.ID_REDO, '', wx.Bitmap('icons/tredo.png'))
        self.toolbar.EnableTool(wx.ID_REDO, False)
        self.toolbar.AddSeparator()
        t_exit = self.toolbar.AddTool(wx.ID_EXIT, '', wx.Bitmap('icons/texit.png'))
        self.toolbar.Realize()

        self.Bind(wx.EVT_TOOL, self.OnQuit, t_exit)
        self.Bind(wx.EVT_TOOL, self.OnUndo, t_undo)
        self.Bind(wx.EVT_TOOL, self.OnRedo, t_redo)

        self.SetSize((1000, 800))
        self.SetTitle('Undo Redo')
        self.Center()

    def OnUndo(self, e):
        if 1 < self.count <= 5:
            self.count -= 1

        if self.count == 1:
            self.toolbar.EnableTool(wx.ID_UNDO, False)

        if self.count == 4:
            self.toolbar.EnableTool(wx.ID_REDO, True)

    def OnRedo(self, e):
        if 1 <= self.count < 5:
            self.count += 1

        if self.count == 5:
            self.toolbar.EnableTool(wx.ID_REDO, False)

        if self.count == 2:
            self.toolbar.EnableTool(wx.ID_UNDO, True)

    def OnQuit(self, e):
        self.Close()


def main():
    app = wx.App()

    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
