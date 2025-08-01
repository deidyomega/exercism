defmodule BirdCount do
  def today([head | _tail]), do: head
  def today([]), do: nil

  def increment_day_count([head | tail]) do
    [head + 1 | tail]
  end
  def increment_day_count([]) do
    [1]
  end

  def has_day_without_birds?(list) do
    Enum.any?(list, fn x -> x == 0 end)
  end

  def total(list) do
    Enum.sum(list)
  end

  @spec busy_days(any()) :: nil
  def busy_days(list) do
    Enum.count(list, fn x -> x >= 5 end)
  end
end
