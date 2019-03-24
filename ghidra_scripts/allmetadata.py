#Set unity meta-data
#@b1ueb1ues 
#@category _NEW_
#@keybinding 
#@menupath 
#@toolbar 


ab = currentProgram.getMinAddress()
def SetMethod(addr, name):
    global ab
    addr = ab.getNewAddress(addr)
    func = getFunctionAt(addr)
    if func:
        func.setName(name,ghidra.program.model.symbol.SourceType.USER_DEFINED)
    else:
        print 'nofunc at ',addr, '(%s)'%name
        createFunction(addr,name)


path = getSourceFile()
name = getScriptName()
path = str(path)[:-len(name)]
for i in open(path+'method.txt'):
    an = i.strip().split(', ')
    addr = int(an[0],16)
    name = an[1].strip()
    SetMethod(addr, name)
