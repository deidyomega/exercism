defmodule Username do

  defp sanitize_char(char) do
    case char do
      c when c >= 97 and c <= 122 -> c
      c when c == 95 -> c
      c when c == 252 -> [117, 101]
      c when c == 246 -> [111, 101]
      c when c == 228 -> [97, 101]
      c when c == 223 -> [115, 115]
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
