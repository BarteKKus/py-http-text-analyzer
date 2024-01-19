from dataclasses import dataclass, field
from typing import Optional, Dict, Type

@dataclass
class ReplacementInstruction:
    find: str
    replace_to: str
    info: Optional[str] = field(default=None)
    active: Optional[bool] = field(default=True)

    @classmethod
    def init_from_dict(cls, cfg_dict:Dict)->Type['ReplacementInstruction']:
        return cls(
            find=cfg_dict['find'],
            replace_to=cfg_dict['replace_to'],
            info=cfg_dict.get('info',None),
            active=cfg_dict.get('active',True)
        )

CONFIGURATION_TYPES={
    "replacement":ReplacementInstruction,
}