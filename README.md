# AI Workflow Prompt Organizer CLI

A Python terminal application that organizes and serves AI workflow prompts for software development projects. It walks you through a structured planning process — from project description to research, PRD, architecture, and task breakdown — copying the right prompt to your clipboard at each step and injecting prior responses into subsequent prompts.

**This is NOT an AI tool.** It contains no AI integration. It is a prompt clipboard manager that works with your existing AI tools (Poppy/Claude, Grok, Cursor).

## Quick Start

```powershell
# Create and activate a virtual environment (recommended)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install in editable mode
pip install -e .

# Run the application
workflow
# or: python -m app
```

## Main Menu

| Option | Description |
|--------|-------------|
| **Create Project** | Multi-step workflows for software projects (New, Continue, List, Delete) |
| **Other Prompts** | One-shot prompts for research, tool selection, meeting prep, and more |
| **Settings** | View paths for prompts and workflows |
| **Exit** | Quit the application |

## How It Works

### Create Project (multi-step workflows)

1. **Answer a few questions** about your project (complexity, type, tech stack)
2. **The app selects a workflow** (Quick / Standard / Complex) and walks you through each step
3. **At each step**: the app copies a prompt to your clipboard, tells you which AI tool to paste it into, and captures the AI's response
4. **Responses are injected** into subsequent prompts automatically (template variable replacement)
5. **At the end**: the app outputs all generated docs and Cursor configuration files to your project directory

### Other Prompts (one-shot)

1. Pick a prompt type from the menu (e.g. Find Best Tool, Research Topic)
2. Answer 1–2 input questions (e.g. "What do you need to accomplish?")
3. The prompt is rendered with your inputs and copied to your clipboard
4. Paste into Grok, Poppy, or Cursor and get the AI's response — no project state is saved

## Workflow Tiers

| Tier | Complexity | Steps | Duration |
|------|-----------|-------|----------|
| **Quick** | Under 1 day | 2 | ~15 min |
| **Standard** | 1-5 days | 5 | ~45 min |
| **Complex** | 1+ weeks | 7 | ~90 min |

### Overlays
- **Brainstorm**: Prepended when you need help fleshing out your project idea
- **Collaborative**: Appended when working with other developers (adds interface contracts + ADRs)

For **Complex** projects, you can choose **Hierarchical task breakdown** at questionnaire time to get a master plan plus per-workstream task lists in one document (e.g. infrastructure, app store, compliance as separate workstreams).

## Other Prompts (one-shot)

Standalone prompts for research, decisions, and stakeholder work. No project state — copy, paste, done.

| Prompt | Use case |
|--------|----------|
| **Find Best Tool** | "What's the best tool for [X]?" — build-vs-buy style scan |
| **Research Topic** | Learn about a topic — summary, sources, getting started |
| **Compare Options & Decide** | Compare vendors/options, get a recommendation |
| **Build vs Buy** | Should we build custom or use existing? |
| **Meeting Prep** | Key points, anticipated questions, talking points |
| **Stakeholder Brief** | 1-pager explaining a complex topic to non-experts |
| **Competitive Landscape** | Analyze a product category or competitor |
| **Vendor Comparison** | Evaluate and recommend vendors for a need |
| **Learning Path** | Structured steps and resources to learn something |
| **Summarize / TL;DR** | Condense content into key points |
| **Process Documentation** | Document a workflow into steps and roles |

Defined in `workflows/oneshot.yaml`; templates in `prompts/oneshot_*.md`.

## Project Structure

```
├── app/                        # Application code
│   ├── __main__.py             # Entry point (python -m app / workflow)
│   ├── main.py                 # Main menu loop
│   ├── oneshot.py              # One-shot prompt flow (no project state)
│   ├── questionnaire.py        # Multi-choice questions
│   ├── sequencer.py            # Maps answers → workflow → prompt list
│   ├── runner.py               # Core loop: prompt → clipboard → capture → advance
│   ├── state.py                # Save/load project state (JSON)
│   ├── output.py               # Generate final output files
│   ├── display.py              # Rich console formatting helpers
│   └── config.py               # Paths and constants
│
├── prompts/                    # Prompt templates (Markdown + YAML frontmatter)
│   ├── brainstorm.md
│   ├── landscape_quick.md
│   ├── landscape_full.md
│   ├── research_quick.md
│   ├── research_standard.md
│   ├── research_deep.md
│   ├── prd_architecture_combined.md
│   ├── prd_full.md
│   ├── architecture_full.md
│   ├── tasks_standard.md
│   ├── tasks_detailed.md
│   ├── testing_plan.md
│   ├── setup.md
│   ├── interface_contract.md
│   ├── adr.md
│   ├── oneshot_find_best_tool.md
│   ├── oneshot_research_topic.md
│   ├── oneshot_compare_options.md
│   ├── oneshot_build_vs_buy.md
│   ├── oneshot_meeting_prep.md
│   ├── oneshot_stakeholder_brief.md
│   ├── oneshot_competitive_landscape.md
│   ├── oneshot_vendor_comparison.md
│   ├── oneshot_learning_path.md
│   ├── oneshot_summarize.md
│   └── oneshot_process_documentation.md
│
├── workflows/                  # Workflow definitions (YAML)
│   ├── quick.yaml
│   ├── standard.yaml
│   ├── complex.yaml
│   ├── overlay_brainstorm.yaml
│   ├── overlay_collaborative.yaml
│   └── oneshot.yaml            # One-shot prompt definitions
│
├── cursor_templates/           # Cursor rules and commands copied to projects
│   ├── rules/
│   │   ├── 000-core.mdc
│   │   ├── 001-project-context.mdc.template
│   │   ├── python.mdc
│   │   ├── dotnet.mdc
│   │   ├── web-frontend.mdc
│   │   └── security.mdc
│   └── commands/
│       ├── start-task.md
│       ├── verify-task.md
│       ├── complete-task.md
│       ├── escalate-issue.md
│       ├── sync-docs.md
│       ├── explain.md
│       ├── debug.md
│       └── review-code.md
│
├── projects/                   # Saved project state (auto-created)
├── pyproject.toml
├── run-workflow.bat            # Windows launcher (see Desktop Shortcut below)
└── README.md
```

