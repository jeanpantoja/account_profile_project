# -*- coding: utf-8 -*-
import re
import account_profile.core as core
import csv

class BillLine( object ):
    SMS_REGEX = r'TIM\s*Torpedo'
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
    CSV_N_COLUMNS = 20

    def __init__( self,
                  phone_number = "",
                  service_type = "",
                  destiny = "",
                  duration = "" ):
        """
        Args:
            bill_line( dict ): A dict with all fields from a bill line
        """

        self.phone_number = phone_number.strip()
        self.service_type = service_type
        self.destiny = destiny
        self.duration = duration

    def _match_service_type( self, regex ):
        match = re.search( regex, self.service_type, re.I )
        return bool( match )

    def is_SMS( self ):
        """
        Detect if this bill line is relative to a SMS sending

        Returns:
            True if is a SMS sending otherwise return False
        """

        return self._match_service_type( BillLine.SMS_REGEX )

    def is_internet( self ):
        """
        Detect if this bill line is relative to an internet access

        Returns:
            True if is relative to internet access otherwise return False
        """

        return self._match_service_type( BillLine.INTERNET_REGEX )

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

        return self._match_service_type( BillLine.LONG_DISTANCE_CALL_REGEX )

    def is_local_call( self ):
        """
        Returns:
            True if is a local call  otherwise return False
        """

        return self._match_service_type( BillLine.LOCAL_CALL_REGEX )

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
                duration of this call.

            Raises:
                 If this bill line is not from a call it raise Exception
        """

        if self.is_call():
            return core.Duration.from_string( self.duration )

        raise Exception( "Fail attemp to read duration as call duration" )

    def retrieve_internet_usage( self ):
        """
            Returns:
                An instance of account_profile.core.DigitalDataSize representing the
                internet usage.

            Raises:
                 If this bill line is not from a call it raise Exception
        """

        if self.is_internet():
            return core.DigitalDataSize( self.duration )

        raise Exception( "Fail attemp to read duration as call internet usage" )

    @staticmethod
    def from_csv_line( csv_line ):
        """
        Args:
            csv_line( list ): A list with the line values of csv file
        """
        n_cols = len( csv_line )

        if n_cols != BillLine.CSV_N_COLUMNS:
            raise Exception(
                "The csv file must have %d columns, this file have %d"
                % ( BillLine.CSV_N_COLUMNS, n_cols )
            )

        bline = BillLine(
            csv_line[ BillLine.CSV_PHONE_NUMBER_COLUMN ],
            csv_line[ BillLine.CSV_SERVICE_TYPE_COLUMN ],
            csv_line[ BillLine.CSV_DESTINY_CONLUMN ],
            csv_line[ BillLine.CSV_DURATION_COLUMN ]
        )

        return bline
    @staticmethod
    def is_valid_phone_number( bline ):
        """
        Args:
            bline( account_profile.parser.BillLine ): An instance to verify
            the phone number format

        Returns:
            bool
        """
        match = re.match( BillLine.PHONE_NUMBER_REGEX, bline.phone_number )
        return bool( match )

    @staticmethod
    def load( bill_file_name ):
        file_handler = open( bill_file_name )
        csv_reader = csv.reader( file_handler, delimiter = BillLine.CSV_COLUMN_DELIMITER  )

        bill_lines = [ BillLine.from_csv_line( csv_line ) for csv_line in csv_reader ]
        file_handler.close()

        phone_number_by_bill_lines = dict()
        for bline in filter( BillLine.is_valid_phone_number, bill_lines ):
            if not bline.phone_number in phone_number_by_bill_lines:
                phone_number_by_bill_lines[ bline.phone_number ] = list()

            phone_number_lines = phone_number_by_bill_lines[ bline.phone_number ]
            phone_number_lines.append( bline )

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
                ditital_data_size = line.retrieve_internet_usage()
                profile.add_internet( ditital_data_size )

        return profile

class BillParser( object ):

    def __init__( self, file_name ):
        """
        Args:
            file_name( str ): The file name of the bill to be parsed
        """
        self.phone_by_lines = BillLine.load( file_name )

    def retrieve_phone_profile( self, phone_number ):
        """
        Args:
            phone_number( str ): The phone number to recover the profile from bill parsed

        Returns:
            An instance of account_profile.core.Profile with
            informations relative to phone_number
        """
        if phone_number in self.phone_by_lines:
            lines = self.phone_by_lines[ phone_number ]
            profile = BillLine.mount_profile( lines )
            return profile

        raise Exception(
            "No profile was founded to the number[%s]" % ( phone_number )
        )
