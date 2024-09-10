# CourseConstrainSolver
A constrain solver for course planning

## Development

Best practice for development is to create a new branch for whatever you're working on (titled `[your name]/[what you're working on]`, and then make a PR when it's done.
```
git checkout -b [BRANCH NAME]
```

Example:
```
git checkout -b ali/test-cases
```

We should strive to have PRs reviewed by one other member on the team before they are ready to be merged into main.

## Testing
Before running tests, you need to set the `PYTHONPATH` to include the `src/` directory. This will allow Python to locate the modules in `src/` when importing to run tests in `test/`.

### Linux/macOS
Run the following command in the terminal from the root of the repository:

source ./test_setup.sh

### Windows
Run the following command in the terminal from the root of the repository:

test_setup.bat

## Prerequisites

Click [here](https://github.com/ChapSpace/CourseConstrainSolver/blob/main/GettingStarted.md) to get started with developing.
