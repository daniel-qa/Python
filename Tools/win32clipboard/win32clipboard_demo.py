# 需要導入模塊: import win32clipboard [as 別名]
# 或者: from win32clipboard import GetClipboardData [as 別名]
def get_paste_buffer():
            win32clipboard.OpenClipboard(0)
            try:
                result = win32clipboard.GetClipboardData()
            except TypeError:
                result = ''  #non-text
            win32clipboard.CloseClipboard()
