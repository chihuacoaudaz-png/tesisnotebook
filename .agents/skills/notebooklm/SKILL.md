---
name: notebooklm
description: Use NotebookLM to inspect notebooks, list sources, read full texts of uploaded documents, query notes, and generate summaries.
---

# NotebookLM Skill Guide

This skill enables Antigravity to interact directly with Google NotebookLM notebooks via the `notebooklm` CLI tool and Python API (`notebooklm-py`).

## Requirements
- `notebooklm-py` installed (`pip install "notebooklm-py[browser]"`)
- Playwright Chromium installed (`playwright install chromium`)
- Active Google authentication stored in `~/.notebooklm/profiles/default/storage_state.json` (created via `notebooklm login`).

## Common Operations

### 1. Check Authentication Status
```bash
notebooklm doctor
```

### 2. List Notebooks
```bash
notebooklm list
```

### 3. Inspect a Notebook
```bash
# View summary and AI insights
notebooklm summary -n <notebook_id>

# View metadata and list sources
notebooklm metadata -n <notebook_id>

# List sources in a notebook
notebooklm source list -n <notebook_id>

# List user notes in a notebook
notebooklm note list -n <notebook_id>
```

### 4. Query a Notebook
```bash
notebooklm ask "<question>" -n <notebook_id>
```

### 5. Export / Read Fulltext of Sources
```bash
notebooklm source fulltext <source_id> -n <notebook_id>
```
