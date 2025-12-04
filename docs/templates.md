# PMF-Kit Templates

## Overview

PMF-Kit templates provide a structured starting point for product-market-fit discovery projects using AI coding agents. Templates are automatically downloaded when you run `pmf init`, but can also be downloaded manually from [GitHub Releases](https://github.com/agentii-ai/pmf-kit/releases).

## Template Contents

Each template includes:

```
project-root/
├── .specify/                      # Shared toolkit files
│   ├── memory/
│   │   └── constitution.md       # PMF-Kit constitution v1.0.0
│   ├── scripts/
│   │   ├── bash/                 # Bash automation scripts
│   │   └── powershell/           # PowerShell automation scripts
│   └── templates/
│       ├── spec-template.md      # Feature specification template
│       ├── plan-template.md      # Implementation planning template
│       └── tasks-template.md     # Task breakdown template
└── .{agent}/                      # Agent-specific directory
    ├── commands/                  # Slash command files (agent varies)
    │   ├── pmfkit.specify.md     # /pmfkit.specify command
    │   ├── pmfkit.plan.md        # /pmfkit.plan command
    │   ├── pmfkit.tasks.md       # /pmfkit.tasks command
    │   ├── pmfkit.implement.md   # /pmfkit.implement command
    │   ├── pmfkit.clarify.md     # /pmfkit.clarify command
    │   ├── pmfkit.analyze.md     # /pmfkit.analyze command
    │   ├── pmfkit.checklist.md   # /pmfkit.checklist command
    │   ├── pmfkit.taskstoissues.md # /pmfkit.taskstoissues command
    │   └── pmfkit.constitution.md  # /pmfkit.constitution command
    └── (other agent-specific files as needed)
```

## Command Reference

### /pmfkit.specify

**Purpose**: Create or update your PMF specification from a natural language description

**Usage**: `/pmfkit.specify "Add user authentication to the SaaS dashboard"`

**Generates**:
- Target personas with skills and environment
- Top 3 jobs-to-be-done (customer problems)
- 1-2 hero workflows (end-to-end flows)
- Success metrics (activation, engagement, business)
- Key constraints and risks

### /pmfkit.clarify

**Purpose**: Identify and resolve ambiguities in your specification

**Usage**: `/pmfkit.clarify` (in a conversation with your specification)

**Resolves**:
- Unclear persona definitions
- Vague success criteria
- Missing validation criteria
- Unstated assumptions

### /pmfkit.plan

**Purpose**: Create a detailed research and execution plan

**Usage**: `/pmfkit.plan` (in a conversation with your specification)

**Generates**:
- Research methodology
- Sample sizes and recruitment strategy
- Data collection instruments
- Analysis approach
- Validation checkpoints

### /pmfkit.tasks

**Purpose**: Break your plan into actionable research tasks

**Usage**: `/pmfkit.tasks` (in a conversation with your plan)

**Generates**:
- Recruit participants
- Conduct interviews and research
- Analyze results
- Validate hypotheses
- Document learnings

### /pmfkit.implement

**Purpose**: Execute your research tasks with AI assistance

**Usage**: `/pmfkit.implement` (ready to execute your tasks)

**Provides**:
- Step-by-step execution guidance
- Evidence collection templates
- Analysis frameworks
- Decision-making support

### /pmfkit.analyze

**Purpose**: Cross-validate your specification, plan, and tasks for consistency

**Usage**: `/pmfkit.analyze`

**Checks**:
- Spec completeness and clarity
- Plan feasibility
- Task dependency ordering
- Evidence collection alignment

### /pmfkit.clarify (Targeted)

**Purpose**: Ask specific clarification questions about underspecified areas

**Usage**: `/pmfkit.clarify` (in a specification context)

**Generates**:
- Up to 5 targeted questions
- Question categories (customer, market, technical, business)
- Suggested answer formats

### /pmfkit.checklist

**Purpose**: Create a custom checklist for your discovery project

**Usage**: `/pmfkit.checklist "customer interviews"` or `/pmfkit.checklist`

**Generates**:
- Custom checklist based on your needs
- Actionable items
- Success criteria for each item

### /pmfkit.taskstoissues

**Purpose**: Convert your research tasks into GitHub issues

**Usage**: `/pmfkit.taskstoissues`

**Creates**:
- One GitHub issue per task
- Proper dependency ordering
- Labels for priority and category
- Links to related documentation

### /pmfkit.constitution

**Purpose**: Manage project-specific principles and governance

**Usage**: `/pmfkit.constitution` or `/pmfkit.constitution "add principle"`

**Enables**:
- View base PMF-Kit constitution
- Add project-specific principles
- Define team decision-making rules
- Document governance

## Agent-Specific Information

### Claude Code
- **Directory**: `.claude/commands/`
- **Format**: Markdown with YAML frontmatter
- **Invocation**: `/pmfkit.specify "your request"`

### GitHub Copilot
- **Directory**: `.github/agents/` and `.github/prompts/`
- **Format**: Special `.agent.md` and `.prompt.md` files
- **Configuration**: `.vscode/settings.json`

### Google Gemini / Qwen
- **Directory**: `.gemini/commands/` or `.qwen/commands/`
- **Format**: TOML configuration files
- **Argument syntax**: `{{args}}` instead of `$ARGUMENTS`

### Other Agents
Each agent has a specific directory structure and command format. Refer to the agent's documentation within your template for details.

## Release History

### v0.1.0 (First Release)

**Initial Release**: PMF-Kit v0.1.0 introduces automated template generation for 18 AI agents (36 variants total).

**Includes**:
- PMF-Kit Constitution v1.0.0
- 9 core slash commands
- Templates for spec, plan, and tasks
- Support for bash and PowerShell

**Download**: [PMF-Kit v0.1.0 Release](https://github.com/agentii-ai/pmf-kit/releases/tag/v0.1.0)

## Manual Template Download

If you prefer to manually manage templates:

1. Go to [GitHub Releases](https://github.com/agentii-ai/pmf-kit/releases)
2. Find your desired agent version (e.g., `spec-kit-template-claude-sh-v0.1.0.zip`)
3. Download the ZIP file
4. Extract to your project root
5. All commands will be available in your AI agent

Each ZIP file includes SHA-256 checksums for verification.

## Template Customization

All templates can be customized for your specific needs:

- Modify `/specify/memory/constitution.md` to add project-specific principles
- Edit template files in `/specify/templates/` for your workflow
- Customize command files in `.{agent}/commands/` for agent-specific tweaks
- Add new commands by copying and modifying existing templates

## Support

For issues, questions, or contributions:
- **Issues**: [GitHub Issues](https://github.com/agentii-ai/pmf-kit/issues)
- **Discussions**: [GitHub Discussions](https://github.com/agentii-ai/pmf-kit/discussions)
- **Documentation**: [PMF-Kit Docs](https://github.com/agentii-ai/pmf-kit#-reference-documentation)

## Contributing

We welcome contributions to improve PMF-Kit templates:

1. Fork the repository
2. Create a feature branch: `git checkout -b improve-templates`
3. Make your changes to `templates/commands/` or documentation
4. Test locally: `./scripts/validate-templates.sh dist/templates/`
5. Submit a pull request

See [CONTRIBUTING.md](../CONTRIBUTING.md) for detailed guidelines.
