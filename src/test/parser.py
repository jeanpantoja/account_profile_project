# -*- coding: utf-8 -*-

import unittest
import account_profile.core as core
import account_profile.parser as parser
import test.constants as constants

class TestBillLine( unittest.TestCase ):

    def test_is_SMS( self ):
        bline = parser.BillLine(
            "111-1111-1111",
            "TIM Torpedo",
            "SC FIXO - AREA 48",
            ""
        )
        self.assertEqual( True, bline.is_SMS() )

    def test_is_SMS_service( self ):
        bline = parser.BillLine(
            "111-1111-1111",
            "Serviços de SMS",
            "TIM Agenda - Backup",
            "-"
        )
        self.assertEqual( True, bline.is_SMS() )

    def test_is_internet( self ):
        bline = parser.BillLine(
            "111-1111-1111",
            "TIM Wap Fast",
            "-",
            " 6,200 KB"
        )

        self.assertEqual( True, bline.is_internet() )

        bline = parser.BillLine(
            "111-1111-1111",
            "TIM Connect Fast",
            "-",
            "200,220 KB"
        )

        self.assertEqual( True, bline.is_internet() )

        bline = parser.BillLine(
            "111-1111-1111",
            "BlackBerry Professional - MB",
            "-",
            "730 B"
        )

        self.assertEqual( True, bline.is_internet() )

    def test_features_from_local_call_to_mobile( self ):
        bline = parser.BillLine(
            "111-1111-1111",
            "Chamadas Locais para Celulares TIM",
            "SC MOVEL TIM - AREA 48",
            "01m06s"
        )

        features = bline.retrieve_call_features()

        self.assertEqual(
            core.Call.Features.LOCAL & features,
            core.Call.Features.LOCAL
        )

        self.assertEqual(
            core.Call.Features.DEST_MOBILE & features,
            core.Call.Features.DEST_MOBILE
        )

    def test_features_from_local_call_to_landline( self ):
        bline = parser.BillLine(
            "111-1111-1111",
            "Chamadas Locais para Telefones Fixos",
            "SC FIXO - AREA 48",
            "01m06s"
        )

        features = bline.retrieve_call_features()

        self.assertEqual(
            core.Call.Features.LOCAL & features,
            core.Call.Features.LOCAL
        )

        self.assertEqual(
            core.Call.Features.DEST_LANDLINE & features,
            core.Call.Features.DEST_LANDLINE
        )

    def test_features_from_long_distance_call_to_mobile( self ):
        bline = parser.BillLine(
            "111-1111-1111",
            "Chamadas Longa Distância: TIM LD 41",
            "SC MOVEL TIM - AREA 48",
            "01m06s"
        )

        features = bline.retrieve_call_features()

        self.assertEqual(
            core.Call.Features.LONG_DISTANCE & features,
            core.Call.Features.LONG_DISTANCE
        )

        self.assertEqual(
            core.Call.Features.DEST_MOBILE & features,
            core.Call.Features.DEST_MOBILE
        )

    def test_features_from_long_distance_call_to_landline( self ):
        bline = parser.BillLine(
            "111-1111-1111",
            "Chamadas Longa Distância: TIM LD 41",
            "SP FIXO - AREA 11",
            "01m06s"
        )

        features = bline.retrieve_call_features()

        self.assertEqual(
            core.Call.Features.LONG_DISTANCE & features,
            core.Call.Features.LONG_DISTANCE
        )

        self.assertEqual(
            core.Call.Features.DEST_LANDLINE & features,
            core.Call.Features.DEST_LANDLINE
        )

    def test_is_destiny_call_mobile( self ):
        self._test_calls(
            parser.BillLine.is_destiny_call_mobile,
            constants.BILL_LINES_OF_CALL_TO_MOBILE_PHONE
        )

    def test_is_destiny_call_landline( self ):
        self._test_calls(
            parser.BillLine.is_destiny_call_landline,
            constants.BILL_LINES_OF_CALL_TO_LANDLINE_PHONE
        )

    def test_is_long_distance_call( self ):
        self._test_calls(
            parser.BillLine.is_long_distance_call,
            constants.BILL_LINES_OF_LONG_DISTANCE_CALL
        )

    def test_is_local_call( self ):
        self._test_calls(
            parser.BillLine.is_local_call,
            constants.BILL_LINES_OF_LOCAL_CALL
        )

    def test_retrieve_call_duration( self ):
        bline = parser.BillLine(
            "111-1111-1111",
            "Chamadas Longa Distância: TIM LD 41",
            "SP FIXO - AREA 11",
            "01m06s"
        )

        duration = bline.retrieve_call_duration()
        self.assertEqual( duration.to_seconds(), 66 )

    def test_retrieve_call_duration_from_not_call( self ):
        bline = parser.BillLine(
            "111-1111-1111",
            "TIM torpedo",
            "SP MOVEL - AREA 11",
            ""
        )
        with self.assertRaises( Exception ):
            bline.retrieve_call_duration()

    def _test_calls( self, assertion, lines ):
        for bline in lines:
            msg = "[%s/%s] is not valid" % ( bline.service_type, bline.destiny )
            self.assertEqual( True, assertion( bline ), msg = msg )

class TestBillParser( unittest.TestCase ):

    def test_mount_profile( self ):
        profile = parser.BillLine.mount_profile( constants.BILL_LINES_01 )

        self.assertAlmostEqual(
            profile.get_local_mobile_call_usage(),
            ( 2 * 66 ) / 60.0
        )

        self.assertAlmostEqual(
            profile.get_local_landline_call_usage(),
            66 / 60.0
        )

        self.assertAlmostEqual(
            profile.get_long_distance_mobile_call_usage(),
            ( 90 + 85 ) / 60.0
        )

        self.assertAlmostEqual(
            profile.get_long_distance_landline_call_usage(),
            ( 65 + 45 ) / 60.0
        )

        self.assertEqual( profile.get_SMS_usage(), 2 )

        self.assertAlmostEqual(
            profile.get_internet_usage(),
            18.67969 * ( 2**10 )
            + 1.95332 * ( 2 ** 20 )
            + 5.64551 * ( 2 ** 10 )
            + 527
        )
