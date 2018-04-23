import pytest

from hr import cli

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
    args = parser.parse_args("path/to/inventory.json")
    assert args.destination == "path/to/inventory.json"
    
