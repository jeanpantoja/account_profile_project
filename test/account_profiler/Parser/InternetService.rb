require "account_profiler/Parser/InternetService"
require "account_profiler/Parser/AccountLine"

describe AccountProfiler::Parser::InternetService do
    context "When detecting if account line is internet service" do
        it "Should reponse true when account_line service description is internet" do
            account_line = AccountProfiler::Parser::AccountLine.new(
                "000-00000-0000",
                "TIM Connect Fast",
                "",
                "SC FIXO - AREA 48"
            )
            service = AccountProfiler::Parser::InternetService.new()
            response = service.service?( account_line )
            expect( response ).to eq true
        end

        it "Should reponse true when account_line service description is internet" do
            account_line = AccountProfiler::Parser::AccountLine.new(
                "000-00000-0000",
                "TIM Wap Fast",
                "",
                "SC FIXO - AREA 48"
            )
            service = AccountProfiler::Parser::InternetService.new()
            response = service.service?( account_line )
            expect( response ).to eq true
        end

        it "Should reponse true when account_line service description is internet" do
            account_line = AccountProfiler::Parser::AccountLine.new(
                "000-00000-0000",
                "BlackBerry Professional - MB",
                "",
                "SC FIXO - AREA 48"
            )
            service = AccountProfiler::Parser::InternetService.new()
            response = service.service?( account_line )
            expect( response ).to eq true
        end
    end
end
