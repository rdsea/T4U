#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CAVEAT UTILITOR
#
# This file was automatically generated by Grako.
#
#    https://pypi.python.org/pypi/grako/
#
# Any changes you make to it will be overwritten the next time
# the file is generated.


from __future__ import print_function, division, absolute_import, unicode_literals

from grako.parsing import graken, Parser
from grako.util import re, RE_FLAGS


__version__ = (2016, 4, 29, 9, 5, 23, 4)

__all__ = [
    'TestDescriptionGrammarParser',
    'TestDescriptionGrammarSemantics',
    'main'
]


class TestDescriptionGrammarParser(Parser):
    def __init__(self,
                 whitespace=None,
                 nameguard=None,
                 comments_re=None,
                 eol_comments_re=None,
                 ignorecase=None,
                 left_recursion=True,
                 **kwargs):
        super(TestDescriptionGrammarParser, self).__init__(
            whitespace=whitespace,
            nameguard=nameguard,
            comments_re=comments_re,
            eol_comments_re=eol_comments_re,
            ignorecase=ignorecase,
            left_recursion=left_recursion,
            **kwargs
        )

    @graken()
    def _grammar_(self):
        self._PropertiesDescriptionExpression_()
        self._TriggeredByExpression_()
        self._ExecutionInfoExpression_()

    @graken()
    def _ExecutionInfoExpression_(self):
        self._token('Execution')

        def block0():
            self._executorExpression_()
            self.ast['@'] = self.last_node
        self._positive_closure(block0)

    @graken()
    def _TriggeredByExpression_(self):
        self._token('Triggers')

        def block0():
            with self._choice():
                with self._option():
                    self._PeriodExpression_()
                    self.ast['@'] = self.last_node
                with self._option():
                    self._EventExpression_()
                    self.ast['@'] = self.last_node
                self._error('no available options')
        self._positive_closure(block0)

    @graken()
    def _EventExpression_(self):
        self._token('event')
        self._token(':')

        def block0():
            self._eventOnExpression_()
            self.ast['@'] = self.last_node
        self._positive_closure(block0)

    @graken()
    def _PeriodExpression_(self):
        self._token('every')
        self._token(':')
        self._int_()
        self.ast['@'] = self.last_node
        self._timeUnit_()
        self.ast['@'] = self.last_node

    @graken()
    def _executorExpression_(self):
        self._token('executor')
        self._token(':')
        with self._optional():
            self._token('distinct')
        self.ast.setlist('@', self.last_node)
        self._unit_identifier_()
        self.ast.setlist('@', self.last_node)
        self._token('for')
        self._unit_identifier_expr_()
        self.ast['@'] = self.last_node

    @graken()
    def _timeUnit_(self):
        with self._choice():
            with self._option():
                self._token('s')
            with self._option():
                self._token('m')
            with self._option():
                self._token('h')
            with self._option():
                self._token('d')
            self._error('expecting one of: d h m s')

    @graken()
    def _eventOnExpression_(self):
        self._literalExpr_()
        self.ast.setlist('@', self.last_node)
        self._token('on')
        self._unit_identifier_expr_()
        self.ast.setlist('@', self.last_node)

    @graken()
    def _VerifyExpression_(self):
        self._token('verifies')
        self._token(':')
        self._unit_identifier_expr_()
        self.ast['@'] = self.last_node

    @graken()
    def _PropertiesDescriptionExpression_(self):
        self._token('Description')
        self._name_()
        self._description_()
        self._timeout_()

    @graken()
    def _path_(self):
        self._token('path')
        self.ast['@'] = self.last_node
        self._token(':')
        self._token('"')
        self._pattern(r'[A-Za-z0-9_\-\/:.]*')
        self.ast['@'] = self.last_node
        self._token('"')

    @graken()
    def _name_(self):
        self._token('name')
        self.ast['@'] = self.last_node
        self._token(':')
        self._string_()
        self.ast['@'] = self.last_node

    @graken()
    def _description_(self):
        self._token('description')
        self._token(':')
        self._token('"')
        self._pattern(r'[A-Za-z0-9_\-\/:. ]*')
        self.ast['@'] = self.last_node
        self._token('"')

    @graken()
    def _literalExpr_(self):
        self._literal_()
        self.ast.setlist('@', self.last_node)

        def block1():
            self._token(',')
            self._literal_()
            self.ast.setlist('@', self.last_node)
        self._closure(block1)

    @graken()
    def _timeout_(self):
        self._token('timeout')
        self.ast['@'] = self.last_node
        self._token(':')
        self._int_()
        self.ast['@'] = self.last_node

    @graken()
    def _literal_(self):
        with self._choice():
            with self._option():
                self._string_()
            with self._option():
                self._int_()
            self._error('no available options')

    @graken()
    def _unit_identifier_expr_(self):
        self._unit_identifier_()
        self.ast.setlist('@', self.last_node)

        def block1():
            self._token(',')
            self._unit_identifier_()
            self.ast.setlist('@', self.last_node)
        self._closure(block1)

    @graken()
    def _unit_identifier_(self):
        with self._choice():
            with self._option():
                with self._group():
                    self._token('UnitType')
                    self.ast['@'] = self.last_node
                    self._token('.')
                    self._level_()
                    self.ast['@'] = self.last_node
            with self._option():
                with self._group():
                    with self._group():
                        with self._choice():
                            with self._option():
                                self._token('UnitID')
                                self.ast['@'] = self.last_node
                            with self._option():
                                self._token('UnitUUID')
                                self.ast['@'] = self.last_node
                            self._error('expecting one of: UnitID UnitUUID')
                    self._token('.')
                    with self._group():
                        with self._choice():
                            with self._option():
                                self._string_()
                                self.ast['@'] = self.last_node
                            with self._option():
                                self._int_()
                                self.ast['@'] = self.last_node
                            self._error('no available options')
            self._error('no available options')

    @graken()
    def _level_(self):
        with self._choice():
            with self._option():
                self._token('Service')
            with self._option():
                self._token('Process')
            with self._option():
                self._token('SoftwarePlatform')
            with self._option():
                self._token('PhysicalDevice')
            with self._option():
                self._token('SoftwareContainer')
            with self._option():
                self._token('VirtualContainer')
            with self._option():
                self._token('Gateway')
            with self._option():
                self._token('VirtualMachine')
            with self._option():
                self._token('PhysicalMachine')
            self._error('expecting one of: Gateway PhysicalDevice PhysicalMachine Process Service SoftwareContainer SoftwarePlatform VirtualContainer VirtualMachine')

    @graken()
    def _lower_name_(self):
        self._pattern(r'[a-z][A-Za-z0-9_]*')

    @graken()
    def _upper_name_(self):
        self._pattern(r'[A-Z][A-Za-z0-9_]*')

    @graken()
    def _char_(self):
        self._string_()

    @graken()
    def _string_(self):
        self._STRING_()

    @graken()
    def _STRING_(self):
        with self._choice():
            with self._option():
                self._token('"')
                self._pattern(r'[A-Za-z0-9_.-]*')
                self.ast['@'] = self.last_node
                self._token('"')
            with self._option():
                self._token("'")
                self._pattern(r'\w+')
                self.ast['@'] = self.last_node
                self._token("'")
            self._error('expecting one of: " \'')

    @graken()
    def _LITERAL_(self):
        self._pattern(r'(?:\\.|[^|*\\()])+')

    @graken()
    def _int_(self):
        self._pattern(r'[0-9]+')

    @graken()
    def _ESC_(self):
        with self._choice():
            with self._option():
                self._pattern(r'\\[\'"\\nrtbfv]')
            with self._option():
                self._pattern(r'\\u[a-fA-F0-9]{4}')
            self._error('expecting one of: \\\\[\'"\\\\nrtbfv] \\\\u[a-fA-F0-9]{4}')


