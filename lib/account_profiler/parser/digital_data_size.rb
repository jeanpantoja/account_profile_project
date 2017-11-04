module AccountProfiler
  module Parser
    class DigitalDataSize
      @@BYTE = 1
      @@KILO_BYTE = 1024 * @@BYTE
      @@MEGA_BYTE = 1024 * @@KILO_BYTE

      @@BYTE_UNIT = "B"
      @@KILO_BYTE_UNIT = "KB"
      @@MEGA_BYTE_UNIT = "MB"

      def initialize( n_bytes )
        @n_bytes = n_bytes
      end

      def self.from_string( digital_data_size_text )
        types = [
          DigitalDataType.new( @@BYTE_UNIT, @@BYTE ),
          DigitalDataType.new( @@KILO_BYTE_UNIT, @@KILO_BYTE ),
          DigitalDataType.new( @@MEGA_BYTE_UNIT, @@MEGA_BYTE )
        ]

        for type in types do
          if type.match?( digital_data_size_text )
            n_bytes = type.to_n_bytes( digital_data_size_text )
            return DigitalDataSize.new( n_bytes )
          end
        end

        raise ArgumentError,
          "The digital data size is in an unknown format.
            Accepted formats are '%d[,%d] [ B | KB | MB ]'"
      end

      def length_in_bytes()
        @n_bytes
      end
    end

    class DigitalDataType
      def initialize( unit_text, length_in_bytes )
        @regex = /(\d+)(,(\d+)){0,1}\s*#{unit_text}$/
        @length_in_bytes = length_in_bytes
      end

      def match?( digital_data_text )
        ( digital_data_text =~ @regex ) != nil
      end

      def to_n_bytes( digital_data_text )
        matched = @regex.match( digital_data_text )

        integer_part = matched[ 1 ]
        decimal_part = matched[ 3 ]

        n_units = integer_part.to_i()
        if decimal_part
          decimal_part = decimal_part.tr( ",","" )
          n_units = "#{integer_part}.#{decimal_part}"
          n_units = n_units.to_f()
        end

        n_units * @length_in_bytes
      end
    end
  end
end

