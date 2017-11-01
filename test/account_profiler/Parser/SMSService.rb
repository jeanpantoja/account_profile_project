require "account_profiler/Parser/SMSService"
require "account_profiler/Parser/AccountLine"

describe AccountProfiler::Parser::SMSService do
    context "When detecting if account line is SMS service" do
        it "Should reponse true when account line service description is sms" do
            account_line = AccountProfiler::Parser::AccountLine.new(
                "000-00000-0000",
                "Tim Torpedo",
                "",
                "SC FIXO - AREA 48"
            )
            service = AccountProfiler::Parser::SMSService.new()
            response = service.service?( account_line )
            expect( response ).to eq true
        end

        it "Should reponse true when account line service description is sms" do
            account_line = AccountProfiler::Parser::AccountLine.new(
                "000-00000-0000",
                "  Tim  Torpedo ",
                "",
                "SC FIXO - AREA 48"
            )
            service = AccountProfiler::Parser::SMSService.new()
            response = service.service?( account_line )
            expect( response ).to eq true
        end

        it "Should reponse true when account line service description is sms" do
            account_line = AccountProfiler::Parser::AccountLine.new(
                "000-00000-0000",
                "  tim torpedo",
                "",
                "SC FIXO - AREA 48"
            )
            service = AccountProfiler::Parser::SMSService.new()
            response = service.service?( account_line )
            expect( response ).to eq true
        end
    end
end
