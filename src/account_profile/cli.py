# -*- coding: utf-8 -*-

"""
Command Line Interface Module
"""
import argparse
import json
import account_profile.parser

class CommandLineArgs( object ):

    def __init__( self ):
        parser = argparse.ArgumentParser(
            description = 'Command line interface to bill profiler.'
        )

        parser.add_argument( 'file_name',
                help='The file name of bill to read' )

        parser.add_argument( 'phone_number',
                help='The phone number in the bill to create the profile' )

        self.args = parser.parse_args()

    def get_file_name( self ):
        return self.args.file_name

    def get_phone_number( self ):
        return self.args.phone_number

class Program( object ):

    def run( self ):
        try:
            args = CommandLineArgs()
            parser = account_profile.parser.BillParser( args.get_file_name() )
            profile = parser.retrieve_phone_profile( args.get_phone_number() )
            Program.display_profile_as_json( profile )
        except Exception as e:
            print( "An error happened. See message detail: %s" % ( e ) )
            quit( 1 )

    @staticmethod
    def display_profile_as_json( profile ):
        profile_dict= {
            "calls" : {
                "Local" : {
                    "mobile" : "%f minutes" % ( profile.get_local_mobile_call_usage() ),
                    "landline" : "%f minutes" % ( profile.get_local_landline_call_usage() )
                },
                "Long Distance" : {
                    "mobile" : "%f minutes" % ( profile.get_long_distance_mobile_call_usage() ),
                    "landline" : "%f minutes" % ( profile.get_long_distance_landline_call_usage() )
                },
            },
            "SMS":"%d und" % ( profile.get_SMS_usage() ),
            "Internet" :"%f B" % ( profile.get_internet_usage() )
        }

        profile_json = json.dumps( profile_dict, indent = 4 )
        print( profile_json )

