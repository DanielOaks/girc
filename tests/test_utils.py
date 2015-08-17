#!/usr/bin/env python3
# Written by Daniel Oaks <daniel@danieloaks.net>
# Released under the ISC license
import unittest

import base
from girc import utils


class UtilsTestCase(unittest.TestCase):
    """Tests our utils."""

    def setUp(self):
        errmsg = 'utils.{} does not exist!'
        self.assertTrue(utils.NickMask, msg=errmsg.format('NickMask'))

    def test_nickmask(self):
        nm = utils.NickMask('dan!~lol@localhost')

        self.assertEqual(nm.nick, 'dan')
        self.assertEqual(nm.user, '~lol')
        self.assertEqual(nm.host, 'localhost')
        self.assertEqual(nm.userhost, '~lol@localhost')
        self.assertEqual(nm.nickmask, 'dan!~lol@localhost')

        nm = utils.NickMask('dan!~lol')

        self.assertEqual(nm.nick, 'dan')
        self.assertEqual(nm.user, '~lol')
        self.assertEqual(nm.host, '')

        nm = utils.NickMask('dan@localhost')

        self.assertEqual(nm.nick, 'dan')
        self.assertEqual(nm.user, '')
        self.assertEqual(nm.host, 'localhost')

        nm = utils.NickMask('dan')

        self.assertEqual(nm.nick, 'dan')
        self.assertEqual(nm.user, '')
        self.assertEqual(nm.host, '')

    def test_caseinsensitivelist(self):
        ls = utils.CaseInsensitiveList(['LoL', 'yOLo', 'Tres'])

        self.assertTrue('lol' in ls)
        self.assertTrue('YoLo' in ls)
        self.assertTrue('tRES' in ls)

        self.assertEqual(len(ls), 3)

    def test_caseinsensitivedict(self):
        dc = utils.CaseInsensitiveDict()

        dc['LoL'] = 35
        dc['yOlE'] = 'okay'
        dc['tRES'] = [4, 5, 6]

        self.assertEqual(dc['loL'], 35)
        self.assertEqual(dc.get('lOL'), 35)
        self.assertEqual(dc['YoLE'], 'okay')
        self.assertEqual(dc.get('YoLe'), 'okay')
        self.assertEqual(dc['TrEs'], [4, 5, 6])
        self.assertEqual(dc.get('TRES'), [4, 5, 6])

        self.assertEqual(len(dc), 3)

    def test_hostnames(self):
        hn = utils.validate_hostname

        self.assertTrue(hn('google.com'))
        self.assertTrue(hn('google.com.'))
        self.assertTrue(hn('eth3rt.wrthwrt.qeht.ethwe.local'))

        self.assertFalse(hn(''))
        self.assertFalse(hn('hdfh.fgeth..ehf.egds'))
        self.assertFalse(hn('-lol-.43wrthwrt.qeht.ethwe.local'))
