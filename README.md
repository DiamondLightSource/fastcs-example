[![CI](https://github.com/DiamondLightSource/fastcs-example/actions/workflows/ci.yml/badge.svg)](https://github.com/DiamondLightSource/fastcs-example/actions/workflows/ci.yml)
[![Coverage](https://codecov.io/gh/DiamondLightSource/fastcs-example/branch/main/graph/badge.svg)](https://codecov.io/gh/DiamondLightSource/fastcs-example)
[![PyPI](https://img.shields.io/pypi/v/fastcs-example.svg)](https://pypi.org/project/fastcs-example)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)

# fastcs_example

An example simulation IOC for testing fastCS


Source          | <https://github.com/DiamondLightSource/fastcs-example>
:---:           | :---:
PyPI            | `pip install fastcs-example[demo]`
Docker          | `docker run ghcr.io/diamondlightsource/fastcs-example:latest`
Releases        | <https://github.com/DiamondLightSource/fastcs-example/releases>

# Usage

Start the simulation temperature controller by running the following command:

```bash
tickit all src/fastcs_example/simulation/temp_controller.yaml
```

Start the fastCS IOC by running the following command:

```bash
fastcs-example run src/fastcs_example/controller.yaml
```
