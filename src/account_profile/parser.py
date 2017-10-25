# -*- coding: utf-8 -*-
import re

class BillLine( object ):
    SMS_REGEX = r'TIM\s*Torpedo|Serviços\s*de\s*SMS'
    INTERNET_REGEX = r'TIM\s*(Wap\s*Fast|Connect\s*Fast)|BlackBerry\s*Professional\s*-\s*MB'
    LONG_DISTANCE_CALL_REGEX = r'Chamadas\s*Longa\s*(Distância|Distancia)'
    LOCAL_CALL_REGEX = r'Chamadas\s*Locais'

    def __init__( self, bill_line ):
        """
        Args:
            bill_line( dict ): A dict with all fields from a bill line
        """
        self.service_type = bill_line[ "Tpserv" ]

    def is_SMS( self ):
        """
        Detect if this bill line is relative to a SMS sending

        Returns:
            True if is a SMS sending otherwise return False
        """

        match = re.search( BillLine.SMS_REGEX, self.service_type, re.I )
        return bool( match )

    def is_internet( self ):
        """
        Detect if this bill line is relative to an internet access

        Returns:
            True if is relative to internet access otherwise return False
        """

        match = re.search( BillLine.INTERNET_REGEX, self.service_type, re.I )
        return bool( match )

    def retrieve_call_features( self ):
        """
        Returns:
            An integer flag with all features detected
        """
        return 0

    def is_long_distance_call( self ):
        """
        Returns:
            True if is a long distance call  otherwise return False
        """

        match = re.search( BillLine.LONG_DISTANCE_CALL_REGEX, self.service_type, re.I )
        return bool( match )

    def is_local_call( self ):
        """
        Returns:
            True if is a local call  otherwise return False
        """

        match = re.search( BillLine.LOCAL_CALL_REGEX, self.service_type, re.I )
        return bool( match )

    def is_destiny_call_mobile( self ):
        """
        Returns:
            True if is a call to a mobile phone otherwise return False
        """
        pass

    def is_destiny_call_landline( self ):
        """
        Returns:
            True if is a call to a landline phone otherwise return False
        """
        pass
