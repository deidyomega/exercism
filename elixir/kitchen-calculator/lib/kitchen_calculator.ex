defmodule KitchenCalculator do
  def get_volume({_, v}), do: v

  def to_milliliter(volume_pair) when elem(volume_pair, 0) == :milliliter, do: volume_pair
  def to_milliliter({:cup, volume}), do: {:milliliter, volume * 240}
  def to_milliliter({:fluid_ounce, volume}), do: {:milliliter, volume * 30}
  def to_milliliter({:teaspoon, volume}), do: {:milliliter, volume * 5}
  def to_milliliter({:tablespoon, volume}), do: {:milliliter, volume * 15}

  def from_milliliter({_, volume}, :milliliter), do: {:milliliter, volume}
  def from_milliliter({_, volume}, :cup), do: {:cup, volume / 240.0}
  def from_milliliter({_, volume}, :fluid_ounce), do: {:fluid_ounce, volume / 30}
  def from_milliliter({_, volume}, :teaspoon), do: {:teaspoon, volume / 5}
  def from_milliliter({_, volume}, :tablespoon), do: {:tablespoon, volume / 15}

  def convert({vp_unit, volume}, unit) when vp_unit == unit, do: volume
  def convert(volume_pair, unit) do
    volume_pair
    |> to_milliliter
    |> from_milliliter(unit)
  end
end
