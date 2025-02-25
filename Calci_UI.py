import wx
import wx.xrc
import math

class CalculatorFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title="Calculator", size=(400, 500))
        
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        self.display = wx.TextCtrl(panel, style=wx.TE_RIGHT | wx.TE_READONLY)
        vbox.Add(self.display, 0, wx.EXPAND | wx.ALL, 10)
        
        grid = wx.GridSizer(5, 4, 5, 5)
        
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C', '√', '^', '%'
        ]
        
        self.btn_map = {}
        
        for label in buttons:
            btn = wx.Button(panel, label=label)
            self.btn_map[label] = btn
            grid.Add(btn, 1, wx.EXPAND)
            btn.Bind(wx.EVT_BUTTON, self.OnButtonClicked)
        
        vbox.Add(grid, 1, wx.EXPAND | wx.ALL, 10)
        panel.SetSizer(vbox)
        
    def OnButtonClicked(self, event):
        label = event.GetEventObject().GetLabel()
        current_text = self.display.GetValue()
        
        if label == "C":
            self.display.SetValue("")
        elif label == "=":
            try:
                result = eval(current_text)
                self.display.SetValue(str(result))
            except:
                self.display.SetValue("Error")
        elif label == "√":
            try:
                result = math.sqrt(float(current_text))
                self.display.SetValue(str(result))
            except:
                self.display.SetValue("Error")
        elif label == "^":
            self.display.SetValue(current_text + "**")
        elif label == "%":
            try:
                result = float(current_text) / 100
                self.display.SetValue(str(result))
            except:
                self.display.SetValue("Error")
        else:
            self.display.SetValue(current_text + label)

if __name__ == "__main__":
    app = wx.App(False)
    frame = CalculatorFrame(None)
    frame.Show()
    app.MainLoop()
