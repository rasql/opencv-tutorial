from cvlib import *

a = App()
w = Window()

def test_app():
    assert isinstance(a, App)
    assert isinstance(w, Window)