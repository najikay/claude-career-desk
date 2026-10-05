# Career Desk: tests

This branch holds only the tests for [Career Desk](https://github.com/najikay/claude-career-desk). They are kept off `main` so that the published plugin contains instructions and no code.

The workflow on `main` checks this branch out next to the plugin and runs:

```
PLUGIN_ROOT=<checkout of main> python -m unittest discover -s tests -v
```
