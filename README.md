# vred-python-typings
This is a collection of VRED specific stub files (.pyi) for integration into VRED Python projects.

# Getting started
Just download or clone this repository to your vred python project folder in a folder named "typings".
You can add it also as a submodule with the command:
```
git submodule add -b VREDPro-2024.2 https://github.com/EduardtAlbergII/vred-python-typings.git typings
```
You are invited to commit changes, extensions & corrections. You are also welcome to add a branch with a different version.

# Who needs this?
If you are a developer and are annoyed that neither autocompletion nor linting work with VRED Python projects, then this repository is for you.

![here should be a cool picture](/resources/preview_autocompletion.png)

As you can see, there is still a lot missing, but this is a good start.

# VRED API v2 Services

In VRED, the services from the API v2 are initialised when VRED is started and have the same name as their modules. If you import these with one, the instances are overwritten by the import and your script no longer works. That's why I built this little "diversions":

```python
########### just doing this to get linting and autocompletion in vscode
if not "vrNodeService" in globals(): # this is always False
    from vrKernelServices import (   # we just want to trick the vscode linter
        vrMaterialService as vrMaterialServiceClass,
        vrGeometryService as vrGeometryServiceClass,
        vrCameraService as vrCameraServiceClass,
        vrScenegraphService as vrScenegraphServiceClass,
        vrNodeService as vrNodeServiceClass,
    )

vrGeometryService: vrGeometryServiceClass
vrScenegraphService: vrScenegraphServiceClass
vrMaterialService: vrMaterialServiceClass
vrCameraService: vrCameraServiceClass
vrNodeService: vrNodeServiceClass
##########################################################################
```