## Customization

### Editing Prompts
Prompt templates are Markdown files in `prompts/`. Each has YAML frontmatter (metadata) and a body with `{{VARIABLE}}` placeholders that get replaced with prior responses during execution.

To customize a prompt, edit the Markdown file directly. The app will use your changes on the next run.

### Editing Workflows
Workflow definitions are YAML files in `workflows/`. Each defines an ordered list of steps with:
- `prompt_file` — which prompt template to use
- `target_tool` — which AI tool the user should paste into
- `stores_as` — variable name to store the response under
- `injects` — which prior responses to inject into this prompt

### Adding New Workflows
Create a new YAML file in `workflows/` following the existing format. To use it, update `app/sequencer.py` to map a new complexity level to your workflow.

### Adding New One-Shot Prompts
1. Create a prompt template in `prompts/oneshot_*.md` with `{{VARIABLE}}` placeholders
2. Add an entry to `workflows/oneshot.yaml` with `id`, `name`, `prompt_file`, `target_tool`, and `inputs`

## Output Files

When a workflow completes, the app generates these files in your project directory:

**docs/**
- `RESEARCH.md` — Technology decisions and documentation links
- `PRD.md` — Product requirements and acceptance criteria
- `ARCHITECTURE.md` — System design and component interfaces
- `TASKS.md` — Implementation plan with dependencies
- `TESTING_PLAN.md` — Testing strategy (Complex tier only)

**.cursor/rules/**
- `000-core.mdc` — Core coding standards (always active)
- `001-project-context.mdc` — Project-specific context (generated)
- Tech-stack-specific rules (Python, .NET, Web, Security)

**.cursor/commands/**
- `start-task.md` — Begin implementing a task
- `verify-task.md` — Verify implementation quality
- `complete-task.md` — Finalize and document a task
- `escalate-issue.md` — Generate issue brief for external AI
- `sync-docs.md` — Sync documentation with codebase
- `explain.md` — Explain code and architectural decisions
- `debug.md` — Debug assistance
- `review-code.md` — Code review prompts

## Desktop Shortcut (Windows)

The easiest way to run the app from your desktop:

1. **Right-click Desktop** → **New** → **Shortcut**
2. **Target:** paste the full path to `run-workflow.bat` in this repo, e.g.:
   ```
   C:\Users\GabeCarmichael\source\repos\PromptSystem\run-workflow.bat
   ```
3. **Name:** e.g. `Workflow CLI`
4. Click **Finish**

Double-clicking the shortcut opens a terminal, activates the venv, and runs the app. (Requires a venv and `pip install -e .` to be run once first.)

## Syncing Between Two PCs (GitHub)

This repo is used on two PCs; progress is synced via GitHub. **Downloading the repo as a ZIP from GitHub does not include Git** — you get no `.git` folder, so `git add` / `git status` fail with "fatal: not a git repository".

### First time on this PC (you already have the ZIP / `PromptSystem-main` folder)

Turn the current folder into a real Git repo and connect it to GitHub:

```powershell
cd C:\Users\Gabe\source\repos\PromptSystem-main

git init
git remote add origin https://github.com/YOUR_USERNAME/PromptSystem.git
git fetch origin
git branch -M main
git reset --hard origin/main
```

Replace `YOUR_USERNAME/PromptSystem` with your actual GitHub repo URL (from the repo’s "Code" → clone URL). After this, you have a full Git history and can pull/push.

**Optional:** To match the other PC’s folder name, rename the folder to `PromptSystem` (e.g. in File Explorer or `Rename-Item`). Then use that path in the Desktop Shortcut and when opening the project.

### Next time on this PC (or any PC): use clone instead of ZIP

To avoid the "not a git repository" issue, clone instead of downloading ZIP:

```powershell
cd C:\Users\Gabe\source\repos
git clone https://github.com/YOUR_USERNAME/PromptSystem.git
cd PromptSystem
```

The folder will be `PromptSystem` (no `-main`). Then create/activate venv and `pip install -e .` as in Quick Start.

### Daily workflow: pull ↔ push

- **Before you start work (on either PC):** pull the latest so you’re in sync.
  ```powershell
  git pull origin main
  ```
- **When you’re done (on this PC):** commit and push so the other PC can pull.
  ```powershell
  git add .
  git commit -m "feat: describe your changes"
  git push origin main
  ```

On the other PC, run `git pull origin main` to get these updates. Resolve any merge conflicts if you edited the same files on both PCs.

## Requirements

- Python 3.11+
- Dependencies: `rich`, `pyperclip`, `pyyaml`
