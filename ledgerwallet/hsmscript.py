"""
from dataclasses import dataclass

@dataclass
class HsmScript:
    name: str
    default_params: dict
    use_large_stack: bool = True
"""


class HsmScript(object):
    def __init__(self, name: str, default_params: dict, target_id: int, use_large_stack: bool = True):
        self.name = name
        self.default_params = default_params
        self.use_large_stack = use_large_stack
        if target_id & 0xF <= 2:
            self.scpv2 = False
        else:
            self.scpv2 = True