from diffenator.screenshot import ScreenShotter
import os

s = ScreenShotter()
s.take("https://www.google.com", "out")

fp = os.path.abspath("test.html")
fp = "file:///" + fp
s.take(fp, "out")