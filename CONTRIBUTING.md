# Contributing

## Before You Start

Every contribution must be tied to an existing issue. If no issue exists for your change, open one first using the appropriate issue template.

## Branch Naming

Branches must follow this pattern:

```
<issue-number>-<short-description>
```

Examples: `12-fix-tts-crash`, `7-add-voice-wake-word`

## Workflow

1. Pick or create an issue
2. Create a branch from `main` using the naming convention above
3. Make your changes
4. Open a pull request  use `Closes #<issue-number>` in the PR body
5. Wait for the PR validation check to pass
6. Request a review

## Commit Messages

Follow conventional commits:

| Prefix | Use for |
|---|---|
| `feat:` | New feature |
| `fix:` | Bug fix |
| `docs:` | Documentation only |
| `refactor:` | Code change with no behavior change |
| `ci:` | CI / workflow changes |
| `chore:` | Maintenance, deps, tooling |

## Code Style

- TypeScript strict mode
- No unused imports or variables
- Run `npm run lint` before pushing
