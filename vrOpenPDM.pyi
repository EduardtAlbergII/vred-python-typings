from builtins import NoneType
from typing import Any

__name__: str
__doc__: NoneType
__package__: str
__spec__: ModuleSpec

def __loader__(self) -> None: ...
def pdmBar(self) -> None: ...
def pdmExport(self, type: Any, name: str, revision: Any) -> None: ...
def pdmFoo(self, type: Any, name: str, revision: Any) -> None: ...
def pdmLoadTest(self) -> None: ...
def pdmLogin(self, user: Any, password: Any, system: Any) -> None: ...
def pdmPullTest(self) -> None: ...
