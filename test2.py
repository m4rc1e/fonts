from diffenator.screenshot import ScreenShotter
import os

s = ScreenShotter()
s.take("https://www.google.com", "out")

s.take("test.html")