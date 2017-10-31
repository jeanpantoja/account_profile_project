require "csv"
require "json"

require "AccountProfiler/Parser/AccountReader"

module AccountProfiler
    module Cli
        class Program
            def run()
                begin
                    args = load_args()
                    csv_file_path = args[ "csv_file" ]
                    phone_number = args[ "phone_number" ]

                    profiler = AccountProfiler::Parser::AccountReader.build_profiler_from_csv(
                        csv_file_path
                    )

                    profile = profiler.resume( phone_number )
                    json_text = create_profile_json( profile, phone_number )
                    puts json_text
                rescue StandardError=>e
                    puts "Error: #{e}"
                    exit
                end
            end

            def load_args()
                if ARGV.length < 2
                    raise "
                        The program must csv_file and phone_number
                        in this order as argument
                    "
                end

                args = {
                    "csv_file" => ARGV[ 0 ],
                    "phone_number"  => ARGV[ 1 ]
                }
                return args
            end

            def create_profile_json( usage_profile, phone_number )
                profile_dict = {
                    :phone_number => phone_number,
                    :profile => {
                        :sms_usage => "#{usage_profile.sms_usage} und",
                        :internet_usage => "#{usage_profile.internet_usage} bytes",
                        :call => {
                            :local => {
                                :mobile => "#{usage_profile.local_mobile_call_usage} min",
                                :landline => "#{usage_profile.local_landline_call_usage} min"
                            },
                            :long_distante => {
                                :mobile => "#{usage_profile.long_distance_mobile_call_usage} min",
                                :landline => "#{usage_profile.long_distance_landline_call_usage} min"
                            }
                        }
                    }
                }

                return JSON.pretty_generate( profile_dict )
            end
        end
    end
end
