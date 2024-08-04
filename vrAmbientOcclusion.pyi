from builtins import NoneType

__name__: str
__doc__: NoneType
__package__: str
__spec__: ModuleSpec
VR_AO_MODE_CLASSIC: int
VR_AO_MODE_SHADOWS: int
VR_AO_MODE_LIGHT_AND_SHADOWS: int
VR_AO_WEIGHTING_COSINE: int
VR_AO_WEIGHTING_UNIFORM: int

def __loader__(self) -> None: ...
def computeAmbientOcclusion(
    self,
    quality: int,
    minDistance: float,
    maxDistance: float,
    indirectIllumination: bool,
    colorBleeding: bool,
    gatherQuality: int,
    numIndirections: int,
    subdivide: bool,
    minEdgeLength: float,
    overrideMaterialColor: bool,
    materialColorR: float,
    materialColorG: float,
    materialColorB: float,
    subdivisionQuality: int,
    intensityThreshold: float,
    weighting: int,
) -> None: ...
def computeMissingAmbientOcclusion(
    self,
    quality: int,
    minDistance: float,
    maxDistance: float,
    indirectIllumination: bool,
    colorBleeding: bool,
    gatherQuality: int,
    numIndirections: int,
    subdivide: bool,
    minEdgeLength: float,
    intensityThreshold: float,
    overrideMaterialColor: bool,
    materialColorR: float,
    materialColorG: float,
    materialColorB: float,
    subdivisionQuality: int,
    weighting: int,
) -> None: ...
def getAmbientOcclusionMode(self) -> int: ...
def setAmbientOcclusionMode(self, mode: int) -> None: ...
