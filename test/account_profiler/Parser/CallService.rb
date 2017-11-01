require "account_profiler/Parser/CallService"
require "account_profiler/Parser/AccountLine"

describe AccountProfiler::Parser::CallService do
    context "When detecting if account line is call service" do
        it "Should reponse true when account_line service description
                is from local call" do
            account_line = AccountProfiler::Parser::AccountLine.new(
                "000-00000-0000",
                "Chamadas Locais para Celulares TIM",
                "01m:10s",
                "SC MOVEL TIM - AREA 48"
            )
            service = AccountProfiler::Parser::CallService.new()
            response = service.service?( account_line )
            expect( response ).to eq true
        end

        it "Should reponse true when account_line service description is
                from long distance call" do
            account_line = AccountProfiler::Parser::AccountLine.new(
                "000-00000-0000",
                "Chamadas Longa Distância: Embratel",
                "01m:10s",
                "SC MOVEL TIM - AREA 48"
            )
            service = AccountProfiler::Parser::CallService.new()
            response = service.service?( account_line )
            expect( response ).to eq true
        end
    end

    context "When detecting if account line is local call" do
        it "Should reponse true when account_line service description
                is from local call" do
            account_line = AccountProfiler::Parser::AccountLine.new(
                "000-00000-0000",
                "Chamadas Locais para Celulares TIM",
                "01m:10s",
                "SC MOVEL TIM - AREA 48"
            )
            service = AccountProfiler::Parser::CallService.new()
            response = service.is_local?( account_line )
            expect( response ).to eq true
        end
    end

    context "When detecting if account line is long distance call" do
        it "Should reponse true when account_line service description
                is from long distance" do
            account_line = AccountProfiler::Parser::AccountLine.new(
                "000-00000-0000",
                "Chamadas Longa Distância: Embratel",
                "01m:10s",
                "SC MOVEL TIM - AREA 48"
            )
            service = AccountProfiler::Parser::CallService.new()
            response = service.is_long_distance?( account_line )
            expect( response ).to eq true
        end
    end

    context "When detecting if account line is mobile call" do
        it "Should reponse true when account_line service description
                is mobile call" do
            account_line = AccountProfiler::Parser::AccountLine.new(
                "000-00000-0000",
                "Chamadas Locais para Celulares TIM",
                "01m:10s",
                ""
            )
            service = AccountProfiler::Parser::CallService.new()
            response = service.is_destiny_mobile?( account_line )
            expect( response ).to eq true
        end

        it "Should reponse true when account_line destiny
                is mobile" do
            account_line = AccountProfiler::Parser::AccountLine.new(
                "000-00000-0000",
                "Chamadas Longa Distância: Embratel",
                "01m:10s",
                "SC MOVEL TIM - AREA 48"
            )
            service = AccountProfiler::Parser::CallService.new()
            response = service.is_destiny_mobile?( account_line )
            expect( response ).to eq true
        end

        it "Should reponse true when account_line destiny
                is mobile and service description is from mobile" do
            account_line = AccountProfiler::Parser::AccountLine.new(
                "000-00000-0000",
                "Chamadas Locais para Celulares TIM",
                "01m:10s",
                "SC MOVEL TIM - AREA 48"
            )
            service = AccountProfiler::Parser::CallService.new()
            response = service.is_destiny_mobile?( account_line )
            expect( response ).to eq true
        end
    end

    context "When detecting if account line is landline call" do
        it "Should reponse true when account_line service description
                is landline call" do
            account_line = AccountProfiler::Parser::AccountLine.new(
                "000-00000-0000",
                "Chamadas Locais para Telefones Fixos",
                "01m:10s",
                ""
            )
            service = AccountProfiler::Parser::CallService.new()
            response = service.is_destiny_landline?( account_line )
            expect( response ).to eq true
        end

        it "Should reponse true when account_line destiny
                is landline" do
            account_line = AccountProfiler::Parser::AccountLine.new(
                "000-00000-0000",
                "Chamadas Longa Distância: Embratel",
                "01m:10s",
                "RS FIXO - AREA 51"
            )
            service = AccountProfiler::Parser::CallService.new()
            response = service.is_destiny_landline?( account_line )
            expect( response ).to eq true
        end

        it "Should reponse true when account_line destiny
                is landline and service description is landline call" do
            account_line = AccountProfiler::Parser::AccountLine.new(
                "000-00000-0000",
                "Chamadas Locais para Telefones Fixos",
                "01m:10s",
                "RS FIXO - AREA 51"
            )
            service = AccountProfiler::Parser::CallService.new()
            response = service.is_destiny_landline?( account_line )
            expect( response ).to eq true
        end
    end
end
