import pytest

from hr import cli
from sys import path

@pytest.fixture
def parser():
    return cli.create_parser()

def test_parser_without_argument(parser):
    """
    Without a specified argument, the parser will exit
    and an error will raise too
    """
    with pytest.raises(SyntaxError):
        parser.parse_args(None)

def test_parser_with_argument(parser):
    """
    No error is raised if a path is given as an argument.
    """
    args = parser.parse_args(["--export", "path/to/inventory.json"])
    assert args.destination == "path/to/inventory.json"


def test_parser_with_flagvalue(parser):

    """
    The export value is set to True if the --export flag is given
    """
    args = parser.parse_args(["--export", "path/to/inventory.json"])
    assert args.export == True
    """
    The export value is default to False if the --export flag is abscent
    """
    args = parser.parse_args(["path/to/inventory.json"])
    assert args.export == False
