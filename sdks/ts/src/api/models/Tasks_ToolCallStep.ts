/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Common_PyExpression } from "./Common_PyExpression";
import type { Common_toolRef } from "./Common_toolRef";
import type { Tasks_BaseWorkflowStep } from "./Tasks_BaseWorkflowStep";
export type Tasks_ToolCallStep = Tasks_BaseWorkflowStep & {
  kind_: "tool_call";
  /**
   * The tool to run
   */
  tool: Common_toolRef;
  /**
   * The input parameters for the tool (defaults to last step output)
   */
  arguments: Record<string, Common_PyExpression> | "_";
};