class TestDescriptionGrammarSemantics(object):
    def grammar(self, ast):
        return ast

    def ExecutionInfoExpression(self, ast):
        return ast

    def TriggeredByExpression(self, ast):
        return ast

    def EventExpression(self, ast):
        return ast

    def PeriodExpression(self, ast):
        return ast

    def executorExpression(self, ast):
        return ast

    def timeUnit(self, ast):
        return ast

    def eventOnExpression(self, ast):
        return ast

    def VerifyExpression(self, ast):
        return ast

    def PropertiesDescriptionExpression(self, ast):
        return ast

    def path(self, ast):
        return ast

    def name(self, ast):
        return ast

    def description(self, ast):
        return ast

    def literalExpr(self, ast):
        return ast

    def timeout(self, ast):
        return ast

    def literal(self, ast):
        return ast

    def unit_identifier_expr(self, ast):
        return ast

    def unit_identifier(self, ast):
        return ast

    def level(self, ast):
        return ast

    def lower_name(self, ast):
        return ast

    def upper_name(self, ast):
        return ast

    def char(self, ast):
        return ast

    def string(self, ast):
        return ast

    def STRING(self, ast):
        return ast

    def LITERAL(self, ast):
        return ast

    def int(self, ast):
        return ast

    def ESC(self, ast):
        return ast


def main(filename, startrule, trace=False, whitespace=None, nameguard=None):
    import json
    with open(filename) as f:
        text = f.read()
    parser = TestDescriptionGrammarParser(parseinfo=False)
    ast = parser.parse(
        text,
        startrule,
        filename=filename,
        trace=trace,
        whitespace=whitespace,
        nameguard=nameguard)
    print('AST:')
    print(ast)
    print()
    print('JSON:')
    print(json.dumps(ast, indent=2))
    print()

if __name__ == '__main__':
    import argparse
    import string
    import sys

    class ListRules(argparse.Action):
        def __call__(self, parser, namespace, values, option_string):
            print('Rules:')
            for r in TestDescriptionGrammarParser.rule_list():
                print(r)
            print()
            sys.exit(0)

    parser = argparse.ArgumentParser(description="Simple parser for TestDescriptionGrammar.")
    parser.add_argument('-l', '--list', action=ListRules, nargs=0,
                        help="list all rules and exit")
    parser.add_argument('-n', '--no-nameguard', action='store_true',
                        dest='no_nameguard',
                        help="disable the 'nameguard' feature")
    parser.add_argument('-t', '--trace', action='store_true',
                        help="output trace information")
    parser.add_argument('-w', '--whitespace', type=str, default=string.whitespace,
                        help="whitespace specification")
    parser.add_argument('file', metavar="FILE", help="the input file to parse")
    parser.add_argument('startrule', metavar="STARTRULE",
                        help="the start rule for parsing")
    args = parser.parse_args()

    main(
        args.file,
        args.startrule,
        trace=args.trace,
        whitespace=args.whitespace,
        nameguard=not args.no_nameguard
    )
