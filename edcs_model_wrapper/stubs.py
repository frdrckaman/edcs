from typing import List, Optional, Protocol, Type, TypeVar

from edcs_model.stubs import BaseUuidModelStub


class ModelStub(BaseUuidModelStub, Protocol):
    wrapped: bool
    ...


TModelStub = TypeVar("TModelStub", bound="ModelStub")


class ModelWrapperStub(Protocol):
    model_obj: ModelStub
    model: str
    model_cls: Type[ModelStub]
    cancel_url_name: str
    cancel_url_attrs: List[str]
    next_url_name: str
    next_url_attrs: List[str]
    querystring_attrs: List[str]
    force_wrap: Optional[bool]
    ...
