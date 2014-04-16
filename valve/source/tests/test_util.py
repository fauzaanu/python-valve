# -*- coding: utf-8 -*-
# Copyright (C) 2014 Oliver Ainsworth

from __future__ import (absolute_import,
                        unicode_literals, print_function, division)

import pytest

from .. import util


class TestPlatform(object):

    @pytest.mark.parametrize("identifier", [108, 109, 111, 119])
    def test_valid_numeric_identifer(self, identifier):
        platform = util.Platform(identifier)
        assert platform.value == identifier

    def test_invalid_numeric_identifier(self):
        with pytest.raises(ValueError):
            util.Platform(50)

    @pytest.mark.parametrize(("identifier", "expected"), [
        ("l", 108),
        ("m", 109),
        ("o", 111),
        ("w", 119),
    ])
    def test_valid_character_identifier(self, identifier, expected):
        platform = util.Platform(identifier)
        assert platform.value == expected

    def test_invalid_character_identifier(self):
        with pytest.raises(ValueError):
            util.Platform("a")

    @pytest.mark.parametrize(("identifier", "expected"), [
        ("linux", 108),
        ("Linux", 108),
        ("LINUX", 108),
        ("mac os x", 111),  # Note: not 109
        ("Mac OS X", 111),
        ("MAC OS X", 111),
        ("windows", 119),
        ("Windows", 119),
        ("WINDOWS", 119),
    ])
    def test_valid_string_identifier(self, identifier, expected):
        platform = util.Platform(identifier)
        assert platform.value == expected

    def test_invalid_string_identifier(self):
        with pytest.raises(ValueError):
            util.Platform("raindeer")

    def test_empty_string_identifier(self):
        with pytest.raises(ValueError):
            util.Platform("")

    @pytest.mark.parametrize(("identifier", "string"), [
        (108, "Linux"),
        (109, "Mac OS X"),
        (111, "Mac OS X"),
        (119, "Windows"),
    ])
    def test_to_unicode(self, identifier, string):
        platform = util.Platform(identifier)
        assert unicode(platform) == string

    @pytest.mark.parametrize(("identifier", "string"), [
        (108, b"Linux"),
        (109, b"Mac OS X"),
        (111, b"Mac OS X"),
        (119, b"Windows"),
    ])
    def test_to_bytestring(self, identifier, string):
        platform = util.Platform(identifier)
        assert bytes(platform) == string

    @pytest.mark.parametrize("identifier", [108, 109, 111, 119])
    def test_to_integer(self, identifier):
        platform = util.Platform(identifier)
        assert int(platform) == identifier

    @pytest.mark.parametrize(("identifier", "os_name"), [
        (108, "posix"),
        (109, "posix"),
        (111, "posix"),
        (119, "nt"),
    ])
    def test_os_name(self, identifier, os_name):
        platform = util.Platform(identifier)
        assert platform.os_name == os_name

    @pytest.mark.parametrize(("platform", "other"), [
        (util.Platform(108), util.Platform(108)),
        (util.Platform(109), util.Platform(109)),
        (util.Platform(111), util.Platform(111)),
        (util.Platform(109), util.Platform(111)),  # Special Mac case
        (util.Platform(111), util.Platform(109)),  # Special Mac case
        (util.Platform(119), util.Platform(119)),
    ])
    def test_equality(self, platform, other):
        assert platform == other

    @pytest.mark.parametrize(("platform", "other"), [
        (util.Platform(108), 108),
        (util.Platform(109), 109),
        (util.Platform(111), 111),
        (util.Platform(109), 111),  # Special Mac case
        (util.Platform(111), 109),  # Special Mac case
        (util.Platform(119), 119),
    ])
    def test_equality_integer(self, platform, other):
        assert platform == other

    @pytest.mark.parametrize(("platform", "other"), [
        (util.Platform(108), "l"),
        (util.Platform(109), "m"),
        (util.Platform(111), "o"),
        (util.Platform(109), "o"),  # Special Mac case
        (util.Platform(111), "m"),  # Special Mac case
        (util.Platform(119), "w"),
    ])
    def test_equality_character(self, platform, other):
        assert platform == other

    @pytest.mark.parametrize(("platform", "other"), [
        (util.Platform(108), "Linux"),
        (util.Platform(109), "Mac OS X"),
        (util.Platform(111), "Mac OS X"),
        (util.Platform(119), "Windows"),
    ])
    def test_equality_string(self, platform, other):
        assert platform == other
