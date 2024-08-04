from builtins import NoneType
from typing import Any
from vrNodePtr import NodePtr

__name__: str
__doc__: NoneType
__package__: str
__spec__: ModuleSpec

def __loader__(self) -> None: ...
def activateRenderLayer(self, name: str) -> None: ...
def activateRenderLayerState(self, name: str) -> None: ...
def addNodesToRenderLayer(self, nodes: Any, layerName: str) -> None: ...
def createRenderLayer(self, name: str) -> None: ...
def resetNodeVisibilityFlags(self, node: NodePtr) -> None: ...
def resetRenderLayers(self) -> None: ...
def setNodeVisibilityFlags(
    self,
    node: NodePtr,
    visible: bool,
    visibleInAlpha: bool,
    primaryVisibility: bool,
    visibleInReflections: bool,
    visibleInRefractions: bool,
    castShadows: bool,
    receiveShadows: bool,
    doubleSided: bool,
    visibleForPhotons: bool,
    castShadowOnShadowMaterial: bool,
    useOverrideMaterial: bool,
    overrideMaterial: str,
) -> None: ...
