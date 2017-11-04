require "account_profiler/parser/AccountReader"

def create_account_line( phone_number, service_description, destiny, duration )
    line = [
            "", "", "", phone_number, "",
            "", service_description, "", "", "",
            destiny, "", "", duration, "",
            "", "", "", "", "",
            "", "", "", "", ""
    ]
    return line
end

describe AccountProfiler::Parser::AccountReader do
    context "When testing build_profiler" do
        it "The profiler constructed must match the data read" do
            lines = [
                #internet 2048 bytes
                create_account_line(
                    "111-1111-1111", "TIM Wap Fast", "", "1 KB"
                ),
                create_account_line(
                    "111-1111-1111", "TIM Wap Fast", "", "1 KB"
                ),
                #sms 2
                create_account_line(
                    "111-1111-1111", "TIM Torpedo", "TIM - AREA 83", ""
                ),
                create_account_line(
                    "111-1111-1111", "TIM Torpedo", "TIM - AREA 83", ""
                ),
                #local mobile call 3min
                create_account_line(
                    "111-1111-1111", "Chamadas Locais para Celulares",
                    "TIM - AREA 83", "01m30s"
                ),
                create_account_line(
                    "111-1111-1111", "Chamadas Locais para Celulares",
                    "TIM - AREA 83", "01m30s"
                ),
                #local landline call 4.5min
                create_account_line(
                    "111-1111-1111", "Chamadas Locais para Outros Telefones",
                    "SC FIXO - AREA 48", "01m30s"
                ),
                create_account_line(
                    "111-1111-1111", "Chamadas Locais para Outros Telefones",
                    "SC FIXO - AREA 48", "03m00s"
                ),
                #long distance  mobile call 2.5
                create_account_line(
                    "111-1111-1111", "Chamadas Longa Distância: TIM LD",
                    "RS MOVEL - AREA 51", "01m30s"
                ),
                create_account_line(
                    "111-1111-1111", "Chamadas Longa Distância: TIM LD",
                    "RS MOVEL - AREA 51", "01m00s"
                ),
                #long distance landline call 5.5min
                create_account_line(
                    "111-1111-1111", "Chamadas Longa Distância: TIM LD 41",
                    "SC FIXO - AREA 48", "01m30s"
                ),
                create_account_line(
                    "111-1111-1111", "Chamadas Longa Distância: TIM LD 41",
                    "SC FIXO - AREA 48", "04m00s"
                ),
            ]

            reader = AccountProfiler::Parser::AccountReader.new()
            profiler = reader.build_profiler( lines )
            resumed_profile = profiler.resume( "111-1111-1111" )
            call = resumed_profile.call_usage_profile

            expect( resumed_profile.sms_usage ).to eq 2
            expect( resumed_profile.internet_usage ).to eq 2048
            expect( call.local_mobile ).to eq 3
            expect( call.local_landline ).to eq 4.5
            expect( call.long_distance_mobile ).to eq 2.5
            expect( call.long_distance_landline ).to eq 5.5
        end
    end
end
