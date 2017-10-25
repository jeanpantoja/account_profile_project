# -*- coding: utf-8 -*-

import unittest
import account_profile.core as core
import account_profile.parser as parser

class TestProfile( unittest.TestCase ):

    def test_adding_long_distance_landline_call( self ):
        profile = core.Profile()
        feature = ( core.Call.Features.LONG_DISTANCE
                    | core.Call.Features.DEST_LANDLINE )
        call = core.Call( feature, 1 )

        profile.add_call( call )
        profile.add_call( call )
        self.assertEqual( profile.get_long_distance_landline_call_usage(), 2 )

    def test_adding_long_distance_mobile_call( self ):
        profile = core.Profile()
        feature = ( core.Call.Features.LONG_DISTANCE
                    | core.Call.Features.DEST_MOBILE )
        call = core.Call( feature, 2 )

        profile.add_call( call )
        profile.add_call( call )
        self.assertEqual( profile.get_long_distance_mobile_call_usage(), 4 )

    def test_adding_local_landline_call( self ):
        profile = core.Profile()
        feature = ( core.Call.Features.LOCAL
                    | core.Call.Features.DEST_LANDLINE )
        call = core.Call( feature, 3 )

        profile.add_call( call )
        profile.add_call( call )
        self.assertEqual( profile.get_local_landline_call_usage(), 6 )

    def test_adding_local_mobile_call( self ):
        profile = core.Profile()
        feature = ( core.Call.Features.LOCAL
                    | core.Call.Features.DEST_MOBILE )
        call = core.Call( feature, 4 )

        profile.add_call( call )
        profile.add_call( call )
        self.assertEqual( profile.get_local_mobile_call_usage(), 8 )

    def test_adding_SMS( self ):
        profile = core.Profile()

        profile.add_SMS( 1 )
        profile.add_SMS( 2 )
        self.assertEqual( profile.get_SMS_usage(), 3 )

    def test_adding_internet( self ):
        profile = core.Profile()

        profile.add_internet( 1 )
        profile.add_internet( 2 )
        self.assertEqual( profile.get_internet_usage(), 3 )

class TestCall( unittest.TestCase ):

    def test_is_long_distance( self ):
        feature = ( core.Call.Features.LONG_DISTANCE
                    | core.Call.Features.DEST_LANDLINE )
        call = core.Call( feature )

        self.assertEqual( True, call.is_long_distance() )

    def test_is_local( self ):
        feature = ( core.Call.Features.LOCAL
                    | core.Call.Features.DEST_LANDLINE )
        call = core.Call( feature )

        self.assertEqual( True, call.is_local() )

    def test_is_destiny_landline( self ):
        feature = ( core.Call.Features.LOCAL
                    | core.Call.Features.DEST_LANDLINE )
        call = core.Call( feature )

        self.assertEqual( True, call.is_destiny_landline() )

    def test_is_destiny_mobile( self ):
        feature = ( core.Call.Features.LOCAL
                    | core.Call.Features.DEST_MOBILE )
        call = core.Call( feature )

        self.assertEqual( True, call.is_destiny_mobile() )

