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
        call = core.Call( feature, 0 )

        self.assertEqual( True, call.is_long_distance() )

    def test_is_local( self ):
        feature = ( core.Call.Features.LOCAL
                    | core.Call.Features.DEST_LANDLINE )
        call = core.Call( feature, 0 )

        self.assertEqual( True, call.is_local() )

    def test_is_destiny_landline( self ):
        feature = ( core.Call.Features.LOCAL
                    | core.Call.Features.DEST_LANDLINE )
        call = core.Call( feature, 0 )

        self.assertEqual( True, call.is_destiny_landline() )

    def test_is_destiny_mobile( self ):
        feature = ( core.Call.Features.LOCAL
                    | core.Call.Features.DEST_MOBILE )
        call = core.Call( feature, 0 )

        self.assertEqual( True, call.is_destiny_mobile() )

if __name__ == "__main__":
    unittest.main()
