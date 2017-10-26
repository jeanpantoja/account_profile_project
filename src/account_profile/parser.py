# -*- coding: utf-8 -*-
import re
import account_profile.core as core
import csv

class BillLine( object ):
    SMS_REGEX = r'TIM\s*Torpedo|Serviços\s*de\s*SMS'
    INTERNET_REGEX = r'TIM\s*(Wap\s*Fast|Connect\s*Fast)|BlackBerry\s*Professional\s*-\s*MB'
    LONG_DISTANCE_CALL_REGEX = r'Chamadas\s*Longa\s*(Distância|Distancia)'
    LOCAL_CALL_REGEX = r'Chamadas\s*Locais'
    DEST_CALL_MOBILE_REGEX = r'Movel|Celulares'
    DEST_CALL_LANDLINE_REGEX = r'Fixo'
    PHONE_NUMBER_REGEX = r'\d{3}-\d{4,5}-\d{4}'

    CSV_COLUMN_DELIMITER = ";"
    CSV_PHONE_NUMBER_COLUMN = 3
    CSV_SERVICE_TYPE_COLUMN = 6
    CSV_DESTINY_CONLUMN = 10
    CSV_DURATION_COLUMN = 13

    def __init__( self,
                  phone_number = "",
                  service_type = "",
                  destiny = "",
                  duration = "" ):
        """
        Args:
            bill_line( dict ): A dict with all fields from a bill line
        """

        self.phone_number = phone_number
        self.service_type = service_type
        self.destiny = destiny
        self.duration = duration

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

        features = 0

        if not self.is_call():
            return features

        if( self.is_long_distance_call() ):
            features = features | core.Call.Features.LONG_DISTANCE

        if( self.is_local_call() ):
            features = features | core.Call.Features.LOCAL

        if( self.is_destiny_call_landline() ):
            features = features | core.Call.Features.DEST_LANDLINE

        if( self.is_destiny_call_mobile() ):
            features = features | core.Call.Features.DEST_MOBILE

        return features

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

        matchService = re.search( BillLine.DEST_CALL_MOBILE_REGEX,
                                  self.service_type, re.I )

        matchDest = re.search( BillLine.DEST_CALL_MOBILE_REGEX,
                               self.destiny, re.I )

        return bool( self.is_call() and ( matchDest or matchService ) )

    def is_destiny_call_landline( self ):
        """
        Returns:
            True if is a call to a landline phone otherwise return False
        """

        matchService = re.search( BillLine.DEST_CALL_LANDLINE_REGEX,
                                  self.service_type, re.I )

        matchDest = re.search( BillLine.DEST_CALL_LANDLINE_REGEX,
                               self.destiny, re.I )

        return bool( self.is_call() and ( matchDest or matchService ) )

    def is_call( self ):
        return self.is_local_call() or self.is_long_distance_call()

    def retrieve_call_duration( self ):
        """
            Returns:
                An instance of account_profile.core.Duration representing the
                duration of this call. If this bill line is not from a call
                None is returned
        """

        if self.is_call():
            return core.Duration.from_string( self.duration )

        return None

    @staticmethod
    def _load_phone_numbers_bill_lines( bill_file_name ):
        file_handler = open( bill_file_name )
        csv_reader = csv.reader( file_handler, delimiter = BillLine.CSV_COLUMN_DELIMITER  )
        phone_number_by_bill_lines = dict()

        for csv_line in csv_reader:
            bline = BillLine()

            bline.phone_number = csv_line[ BillLine.CSV_PHONE_NUMBER_COLUMN ]
            bline.service_type = csv_line[ BillLine.CSV_SERVICE_TYPE_COLUMN ]
            bline.destiny = csv_line[ BillLine.CSV_DESTINY_CONLUMN ]
            bline.duration = csv_line[ BillLine.CSV_DURATION_COLUMN ]

            bline.phone_number = bline.phone_number.strip()

            if re.match( BillLine.PHONE_NUMBER_REGEX, bline.phone_number ):
                if not bline.phone_number in phone_number_by_bill_lines:
                    phone_number_by_bill_lines[ bline.phone_number ] = list()

                phone_number_lines = phone_number_by_bill_lines[ bline.phone_number ]
                phone_number_lines.append( bline )

        file_handler.close()
        return phone_number_by_bill_lines

    @staticmethod
    def mount_profile( bill_lines ):
        """
        Args:
            bill_lines( list ): A list with account_profile.parser.BillLine instances

        Returns:
            An account_profile.core.Profile instance
        """
        profile = core.Profile()

        for line in bill_lines:
            if line.is_call():
                duration = line.retrieve_call_duration()
                features = line.retrieve_call_features()
                call = core.Call( features, duration )
                profile.add_call( call )
            elif line.is_SMS():
                profile.add_SMS( 1 )
            elif line.is_internet():
                duration_str = line.duration
                duration_str = duration_str.replace( ",", "." )
                duration_str = duration_str.strip()
                duration = 0

                match = re.match(  r'((\d+)(\.\d+){0,1})\s*B', duration_str )
                if match:
                    groups = match.groups()
                    duration = float( groups[ 0 ] )

                match = re.match(  r'((\d+)(\.\d+){0,1})\s*KB', duration_str )
                if match:
                    groups = match.groups()
                    duration = float( groups[ 0 ] ) * 1024

                match = re.match(  r'((\d+)(\.\d+){0,1})\s*MB', duration_str )
                if match:
                    groups = match.groups()
                    duration = float( groups[ 0 ] ) * 1024 * 1024

                profile.add_internet( duration )

        return profile

class BillParser( object ):
    pass
