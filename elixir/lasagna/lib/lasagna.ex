defmodule Lasagna do
  @spec expected_minutes_in_oven :: 40
  def expected_minutes_in_oven() do
    40
  end

  @spec remaining_minutes_in_oven(integer()) :: integer()
  def remaining_minutes_in_oven(time_in_oven) do
    expected_minutes_in_oven() - time_in_oven
  end

  @spec preparation_time_in_minutes(integer()) :: integer()
  def preparation_time_in_minutes(layers) do
    layers * 2
  end

  @spec total_time_in_minutes(integer(), integer()) :: integer()
  def total_time_in_minutes(layers, time_in_oven) do
    preparation_time_in_minutes(layers) + expected_minutes_in_oven() - remaining_minutes_in_oven(time_in_oven)
  end

  @spec alarm :: String.t()
  def alarm() do
    "Ding!"
  end
end
