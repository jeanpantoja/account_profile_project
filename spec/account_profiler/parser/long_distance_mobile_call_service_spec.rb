require "account_profiler/parser/long_distance_mobile_call_service"
require "account_profiler/parser/account_line"

describe AccountProfiler::Parser::LongDistanceMobileCallService do
  context "When detecting if account line is long distance mobile call service" do
    it "Should reponse true when account_line service description
      is long distance call and destiny is mobile phone" do
      account_line = AccountProfiler::Parser::AccountLine.new(
        "000-00000-0000",
        "Chamadas Longa Distância: TIM LD 41",
        "01m:10s",
        "SC MOVEL TIM - AREA 48"
      )
      service = AccountProfiler::Parser::LongDistanceMobileCallService.new()
      response = service.service?( account_line )
      expect( response ).to eq true
    end

    it "Should reponse false when account_line service description
      is to local call" do
      account_line = AccountProfiler::Parser::AccountLine.new(
        "000-00000-0000",
        "Chamadas Locais para Outros Telefones Fixos",
        "01m:10s",
        "SC FIXO TIM - AREA 48"
      )
      service = AccountProfiler::Parser::LongDistanceMobileCallService.new()
      response = service.service?( account_line )
      expect( response ).to eq false
    end

    it "Should reponse false when account_line service description
      is to local call" do
      account_line = AccountProfiler::Parser::AccountLine.new(
        "000-00000-0000",
        "Chamadas Locais para Outros Telefones Fixos",
        "01m:10s",
        "SC FIXO TIM - AREA 48"
      )
      service = AccountProfiler::Parser::LongDistanceMobileCallService.new()
      response = service.service?( account_line )
      expect( response ).to eq false
    end
  end
end

