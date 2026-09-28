# Release Notes

* **ENHANCEMENT**: `publish.yml` now runs on every push to `main`: when the version in `__version__.py` has no GitHub release, it tags the commit, builds from the tag, publishes to PyPI and creates the GitHub release; a failed release resumes from the existing tag via a manual run.
* **DOCS**: `CHANGES.md` release headings now use the `## vX.Y.Z - Month D, YYYY` form that `publish.yml` reads.
* **FIXED**: `test.yml` never ran because it triggered on a non-existent `tests` event; it now installs the package and runs pytest on pull requests to `main` and `develop` and on pushes to `develop`.

## v0.2.2 - May 21, 2026

* **FIXED**: fixing readline import for windows

## v0.2.1 - May 12, 2026

* **REFACTOR**: triggering github publishing

## v0.2.0 - May 12, 2026

* **FEATURE**: adding github publishing
