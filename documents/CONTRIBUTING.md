# Contributing guide

## Branching model

### The `integration` branch

Because building and testing whole metwork-framework is a long and difficult task, we use a specific branch `integration` to
merge pull-requests. Every change is made by a pull-request on this branch and every change must be reviewed by a team member
to be accepted.

We use a [https://mergify.io/](mergify bot) to merge pull-requests, so merging rules are clear and described in the `.mergify.yml` file in the repository.

### The `master` branch

Nobody (including administrators) can't commit to the `master` branch. So pull-requests are not accepted in the `master` branch. The only way to commit code in this branch is to pass through the `integration` branch.

When the whole framework is "stable", a team member will copy the `integration` branch on the `master` branch with a specific non-interactive script (we are thinking of a way to automatize this).

So the `master` branch is always "behind" the `integration` branch. But only for a few hours or (at worse) days.

### Released branches

FIXME

### Which branch do i use ?

FIXME

## Version numbering 

We follow the [https://semver.org/](semantic versionning specification). 

### Summary (see above specification for more details)

Given a version number `MAJOR.MINOR.PATCH`, we increment the:

- `MAJOR` version when we make incompatible API changes,
- `MINOR` version when we add functionality in a backwards-compatible manner, and
- `PATCH` version when we make backwards-compatible bug fixes.

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
