# campus_tools/__init__.py
# This file turns the folder into a PACKAGE.
# Whatever we import here is available as campus_tools.<name>

from .grades import calculate_grade
from .fees import fee_after_discount

__all__ = ["calculate_grade", "fee_after_discount"]
