from builtins import NoneType
from vrNodePtr import vrNodePtr
from vrOSGTypes import Pnt3f
from typing import Any

__name__: str
__doc__: NoneType
__package__: str
__spec__: ModuleSpec

def __loader__(self) -> None: ...
def createCircleMeasurement(
    self, node1: vrNodePtr, hitPoint1: Pnt3f, node2: vrNodePtr, hitPoint2: Pnt3f, node3: vrNodePtr, hitPoint3: Pnt3f
) -> None: ...
def createGapMeasurement(self, node1: vrNodePtr, hitPoint1: Pnt3f, node2: vrNodePtr, hitPoint2: Pnt3f) -> None: ...
def createLineObjectMeasurement(self, lineNode: Any, linehitPoint: Any, node2: vrNodePtr) -> None: ...
def createObjectObjectMeasurement(self, node1: vrNodePtr, node2: vrNodePtr) -> None: ...
def createPointObjectMeasurement(self, node1: vrNodePtr, hitPoint1: Pnt3f, node2: vrNodePtr) -> None: ...
def createPointPointMeasurement(self, node1: vrNodePtr, hitPoint1: Pnt3f, node2: vrNodePtr, hitPoint2: Pnt3f) -> None: ...
def removeAllMeasurements(self) -> None: ...
def removeSelectedMeasurement(self) -> None: ...
def updateAllMeasurements(self) -> None: ...
def updateMeasurement(self) -> None: ...
def zoomOnMeasurement(self) -> None: ...
