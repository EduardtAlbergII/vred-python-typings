__name__: str
__doc__: str
__package__: str
__spec__: ModuleSpec
Key_Spacemouse_1: int
Key_Spacemouse_2: int
Key_Spacemouse_3: int
Key_Spacemouse_4: int
Key_Spacemouse_5: int
Key_Spacemouse_6: int
Key_Spacemouse_7: int
Key_Spacemouse_8: int
Key_Spacemouse_9: int
Key_Spacemouse_10: int
Key_Spacemouse_11: int
Key_Spacemouse_12: int
Key_Spacemouse_13: int
Key_Spacemouse_14: int
Key_Spacemouse_15: int
Key_Spacemouse_16: int
Key_Spacemouse_17: int
Key_Spacemouse_18: int
Key_Spacemouse_19: int
Key_Spacemouse_20: int
Key_Spacemouse_21: int
Key_Spacemouse_22: int
Key_Spacemouse_23: int
Key_Spacemouse_24: int
Key_Spacemouse_25: int
Key_Spacemouse_26: int
Key_Spacemouse_27: int
Key_Spacemouse_28: int
Key_Spacemouse_29: int
Key_Spacemouse_30: int
Key_Spacemouse_31: int
Key_Spacemouse_32: int

def __loader__(self) -> None: ...
def setSpacemouseButtonText(self, index: int, text: str) -> None: ...
def setSpacemouseMenuText(self, text: str) -> None: ...

class vrSpacemouseButton:
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
    def __init__(self, button: int) -> None: ...
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
    def addLoop(self) -> None: ...
    def callAllConnected(self) -> None: ...
    def connect(self, o: object, arg1: object, arg2: object) -> bool: ...
    def connectSignal(self, signal: str, slot: object, arg1: object, arg2: object) -> bool: ...
    def emitSignal(self, signal: str, arg1: object, arg2: object) -> None: ...
    def getModuleName(self) -> None: ...
    def isActive(self) -> bool: ...
    def loop(self) -> None: ...
    def recEvent(self, state: int) -> None: ...
    def removeConnections(self) -> None: ...
    def setActive(self, state: int) -> None: ...
    def setUpdateGUIEnabled(self, state: bool) -> None: ...
    def subLoop(self) -> None: ...
