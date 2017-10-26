# -*- coding: utf-8 -*-

import unittest
import account_profile.core as core

class TestProfile( unittest.TestCase ):

    def test_adding_long_distance_landline_call( self ):
        profile = core.Profile()
        feature = ( core.Call.Features.LONG_DISTANCE
                    | core.Call.Features.DEST_LANDLINE )
        call = core.Call( feature, core.Duration( 1 ) )

        profile.add_call( call )
        profile.add_call( call )
        self.assertEqual( profile.get_long_distance_landline_call_usage(), 2 )

    def test_adding_long_distance_mobile_call( self ):
        profile = core.Profile()
        feature = ( core.Call.Features.LONG_DISTANCE
                    | core.Call.Features.DEST_MOBILE )
        call = core.Call( feature, core.Duration( 2 ) )

        profile.add_call( call )
        profile.add_call( call )
        self.assertEqual( profile.get_long_distance_mobile_call_usage(), 4 )

    def test_adding_local_landline_call( self ):
        profile = core.Profile()
        feature = ( core.Call.Features.LOCAL
                    | core.Call.Features.DEST_LANDLINE )
        call = core.Call( feature, core.Duration( 3 ) )

        profile.add_call( call )
        profile.add_call( call )
        self.assertEqual( profile.get_local_landline_call_usage(), 6 )

    def test_adding_local_mobile_call( self ):
        profile = core.Profile()
        feature = ( core.Call.Features.LOCAL
                    | core.Call.Features.DEST_MOBILE )
        call = core.Call( feature, core.Duration( 4 ) )

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

        profile.add_internet( core.DigitalDataSize( "1 B" ) )
        profile.add_internet( core.DigitalDataSize( "2 B" ) )
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

class TestDuration( unittest.TestCase ):

    def test_creation( self ):
        duration = core.Duration( 1, 30 )
        self.assertEqual( duration.to_seconds(), 90 )

    def test_creation_from_string( self ):
        duration = core.Duration.from_string( "2m30s")
        self.assertEqual( duration.to_seconds(), 150 )

    def test_invalid_creation( self ):
        with self.assertRaises( Exception ):
            core.Duration( -1, 90 )

    def test_invalid_creation_from_string( self ):
        with self.assertRaises( Exception ):
            core.Duration.from_string( "-1m90s")

    def test_addition_seconds_result( self ):
        duration_01 = core.Duration( 1, 30 )
        duration_02 = core.Duration( 2, 30 )
        duration_03 = duration_01 + duration_02

        self.assertEqual( duration_03.to_seconds(), 90 + 150  )

    def test_addition_minutes_result( self ):
        duration_01 = core.Duration( 2, 20 )
        duration_02 = core.Duration( 3, 10 )
        duration_03 = duration_01 + duration_02

        self.assertAlmostEqual( duration_03.to_minutes(), 5.5  )

class TestDigitalDataSize( unittest.TestCase ):

    def test_create_data_in_B_01( self ):
        datasize = core.DigitalDataSize( "10 B" )
        self.assertAlmostEqual( 10.0, datasize.get_number_of_bytes() )

    def test_create_data_in_B_02( self ):
        datasize = core.DigitalDataSize( "10,1 B" )
        self.assertAlmostEqual( 10.1, datasize.get_number_of_bytes() )

    def test_create_data_in_KB_01( self ):
        datasize = core.DigitalDataSize( "10 KB" )
        self.assertAlmostEqual( 10.0 * 1024, datasize.get_number_of_bytes() )

    def test_create_data_in_KB_02( self ):
        datasize = core.DigitalDataSize( "10,1 KB" )
        self.assertAlmostEqual( 10.1 * 1024, datasize.get_number_of_bytes() )


    def test_create_data_in_MB_01( self ):
        datasize = core.DigitalDataSize( "10 MB" )
        self.assertAlmostEqual( 10.0 * 1024 * 1024, datasize.get_number_of_bytes() )

    def test_create_data_in_MB_02( self ):
        datasize = core.DigitalDataSize( "10,1 MB" )
        self.assertAlmostEqual( 10.1 * 1024 * 1024, datasize.get_number_of_bytes() )

    def test_invalid_creation( self ):
        with self.assertRaises( Exception ):
            datasize = core.DigitalDataSize( "10,1 BB" )

        with self.assertRaises( Exception ):
            datasize = core.DigitalDataSize( "10,1 KBB" )

        with self.assertRaises( Exception ):
            datasize = core.DigitalDataSize( "10,1 MBB" )

        with self.assertRaises( Exception ):
            datasize = core.DigitalDataSize( "10.1 K" )

        with self.assertRaises( Exception ):
            datasize = core.DigitalDataSize( "10.1" )

        with self.assertRaises( Exception ):

            datasize = core.DigitalDataSize( "10,1" )

    def test_addition( self ):
        d01 = core.DigitalDataSize( "1 B" )
        d02 = core.DigitalDataSize( "2 B" )

        result = d01 + d02
        expected = core.DigitalDataSize( "3 B" )

        self.assertAlmostEqual( result.get_number_of_bytes(), expected.get_number_of_bytes() )
