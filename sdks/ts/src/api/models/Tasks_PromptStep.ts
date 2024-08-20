/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Chat_ChatSettings } from "./Chat_ChatSettings";
import type { Common_JinjaTemplate } from "./Common_JinjaTemplate";
import type { Tasks_BaseWorkflowStep } from "./Tasks_BaseWorkflowStep";
export type Tasks_PromptStep = Tasks_BaseWorkflowStep & {
  kind_: "prompt";
  /**
   * The prompt to run
   */
  prompt: Common_JinjaTemplate;
  /**
   * Settings for the prompt
   */
  settings: Chat_ChatSettings;
};
