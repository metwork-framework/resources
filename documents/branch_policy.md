# branch management (if integration_level >= 4)

## Github branch protection rules

### integration

- enforce_admins = True
- required_pull_request_reviews = False
- required_status_checks = "pr ready to merge" (strict = True)

### master

- enforce_admins = True
- required_pull_request_reviews = False
- required_status_checks = "no pullrequest on master" (strict = True)

### Why not enforcing no pullrequest on master at github branch protection level ?

Because we want :

- to be able to auto-accept pull-requests of `metworkbot` user
- to be able to force an urgent pull-request merge with label `Merge Now` (without explicit review)

