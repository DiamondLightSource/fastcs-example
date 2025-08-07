"""Interface for ``python -m fastcs_example``."""

from fastcs.launch import launch

from . import __version__
from .controllers import TemperatureController

__all__ = ["main"]


def main() -> None:
    launch(TemperatureController, version=__version__)


if __name__ == "__main__":
    main()
