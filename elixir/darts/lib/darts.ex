defmodule Darts do
  @type position :: {number, number}

  @doc """
  Calculate the score of a single dart hitting a target
  """
  @spec score(position) :: integer
  def score({x, y}) when abs(x) > 10 or abs(y) > 10, do: 0
  def score({x, y}) when abs(x) < 0.7 and abs(y) < 0.7, do: 10
  def score({x, y}) do
    distance = :math.sqrt(x * x + y * y)

    cond do
      distance > 10 -> 0
      distance > 5 -> 1
      distance > 1 -> 5
      true -> 10
    end

  end
end
