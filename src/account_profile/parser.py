# -*- coding: utf-8 -*-

class BillLine( object ):

    def __init__( self, bill_line ):
        """
        Args:
            bill_line( dict ): A dict with all fields from a bill line
        """
        self.bill_line = bill_line

    def is_SMS( self ):
        """
        Detect if this bill line is relative to a SMS sending

        Returns:
            True if is a SMS sending otherwise return False
        """
        pass

    def is_internet( self ):
        """
        Detect if this bill line is relative to an internet access

        Returns:
            True if is relative to internet access otherwise return False
        """
        pass

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
        pass

    def is_local_call( self ):
        """
        Returns:
            True if is a local call  otherwise return False
        """
        pass

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
