from vrNodePtr import NodePtr

__name__: str
__doc__: str
__package__: str
__spec__: ModuleSpec

def __loader__(self) -> None: ...
def triggerTouchSensor(self, name: str) -> None: ...

class vrTouchSensor:
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
    def __init__(self, node: NodePtr) -> None: ...
    def __init_subclass__(cls) -> None: ...
    def __le__(self) -> None: ...
    def __lt__(self) -> None: ...
    def __ne__(self) -> None: ...
    def __new__(cls) -> vrTouchSensor: ...
    def __reduce__(self) -> None: ...
    def __reduce_ex__(self, protocol, /): ...
    def __repr__(self) -> None: ...
    def __setattr__(self) -> None: ...
    def __sizeof__(self, /): ...
    def __str__(self) -> None: ...
    def __subclasshook__(self) -> None: ...
    def addLoop(self) -> None: ...
    def callAllConnected(self) -> None: ...
    def connect(self, o: object, arg1: object, arg2: object) -> bool: ...
    def connectSignal(self, signal: str, slot: object, arg1: object, arg2: object) -> bool: ...
    def emitSignal(self, signal: str, arg1: object, arg2: object) -> None: ...
    def getModuleName(self) -> None: ...
    def isActive(self) -> bool: ...
    def isEnabled(self) -> bool: ...
    def loop(self) -> None: ...
    def recEvent(self, state: int) -> None: ...
    def removeConnections(self) -> None: ...
    def setActive(self, state: int) -> None: ...
    def setEnabled(self, state: bool) -> None: ...
    def setUpdateGUIEnabled(self, state: bool) -> None: ...
    def subLoop(self) -> None: ...
