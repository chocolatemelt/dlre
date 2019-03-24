worrysweat
=====

steps
1) install and run ghidra
2) new project > ghidra_dlre folder (ignored in .gitignore)
3) open the codebrowser (dragon icon)
4) drag in / open libil2cpp.so
5) hit ok etc. then hit analyze and wait 5-8 hours
6) window > memory map > base address (home icon second to last) > change it to 00000000
7) window > script manager > new script (5th from the right) > python
8) create the script or w.e, then copy paste allmetadata.py and method.txt from /ghidra_scripts into the default script directory
9) run the script
10) ???
