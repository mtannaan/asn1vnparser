#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `asn1vnparser` package."""


import json
import pathlib
import sys
import test.support
import unittest

import asn1vnparser
from asn1vnparser import cli


class TestAsn1vnparser(unittest.TestCase):
    """Tests for `asn1vnparser` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_json(self):
        """Test conversion to JSON representations."""

        cases_dir = pathlib.Path(__file__).parent / 'cases'

        asn_strs = {
            asn_path.stem: asn_path.read_text()
            for asn_path in cases_dir.glob('*.asn')
        }
        json_strs = {
            json_path.stem: json_path.read_text()
            for json_path in cases_dir.glob('*.json')
        }

        assert set(asn_strs.keys()) == set(json_strs.keys())
        assert len(asn_strs) > 0

        for key in asn_strs:
            with self.subTest(key=key):
                res_json = asn1vnparser.parse_asn1_value_assignment(
                    asn_strs[key], as_json=True)
                res_py = json.loads(res_json)
                self.maxDiff = None
                self.assertEqual(res_py, json.loads(json_strs[key]))

    def test_command_line_interface(self):
        """Test the CLI."""

        with self.subTest('parsing value assignment into python obj dump'):
            with test.support.captured_stdout() as stdout, \
                    test.support.captured_stdin() as stdin:
                stdin.write(r'value-1 Type-1 ::= {f1 v1, f2 a2 : 2}')
                stdin.seek(0)
                cli.main([])
                self.assertEqual(
                    stdout.getvalue(),
                    "{'value_name': 'value-1', 'type_name': 'Type-1', " +
                    "'value': {'f1': 'v1', 'f2': {'a2': 2}}}\n"
                )

        with self.subTest('parsing value assignment into JSON'):
            with test.support.captured_stdout() as stdout, \
                    test.support.captured_stdin() as stdin:
                stdin.write(r'value-1 Type-1 ::= {a1 : enum1, a2 : 2}')
                stdin.seek(0)
                cli.main(["-j"])
                self.assertEqual(
                    stdout.getvalue(),
                    '{"value_name": "value-1", "type_name": "Type-1", "value": [{"a1": "enum1"}, {"a2": 2}]}\n'
                )
