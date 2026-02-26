# LLM Workflow Orchestrator

## Overview
This project demonstrates a practical orchestration pattern for using multiple LLMs in a single workflow.

It’s designed around a simple idea:
**use a local model for fast/cheap iteration, then hand off to a stronger cloud model when needed, then run a final review/audit pass.**

## Workflow (high level)
1. **Draft (Local LLM):** generate an initial answer/plan using a local model (Ollama)
2. **Improve (Cloud LLM):** send the draft to a cloud model for refinement
3. **Audit (Optional):** run a second pass to check clarity, completeness, and risks
4. **Output:** return the final result + a short structured summary

## Why I built this
I wanted a repeatable workflow that balances:
- speed + cost (local)
- quality (cloud)
- reliability (audit pass)

This repo is intentionally small and focused so the pattern is easy to reuse.

## Tech
- Python
- Ollama (local inference)
- Optional: OpenAI / Anthropic / Google model APIs

## Status
Initial scaffold. I’m adding example workflows and adapters over time.
