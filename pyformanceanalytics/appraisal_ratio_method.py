"""An enumeration for the appraisal ratio method."""
from enum import Enum


class AppraisalRatioMethod(Enum):
    APPRAISAL = "appraisal"
    MODIFIED = "modified"
    ALTERNATIVE = "alternative"
