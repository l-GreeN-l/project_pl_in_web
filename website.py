from dataclasses import dataclass
from cffi.backend_ctypes import long

@dataclass
class Website:
    website: str
    popularity: long
    frontend: str
    backend: str
    database: str
    notes: str
