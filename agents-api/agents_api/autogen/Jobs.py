# generated by datamodel-codegen:
#   filename:  openapi-0.4.0.yaml

from __future__ import annotations

from typing import Annotated, Literal
from uuid import UUID

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field, StrictBool


class JobStatus(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    id: Annotated[UUID, Field(json_schema_extra={"readOnly": True})]
    created_at: Annotated[AwareDatetime, Field(json_schema_extra={"readOnly": True})]
    """
    When this resource was created as UTC date-time
    """
    updated_at: Annotated[AwareDatetime, Field(json_schema_extra={"readOnly": True})]
    """
    When this resource was updated as UTC date-time
    """
    name: Annotated[
        str,
        Field(
            "",
            max_length=120,
            pattern="^[\\p{L}\\p{Nl}\\p{Pattern_Syntax}\\p{Pattern_White_Space}]+[\\p{ID_Start}\\p{Mn}\\p{Mc}\\p{Nd}\\p{Pc}\\p{Pattern_Syntax}\\p{Pattern_White_Space}]*$",
        ),
    ]
    """
    Name of the job
    """
    reason: str = ""
    """
    Reason for the current state of the job
    """
    has_progress: StrictBool = False
    """
    Whether this Job supports progress updates
    """
    progress: Annotated[float, Field(0, ge=0.0, le=100.0)]
    """
    Progress percentage
    """
    state: Literal[
        "pending",
        "in_progress",
        "retrying",
        "succeeded",
        "aborted",
        "failed",
        "unknown",
    ] = "pending"
    """
    Current state of the job
    """
