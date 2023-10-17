# DoozieDo

DoozieDo is a Command-Line Task and Project Manager

## Project Structure

Our project is organized following a clear structure to keep things organized and maintainable. Below is an overview of the directory structure:

```plaintext
dooziedo/
    - src/
        - components/
            - task/
                - ...
        - app.py
    - tests/
        - unit/
            - ...
```

## File and Directory Naming Convention

In this project, we follow the conventions outlined in [PEP 8](https://www.python.org/dev/peps/pep-0008/) for code style. PEP 8 provides guidelines for writing clean, readable Python code, including naming conventions.

Here are some key points to keep in mind:

- **Directory Names**: Directory names should be in lowercase and use underscores to separate words if necessary, following PEP 8 recommendations. Example: `my_directory`.

- **File Names**: File names should also be in lowercase and use underscores to separate words if necessary, as recommended by PEP 8. Example: `my_file.py`.


## Version Control

We use Git as our version control system to manage the development and versions of this project. Our chosen model for branching is the "Feature Branch Workflow," which follows the general principles outlined below:

- **Main Branch**: The `main` branch represents the production-ready codebase. It should always contain stable and deployable code.

- **Develop Branch**: The `develop` branch serves as the integration branch for ongoing development. Features and bug fixes are developed in feature branches and merged into `develop` for testing.

- **Feature Branches**: When working on a new feature or bug fix, contributors create feature branches from `develop`. These branches have descriptive names (e.g., `feature/user-authentication`) and are used for isolated development.

- **Release Branches**: Before releasing a new version, a release branch (e.g., `release/1.0.0`) is created from `develop`. This branch is for final testing and preparations for a release.

By following this branching strategy, we aim to keep our codebase organized.

For detailed instructions on using Git and our branching model, please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file.
