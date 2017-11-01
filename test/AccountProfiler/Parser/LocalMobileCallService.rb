require "AccountProfiler/Parser/LocalMobileCallService"
require "AccountProfiler/Parser/AccountLine"

describe AccountProfiler::Parser::LocalMobileCallService do
    context "When detecting if account line is local mobile call service" do
        it "Should reponse true when account_line service description
                is local call and destiny is mobile phone" do
            account_line = AccountProfiler::Parser::AccountLine.new(
                "000-00000-0000",
                "Chamadas Locais para Celulares TIM",
                "01m:10s",
                "SC MOVEL TIM - AREA 48"
            )
            service = AccountProfiler::Parser::LocalMobileCallService.new()
            response = service.service?( account_line )
            expect( response ).to eq true
        end

        it "Should reponse true when account_line service description
                is local mobile call" do
            account_line = AccountProfiler::Parser::AccountLine.new(
                "000-00000-0000",
                "Chamadas Locais para Celulares TIM",
                "01m:10s",
                "SC TIM - AREA 48"
            )
            service = AccountProfiler::Parser::LocalMobileCallService.new()
            response = service.service?( account_line )
            expect( response ).to eq true
        end

        it "Should reponse false when account_line service description
                is to long distance" do
            account_line = AccountProfiler::Parser::AccountLine.new(
                "000-00000-0000",
                "Chamadas Longa Distância: Telemar",
                "01m:10s",
                "SC MOVEL TIM - AREA 48"
            )
            service = AccountProfiler::Parser::LocalMobileCallService.new()
            response = service.service?( account_line )
            expect( response ).to eq false
        end

        it "Should reponse false when account_line service description
                is to long distance" do
            account_line = AccountProfiler::Parser::AccountLine.new(
                "000-00000-0000",
                "Chamadas Longa Distância: Telemar",
                "01m:10s",
                "SC FIXO TIM - AREA 48"
            )
            service = AccountProfiler::Parser::LocalMobileCallService.new()
            response = service.service?( account_line )
            expect( response ).to eq false
        end
    end
end
