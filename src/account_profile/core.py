# -*- coding: utf-8 -*-

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
        self.internet_usage = self.internet_usage + n_bytes

    def get_internet_usage( self ):
        """
        Returns:
            An integer value representing the number of bytes
        """
        return self.internet_usage



class Call( object ):
    class Features( enum.IntEnum ):
        LONG_DISTANCE = 0b00001
        LOCAL = 0b0010
        DEST_LANDLINE = 0b0100
        DEST_MOBILE = 0b1000

    def __init__( self, call_features, duration = 0):
        """
        Args:
            call_features ( account_profile.core.Call.Features ): Feature
                flag from call. Use or bitwise operation to set the flag.
                Example a call that is Local to a mobile phone:
                   call = Call( Call.Features.LOCAL | Call.Features.DEST_MOBILE, 2.5 )

            duration( float ): Call duration in minutes
        """
        self.call_features = call_features
        self.duration = duration

    def is_local( self ):
        return bool( self.call_features & Call.Features.LOCAL )

    def is_long_distance( self ):
        return bool( self.call_features & Call.Features.LONG_DISTANCE )

    def is_destiny_landline( self ):
        return bool( self.call_features & Call.Features.DEST_LANDLINE )

    def is_destiny_mobile( self ):
        return bool( self.call_features & Call.Features.DEST_MOBILE )

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

class Duration( object ):
    SECONDS_BY_MINUTE = 60

    def __init__( self, minutes = 0, seconds = 0 ):
        """
        Args:
            minutes( int ): Number of minutes. Must be bigger than -1
            seconds( int ): Number of seconds. Must be in interval [ 0, 59 ]

        Raises:
            Exception if minutes or seconds is not valid
        """

        if not ( minutes > -1 ):
            msg = "The param minutes[%d] must be bigger than -1" % ( minutes )
            raise Exception( msg )

        if not ( seconds >= 0 and seconds <= 59 ):
            msg =  "The param seconds[%d] must be in interval [ 0, 59 ]" % ( minutes )
            raise Exception( msg )

        self._seconds = Duration._calculate_seconds( minutes, seconds )

    @staticmethod
    def from_string( duration ):
        """
        Args:
            duration( str ): A duration representation in format %dm%ds

        Returns:
            New account_profile.core.Duration instance created from string

        Raises:
            Exception if the duration string is not valid
        """

        return Duration()

    @staticmethod
    def _calculate_seconds( minutes, seconds ):
        """
        Args:
            minutes( int ): Number of minutes
            seconds( int ): Number of seconds

        Returns:
            The computed seconds
        """

        return minutes * Duration.SECONDS_BY_MINUTE + seconds

    def __add__( self, duration ):
        """
        Args:
            duration( account_profile.core.Duration ): A duration to add with this

        Returns:
            New account_profile.core.Duration whit the addition result
        """
        return self

    def to_minutes( self ):
        return 0

    def to_seconds( self ):
        return self._seconds

