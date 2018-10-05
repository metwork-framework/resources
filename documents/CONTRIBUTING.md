# Contributing guide

## Commit Message Guidelines

Inspired by Angular project and [https://www.conventionalcommits.org](conventional commits initiative), 
we have very precise rules over how our git commit messages can be formatted. This leads to more readable messages that are 
easy to follow when looking through the project history. But also, we use the git commit messages to generate the project 
changelog.

So we follow the [https://www.conventionalcommits.org](conventional commits initiative) specification.

### Summary (see above specification for more details)

Each commit message consists of a `header`, a `body` and a `footer`. The `header` has a special format that includes a `type`, 
a `scope` and a `description`. The commit message should be structured as follows:

```
<type>[optional scope]: <description>
<BLANK LINE>
[optional body]
<BLANK LINE>
[optional footer]
```

The commit message contains the following structural elements, to communicate intent to the consumers of the project:

 - `fix`: a commit of the type fix patches a bug in your codebase (this correlates with `PATCH` in semantic versioning).
 - `feat`: a commit of the type feat introduces a new feature to the codebase (this correlates with `MINOR` in semantic versioning).
 - `BREAKING CHANGE`: a commit that has the text `BREAKING CHANGE:` at the beginning of its optional body or footer section 
    introduces a breaking API change (correlating with `MAJOR` in semantic versioning). 
    A breaking change can be part of commits of any type. e.g., a `fix:`, `feat:` & `chore:` types would all be valid, 
    in addition to any other type.
    Others: commit types other than fix: and feat: are allowed, for example commitlint-config-conventional (based on the the Angular convention) recommends chore:, docs:, style:, refactor:, perf:, test:, and others. We also recommend improvement for commits that improve a current implementation without adding a new feature or fixing a bug. Notice these types are not mandated by the conventional commits specification, and have no implicit effect in semantic versioning (unless they include a BREAKING CHANGE, which is NOT recommended).
    A scope may be provided to a commit’s type, to provide additional contextual information and is contained within parenthesis, e.g., feat(parser): add ability to parse arrays.

### Examples

#### Commit message with description and breaking change in body

```
feat: allow provided config object to extend other configs

BREAKING CHANGE: `extends` key in config file is now used for extending other config files
```

#### Commit message with no body

```
docs: correct spelling of CHANGELOG
```

#### Commit message with scope

```
feat(lang): added polish language
```

#### Commit message for a fix using an (optional) issue number.

```
fix: minor typos in code

see the issue for details on the typos fixed

fixes issue #12
```

### Revert

If the commit reverts a previous commit, it should begin with `revert:`, followed by the header of the reverted commit. 
In the body it should say: `This reverts commit <hash>.`, where the `hash` is the SHA of the commit being reverted.

### Type

Must be one of the following:

- `build`: Changes that affect the build or CI system (`chore` is also accepted for compatibility)
- `docs`: Documentation only changes
- `feat`: A new feature
- `fix`: A bug fix
- `perf`: A code change that improves performance
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `style`: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
- `test`: Adding missing tests or correcting existing tests

### Scope

The scope is not used for the moment. Please don't use scopes in commit messages.

### Description

The description contains a succinct description of the change:

```
    use the imperative, present tense: "change" not "changed" nor "changes"
    don't capitalize the first letter
    no dot (.) at the end
```

### Body

Just as in the subject, use the imperative, present tense: "change" not "changed" nor "changes". The body should include 
the motivation for the change and contrast this with previous behavior.

### Footer

The footer should contain any information about `Breaking Changes` and is also the place to reference GitHub issues 
that this commit Closes.

`Breaking Changes` should start with the word `BREAKING CHANGE:` with a space or two newlines. The rest of the commit 
message is then used for this.
