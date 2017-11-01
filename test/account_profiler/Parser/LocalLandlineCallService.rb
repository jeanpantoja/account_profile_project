require "account_profiler/Parser/LocalLandlineCallService"
require "account_profiler/Parser/AccountLine"

describe AccountProfiler::Parser::LocalLandlineCallService do
    context "When detecting if account line is locallandline call service" do
        it "Should reponse true when account_line service description
                is local landline call and destiny is landline phone" do
            account_line = AccountProfiler::Parser::AccountLine.new(
                "000-00000-0000",
                "Chamadas Locais para Telefones Fixos",
                "01m:10s",
                "SC FIXO - AREA 48"
            )
            service = AccountProfiler::Parser::LocalLandlineCallService.new()
            response = service.service?( account_line )
            expect( response ).to eq true
        end

    it "Should reponse true when account_line service description
                is local landline call and destiny is landline phone" do
            account_line = AccountProfiler::Parser::AccountLine.new(
                "000-00000-0000",
                "Chamadas Locais",
                "01m:10s",
                "SC FIXO - AREA 48"
            )
            service = AccountProfiler::Parser::LocalLandlineCallService.new()
            response = service.service?( account_line )
            expect( response ).to eq true
        end

        it "Should reponse true when account_line service description
                is local landline call" do
            account_line = AccountProfiler::Parser::AccountLine.new(
                "000-00000-0000",
                "Chamadas Locais para Telefones Fixos",
                "01m:10s",
                "SC TIM - AREA 48"
            )
            service = AccountProfiler::Parser::LocalLandlineCallService.new()
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
            service = AccountProfiler::Parser::LocalLandlineCallService.new()
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
            service = AccountProfiler::Parser::LocalLandlineCallService.new()
            response = service.service?( account_line )
            expect( response ).to eq false
        end
    end
end
