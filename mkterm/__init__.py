from .app import main as app_main

__version_info__ = ("1","0","0")
__version__ = ".".join(__version_info__)

def main():
    app_main()
    return True

