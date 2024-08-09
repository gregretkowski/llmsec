''' noxfile for testing via github actions '''
# this file is *not* meant to cover or endorse the use of nox or pytest or
# testing in general,
#
#  It's meant to show the use of:
#
#  - check-manifest
#     confirm items checked into vcs are in your sdist
#  - readme_renderer (when using a reStructuredText README)
#     confirms your long_description will render correctly on PyPI.
#
#  and also to help confirm pull requests to this project.

import os

import nox

nox.options.sessions = ["lint"]

# Define the minimal nox version required to run
nox.options.needs_version = ">= 2024.3.2"


@nox.session
def lint(session):
    ''' lint code'''
    session.install("-r", "requirements.txt")
    #session.install("pylint")
    session.run(
        "pylint", "tests", "llmsec"
    )


@nox.session
def build_and_check_dists(session):
    ''' build dists '''
    session.install("build", "check-manifest >= 0.42", "twine")
    # If your project uses README.rst, uncomment the following:
    # session.install("readme_renderer")

    session.run("check-manifest", "--ignore",
                "noxfile.py,.vscode/settings.json,requirements.txt,tests/**")
    session.run("python", "-m", "build")
    session.run("python", "-m", "twine", "check", "dist/*")


@nox.session(python=["3.8", "3.9", "3.10", "3.11", "3.12"])
def tests(session):
    ''' tests '''
    #session.install("pytest")
    session.install("-r", "requirements.txt")
    build_and_check_dists(session)

    generated_files = os.listdir("dist/")
    generated_sdist = os.path.join("dist/", generated_files[1])

    session.install(generated_sdist)

    session.run("py.test", "tests/", *session.posargs)
