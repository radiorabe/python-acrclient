# Python ACR Client module

Contains a simple client for calling the v2 endpoints of the [ACRCloud](https://www.acrcloud.com) API.

## Installation

```bash
poetry add acrclient

# or on old setup style projects
pip -m install acrclient
```

## Usage

```python
>>> from acrclient import Client
>>> client = Client(bearer_token="bearer-token")

```

## Development

```bash
# setup a dev env
python -mvenv env
. env/bin/activate

# install a modern poetry version
python -mpip install poetry>=1.2.0

# install deps and dev version
poetry install

# make changes, run tests
poetry run pytest
```

## Release Management

The CI/CD setup uses semantic commit messages following the [conventional commits standard](https://www.conventionalcommits.org/en/v1.0.0/).
There is a GitHub Action in [.github/workflows/semantic-release.yaml](./.github/workflows/semantic-release.yaml)
that uses [go-semantic-commit](https://go-semantic-release.xyz/) to create new
releases.

The commit message should be structured as follows:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

The commit contains the following structural elements, to communicate intent to the consumers of your library:

1. **fix:** a commit of the type `fix` patches gets released with a PATCH version bump
1. **feat:** a commit of the type `feat` gets released as a MINOR version bump
1. **BREAKING CHANGE:** a commit that has a footer `BREAKING CHANGE:` gets released as a MAJOR version bump
1. types other than `fix:` and `feat:` are allowed and don't trigger a release

If a commit does not contain a conventional commit style message you can fix
it during the squash and merge operation on the PR.

Once a commit has landed on the `main` branch a release will be created and automatically published to [pypi](https://pypi.org/)
using the GitHub Action in [.github/workflows/release.yaml](./.github/workflows/release.yaml) which uses [poetry](https://python-poetry.org/)
to publish the package to pypi.

## License

This package is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, version 3 of the License.

## Copyright

Copyright (c) 2023 [Radio Bern RaBe](http://www.rabe.ch)