class TestBillLine( unittest.TestCase ):

    def get_bill_lines_of_long_distance_calls( self ):
        lines = [
            {
                "Tpserv" : "Chamadas Longa Distância: Telefônica",
                "Destino" : "SP AREA 14"
            },
            {
                "Tpserv" : "Chamadas Longa Distância: Brasil Telecom",
                "Destino" : "SC FIXO - AREA 48"
            },
            {
                "Tpserv" : "Chamadas Longa Distância: Embratel",
                "Destino" : "RJ FIXO - AREA 21"
            },
            {
                "Tpserv" : "Chamadas Longa Distância: TIM LD 41",
                "Destino" : "SC FIXO - AREA 48"
            },
            {
                "Tpserv" : "Chamadas Longa Distância: Telemar",
                "Destino" : "SP FIXO - AREA 15"
            }
        ]

        return lines

    def get_bill_lines_of_local_calls( self ):
        lines = [
            {
                "Tpserv" : "Chamadas Locais para Outros Telefones Fixos",
                "Destino" : "SC FIXO - AREA 48"
            },
            {
                "Tpserv" : "Chamadas Locais para Outros Celulares",
                "Destino" : "SP MOVEL - AREA 11"
            },
            {
                "Tpserv" : "Chamadas Locais para Celulares TIM",
                "Destino" : "SC MOVEL TIM - AREA 48"
            },
            {
                "Tpserv" : "Chamadas Locais para Telefones Fixos",
                "Destino" : "SC FIXO - AREA 48"
            }
        ]

        return lines

    def test_is_SMS( self ):
        line = {
            "Tpserv" : "TIM Torpedo",
            "Destino" : "SC FIXO - AREA 48"
        }

        bline = parser.BillLine( line )
        self.assertEqual( True, bline.is_SMS() )

    def test_is_SMS_service( self ):
        line = {
            "Tpserv" : "Serviços de SMS",
            "Destino" : "TIM Agenda - Backup"
        }

        bline = parser.BillLine( line )
        self.assertEqual( True, bline.is_SMS() )

    def test_is_internet( self ):
        line = {
            "Tpserv" : "TIM Wap Fast",
            "Destino" : "-"
        }

        bline = parser.BillLine( line )
        self.assertEqual( True, bline.is_SMS() )

        line = {
            "Tpserv" : "TIM Connect Fast",
            "Destino" : "-"
        }

        bline = parser.BillLine( line )
        self.assertEqual( True, bline.is_SMS() )

        line = {
            "Tpserv" : "BlackBerry Professional - MB",
            "Destino" : "-"
        }

        bline = parser.BillLine( line )
        self.assertEqual( True, bline.is_SMS() )

    def test_features_from_local_call_to_mobile( self ):
        line = {
            "Tpserv" : "Chamadas Locais para Celulares TIM",
            "Destino" : "SC MOVEL TIM - AREA 48"
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
            "Destino" : "SC FIXO - AREA 48"
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
            "Destino" : "SC MOVEL TIM - AREA 48"
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
            "Destino" : "SP FIXO - AREA 11"
        }

        bline = parser.BillLine( line )
        features = bline.retrieve_call_features()
        self.assertEqual( core.Call.Features.LONG_DISTANCE & features,
                          core.Call.Features.LONG_DISTANCE )
        self.assertEqual( core.Call.Features.DEST_LANDLINE & features,
                          core.Call.Features.DEST_LANDLINE )

    def test_is_destiny_call_mobile( self ):
        lines =[
            {
                "Tpserv" : "Chamadas Locais para Celulares TIM",
                "Destino" : "SC MOVEL TIM - AREA 48"
            },
            {
                "Tpserv" : "Chamadas Locais para Outros Celulares",
                "Destino" : "SC MOVEL - AREA 48"
            },
            {
                "Tpserv" : "Chamadas Longa Distância: TIM LD 41",
                "Destino" : "SC MOVEL TIM - AREA 48"
            }
        ]

        for line in lines:
            bline = parser.BillLine( line )
            msg = "[%s/%s] is not valid" % ( line[ "Tpserv" ], line[ "Destino" ] )
            self.assertEqual( True, bline.is_destiny_call_mobile(), msg = msg )

    def test_is_destiny_call_landline( self ):
        lines =[
            {
                "Tpserv" : "Chamadas Longa Distância: Embratel",
                "Destino" : "RJ FIXO - AREA 21"
            },
            {
                "Tpserv" : "Chamadas Locais para Outros Telefones Fixos",
                "Destino" : "SC FIXO - AREA 48"
            },
            {
                "Tpserv" : "Chamadas Locais para Telefones Fixos",
                "Destino" : "HORA CERTA"
            },
            {
                "Tpserv" : "Chamadas Longa Distância: Telemar",
                "Destino" : "RS FIXO - AREA 51"
            },
            {
                "Tpserv" : "Chamadas Longa Distância: TIM LD 41",
                "Destino" : "SP FIXO - AREA 11"
            },
            {
                "Tpserv" : "Chamadas Longa Distância: Brasil Telecom",
                "Destino" : "SC FIXO - AREA 48"
            }
        ]

        for line in lines:
            bline = parser.BillLine( line )
            msg = "[%s/%s] is not valid" % ( line[ "Tpserv" ], line[ "Destino" ] )
            self.assertEqual( True, bline.is_destiny_call_landline(), msg = msg )

    def test_is_long_distance_call( self ):
        lines = self.get_bill_lines_of_long_distance_calls()

        for line in lines:
            bline = parser.BillLine( line )
            msg = "[%s] is not valid" % ( line[ "Tpserv" ] )
            self.assertEqual( True, bline.is_long_distance_call(), msg = msg )

    def test_is_local_call( self ):
        lines = self.get_bill_lines_of_local_calls()

        for line in lines:
            bline = parser.BillLine( line )
            msg = "[%s] is not valid" % ( line[ "Tpserv" ] )
            self.assertEqual( True, bline.is_local_call(), msg = msg )

if __name__ == "__main__":
    unittest.main()
