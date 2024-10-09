# gha-composite-actions-experiments

Example of how to setup a "composite action" to allow re-using a yaml-format workflow
from within the same repo.

## Contents
- `.github/workflows/example.yml`: The workflow, which calls the composite action
- `.github/actions/setup/action.yml`: The composite action

## Notes
- Docs for the yaml actions format, of which composite actions are a subset (so be careful you're not reading e.g. Docker-related docs) are at https://docs.github.com/en/actions/sharing-automations/creating-actions/metadata-syntax-for-github-actions#runs-for-composite-actions.
- Composite action files have to be called `action.y{,a}ml` so have to use a directory to disambiguate.
- The default checkout option will check them out.
- Because composite workflows don't specify a runner, you have to explicitly set `shell:` for `run:` steps.
- You can't set `env:` at the top-level of a composite action. So the best you can do is define/use an input with a default value, or a workaround like [this](https://github.com/orgs/community/discussions/51280#discussioncomment-8726096).
- The stuff in https://github.com/orgs/community/discussions/11771 doesn't appear to be necessary.
  From experiments I can see that the composite action I'm using DOES come from the current branch (well, presumably merge candidate), once I've done a checkout action. So maybe it was just they didn't want to do/repeat a checkout ... I don't think this is a concern for our use-case.

