defmodule Username do

  defp sanitize_char(char) do
    case char do
      c when c >= ?a and c <= ?z -> c
      c when c == ?_ -> c
      c when c == ?ü -> [117, 101]
      c when c == ?ö -> [111, 101]
      c when c == ?ä -> [97, 101]
      c when c == ?ß -> [115, 115]
      _ -> nil
    end
  end

  @spec sanitize(charlist) :: charlist
  def sanitize(~c""), do: []
  def sanitize(list) do
    Enum.map(list, &sanitize_char/1)
    |> List.flatten
    |> Enum.filter(& &1 != nil)
  end

end
