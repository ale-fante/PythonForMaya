from maya import cmds

selection = cmds.ls(selection=True)
print(selection)

if len(selection) == 0:
    selection = cmds.ls(dag=True, long=True)
    
    
selection.sort(key=len, reverse=True)
print(selection)


for obj in selection:
    shortName = obj.split("|")[-1]
    print shortName
