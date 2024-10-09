# gha-composite-actions-experiments

Example of how to setup a "composite action" to allow re-using a yaml-format workflow
from within the same repo.

## Contents
- `.github/workflows/example.yml`: The workflow, which calls the composite action
- `.github/actions/setup/action.yml`: The composite action

## Notes
- Composite action files have to be called `action.y{,a}ml` so have to use a directory to disambiguate.
- The default checkout option will check them out.
- Because composite workflows don't specify a runner, you have to explicitly set `shell:` for `run:` steps.
- The stuff in https://github.com/orgs/community/discussions/11771 doesn't appear to be necessary.
  From experiments I can see that the composite action I'm using DOES come from the current branch (well, presumably merge candidate), once I've done a checkout action. So maybe it was just they didn't want to do/repeat a checkout ... I don't think this is a concern for our use-case.

