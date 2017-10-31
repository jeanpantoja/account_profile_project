$LOAD_PATH << '.'

require "csv"
require "json"

require "AccountProfiler/Parser/AccountLine"
require "AccountProfiler/Parser/LongDistanceMobileCallService"
require "AccountProfiler/Parser/LongDistanceLandlineCallService"
require "AccountProfiler/Parser/LocalMobileCallService"
require "AccountProfiler/Parser/LocalLandlineCallService"
require "AccountProfiler/Parser/SMSService"
require "AccountProfiler/Parser/InternetService"

require "AccountProfiler/Profile/Profiler"


sms = 0
internet = 0
ld_mobile = 0
ld_landline = 0
l_mobile = 0
l_landline = 0

account_lines = []

CSV.foreach( "/home/jean/dev/minerator/sample-tim.csv", col_sep: ";" ) do |row|
    account_line = AccountProfiler::Parser::AccountLine.from_array( row )
    if account_line.phone_number && account_line.phone_number.strip() != ""
        account_lines[ account_lines.size() ] = account_line
    end
end

services = [
    AccountProfiler::Parser::InternetService.new(),
    AccountProfiler::Parser::SMSService.new(),
    AccountProfiler::Parser::LocalMobileCallService.new(),
    AccountProfiler::Parser::LocalLandlineCallService.new(),
    AccountProfiler::Parser::LongDistanceMobileCallService.new(),
    AccountProfiler::Parser::LongDistanceLandlineCallService.new(),
]

def to_dict( account_line )
    dict = {
        :phone_number => account_line.phone_number,
        :service_description => account_line.service_description,
        :destiny => account_line.destiny,
        :duration => account_line.duration
    }
    #return dict
    return account_line
end

def print_line( account_line )
    puts" #{account_line.phone_number} #{account_line.service_description} #{account_line.destiny} #{account_line.duration}"
end

output = {
    :sms => [],
    :internet =>[],
    :ld_mobile =>[],
    :ld_lanline => [],
    :l_mobile => [],
    :l_landline => [],
    :no_group => []
}

account_lines.each do |account_line|

    internet = AccountProfiler::Parser::InternetService.new()
    sms = AccountProfiler::Parser::SMSService.new()
    lmobile = AccountProfiler::Parser::LocalMobileCallService.new()
    llandline = AccountProfiler::Parser::LocalLandlineCallService.new()
    ldmobile = AccountProfiler::Parser::LongDistanceMobileCallService.new()
    ldlandline = AccountProfiler::Parser::LongDistanceLandlineCallService.new()

    if internet.service?( account_line )
       # print_line( account_line )
        output[ :internet ][ output[ :internet ].size() ] = to_dict( account_line )
    elsif sms.service?( account_line )
       # print_line( account_line )
        output[ :sms ][ output[ :sms ].size() ] = to_dict( account_line )
    elsif lmobile.service?( account_line )
       # print_line( account_line )
        output[ :l_mobile ][ output[ :l_mobile ].size() ] = to_dict( account_line )
    elsif llandline.service?( account_line )
        #print_line( account_line )
       output[ :l_landline ][ output[ :l_landline ].size() ] = to_dict( account_line )
    elsif ldmobile.service?( account_line )
        #print_line( account_line )
    elsif ldlandline.service?( account_line )
        print_line( account_line )
    else
#        print_line( account_line )
        output[ :no_group ][ output[ :no_group ].size() ] = to_dict( account_line )
    end
end

#output[ :no_group ].each do |acc|
#    print_line( acc )
#end
