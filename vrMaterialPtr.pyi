from builtins import NoneType
from vrOSGTypes import Pnt3f, Vec3f
from vrChunkPtr import vrChunkPtr
from vrSHLChunkPtr import vrSHLChunkPtr
from vrFieldAccess import vrFieldAccess

__name__: str
__doc__: str
__package__: str
__spec__: ModuleSpec

def __loader__(self) -> None: ...
def addMaterialTag(self) -> None: ...
def addMaterialTags(self) -> None: ...
def createMaterial(self, type: str) -> vrMaterialPtr: ...
def findMaterial(self, name: str) -> vrMaterialPtr: ...
def findMaterials(self, name: str, regexp: bool) -> list: ...
def getAllMaterials(self) -> list: ...
def getMaterialTags(self, material: MaterialPtr) -> None: ...
def getMaterialsWithTag(self, tag: str) -> list: ...
def getMaterialsWithTags(self, tags: str) -> list: ...
def hasMaterialTag(self, material: MaterialPtr, tag: str) -> None: ...
def hasMaterialTags(self, material: MaterialPtr, tag: str) -> None: ...
def removeMaterialTag(self) -> None: ...
def removeMaterialTags(self) -> None: ...
def replaceMaterialTag(self) -> None: ...
def setEnvironmentImage(self, mat: MaterialPtr, image_path: str) -> None: ...
def setMaterialImage(self, mat: MaterialPtr, field_name: str, image_path: str) -> None: ...
def setSwitchMaterialChoice(self, name: str, choice: int) -> None: ...
def setTextureTransform(self, mat: MaterialPtr, translate: Pnt3f, rotate: Vec3f, scale: Vec3f) -> None: ...
def toMaterial(self, id: int) -> vrMaterialPtr: ...

class MaterialPtr:
    __module__: str
    __doc__: NoneType
    __instance_size__: int
    def __class__(self) -> None: ...
    def __delattr__(self) -> None: ...
    def __dir__(self, /): ...
    def __eq__(self) -> None: ...
    def __format__(self, format_spec, /): ...
    def __ge__(self) -> None: ...
    def __getattribute__(self) -> None: ...
    def __getstate__(self, /): ...
    def __gt__(self) -> None: ...
    def __hash__(self) -> None: ...
    def __init__(self) -> None: ...
    def __init_subclass__(cls) -> None: ...
    def __le__(self) -> None: ...
    def __lt__(self) -> None: ...
    def __ne__(self) -> None: ...
    def __new__(cls) -> None: ...
    def __reduce__(self) -> None: ...
    def __reduce_ex__(self, protocol, /): ...
    def __repr__(self) -> None: ...
    def __setattr__(self) -> None: ...
    def __sizeof__(self, /): ...
    def __str__(self) -> None: ...
    def __subclasshook__(self) -> None: ...

class vrMaterialPtr:
    __module__: str
    __doc__: str
    __instance_size__: int
    def __class__(self) -> None: ...
    def __delattr__(self) -> None: ...
    def __dir__(self, /): ...
    def __eq__(self) -> None: ...
    def __format__(self, format_spec, /): ...
    def __ge__(self) -> None: ...
    def __getattribute__(self) -> None: ...
    def __getstate__(self, /): ...
    def __gt__(self) -> None: ...
    def __hash__(self) -> None: ...
    def __init__(self, source: int) -> None: ...
    def __init_subclass__(cls) -> None: ...
    def __le__(self) -> None: ...
    def __lt__(self) -> None: ...
    def __ne__(self) -> None: ...
    def __new__(cls) -> None: ...
    def __reduce__(self) -> None: ...
    def __reduce_ex__(self, protocol, /): ...
    def __repr__(self) -> None: ...
    def __setattr__(self) -> None: ...
    def __sizeof__(self, /): ...
    def __str__(self) -> None: ...
    def __subclasshook__(self) -> None: ...
    def addChunk(self, chunk: vrChunkPtr) -> bool: ...
    def addMaterial(self, mat: vrMaterialPtr) -> None: ...
    def copy(self) -> vrMaterialPtr: ...
    def fields(self) -> vrFieldAccess: ...
    def getChoice(self) -> int: ...
    def getChunk(self, i: int) -> vrChunkPtr: ...
    def getChunkCount(self) -> int: ...
    def getID(self) -> int: ...
    def getMaterialByChoice(self, choice: int) -> vrMaterialPtr: ...
    def getName(self) -> str: ...
    def getNodes(self) -> list: ...
    def getPtr(self) -> MaterialPtr: ...
    def getSHLChunk(self) -> vrSHLChunkPtr: ...
    def getSubMaterials(self) -> list: ...
    def getType(self) -> str: ...
    def isAsset(self) -> bool: ...
    def isValid(self) -> bool: ...
    def removeAssetManagerReference(self, mat: list) -> None: ...
    def setChoice(self, choice: int) -> None: ...
    def setMaterialChoiceByTag(self, tag: str) -> None: ...
    def setMaterialChoiceByTags(self, tags: str) -> None: ...
    def setName(self, name: str) -> None: ...
    def setTransparency(self, t: float) -> None: ...
    def sub(self, update: bool) -> None: ...
    def subChunk(self, chunk: vrChunkPtr) -> bool: ...
    def subMaterial(self, mat: vrMaterialPtr) -> None: ...
