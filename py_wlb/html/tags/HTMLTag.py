from __future__ import annotations

from typing import List
from abc import ABC, abstractmethod

"""
A general abstract class describing a standard html tag
"""
class HTMLTag(ABC):
    
    @property
    @abstractmethod
    def tag_name(self) -> str:
        """abtract field provides html tag name ( <tag_name></tag_name> )"""
        pass

    @abstractmethod
    def bind(self, child_nodes: List[HTMLTag])