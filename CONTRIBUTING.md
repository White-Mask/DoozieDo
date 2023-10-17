# Contributor Manual

Thank you for considering contributing to this project! Below, we provide information on how to get started.

> **Tip for new contributors:**
> Take a look at [https://github.com/firstcontributions/first-contributions](https://github.com/firstcontributions/first-contributions) for helpful information on contributing

## Quick Guide

### Prerequisites

```shell
python: ">=10"
```

### Setting up your local repo

To clone the repository, follow these steps:

1. Open your terminal or command line.

2. Navigate to the directory where you want to clone the repository.

3. Run the following command:
    >git clone ...

4. Once cloned, navigate to the project directory:
    >cd DoozieDo

5. Create a virtual environment for the project:
    >virtualenv venv --python=python3.10

6. Activate the virtual environment:

   - On Linux or macOS:

     ```
     source venv/bin/activate
     ```

   - On Windows:

     ```
     .\venv\Scripts\activate
     ```

7. Install project dependencies:
    >pip install -r requirements.txt

8. You're ready to go! Your local development environment is set up, and you can start working on the project.

## Code Structure

Our project is organized following a clear structure to keep things organized and maintainable. Below is an overview of the directory structure:

```plaintext
DoozieDo/
    - src/
        - components/
            - task/
                - ...
        - main.py
    - tests/
        - unit/
            - ...
```

## Coding Standards

In this project, we follow the conventions outlined in [PEP 8](https://www.python.org/dev/peps/pep-0008/) for code style. PEP 8 provides guidelines for writing clean, readable Python code, including naming conventions.

Here are some key points to keep in mind:

#### Directory Names 
- Directory names should be in lowercase and use underscores to separate words if necessary, following PEP 8 recommendations. Example: `my_directory`.

#### File Names
- File names should also be in lowercase and use underscores to separate words if necessary, as recommended by PEP 8. Example: `my_file.py`.

## Branches

We use Git as our version control system to manage the development and versions of this project. Our chosen model for branching is the "Feature Branch Workflow," which follows the general principles outlined below:

### `main`
>The `main` branch represents the production-ready codebase. It should always contain stable and deployable code.

### `develop`
>The `develop` branch serves as the integration branch for ongoing development. Features and bug fixes are developed in feature branches and merged into `develop` for testing.

### `feature`
>When working on a new feature or bug fix, contributors create feature branches from `develop`. These branches have descriptive names (e.g., `feature/user-authentication`) and are used for isolated development.

### `release`
>Before releasing a new version, a release branch (e.g., `release/1.0.0`) is created from `develop`. This branch is for final testing and preparations for a release.

## Pull Request Process

- When you submit a pull request, it will be reviewed by the project maintainers.

- Reviewers will assess the code for adherence to coding standards, functionality, and quality.

- Please be responsive to comments and feedback during the review process and make any necessary updates to your code.

- Once your pull request has been approved, it will be merged into the `develop` branch.

- Thank you for your contribution to the project. We hope you have a positive experience contributing with us.
