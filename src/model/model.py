from dataclasses import dataclass, field, post_init
from typing import List, Optional, Type, TypeVar, Dict
from datetime import datetime

T = TypeVar("T")


class Storage:
    """Storage class for managing different types of data objects"""

    def __init__(self):
        self._storage: Dict[Type, Dict[str, object]] = {}

    def add(self, item: object):
        """Add an item to storage, indexed by both identifier and name if available"""
        item_type = type(item)
        if item_type not in self._storage:
            self._storage[item_type] = {}

        if hasattr(item, "identifier"):
            self._storage[item_type][item.identifier] = item
        if hasattr(item, "name"):
            self._storage[item_type][item.name] = item

    def get_by_id(self, item_class: Type[T], identifier: str) -> Optional[T]:
        """Retrieve an item by its identifier"""
        if item_class not in self._storage:
            return None
        return self._storage[item_class].get(identifier)

    def get_by_name(self, item_class: Type[T], name: str) -> Optional[T]:
        """Retrieve an item by its name"""
        if item_class not in self._storage:
            return None
        return self._storage[item_class].get(name)

    def get_by_class(self, item_class: Type[T]) -> List[T]:
        """Get all items of a specific class"""
        if item_class not in self._storage:
            return []
        return list(self._storage[item_class].values())

    def get_by_class_and_id(self, item_class: Type[T], identifier: str) -> Optional[T]:
        """Get an item by class and identifier"""
        return self.get_by_id(item_class, identifier)


@dataclass
class System:
    """Represents a system with basic identification and purpose information"""

    identifier: str = ""
    name: str = ""
    description: str = ""
    purpose: str = ""
    owner: str = ""
    storage: Storage = field(default_factory=Storage)

    def __post_init__(self):
        self.storage.add(self)


@dataclass
class Partei:
    """Represents a party involved in data processing"""

    identifier: str = ""
    name: str = ""
    role: str = ""  # controller/processor/recipient
    storage: Storage = field(default_factory=Storage)

    def __post_init__(self):
        self.storage.add(self)


@dataclass
class DatenItem:
    """Represents a single data item with its classification"""

    data_class: str = ""
    data_category: str = ""
    data_subcategory: str = ""
    data_field_s: list = field(default_factory=list)
    storage: Storage = field(default_factory=Storage)

    def __post_init__(self):
        self.storage.add(self)


@dataclass
class Datenkatalog:
    """Represents a data catalog containing data items and their properties"""

    identifier: str = ""
    items: List[DatenItem] = field(default_factory=list)
    data_category: str = ""
    data_subcategory: str = ""
    data_type: str = ""
    sensitivity: str = ""  # normal/special/confidential
    legal_basis: str = ""
    purpose: str = ""
    affected_persons: List[str] = None
    retention_period: str = ""
    storage: Storage = field(default_factory=Storage)

    def __post_init__(self):
        self.storage.add(self)


@dataclass
class Austauschvorgang:
    """Represents a data exchange process between parties"""

    identifier: str = ""
    sender: str = ""
    recipient: str = ""
    data_categories: List[str] = None
    transfer_type: str = ""  # internal/external
    transfer_method: str = ""
    encryption: bool = False
    legal_basis: str = ""
    storage: Storage = field(default_factory=Storage)

    def __post_init__(self):
        self.storage.add(self)


@dataclass
class Archivierung:
    """Represents an archiving process for data"""

    identifier: str = ""
    storage_location: str = ""
    storage_duration: str = ""
    access_restrictions: List[str] = None
    encryption: bool = False
    deletion_date: Optional[datetime] = None
    storage: Storage = field(default_factory=Storage)

    def __post_init__(self):
        self.storage.add(self)


@dataclass
class Loeschung:
    """Represents a deletion process for data"""

    identifier: str = ""
    data_category: str = ""
    deletion_period: str = ""
    deletion_method: str = ""
    legal_basis: str = ""
    responsible_party: str = ""
    verification_process: str = ""
    storage: Storage = field(default_factory=Storage)

    def __post_init__(self):
        self.storage.add(self)
