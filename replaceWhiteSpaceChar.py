import os, sys

tmpPath = sys.argv[1]
print ("The parent path for replace all whitespace characters is: %s" % (tmpPath))

def replace(parent):
    for path, folders, files in os.walk(parent):
        for f in files:
            os.rename(os.path.join(path, f), os.path.join(path, f.replace(' ', '_')))
        for i in range(len(folders)):
            new_name = folders[i].replace(' ', '_')
            os.rename(os.path.join(path, folders[i]), os.path.join(path, new_name))
            folders[i] = new_name
            print("Folder:",new_name)
            print("File:",f)
replace(tmpPath)