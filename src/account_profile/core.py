# -*- coding: utf-8 -*-

import enum
import re

class Profile( object ):

    def __init__( self ):
        self.calls = []
        self.internet_usage = DigitalDataSize()
        self.sms_usage = 0

    def add_call( self, call ):
        """
        Args:
            call ( account_profile.core.Call ): The call you desire add in profile
        """
        self.calls.append( call )

    def _get_call_usage( self, condition ):
        usage = Call.sum_duration( self.calls, condition )
        return usage

    def get_long_distance_landline_call_usage( self ):
        """
        Returns:
            A value representing the usage in minutes
        """
        return self._get_call_usage(
            lambda call: call.is_long_distance() and call.is_destiny_landline()
        )

    def get_long_distance_mobile_call_usage( self ):
        """
        Returns:
            A value representing the usage in minutes
        """
        return self._get_call_usage(
            lambda call: call.is_long_distance() and call.is_destiny_mobile()
        )

    def get_local_landline_call_usage( self ):
        """
        Returns:
            A value representing the usage in minutes
        """
        return self._get_call_usage(
            lambda call: call.is_local() and call.is_destiny_landline()
        )

    def get_local_mobile_call_usage( self ):
        """
        Returns:
            A value representing the usage in minutes
        """
        return self._get_call_usage(
            lambda call: call.is_local() and call.is_destiny_mobile()
        )

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

    def add_internet( self, ddsize ):
        """
        Args:
            ddsize( account_profile.core.DigitalDataSize ): Increase the internet usage
        """
        self.internet_usage = self.internet_usage + ddsize

    def get_internet_usage( self ):
        """
        Returns:
            An integer value representing the number of bytes
        """
        return self.internet_usage.get_number_of_bytes()

class Duration( object ):
    SECONDS_BY_MINUTE = 60
    REGEX = r'(\d+)m(\d+)s'
    FORMAT = "%dm%ds"

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

        match = re.match( Duration.REGEX, duration )

        if match:
            groups = match.groups()
            minutes = int( groups[ 0 ] )
            seconds = int( groups[ 1 ] )
            return Duration( minutes, seconds )

        msg = ( "The duration[%s] is not int the format[%s]"
                % ( duration, Duration.FORMAT ) )

        raise Exception( msg )

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
        result = Duration()
        result._seconds = self._seconds + duration._seconds
        return result

    def to_minutes( self ):
        return float( self._seconds ) / Duration.SECONDS_BY_MINUTE

    def to_seconds( self ):
        return self._seconds

class Call( object ):
    class Features( enum.IntEnum ):
        LONG_DISTANCE = 0b00001
        LOCAL = 0b0010
        DEST_LANDLINE = 0b0100
        DEST_MOBILE = 0b1000

    def __init__( self, call_features, duration = Duration() ):
        """
        Args:
            call_features ( account_profile.core.Call.Features ): Feature
                flag from call. Use or bitwise operation to set the flag.
                Example a call that is Local to a mobile phone:
                   call = Call( Call.Features.LOCAL | Call.Features.DEST_MOBILE, 2.5 )

            duration( account_profile.core.Duration ): Call duration
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
        duration = Duration()

        for call in filter( condition, calls ):
            duration = duration + call.duration

        return duration.to_minutes()

class DigitalDataSize( object ):

    def __init__( self, n_bytes = 0 ):
        """
        Args:
            n_byte( int | float ): Digital data size in bytes:
        """

        self.n_bytes = n_bytes

    @staticmethod
    def from_string( measure ):
        """
        Args:
            measure( str ): Ditital data size in formats:
                "%d B"
                "%d,%d B"
                "%d KB"
                "%d,%d KB"
                "%d MB"
                "%d,%d MB"
        """
        converter = DigitalDataSize._Converter( measure )
        return DigitalDataSize( converter.convert() )

    def __add__( self, other ):
        result = DigitalDataSize()
        result.n_bytes = self.n_bytes + other.n_bytes
        return result

    def get_number_of_bytes( self ):
        return self.n_bytes

    """
    Helper classes to convert string to DigitalDataSize
    """
    class _UnitType( object ):

        def __init__( self, regex, n_bytes ):
            self.regex = regex
            self.n_bytes = n_bytes

        def _match( self, measure ):
            return re.match( self.regex, measure.strip() )

        def match_type( self, measure ):
            return bool( self._match( measure ) )

        def read_length_in_bytes( self, measure ):
            match = self._match( measure )

            if match:
                groups = match.groups()
                numerical_part = groups[ 0 ]

                numerical_part = numerical_part.replace( ",", "." )
                return float( numerical_part ) * self.n_bytes

    class _Converter( object ):
        BYTE_REGEX = r'((\d+)(,\d+){0,1})\s*B$'
        KILO_BYTE_REGEX = r'((\d+)(,\d+){0,1})\s*KB$'
        MEGA_BYTE_REGEX = r'((\d+)(,\d+){0,1})\s*MB$'

        BYTE = 1
        KILO_BYTE = 1024 * BYTE
        MEGA_BYTE = 1024 * KILO_BYTE

        def __init__( self, measure ):
            self.measure = measure
            self.unit_types = [
                DigitalDataSize._UnitType( self.BYTE_REGEX, self.BYTE ),
                DigitalDataSize._UnitType( self.KILO_BYTE_REGEX, self.KILO_BYTE ),
                DigitalDataSize._UnitType( self.MEGA_BYTE_REGEX, self.MEGA_BYTE )
            ]

        def convert( self ):
            for unit_type in self.unit_types:
                if unit_type.match_type( self.measure ):
                    return unit_type.read_length_in_bytes( self.measure )

            raise Exception(
                "Fail attemp to convert DigitalDataSize with unknown format"
            )
