# -*- coding: utf-8 -*-

import unittest
import account_profile.core as core
import account_profile.parser as parser
import test.constants as constants

class TestBillLine( unittest.TestCase ):

    def test_is_SMS( self ):
        line = {
            "Tpserv" : "TIM Torpedo",
            "Destino" : "SC FIXO - AREA 48",
            "Duração" : ""
        }

        bline = parser.BillLine( line )
        self.assertEqual( True, bline.is_SMS() )

    def test_is_SMS_service( self ):
        line = {
            "Tpserv" : "Serviços de SMS",
            "Destino" : "TIM Agenda - Backup",
            "Duração" : "-"
        }

        bline = parser.BillLine( line )
        self.assertEqual( True, bline.is_SMS() )

    def test_is_internet( self ):
        line = {
            "Tpserv" : "TIM Wap Fast",
            "Destino" : "-",
            "Duração" : " 6,200 KB"
        }

        bline = parser.BillLine( line )
        self.assertEqual( True, bline.is_internet() )

        line = {
            "Tpserv" : "TIM Connect Fast",
            "Destino" : "-",
            "Duração" : "200,220 KB"
        }

        bline = parser.BillLine( line )
        self.assertEqual( True, bline.is_internet() )

        line = {
            "Tpserv" : "BlackBerry Professional - MB",
            "Destino" : "-",
            "Duração" : "730 B"
        }

        bline = parser.BillLine( line )
        self.assertEqual( True, bline.is_internet() )

    def test_features_from_local_call_to_mobile( self ):
        line = {
            "Tpserv" : "Chamadas Locais para Celulares TIM",
            "Destino" : "SC MOVEL TIM - AREA 48",
            "Duração" : "01m06s"
        }

        bline = parser.BillLine( line )
        features = bline.retrieve_call_features()
        self.assertEqual( core.Call.Features.LOCAL & features,
                          core.Call.Features.LOCAL )
        self.assertEqual( core.Call.Features.DEST_MOBILE & features,
                          core.Call.Features.DEST_MOBILE )

    def test_features_from_local_call_to_landline( self ):
        line = {
            "Tpserv" : "Chamadas Locais para Telefones Fixos",
            "Destino" : "SC FIXO - AREA 48",
            "Duração" : "01m06s"
        }

        bline = parser.BillLine( line )
        features = bline.retrieve_call_features()
        self.assertEqual( core.Call.Features.LOCAL & features,
                          core.Call.Features.LOCAL )
        self.assertEqual( core.Call.Features.DEST_LANDLINE & features,
                          core.Call.Features.DEST_LANDLINE )

    def test_features_from_long_distance_call_to_mobile( self ):
        line = {
            "Tpserv" : "Chamadas Longa Distância: TIM LD 41",
            "Destino" : "SC MOVEL TIM - AREA 48",
            "Duração" : "01m06s"
        }

        bline = parser.BillLine( line )
        features = bline.retrieve_call_features()
        self.assertEqual( core.Call.Features.LONG_DISTANCE & features,
                          core.Call.Features.LONG_DISTANCE )
        self.assertEqual( core.Call.Features.DEST_MOBILE & features,
                          core.Call.Features.DEST_MOBILE )

    def test_features_from_long_distance_call_to_landline( self ):
        line = {
            "Tpserv" : "Chamadas Longa Distância: TIM LD 41",
            "Destino" : "SP FIXO - AREA 11",
            "Duração" : "01m06s"
        }

        bline = parser.BillLine( line )
        features = bline.retrieve_call_features()
        self.assertEqual( core.Call.Features.LONG_DISTANCE & features,
                          core.Call.Features.LONG_DISTANCE )
        self.assertEqual( core.Call.Features.DEST_LANDLINE & features,
                          core.Call.Features.DEST_LANDLINE )

    def test_is_destiny_call_mobile( self ):
        self._test_calls( parser.BillLine.is_destiny_call_mobile,
                          constants.BILL_LINES_OF_CALL_TO_MOBILE_PHONE )

    def test_is_destiny_call_landline( self ):
        self._test_calls( parser.BillLine.is_destiny_call_landline,
                          constants.BILL_LINES_OF_CALL_TO_LANDLINE_PHONE )

    def test_is_long_distance_call( self ):
        self._test_calls( parser.BillLine.is_long_distance_call,
                          constants.BILL_LINES_OF_LONG_DISTANCE_CALL )

    def test_is_local_call( self ):
        self._test_calls( parser.BillLine.is_local_call,
                          constants.BILL_LINES_OF_LOCAL_CALL )

    def _test_calls( self, assertion, lines ):
        for line in lines:
            bline = parser.BillLine( line )
            msg = "[%s/%s] is not valid" % ( line[ "Tpserv" ], line[ "Destino" ] )
            self.assertEqual( True, assertion( bline ), msg = msg )
