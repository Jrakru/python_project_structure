# Claude Skills for Company Workflows

This directory contains Claude skills that codify company standards, workflows, and best practices. Skills help AI agents understand and apply consistent patterns across all projects.

## Available Skills

### `python-project-setup`

**Purpose**: Scaffold new Python projects with internal/public content separation

**Use when**:
- Starting a new Python project
- Converting existing project to company standards
- Setting up dual-repository workflow (private + public mirror)

**Key features**:
- Internal vs public content separation using `_internal/` directory
- Company policy compliance (no AI artifacts in public repos)
- Tiered context system for AI agent efficiency
- Complete starter pack with all templates
- Public repository mirroring support

**Usage**:
```
Tell Claude: "Use the python-project-setup skill to help me create a new Python project"
```

## Adding More Skills

As your company develops more standardized workflows, add them here:

### Planned Skills

- **`project-management`** - Company PM workflows and artifact management
- **`code-review`** - Code review standards and checklists
- **`deployment`** - Deployment workflows and procedures
- **`documentation`** - Documentation standards and templates
- **`testing`** - Testing strategies and best practices

### Creating a New Skill

1. Create directory: `.claude/skills/skill-name/`
2. Create `skill.md` with:
   - Clear purpose statement
   - When to use the skill
   - Step-by-step workflows
   - Examples and templates
   - Company-specific policies
   - References to relevant docs
3. Update this README

## Skill Philosophy

**Skills should be**:
- **Specific** - Focused on one clear workflow or domain
- **Actionable** - Provide concrete steps, not just theory
- **Current** - Updated as company practices evolve
- **Policy-aware** - Encode company policies and compliance requirements
- **Example-rich** - Include templates, examples, and references

**Skills should NOT**:
- Duplicate general knowledge Claude already has
- Be overly abstract or theoretical
- Contain sensitive credentials or secrets
- Override safety guidelines

## Benefits

1. **Consistency** - All projects follow same standards
2. **Onboarding** - New team members (human or AI) get up to speed faster
3. **Quality** - Codified best practices reduce errors
4. **Compliance** - Company policies automatically enforced
5. **Efficiency** - Less explaining, more doing

## Usage Tips

- Reference skills explicitly: "Use the python-project-setup skill"
- Skills work best with clear, specific requests
- Review skill output to ensure it matches your needs
- Update skills as your practices evolve
- Share successful patterns by adding new skills

## Maintenance

- **Review frequency**: Quarterly or when practices change
- **Owner**: Engineering team
- **Updates**: Create PR with skill changes, get team review
- **Versioning**: Track version in skill.md file

---

**Last Updated**: 2025-11-05
**Maintained By**: Company Engineering Team
