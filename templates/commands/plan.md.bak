---
description: Create a research execution plan translating your PMF hypotheses into methodology, instruments, and validation checkpoints.
handoffs:
  - label: Break Into Tasks
    agent: pmfkit.tasks
    prompt: Convert the research plan into executable PMF discovery tasks
    send: true
  - label: Create Quality Checklist
    agent: pmfkit.checklist
    prompt: Create a research quality checklist for this PMF initiative...
scripts:
  sh: scripts/bash/setup-plan.sh --json
  ps: scripts/powershell/setup-plan.ps1 -Json
agent_scripts:
  sh: scripts/bash/update-agent-context.sh __AGENT__
  ps: scripts/powershell/update-agent-context.ps1 -AgentType __AGENT__
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

1. **Setup**: Run `{SCRIPT}` from repo root and parse JSON for FEATURE_SPEC, IMPL_PLAN, SPECS_DIR, BRANCH. For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot").

2. **Load context**: Read FEATURE_SPEC (PMF spec with personas, JTBD, hero workflows) and `/memory/constitution.md` for research principles. Load IMPL_PLAN template (research planning instead of technical architecture).

3. **Execute research planning workflow**: Follow the structure in IMPL_PLAN template to:
   - Fill Research Context (evidence collection methods, sample sizes, instruments)
   - Fill Constitution Check section from constitution (verify specification-first, customer-evidence-driven principles)
   - Evaluate research methodology gates (ERROR if violations unjustified)
   - Phase 0: Generate research-questions.md (clarify what you're testing and how)
   - Phase 1: Generate research-instruments.md (interview guides, survey templates, experiment protocols)
   - Phase 1: Generate validation-checkpoints.md (PDCA cycle gates, pivot/persevere criteria)
   - Phase 1: Update agent context by running the agent script
   - Re-evaluate Constitution Check post-design

4. **Stop and report**: Command ends after Phase 1 planning. Report branch, IMPL_PLAN path, and generated research artifacts.

## Phases

### Phase 0: Hypothesis Clarification & Research Design

1. **Extract research questions from PMF spec**:
   - For each hypothesis → clarification task
   - For each JTBD → validation approach task
   - For each hero workflow → usability testing task

2. **Generate research design tasks**:

   ```text
   For each persona/segment:
     Task: "Design research plan to validate {JTBD} with {persona}"
   For each hero workflow:
     Task: "Create validation experiment for {workflow} with {sample size} users"
   For each success metric:
     Task: "Instrument measurement for {metric} across {channels}"
   ```

3. **Consolidate findings** in `research-questions.md` using format:
   - Hypothesis: [what we believe to be true about the market]
   - Research question: [specific, testable question]
   - Methodology: [interviews, surveys, behavioral experiments, etc.]
   - Success criteria: [what evidence proves/disproves hypothesis]

**Output**: research-questions.md with all hypotheses operationalized into testable research questions

### Phase 1: Research Instruments & Validation Gates

**Prerequisites:** `research-questions.md` complete

1. **Create research instruments** from research questions → `research-instruments.md`:
   - Interview protocol (script, structure, follow-up patterns)
   - Survey structure (question types, sampling frame, response targets)
   - Experiment protocol (setup, participant instructions, measurement)
   - Observation guide (for user testing sessions)

2. **Generate validation checkpoints** from success criteria:
   - For each learning objective → checkpoint measurement
   - Use PDCA format: what do we measure, when, who decides go/no-go
   - Output validation-checkpoints.md with Go/Kill/Pivot thresholds

3. **Agent context update**:
   - Run `{AGENT_SCRIPT}`
   - These scripts detect which AI agent is in use
   - Update the appropriate agent-specific context file
   - Add only new research methodology from current plan
   - Preserve manual additions between markers

**Output**: research-instruments.md, validation-checkpoints.md, agent-specific context file

## Key rules

- Use absolute paths
- ERROR on methodology violations or unresolved hypotheses
- All research must be directly traceable to PMF spec hypotheses
