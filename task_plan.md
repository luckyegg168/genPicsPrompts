# Task Plan: AI Image Prompt Generator App

## Goal
Build a Python app that uses OpenRouter AI API to generate bilingual (Chinese + English) image prompts with:
- Character actions and action continuity
- Expression changes
- Scene changes
- Persistent prompt recording (JSON + Markdown)

## Tech Stack
- **Language:** Python 3.10+
- **AI API:** OpenRouter (configurable model)
- **UI:** CLI (rich library for beautiful terminal output)
- **Storage:** JSON + Markdown files
- **Config:** .env file

## Architecture

```
genPicsPrompts/
├── main.py              # Entry point, CLI
├── agent.py             # OpenRouter AI agent
├── prompt_generator.py  # Prompt generation logic
├── recorder.py          # Save/load prompts
├── models.py            # Data models (Pydantic)
├── config.py            # Config & env loading
├── outputs/             # Generated prompts saved here
│   ├── prompts.json     # All prompts (structured)
│   └── prompts.md       # Human-readable log
├── .env.example         # API key template
└── requirements.txt
```

## Phases

### Phase 1: Setup & Models [ ] in_progress
- [ ] Create requirements.txt
- [ ] Create .env.example
- [ ] Create config.py
- [ ] Create models.py (Pydantic data models)

### Phase 2: OpenRouter Agent [ ]
- [ ] Create agent.py (OpenRouter API wrapper)
- [ ] Support model selection
- [ ] Error handling & retries

### Phase 3: Prompt Generator [ ]
- [ ] Create prompt_generator.py
- [ ] Generate character actions (with continuity logic)
- [ ] Generate expression changes
- [ ] Generate scene changes
- [ ] Chinese + English bilingual output

### Phase 4: Recorder [ ]
- [ ] Create recorder.py
- [ ] Save to JSON (structured)
- [ ] Save to Markdown (human-readable)
- [ ] Load/browse history

### Phase 5: CLI Main [ ]
- [ ] Create main.py
- [ ] Interactive CLI with rich
- [ ] Generate single prompt
- [ ] Generate sequence (continuity)
- [ ] Browse saved prompts

### Phase 6: Test & Polish [ ]
- [ ] Test with real OpenRouter API
- [ ] Fix issues
- [ ] Write README

## Decisions
| Decision | Choice | Reason |
|----------|--------|--------|
| API | OpenRouter | Multi-model support, cost effective |
| UI | CLI + rich | Simple, no web server needed |
| Storage | JSON + MD | Portable, human-readable |
| Models | Pydantic | Type-safe data validation |

## Errors Encountered
| Error | Attempt | Resolution |
|-------|---------|------------|
| — | — | — |
