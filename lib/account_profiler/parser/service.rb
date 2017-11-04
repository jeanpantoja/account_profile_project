module AccountProfiler
  module Parser
    class Service
      def initialize( type_regex )
        @type_regex = type_regex
      end

      def service?( account_line )
        account_line.match_service_description?( @type_regex )
      end

      def get_usage_profile( account_line )
        raise "Not implemented yet"
      end
    end
  end
end

