#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
test_emulators.py
Test what emulators exist on the system
(run with nosetests)
"""

from os.path import join, isfile

# TODO: collect more paths (I can't think of any more than these)
paths = [("/", "usr", "bin"),
         ("/", "usr", "sbin"),
         ("/", "usr", "local", "bin"),
         ("/", "bin"),
         ]

# TODO: Collect more terminals
emulators = ["xterm", "eterm", "terminator", "xfce4-terminal",
             "rxvt", "urxvt", "uterm"]

def test_all_emulators():
    """
    Test all emulators
    See which ones are available to use
    """
    print("Beginning test")
    available = [join(spath, prog)
            for prog in emulators for spath in (join(*sp) for sp in paths)
            if isfile(join(spath, prog))]
    list(map(lambda x: print("'{0}' is available".format(x)), available))
    return True
