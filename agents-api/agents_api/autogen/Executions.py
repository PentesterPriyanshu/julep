# generated by datamodel-codegen:
#   filename:  openapi-0.4.0.yaml

from __future__ import annotations

from typing import Annotated, Any, Literal
from uuid import UUID

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field


class CreateExecutionRequest(BaseModel):
    """
    Payload for creating an execution
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    input: dict[str, Any]
    """
    The input to the execution
    """
    metadata: dict[str, Any] | None = None


class Execution(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    task_id: Annotated[UUID, Field(json_schema_extra={"readOnly": True})]
    """
    The ID of the task that the execution is running
    """
    status: Annotated[
        Literal[
            "queued",
            "starting",
            "running",
            "awaiting_input",
            "succeeded",
            "failed",
            "cancelled",
        ],
        Field(json_schema_extra={"readOnly": True}),
    ]
    """
    The status of the execution
    """
    input: dict[str, Any]
    """
    The input to the execution
    """
    created_at: Annotated[AwareDatetime, Field(json_schema_extra={"readOnly": True})]
    """
    When this resource was created as UTC date-time
    """
    updated_at: Annotated[AwareDatetime, Field(json_schema_extra={"readOnly": True})]
    """
    When this resource was updated as UTC date-time
    """
    metadata: dict[str, Any] | None = None
    id: Annotated[UUID, Field(json_schema_extra={"readOnly": True})]


class TaskTokenResumeExecutionRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    status: Literal["running"] = "running"
    input: dict[str, Any] | None = None
    """
    The input to resume the execution with
    """


class Transition(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    type: Annotated[
        Literal["finish", "wait", "resume", "error", "step", "cancelled"],
        Field(json_schema_extra={"readOnly": True}),
    ]
    execution_id: Annotated[UUID, Field(json_schema_extra={"readOnly": True})]
    output: Annotated[dict[str, Any], Field(json_schema_extra={"readOnly": True})]
    current: Annotated[TransitionTarget, Field(json_schema_extra={"readOnly": True})]
    next: Annotated[
        TransitionTarget | None, Field(json_schema_extra={"readOnly": True})
    ]
    id: Annotated[UUID, Field(json_schema_extra={"readOnly": True})]
    metadata: dict[str, Any] | None = None
    created_at: Annotated[AwareDatetime, Field(json_schema_extra={"readOnly": True})]
    """
    When this resource was created as UTC date-time
    """
    updated_at: Annotated[AwareDatetime, Field(json_schema_extra={"readOnly": True})]
    """
    When this resource was updated as UTC date-time
    """


class TransitionTarget(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    workflow: Annotated[
        str,
        Field(
            max_length=120,
            pattern="^[\\p{L}\\p{Nl}\\p{Pattern_Syntax}\\p{Pattern_White_Space}]+[\\p{ID_Start}\\p{Mn}\\p{Mc}\\p{Nd}\\p{Pc}\\p{Pattern_Syntax}\\p{Pattern_White_Space}]*$",
        ),
    ]
    """
    For Unicode character safety
    See: https://unicode.org/reports/tr31/
    See: https://www.unicode.org/reports/tr39/#Identifier_Characters
    """
    step: int


class UpdateExecutionRequest(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    status: Literal[
        "queued",
        "starting",
        "running",
        "awaiting_input",
        "succeeded",
        "failed",
        "cancelled",
    ]


class ResumeExecutionRequest(UpdateExecutionRequest):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    status: Literal["running"] = "running"
    input: dict[str, Any] | None = None
    """
    The input to resume the execution with
    """


class StopExecutionRequest(UpdateExecutionRequest):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    status: Literal["cancelled"] = "cancelled"
    reason: str | None = None
    """
    The reason for stopping the execution
    """
