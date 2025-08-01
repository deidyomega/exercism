defmodule Username do
  def sanitize([]), do: []
  def sanitize([h | t]) do
    cleaned = case h do
      ?_ -> ~c"_"
      ?ß -> ~c"ss"
      ?ä -> ~c"ae"
      ?ö -> ~c"oe"
      ?ü -> ~c"ue"
      c when c >= ?a and c <= ?z -> [c]
      _ -> ~c''
    end
    cleaned ++ sanitize(t)
  end

end
