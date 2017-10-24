import enum

class Profile( object ):

    def __init__( self ):
        self.calls = []
        self.internet_usage = 0
        self.sms_usage = 0

    def add_call( self, call ):
        """
        Args:
            call ( account_profile.core.Call ): The call you desire add in profile
        """
        self.calls.append( call )

    def get_long_distance_landline_call_usage( self ):
        """
        Returns:
            A value representing the usage in minutes
        """
        condition = lambda call: call.is_long_distance() and call.is_destiny_landline()
        usage = Call.sum_duration( self.calls, condition )
        return usage

    def get_long_distance_mobile_call_usage( self ):
        """
        Returns:
            A value representing the usage in minutes
        """
        condition = lambda call: call.is_long_distance() and call.is_destiny_mobile()
        usage = Call.sum_duration( self.calls, condition )
        return usage

    def get_local_landline_call_usage( self ):
        """
        Returns:
            A value representing the usage in minutes
        """
        condition = lambda call: call.is_local() and call.is_destiny_landline()
        usage = Call.sum_duration( self.calls, condition )
        return usage

    def get_local_mobile_call_usage( self ):
        """
        Returns:
            A value representing the usage in minutes
        """
        condition = lambda call: call.is_local() and call.is_destiny_mobile()
        usage = Call.sum_duration( self.calls, condition )
        return usage

    def add_SMS( self, n_units ):
        """
        Args:
            n_units( int ): The number of units to increase the sms usage counter
        """
        self.sms_usage = self.sms_usage + n_units

    def get_SMS_usage( self ):
        """
        Returns:
            An integer value representing the number of sms
        """
        return self.sms_usage

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
        return self.call_type == Call.Type.LOCAL

    def is_long_distance( self ):
        return self.call_type == Call.Type.LONG_DISTANCE

    def is_destiny_landline( self ):
        return self.call_destiny_type == Call.DestinyType.LANDLINE

    def is_destiny_mobile( self ):
        return self.call_destiny_type == Call.DestinyType.MOBILE

    @staticmethod
    def sum_duration( calls, condition ):
        """
        Args:
            calls( list ): The list of call instances to compute duration sum
            condition( callable ): A callable that with format condition( call_instance )->bool
        """
        duration = 0

        for call in filter( condition, calls ):
            duration = duration + call.duration

        return duration

