import wx


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fileItem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit Application')
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.OnQuit, fileItem)

        self.SetSize((1000, 800))
        self.SetTitle('Simple menu')

        self.Center()

    def OnQuit(self, e):
        self.Close()


def main():
    app = wx.App()

    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
