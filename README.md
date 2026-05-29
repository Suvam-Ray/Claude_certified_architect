# Claude Certified Architect - Learning Material

All scripts and illustrations in this repository are in working state and have been tested by **Suvam Ray**.  
**Connect with Suvam:** [suvamray2008@gmail.com](mailto:suvamray2008@gmail.com) for queries.

**Course Source:** [Anthropic Skilljar](https://anthropic.skilljar.com/)

[Open the full notebook](01_Claude_Certified_architect.ipynb) for detailed explanations, code examples, and illustrations.

## Summary

This comprehensive notebook covers everything needed to master Claude's API and build production-ready applications. From API fundamentals to advanced topics like MCP (Model Context Protocol), RAG pipelines, and Claude Code — it includes hands-on code examples, reference images, and utility functions.

---

## Table of Contents

### 1. Claude API Fundamentals
   - a) Using Claude API
   - b) Multi-turn Conversations
   - c) Chat Bot Exercise
   - d) System Prompts
   - e) Temperature
   - f) Response Streaming

### 2. Structured Output & Evaluation
   - a) Generating Structured Data (Prefill & Stop Sequence)
   - b) Using Eval to Refine Prompts
   - c) Eval Task
   - d) Step 1: Using Haiku to Generate Eval Dataset
   - e) Step 2 & 3: Passing Test Cases and Grading Responses
   - f) Step 3: Implementing Grader
   - g) Step 3: Implementing Model-based Grader
   - h) Step 3: Implementing Code-based Grader
   - i) Adding Solution Criteria for Better Grading

### 3. Prompt Engineering
   - a) Prompt Engineering
   - b) Be Clear and Direct
   - c) Be Specific
   - d) Providing Structure using XML Tags
   - e) Providing Examples

### 4. Tool Usage
   - a) Tool Use with Claude
   - b) Tool Function
   - c) Tool Schema
   - d) Multi-block Messages
   - e) Running Tools using ToolUseBlock
   - f) Returning Tool Result Block
   - g) Multi-turn Conversation with Tools
   - h) Explanation for Tool Flow
   - i) Adding More Tools
   - j) Streaming Tool Calls & Fine-grained Calls

### 5. Tools & Extensions
   - a) Text Editor Tool
   - b) Web Search Tool

### 6. RAG (Retrieval Augmented Generation)
   - a) RAG - Retrieval Augmented Generation
   - b) Chunking Strategies (chunk_by_char, chunk_by_sentence, chunk_by_section)
   - c) Semantic Search using Embeddings
   - d) Full RAG Flow

### 7. Vector DB Operations
   - a) In-memory Storage (Volatile)
   - b) Add Vectors
   - c) Search
   - d) Delete
   - e) Persist to Disk
   - f) Retrieve Later

### 8. Advanced Retrieval
   - a) BM25 Lexical Search
   - b) Hybrid Search (Semantic + BM25)
   - c) Notes on RAG Pipeline

### 9. Advanced Claude Features
   - a) Extended Thinking in Claude
   - b) Image Handling in Claude
   - c) PDF Handling in Claude
   - d) Citations in Claude
   - e) Prompt Caching

### 10. Code Execution & Files API
   - a) Code Execution in Claude
   - b) Files API in Claude

### 11. MCP (Model Context Protocol)
   - a) MCP Overview
   - b) MCP Components - Resources, Prompts, Tools

### 12. Advanced MCP
   - a) Sampling
   - b) Logs and Progress Tracking
   - c) Roots
   - d) Streamable HTTP

### 13. Claude Code
   - a) Claude Code - Introduction
   - b) Custom Commands in Claude Code
   - c) Adding Playwright MCP Server in Claude Code
   - d) GitHub Integration with Claude Code
   - e) Skills in Claude Code
   - f) Advanced Concepts in Skills
   - g) Subagents in Claude Code
   - h) Hooks in Claude Code
   - i) Claude Code SDK

### 14. Workflows & Agents
   - a) Workflows and Agents - Overview
   - b) Evaluator-Optimizer Workflow
   - c) Parallelization Workflows
   - d) Chaining Workflows
   - e) Routing Workflows
   - f) Agents

---

## Utility Files

| File | Description |
|------|-------------|
| `utils/eval_functions.py` | Evaluation framework with grading functions |
| `utils/tools_functions.py` | Tool usage helper functions (v1) |
| `utils/tools_functions_v2.py` | Tool usage with multi-block messages |
| `utils/tools_functions_v3.py` | Streaming tool calls implementation |
| `utils/text_editor_tool.py` | Text editor tool implementation |
| `utils/web_search_tool.py` | Web search tool implementation |
| `utils/rag_and_vectordb_v1.py` | RAG pipeline with vector DB |
| `utils/rag_bm25_lexical_search.py` | BM25 lexical search |
| `utils/rag_hybrid_bm25_and_vector.py` | Hybrid search (semantic + BM25) |
| `utils/chunking_v1.py` | Text chunking strategies |
| `utils/claude_thinking_utils.py` | Extended thinking utilities |
| `utils/claude_handling_images.py` | Image handling utilities |
| `utils/claude_citation_testing.py` | Citation testing utilities |
| `utils/prompt_caching.py` | Prompt caching implementation |
| `utils/code_execution.py` | Code execution utilities |

---

## Input & Output Files

| Directory | Contents |
|-----------|----------|
| `Input_and_Output/claude_images_testing/` | Sample images (prop1-prop7.png) |
| `Input_and_Output/claude_pdf_testing/` | Sample PDF (earth.pdf) |
| `Input_and_Output/code_execution_testing/` | Code execution test data |
| `Input_and_Output/eval_dataset.json` | Evaluation dataset |
| `Input_and_Output/prompt_engineering_dataset.json` | Prompt engineering dataset |
| `Input_and_Output/report_chunking_v1.md` | Sample document for chunking |
| `Input_and_Output/text_editor_input.py` | Text editor test input |
| `Input_and_Output/text_editor_output.py` | Text editor test output |

---

## Reference Photos

38 illustrations covering API workflow, temperature, tool calls, RAG pipeline, MCP architecture, Claude Code hooks, and more.
