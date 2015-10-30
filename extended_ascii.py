#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Exports anything passed in as ISRI Extended ASCII, which is a Latin-1 based
encoding which allows for Unicode BMP escapes. Astral code points are
impossible to express in this scheme, lest one wishes to restort to surrogate
pairs (yuck!).
"""

import os
import sys
import fileinput
import codecs

# Set of ASCII and Latin-1 characters.
PRINTABLE  = set(unichr(codepoint) for codepoint in range(0x20, 0x7F))
PRINTABLE |= set(unichr(codepoint) for codepoint in range(0xA1, 0x100))

def to_extended_ascii(character):
    r"""
    >>> print(to_extended_ascii('A'))
    A
    >>> len(to_extended_ascii('Ä'))
    1
    >>> print(to_extended_ascii('Ω'))
    <03A9>
    >>> print(to_extended_ascii('א'))
    <05D0>
    >>> print(to_extended_ascii('\n'))
    <\n>
    >>> to_extended_ascii('🎎')
    Traceback (most recent call last):
    ...
    ValueError: Cannot encode astral code point
    """

    if not isinstance(character, unicode):
        character = unicode(character, 'UTF-8')
    if len(character.encode('UTF-32LE')) != 4:
        raise ValueError('Must be exactly one BMP code point')

    try:
        codepoint = ord(character)
    except TypeError:
        raise ValueError('Cannot encode astral code point')

    if character == '\n':
        # Newlines are given a special escape.
        return ur'<\n>'
    elif codepoint >= 0x100:
        # Use <xxxx> for UCS-2.
        return u'<%04X>' % (codepoint,)
    elif character in PRINTABLE:
        # Any printable Latin-1 character is returned verbatim.
        return character
    else:
        assert codepoint < 0x100
        # Use <xx> for control characters.
        return u'<%02X>' % (codepoint,)

def main():
    # Open stdout in binary mode. Let's write some raw bytes!
    stdout = os.fdopen(sys.stdout.fileno(), 'wb')
    sys.stdout.close()

    # For every unicode character in the input...
    for line in fileinput.input():
        for char in unicode(line, 'UTF-8'):
            # Convert it to extended ASCII
            byte_string = to_extended_ascii(char).encode('latin-1')
            stdout.write(byte_string)

if __name__ == '__main__':
    main()
