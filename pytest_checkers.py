"""
Additional Pylint checkers for pytest.
"""
import os
import sys

import pytest


from pylint.checkers.variables import VariablesChecker
from pylint_plugin_utils import get_checker, suppress_message


class FixtureCollector(object):
    fixtures = None

    def pytest_sessionfinish(self, session):
        session.perform_collect()

        fm = session._fixturemanager

        self.fixtures = set(fm._arg2fixturedefs.keys())


def register(linter):
    sys.path.insert(0, '.')

    old_out = sys.stdout
    old_err = sys.stderr
    sys.stdout = open(os.devnull, 'w')
    sys.stderr = open(os.devnull, 'w')

    fixture_collector = FixtureCollector()

    pytest.main(['--fixtures'], plugins=[fixture_collector])
    sys.stdout = old_out
    sys.stderr = old_err

    def attr_in_fixtures_list(node, fixtures=fixture_collector.fixtures):
        """
        Checks that node is get or post method of the View class and it has valid arguments.
        """
        """Checks that node is get or post method of the View class."""
        funcs = [k for k, v in node.items() if k in fixtures]
        if funcs:
            return True

        return False

    suppress_message(linter, VariablesChecker.visit_functiondef, 'W0621', attr_in_fixtures_list)


