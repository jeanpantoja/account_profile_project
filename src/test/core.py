# -*- coding: utf-8 -*-

import unittest
import account_profile.core as core

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
