__name__: str
__doc__: str
__package__: str
__spec__: ModuleSpec

def __loader__(self) -> None: ...
def createAimConstraint(self, sourceNames: list, upSourceNames: list, targetName: str) -> None: ...
def createRotationConstraint(self, sourceNames: list, targetName: str, maintainOffset: bool) -> None: ...
def createTranslationConstraint(self, sourceNames: list, targetName: str, maintainOffset: bool) -> None: ...
