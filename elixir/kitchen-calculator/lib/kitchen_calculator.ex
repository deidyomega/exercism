defmodule KitchenCalculator do
  @vol %{cup: 240, fluid_ounce: 30, teaspoon: 5, tablespoon: 15, milliliter: 1}

  def get_volume({_, v}), do: v

  def to_milliliter({unit, volume}), do: {:milliliter, volume * @vol[unit]}

  def from_milliliter({_, volume}, unit), do: {unit, volume / @vol[unit]}

  def convert(volume_pair, unit), do: volume_pair |> to_milliliter |> from_milliliter(unit)
end
