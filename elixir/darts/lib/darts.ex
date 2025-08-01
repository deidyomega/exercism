defmodule Darts do
  @type position :: {number, number}

  @doc """
  Calculate the score of a single dart hitting a target
  """
  @spec score(position) :: integer
  def score({x, y}) do
    v = ceil(:math.sqrt(x * x + y * y))

    cond do
      v > 10 -> 0
      v > 5 -> 1
      v > 1 -> 5
      v >= 0 -> 10
      true -> -1
    end

  end
end
