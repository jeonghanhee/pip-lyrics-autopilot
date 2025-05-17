import win32gui

def get_pip_window():
    def callback(hwnd, pip_window_info):
        if win32gui.IsWindowVisible(hwnd):
            window_title = win32gui.GetWindowText(hwnd)
            if window_title == "PIP 모드":
                rect = win32gui.GetWindowRect(hwnd)
                pip_window_info.extend([rect[0], rect[1], rect[2], rect[3]])

    pip_window_info = []
    win32gui.EnumWindows(callback, pip_window_info)
    
    return pip_window_info