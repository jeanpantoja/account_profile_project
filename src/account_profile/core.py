import enum

class Profile( object ):

    def add_call( self, call ):
        """
        Args:
            call ( account_profile.core.Call ): The call you desire add in profile
        """
        pass

    def get_long_distance_landline_call_usage( self ):
        """
        Returns:
            A value representing the usage in minutes
        """
        pass

    def get_long_distance_mobile_call_usage( self ):
        """
        Returns:
            A value representing the usage in minutes
        """
        pass

    def get_local_landline_call_usage( self ):
        """
        Returns:
            A value representing the usage in minutes
        """
        pass

    def get_local_mobile_call_usage( self ):
        """
        Returns:
            A value representing the usage in minutes
        """
        pass

    def add_SMS( self, n_units ):
        """
        Args:
            n_units( int ): The number of units to increase the sms usage counter
        """
        pass

    def get_SMS_usage( self ):
        """
        Returns:
            An integer value representing the number of sms
        """
        pass

    def add_internet( self, n_bytes ):
        """
        Args:
            n_bytes( int ): The number of bytes to increase the internet usage counter
        """
        pass

    def get_internet_usage( self ):
        """
        Returns:
            An integer value representing the number of bytes
        """
        pass



class Call( object ):
    class Type( enum.Enum ):
        LONG_DISTANCE = 0
        LOCAL = 1

    class DestinyType( enum.Enum ):
        LANDLINE = 0
        MOBILE = 1

    def __init__( self, call_type, call_destiny_type, duration ):
        """
        Args:
            call_type ( account_profile.core.Call.Type ): Enum value
                of available types

            call_destiny_type ( account_profile.core.Call.DestinyType ): Enum value
                of available destiny types

            duration( float ): Call duration in minutes
        """
        self.call_type = call_type
        self.call_destiny_type = call_destiny_type
        self.duration = duration

    def is_local( self ):
        pass

    def is_long_distance( self ):
        pass

    def is_destiny_landline( self ):
        pass

    def is_destiny_mobile( self ):
        pass
