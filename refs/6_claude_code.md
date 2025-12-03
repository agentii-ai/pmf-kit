

# Step 6.1: Use Claude Code to build constitution.md

```prompt

/constitution this pmf-kit project is a fork of the github.com spec-kit project. read @README_spec-kit.md to get a global view of the original spec-kit and its spec-driven development workflow.

spec-driven development is a strong methodology for complex work with llm-based agents, and the same pattern can be applied to many domains (project management, product design, marketing, business writing, etc.). pmf-kit is a featured variant of spec-kit focused on project management for discovering and validating product-market fit for ai saas products.

i will also use this project as a worked example of how to create your own spec-kit variants (for example, pm-kit, pd-kit, marketing-kit, biz-writing-kit). i will develop comprehensive documents in @refs/ to show, step by step, how to use prompts and search tools to build up-to-date references and adapt the original spec-kit templates.

in the constitution for this project, a few things are especially important:
1. i want to reuse the overall spec-kit design, including installation model, cli commands, and how it integrates with claude code, cursor, and other coding agents.
2. users may install multiple *-kit variants on the same machine, so the base `specify` command name can conflict across packages. you must design a clean naming and namespace strategy so spec-kit, pmf-kit, pd-kit, and other kits can coexist without collisions.
3. related to (2), slash commands like `speckit.plan` and `speckit.implement` are how agents such as claude code invoke workflows. you must ensure there is no conflict between commands like `speckit.plan` and `pmfkit.plan`, and that they can reliably trigger different agents or workflows.

think carefully and globally about the architecture, naming, and multi-kit coexistence first, then draft a clear, opinionated constitution for pmf-kit that respects these constraints and follows the principles in @memory/constitution.md.

```


# Step 6.2: Use Claude Code to build spec.md



```prompt
/specify is running… this pmf-kit project is a fork of the github.com spec-kit project. read @README_spec-kit.md to get a global view of the original spec-kit project and its spec-driven development workflow.

spec-driven development is a strong methodology for complex work with llm-based agents, and the same pattern can be applied to many domains (project management, product design, marketing, business writing, etc.). pmf-kit is a featured variant of spec-kit focused on project management for discovering and validating product-market fit for ai saas products.

read @memory/constitution.md and generate the spec.md for this project. you MUST also read @refs/2_ define_for_specify.md and follow its structure and intent.

there are a few important constraints:
1. re-use the overall spec-kit design, including the cli model and how it integrates with claude code, cursor, and other coding agents.
2. assume users may install multiple *-kit variants on the same machine, so the base `specify` command name can conflict across packages. design a clean naming and namespace strategy so spec-kit, pmf-kit, pd-kit, and other variants can coexist.
3. related to (2), slash commands like `speckit.plan` and `speckit.implement` are how agents invoke workflows. ensure there is no conflict between commands such as `speckit.plan` and `pmfkit.plan`, and that each reliably triggers the correct workflow.

think carefully and globally about architecture, naming, and multi-kit coexistence first, then draft a clear, opinionated spec.md for pmf-kit that is consistent with @memory/constitution.md and suitable as a reference for future *-kit variants.

```



# Step 6.3: Use Claude Code to build plan.md

```prompt

/plan this pmf-kit project is a fork of the github.com spec-kit project. read @README_spec-kit.md to get a global view of the original spec-kit project and its spec-driven development workflow.

spec-driven development is a strong methodology for complex work with llm-based agents, and the same pattern can be applied to many domains (project management, product design, marketing, business writing, etc.). pmf-kit is a featured variant of spec-kit focused on project management for discovering and validating product-market fit for ai saas products.

for this task, read @memory/constitution.md and @specs/001-pmf-kit-variant/spec.md. you MUST also read @refs/3_project_mangement_for_plan.md and follow its structure and intent when generating plan.md.

there are a few important constraints:
1. re-use the overall spec-kit design, including how it is installed, how the cli works, and how it integrates with claude code, cursor, and other coding agents.
2. assume users may install multiple *-kit variants on the same machine, so the base `specify` command name can conflict across packages. design a clean naming and namespace strategy so spec-kit, pmf-kit, pd-kit, and other variants can coexist.
3. related to (2), slash commands like `speckit.plan` and `speckit.implement` are how agents invoke workflows. ensure there is no conflict between commands such as `speckit.plan` and `pmfkit.plan`, and that each reliably triggers the correct workflow.

think carefully and globally about architecture, naming, and multi-kit coexistence first. then generate a clear, opinionated plan.md for pmf-kit that:
- respects the principles in @memory/constitution.md,
- aligns with the spec in @specs/001-pmf-kit-variant/spec.md, and
- can guide edits to the spec-kit templates in @templates/ and @templates/commands/ to swap `speckit` → `pmfkit` **without** changing the underlying infrastructure.

```



# Step 6.4: User Claude Code to build tasks.md


```prompt

/tasks is running… this pmf-kit project is a fork of the github.com spec-kit project. read @README_spec-kit.md to get a global view of the original spec-kit project and its spec-driven development workflow.

spec-driven development is a strong methodology for complex work with llm-based agents, and the same pattern can be applied to many domains (project management, product design, marketing, business writing, etc.). pmf-kit is a featured variant of spec-kit focused on project management for discovering and validating product-market fit for ai saas products.

for this task, read @memory/constitution.md, @specs/001-pmf-kit-variant/spec.md, and @specs/001-pmf-kit-variant/plan.md. you MUST also read @refs/4_pm_tasking_for_tasks.md and follow its structure and intent when generating tasks.md.

there are a few important constraints:
1. re-use the overall spec-kit design, including how it is installed, how the cli works, and how it integrates with claude code, cursor, and other coding agents.
2. assume users may install multiple *-kit variants on the same machine, so the base `specify` command name can conflict across packages. design a clean naming and namespace strategy so spec-kit, pmf-kit, pd-kit, and other variants can coexist.
3. related to (2), slash commands like `speckit.plan` and `speckit.implement` are how agents invoke workflows. ensure there is no conflict between commands such as `speckit.plan` and `pmfkit.plan`, and that each reliably triggers the correct workflow.

think carefully and globally about architecture, naming, and multi-kit coexistence first. then generate a clear, opinionated tasks.md for pmf-kit that:
- respects the principles in @memory/constitution.md,
- aligns with the spec and plan in @specs/001-pmf-kit-variant/, and
- can guide edits to the spec-kit templates in @templates/ and @templates/commands/ to swap `speckit` → `pmfkit` **without** changing the underlying infrastructure. continue writing tasks.md in the current git branch.
```

# Step 6.5: Use Claude Code to implement






# Step 6.6: Upload to github, install from it, and tests



