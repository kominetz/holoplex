# AI Assistant Terminology Document

This document provides a comprehensive overview of the key terms and concepts related to interacting with the AI assistant. It is designed to help you understand how to effectively communicate your needs, leverage the assistant's capabilities, and navigate advanced features.

- **Reference specific sections or terms** if you want to clarify, revise, or leverage a capability.
- **Efficiently instruct changes** using the edit/request terminology.
- **Navigate advanced features** (reasoning, code, research) by using associated language.

## Overview: Key Capability Areas

The AI assistant can support you through a defined set of capabilities, each with its own operational concepts and terminology. Understanding these categories helps you communicate efficiently and get the most from our collaboration.

### Capability Summary Table

| Area                    | What it Covers                                                         |
|-------------------------|------------------------------------------------------------------------|
| Core Interaction        | Prompts, responses, dialogue, and turn-taking                          |
| Memory & Context        | How context is handled, memory is used, and session state is maintained|
| Change & Edit Requests  | Efficient instructions for edits, updates, batch actions               |
| Data/File Handling      | Upload, parse, extract, and summarize files and data                   |
| Reasoning & Automation | Multi-step logic, workflows, tool use, code execution                  |
| Coding/Technical Tasks  | Code generation, debugging, documentation                              |
| Research & Citation     | Source tracking, synthesizing, attribution                             |
| Personalization         | User profile, prompt tuning, context adaptation                        |
| Conversation Control    | Reset, redact, privacy, consent                                       |

## Core Interaction Terminology

- **Prompt / Query / Input:** Your instruction or question.
- **Response / Output / Answer:** AI’s reply to your input.
- **Session / Turn / Entry:** Each back-and-forth message.
- **Statelessness:** Each new session starts “fresh” unless memory is activated.

## Memory & Context Usage

| Term                      | Description                              |
|---------------------------|------------------------------------------|
| Short-Term Memory (STM)   | Remembers recent conversation history    |
| Context Window            | Limit on how much can be remembered at once |
| Long-Term Memory (LTM)    | Retains information across sessions (if consented) |
| Stateless Operation       | Default “no memory” between sessions     |
| Recall/Retrieval          | Bringing relevant info into the current context |

**Usage Patterns**  
- "Add this to session memory." / "Recall previous info." / "Forget this exchange."

## Making Changes: Edit/Update Instructions

| Task                   | Example Phrase                                 |
|------------------------|------------------------------------------------|
| Add                    | "Add [item/section] to..."                     |
| Update                 | "Update [section/term] with..."                |
| Remove/Delete          | "Remove [item/section]."                       |
| Replace                | "Replace [A] with [B]."                        |
| Show Results           | "Display the updated document."                |
| Multiple at Once       | "Add X, update Y, and display."                |
| General Edit           | "Edit/revise/amend the document with..."       |

**Patterns**
- Imperative phrasing, chaining, batch directives, implicit result display.

## Data/File Handling

| Term             | Description                                         |
|------------------|----------------------------------------------------|
| Upload/Download  | Transfer files to/from the assistant                |
| Parse/Extract    | Analyze documents, extract structured info          |
| Summarize        | Create concise overviews of text or data            |

## Reasoning & Workflow Automation

| Term              | Description                                      |
|-------------------|-------------------------------------------------|
| Chain-of-Thought  | Stepwise logical reasoning                       |
| Agentic Actions   | Taking multi-step, autonomous actions            |
| Tool Use          | Invoking specific functions (run code, search)   |

## Coding & Technical Tasks

| Term             | Description                               |
|------------------|------------------------------------------|
| Code Snippet     | Generated piece of code                   |
| Execution        | Running code or commands                  |
| Debug/Diagnose   | Isolating and resolving coding issues     |
| Documentation    | Linking code to explanations              |

## Research & Citation

| Term              | Description                              |
|-------------------|------------------------------------------|
| Reference/Citation| Tracking and attributing sources         |
| Synthesis         | Combining info from multiple sources      |
| Attribution       | Assigning credit for statements/facts     |

## Personalization

| Term                | Description                              |
|---------------------|------------------------------------------|
| Profile/Settings    | Customizing the experience               |
| Prompt Engineering  | Tuning prompts for better outcomes       |
| Contextual Adaptation| Adjusting behavior to preferences        |

## Conversation Control & Safety

| Term             | Description                               |
|------------------|-------------------------------------------|
| Reset/Restart    | Begin anew; wipe current context          |
| Redact           | Delete or mask sensitive data             |
| Consent          | Grant permission for memory or other features |

## Technical Constraints

- **Token Limit:** My responses are measured in tokens (a token is roughly 4 characters or about ¾ of an English word).
- **Context Window:** This is the maximum number of tokens I can process at once, including your prompt, my response, and recent conversation. For most advanced LLMs, this is typically:
  - **Standard models:** 4,096–8,192 tokens (roughly 3,000–6,000 words).
  - **Extended models (like GPT-4, Claude 3, etc):** Up to **128,000 tokens** (about 90,000 words) for full context, but single responses are usually much smaller.

### Practical Output Limits

- **Single-response cap:**  
  - Most platforms cap individual responses at **2,000–4,000 tokens** (about **1,500–3,000 words**), even if the underlying model can handle more.
- **File/code blocks:**  
  - When outputting code, tables, or documents, practical platform/time limits may further restrict length to avoid overload or timeouts.

### What This Means for You

- **Longest reply:** I can typically generate responses between **8,000–16,000 characters** (around **2,000–4,000 words**), depending on complexity and system policies.
- **Very large outputs:**  
  - For lengthy documents or code, it’s common to break the content into multiple responses.
  - If you request “the full text of X” that’s very large, I may summarize, provide it in segments, or offer you a method to download/assemble it.

## Usage Patterns

- If you ask for something that exceeds the single-response limit, I’ll notify you and may output in consecutive chunks if you prefer.
- For large technical references, documentation, or codebases, batch requests or file generation are recommended.

## Example

- **Max single reply:** About 2,000–4,000 words, or a few thousand lines of code/text, depending on platform.
- **Multi-part replies:** “Continue,” “Next part,” or “Show the rest” instructions are standard for material that exceeds the cap.

## In summary:

- **Practical single-response maximum:** Roughly 2,000–4,000 words (8,000–16,000 characters)
- **Breaks up larger requests** into segments as needed
- **No capability to directly save or write files to your device**, so very large responses are always copied or downloaded in parts.
