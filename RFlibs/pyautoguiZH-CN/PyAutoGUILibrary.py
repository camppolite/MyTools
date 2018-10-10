# -*- coding: utf-8 -*-

__author__ = 'Wu Dirui, camp'
__version__ = "0.1"

try:
    import pyautogui
except ImportError as err:
    print(err + "导入pyautogui失败，请先安装该模块：pip install pyautogui")


class PyAutoGUILibrary:
    """
    本模块只是引用PyAutoGUI模块，将它封装成中文版的接口（目前英文），方便不熟悉英文的用户使用。

    PyAutoGUI是一个面向人类的跨平台GUI自动化Python模块。用于以编程方式控制鼠标和键盘。

    PyAutoGUI官网地址：https://pyautogui.readthedocs.io/en/latest/

    PyAutoGUI源码地址：https://github.com/asweigart/pyautogui

    安装本模块的顺序是：

    1.安装PyAutoIt:

    pip install pyautogui

    2.PyAutoGUILibrary(PyAutoGUILibrary.py文件拷贝到Python\Lib\site-packages目录里，或者拷贝到其他任意PYTHONPATH)。
    """
    ROBOT_LIBRARY_SCOPE = "GLOBAL"

    def __init__(self):
        pass

    # General Functions
    def position(self, x=None, y=None):
        """Returns the current xy coordinates of the mouse cursor as a two-integer
        tuple.

        Args:
          x (int, None, optional) - If not None, this argument overrides the x in
            the return value.
          y (int, None, optional) - If not None, this argument overrides the y in
            the return value.

        Returns:
          (x, y) tuple of the current xy coordinates of the mouse cursor.
        """
        return pyautogui.position(x, y)

    def size(self):
        """Returns the width and height of the screen as a two-integer tuple.

        Returns:
          (width, height) tuple of the screen size, in pixels.
        """
        return pyautogui.size()

    # Mouse Control Functions
    # The Screen and Mouse Position
    def onScreen(self, x, y=None):
        """Returns whether the given xy coordinates are on the screen or not.

        Args:
          Either the arguments are two separate values, first arg for x and second
            for y, or there is a single argument of a sequence with two values, the
            first x and the second y.
            Example: onScreen(x, y) or onScreen([x, y])

        Returns:
          bool: True if the xy coordinates are on the screen at its current
            resolution, otherwise False.
        """
        return pyautogui.onScreen(x, y)

    # Mouse Movement
    def moveTo(self, x=None, y=None, duration=0.0, tween=pyautogui.linear, pause=None, _pause=True):
        """Moves the mouse cursor to a point on the screen.

        The x and y parameters detail where the mouse event happens. If None, the
        current mouse position is used. If a float value, it is rounded down. If
        outside the boundaries of the screen, the event happens at edge of the
        screen.

        Args:
          x (int, float, None, tuple, optional): The x position on the screen where the
            click happens. None by default. If tuple, this is used for x and y.
          y (int, float, None, optional): The y position on the screen where the
            click happens. None by default.
          duration (float, optional): The amount of time it takes to move the mouse
            cursor to the xy coordinates. If 0, then the mouse cursor is moved
            instantaneously. 0.0 by default.
          tween (func, optional): The tweening function used if the duration is not
            0. A linear tween is used by default. See the tweens.py file for
            details.

        Returns:
          None
        """
        return pyautogui.moveTo(x, y, duration, tween, pause, _pause)

    def moveRel(self, xOffset=None, yOffset=None, duration=0.0, tween=pyautogui.linear, pause=None, _pause=True):
        """Moves the mouse cursor to a point on the screen, relative to its current
            position.

            The x and y parameters detail where the mouse event happens. If None, the
            current mouse position is used. If a float value, it is rounded down. If
            outside the boundaries of the screen, the event happens at edge of the
            screen.

            Args:
              x (int, float, None, tuple, optional): How far left (for negative values) or
                right (for positive values) to move the cursor. 0 by default. If tuple, this is used for x and y.
              y (int, float, None, optional): How far up (for negative values) or
                down (for positive values) to move the cursor. 0 by default.
              duration (float, optional): The amount of time it takes to move the mouse
                cursor to the new xy coordinates. If 0, then the mouse cursor is moved
                instantaneously. 0.0 by default.
              tween (func, optional): The tweening function used if the duration is not
                0. A linear tween is used by default. See the tweens.py file for
                details.

            Returns:
              None
            """
        return pyautogui.moveRel(xOffset, yOffset, duration, tween, pause, _pause)

    # Mouse Drags
    def dragTo(self, x=None, y=None, duration=0.0, tween=pyautogui.linear, button='left', pause=None, _pause=True,
               mouseDownUp=True):
        """Performs a mouse drag (mouse movement while a button is held down) to a
            point on the screen.

            The x and y parameters detail where the mouse event happens. If None, the
            current mouse position is used. If a float value, it is rounded down. If
            outside the boundaries of the screen, the event happens at edge of the
            screen.

            Args:
              x (int, float, None, tuple, optional): How far left (for negative values) or
                right (for positive values) to move the cursor. 0 by default. If tuple, this is used for x and y.
              y (int, float, None, optional): How far up (for negative values) or
                down (for positive values) to move the cursor. 0 by default.
              duration (float, optional): The amount of time it takes to move the mouse
                cursor to the new xy coordinates. If 0, then the mouse cursor is moved
                instantaneously. 0.0 by default.
              tween (func, optional): The tweening function used if the duration is not
                0. A linear tween is used by default. See the tweens.py file for
                details.
              button (str, int, optional): The mouse button clicked. Must be one of
                'left', 'middle', 'right' (or 1, 2, or 3) respectively. 'left' by
                default.
              mouseDownUp (True, False): When true, the mouseUp/Down actions are not perfomed.
                Which allows dragging over multiple (small) actions. 'True' by default.

            Returns:
              None
            """
        return pyautogui.dragTo(x, y, duration, tween, button, pause, _pause, mouseDownUp)

    def dragRel(self, xOffset=0, yOffset=0, duration=0.0, tween=pyautogui.linear, button='left', pause=None,
                _pause=True, mouseDownUp=True):
        """Performs a mouse drag (mouse movement while a button is held down) to a
            point on the screen, relative to its current position.

            The x and y parameters detail where the mouse event happens. If None, the
            current mouse position is used. If a float value, it is rounded down. If
            outside the boundaries of the screen, the event happens at edge of the
            screen.

            Args:
              x (int, float, None, tuple, optional): How far left (for negative values) or
                right (for positive values) to move the cursor. 0 by default. If tuple, this is used for xOffset and yOffset.
              y (int, float, None, optional): How far up (for negative values) or
                down (for positive values) to move the cursor. 0 by default.
              duration (float, optional): The amount of time it takes to move the mouse
                cursor to the new xy coordinates. If 0, then the mouse cursor is moved
                instantaneously. 0.0 by default.
              tween (func, optional): The tweening function used if the duration is not
                0. A linear tween is used by default. See the tweens.py file for
                details.
              button (str, int, optional): The mouse button clicked. Must be one of
                'left', 'middle', 'right' (or 1, 2, or 3) respectively. 'left' by
                default.
              mouseDownUp (True, False): When true, the mouseUp/Down actions are not perfomed.
                Which allows dragging over multiple (small) actions. 'True' by default.

            Returns:
              None
            """
        return pyautogui.dragRel(xOffset, yOffset, duration, tween, button, pause, _pause, mouseDownUp)

    # Mouse Clicks
    def click(self, x=None, y=None, clicks=1, interval=0.0, button='left', duration=0.0, tween=pyautogui.linear,
              pause=None, _pause=True):
        """Performs pressing a mouse button down and then immediately releasing it.

            The x and y parameters detail where the mouse event happens. If None, the
            current mouse position is used. If a float value, it is rounded down. If
            outside the boundaries of the screen, the event happens at edge of the
            screen.

            Args:
              x (int, float, None, tuple, optional): The x position on the screen where
                the click happens. None by default. If tuple, this is used for x and y.
              y (int, float, None, optional): The y position on the screen where the
                click happens. None by default.
              clicks (int, optional): The number of clicks to perform. 1 by default.
                For example, passing 2 would do a doubleclick.
              interval (float, optional): The number of seconds in between each click,
                if the number of clicks is greater than 1. 0.0 by default, for no
                pause in between clicks.
              button (str, int, optional): The mouse button clicked. Must be one of
                'left', 'middle', 'right' (or 1, 2, or 3) respectively. 'left' by
                default.

            Returns:
              None

            Raises:
              ValueError: If button is not one of 'left', 'middle', 'right', 1, 2, 3
            """
        return pyautogui.click(x, y, clicks, interval, button, duration, tween, pause, _pause)

    def doubleClick(self, x=None, y=None, interval=0.0, button='left', duration=0.0, tween=pyautogui.linear,
                    pause=None, _pause=True):
        """Performs a double click.

            This is a wrapper function for click('left', x, y, 2, interval).

            The x and y parameters detail where the mouse event happens. If None, the
            current mouse position is used. If a float value, it is rounded down. If
            outside the boundaries of the screen, the event happens at edge of the
            screen.

            Args:
              x (int, float, None, tuple, optional): The x position on the screen where the
                click happens. None by default. If tuple, this is used for x and y.
              y (int, float, None, optional): The y position on the screen where the
                click happens. None by default.
              interval (float, optional): The number of seconds in between each click,
                if the number of clicks is greater than 1. 0.0 by default, for no
                pause in between clicks.
              button (str, int, optional): The mouse button clicked. Must be one of
                'left', 'middle', 'right' (or 1, 2, or 3) respectively. 'left' by
                default.

            Returns:
              None

            Raises:
              ValueError: If button is not one of 'left', 'middle', 'right', 1, 2, 3, 4,
                5, 6, or 7
            """
        return pyautogui.doubleClick(x, y, interval, button, duration, tween, pause, _pause)

    # The mouseDown() and mouseUp() Functions
    def mouseDown(self, x=None, y=None, button='left', duration=0.0, tween=pyautogui.linear, pause=None, _pause=True):
        """Performs pressing a mouse button down (but not up).

            The x and y parameters detail where the mouse event happens. If None, the
            current mouse position is used. If a float value, it is rounded down. If
            outside the boundaries of the screen, the event happens at edge of the
            screen.

            Args:
              x (int, float, None, tuple, optional): The x position on the screen where the
                mouse down happens. None by default. If tuple, this is used for x and y.
              y (int, float, None, optional): The y position on the screen where the
                mouse down happens. None by default.
              button (str, int, optional): The mouse button pressed down. Must be one of
                'left', 'middle', 'right' (or 1, 2, or 3) respectively. 'left' by
                default.

            Returns:
              None

            Raises:
              ValueError: If button is not one of 'left', 'middle', 'right', 1, 2, or 3
            """
        return pyautogui.mouseDown(x, y, button, duration, tween, pause, _pause)

    def mouseUp(self, x=None, y=None, button='left', duration=0.0, tween=pyautogui.linear, pause=None, _pause=True):
        """Performs releasing a mouse button up (but not down beforehand).

        The x and y parameters detail where the mouse event happens. If None, the
        current mouse position is used. If a float value, it is rounded down. If
        outside the boundaries of the screen, the event happens at edge of the
        screen.

        Args:
          x (int, float, None, tuple, optional): The x position on the screen where the
            mouse up happens. None by default. If tuple, this is used for x and y.
          y (int, float, None, optional): The y position on the screen where the
            mouse up happens. None by default.
          button (str, int, optional): The mouse button released. Must be one of
            'left', 'middle', 'right' (or 1, 2, or 3) respectively. 'left' by
            default.

        Returns:
          None

        Raises:
          ValueError: If button is not one of 'left', 'middle', 'right', 1, 2, or 3
        """
        return pyautogui.mouseUp(x, y, button, duration, tween, pause, _pause)

    # Mouse Scrolling
    def scroll(self, clicks, x=None, y=None, pause=None, _pause=True):
        """Performs a scroll of the mouse scroll wheel.

            Whether this is a vertical or horizontal scroll depends on the underlying
            operating system.

            The x and y parameters detail where the mouse event happens. If None, the
            current mouse position is used. If a float value, it is rounded down. If
            outside the boundaries of the screen, the event happens at edge of the
            screen.

            Args:
              clicks (int, float): The amount of scrolling to perform.
              x (int, float, None, tuple, optional): The x position on the screen where the
                click happens. None by default. If tuple, this is used for x and y.
              y (int, float, None, optional): The y position on the screen where the
                click happens. None by default.

            Returns:
              None
            """
        return  pyautogui.scroll(clicks, x, y, pause, _pause)

    def hscroll(self, clicks, x=None, y=None, pause=None, _pause=True):
        """Performs an explicitly horizontal scroll of the mouse scroll wheel,
            if this is supported by the operating system. (Currently just Linux.)

            The x and y parameters detail where the mouse event happens. If None, the
            current mouse position is used. If a float value, it is rounded down. If
            outside the boundaries of the screen, the event happens at edge of the
            screen.

            Args:
              clicks (int, float): The amount of scrolling to perform.
              x (int, float, None, tuple, optional): The x position on the screen where the
                click happens. None by default. If tuple, this is used for x and y.
              y (int, float, None, optional): The y position on the screen where the
                click happens. None by default.

            Returns:
              None
            """
        return pyautogui.hscroll(clicks, x, y, pause, _pause)

    # Keyboard Control Functions
    # The typewrite() Function
    def typewrite(self, message, interval=0.0, pause=None, _pause=True):
        """Performs a keyboard key press down, followed by a release, for each of
            the characters in message.

            The message argument can also be list of strings, in which case any valid
            keyboard name can be used.

            Since this performs a sequence of keyboard presses and does not hold down
            keys, it cannot be used to perform keyboard shortcuts. Use the hotkey()
            function for that.

            Args:
              message (str, list): If a string, then the characters to be pressed. If a
                list, then the key names of the keys to press in order. The valid names
                are listed in KEYBOARD_KEYS.
              interval (float, optional): The number of seconds in between each press.
                0.0 by default, for no pause in between presses.

            Returns:
              None
            """
        return pyautogui.typewrite(message, interval, pause, _pause)

    # The press(), keyDown(), and keyUp() Functions
    def press(self, keys, presses=1, interval=0.0, pause=None, _pause=True):
        """Performs a keyboard key press down, followed by a release.

            Args:
              key (str, list): The key to be pressed. The valid names are listed in
              KEYBOARD_KEYS. Can also be a list of such strings.
              presses (integer, optiional): the number of press repetition
              1 by default, for just one press
              interval (float, optional): How many seconds between each press.
              0.0 by default, for no pause between presses.
              pause (float, optional): How many seconds in the end of function process.
              None by default, for no pause in the end of function process.
            Returns:
              None



            KEYBOARD_KEYS:

            ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
            ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
            '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
            'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
            'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
            'browserback', 'browserfavorites', 'browserforward', 'browserhome',
            'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
            'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
            'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
            'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
            'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
            'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
            'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
            'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
            'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
            'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
            'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
            'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
            'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
            'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
            'command', 'option', 'optionleft', 'optionright']
            """
        return pyautogui.press(keys, presses, interval, pause, _pause)

    def keyDown(self, key, pause=None, _pause=True):
        """Performs a keyboard key press without the release. This will put that
            key in a held down state.

            NOTE: For some reason, this does not seem to cause key repeats like would
            happen if a keyboard key was held down on a text field.

            Args:
              key (str): The key to be pressed down. The valid names are listed in
              KEYBOARD_KEYS.

            Returns:
              None
            """
        return pyautogui.keyDown(key, pause, _pause)

    def keyUp(self, key, pause=None, _pause=True):
        """Performs a keyboard key release (without the press down beforehand).

            Args:
              key (str): The key to be released up. The valid names are listed in
              KEYBOARD_KEYS.

            Returns:
              None
            """
        return pyautogui.keyUp(key, pause, _pause)

    # The hotkey() Function
    def hotkey(self, *args, **kwargs):
        """Performs key down presses on the arguments passed in order, then performs
            key releases in reverse order.

            The effect is that calling hotkey('ctrl', 'shift', 'c') would perform a
            "Ctrl-Shift-C" hotkey/keyboard shortcut press.

            Args:
              key(s) (str): The series of keys to press, in order. This can also be a
                list of key strings to press.
              interval (float, optional): The number of seconds in between each press.
                0.0 by default, for no pause in between presses.

            Returns:
              None
            """
        _interval = float(kwargs.get('interval', 0.0))
        pause, _pause = kwargs.get('pause', None), kwargs.get('_pause', True)

        return pyautogui.hotkey(_interval, pause, _pause)


    # Message Box Functions
    # The alert() Function
    from pyautogui import pymsgbox

    def alert(self, text='', title='', button=pymsgbox.OK_TEXT, root=None, timeout=None):
        """Displays a simple message box with text and a single OK button. Returns the text of the button clicked on."""
        return pyautogui.alert(text, title, button, root, timeout)

    def confirm(self, text='', title='', buttons=[pymsgbox.OK_TEXT, pymsgbox.CANCEL_TEXT], root=None, timeout=None):
        """Displays a message box with OK and Cancel buttons. Number and text of buttons can be customized.
         Returns the text of the button clicked on."""
        return pyautogui.confirm(text, title, buttons, root, timeout)

    def prompt(self, text='', title='' , default='', root=None, timeout=None):
        """Displays a message box with text input, and OK & Cancel buttons. Returns the text entered,
         or None if Cancel was clicked."""
        return pyautogui.prompt(text, title, default, root, timeout)

    def password(self, text='', title='', default='', mask='*', root=None, timeout=None):
        """Displays a message box with text input, and OK & Cancel buttons. Typed characters appear as *.
         Returns the text entered, or None if Cancel was clicked."""
        return pyautogui.password(text, title, default, mask, root, timeout)

    # Screenshot Functions
    def screenshot(self, *args):
        """
        Calling screenshot() will return an Image object (see the Pillow or PIL module documentation for details). Passing a string of a filename will save the screenshot to a file as well as return it as an Image object.

        >>> import pyautogui
        >>> im1 = pyautogui.screenshot()
        >>> im2 = pyautogui.screenshot('my_screenshot.png')
        On a 1920 x 1080 screen, the screenshot() function takes roughly 100 milliseconds - it’s not fast but it’s not slow.

        There is also an optional region keyword argument, if you do not want a screenshot of the entire screen. You can pass a four-integer tuple of the left, top, width, and height of the region to capture:

        >>> import pyautogui
        >>> im = pyautogui.screenshot(region=(0,0, 300, 400))
        """
        sshot = pyautogui.screenshot(args)

        def getpixel(xy):
            """
            Returns the pixel value at a given position.

            :param xy: The coordinate, given as (x, y). See
               :ref:`coordinate-system`.
            :returns: The pixel value.  If the image is a multi-layer image,
               this method returns a tuple.
            """
            return sshot.getpixel(xy)

        return sshot

    def locateOnScreen(self, image, minSearchTime=0, **kwargs):
        """minSearchTime - amount of time in seconds to repeat taking
            screenshots and trying to locate a match.  The default of 0 performs
            a single search.
        """
        return pyautogui.locateOnScreen(image, minSearchTime, **kwargs)

    def center(self, coords):
        """
        . . . you can call the locateOnScreen('calc7key.png') function to get the screen coordinates. The return value is a 4-integer tuple: (left, top, width, height). This tuple can be passed to center() to get the X and Y coordinates at the center of this region. If the image can’t be found on the screen, locateOnScreen() returns None.

        >>> import pyautogui
        >>> button7location = pyautogui.locateOnScreen('calc7key.png')
        >>> button7location
        (1416, 562, 50, 41)
        >>> button7x, button7y = pyautogui.center(button7location)
        >>> button7x, button7y
        (1441, 582)
        >>> pyautogui.click(button7x, button7y)  # clicks the center of where the 7 button was found
        """
        return pyautogui.center(coords)

    def locateCenterOnScreen(self, image, **kwargs):
        """
        Returns (x, y) coordinates of the center of the first found instance of the image on the screen.
         Returns None if not found on the screen.
        """
        return pyautogui.locateCenterOnScreen(image, **kwargs)

    def locateAllOnScreen(self, image, **kwargs):
        """
        Returns a generator that yields (left, top, width, height) tuples for where the image is found on the screen.
        """
        return pyautogui.locateAllOnScreen(image, **kwargs)

    def locate(self, needleImage, haystackImage, **kwargs):
        """
        Returns (left, top, width, height) coordinate of first found instance of needleImage in haystackImage.
         Returns None if not found on the screen.
        """
        return pyautogui.locate(needleImage, haystackImage, **kwargs)

    def locateAll(self, *args):
        """
        Returns a generator that yields (left, top, width, height) tuples for where needleImage is found in haystackImage.
        """
        return pyautogui.locateAll(*args)

    def pixel(self, x, y):
        """
        Or as a single function, call the pixel() PyAutoGUI function, which is a wrapper for the previous calls
        """
        return pyautogui.pixel(x, y)

    def pixelMatchesColor(self, x, y, expectedRGBColor, tolerance=0):
        """
        If you just need to verify that a single pixel matches a given pixel, call the pixelMatchesColor() function,
        passing it the X coordinate, Y coordinate, and RGB tuple of the color it represents
        """
        return pyautogui.pixelMatchesColor(x, y, expectedRGBColor, tolerance)

    def getWindows(self):
        """
        returns a dict of window titles mapped to window IDs
        """
        return pyautogui.getWindows()

    def getWindow(self, str_title_or_int_id, exact=False):
        """
        returns a “Win” object

        win.move(x, y)
        win.resize(width, height)
        win.maximize()
        win.minimize()
        win.restore()
        win.close()
        win.position() # returns (x, y) of top-left corner
        win.moveRel(x=0, y=0) # moves relative to the x, y of top-left corner of the window
        win.clickRel(x=0, y=0, clicks=1, interval=0.0, button=’left’) # click relative to the x, y of top-left corner of the window
        Additions to screenshot functionality so that it can capture specific windows instead of full screen.
        """
        # Flags for ShowWindow:
        SW_MAXIMIZE = 3
        SW_MINIMIZE = 6
        SW_RESTORE = 9
        win = pyautogui.getWindow(str_title_or_int_id, exact)
        def move(x, y):
            """Move window top-left corner to position"""
            return win.move(x, y)

        def resize(width, height):
            """Change window size"""
            return win.resize(width, height)

        def maximize():
            return win.maximize(win._hwnd, SW_MAXIMIZE)

        def minimize():
            return win.minimize(win._hwnd, SW_MINIMIZE)

        def restore():
            return win.restore(win._hwnd, SW_RESTORE)

        def close():
            return win.close(win._hwnd)

        def get_position():
            """Returns tuple of 4 numbers: (x, y)s of top-left and bottom-right corners"""
            return win.get_position()

        def set_position(x, y, width, height):
            """Set window top-left corner position and size"""
            return win.set_position(x, y, width, height)

        def set_foreground():
            return win.set_foreground(win._hwnd)

        return win
