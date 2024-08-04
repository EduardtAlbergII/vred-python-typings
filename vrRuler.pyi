from builtins import NoneType
from vrOSGTypes import Pnt3f, Vec3f

__name__: str
__doc__: NoneType
__package__: str
__spec__: ModuleSpec

def __loader__(self) -> None: ...
def getRulerEnabled(self) -> bool: ...
def getRulerFixAxes(self) -> bool: ...
def getRulerGridEnabled(self) -> bool: ...
def getRulerManipulatorEnabled(self) -> bool: ...
def getRulerPosition(self) -> Pnt3f: ...
def getRulerRotation(self) -> Vec3f: ...
def resetRuler(self) -> None: ...
def setRulerFixAxes(self, state: bool) -> None: ...
def setRulerPosition(self, x: float, y: float, z: float) -> None: ...
def setRulerRotation(self, rotationX: float, rotationY: float, rotationZ: float) -> None: ...
def showRuler(self, state: bool) -> None: ...
def showRulerGrid(self, state: bool) -> None: ...
def showRulerManipulator(self, state: bool) -> None: ...
