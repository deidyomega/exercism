defmodule KitchenCalculator do
  @type unit :: :cup | :fluid_ounce | :teaspoon | :tablespoon | :milliliter
  @type volume_pair :: {unit(), number()}
  @ratio %{cup: 240, fluid_ounce: 30, teaspoon: 5, tablespoon: 15, milliliter: 1}

  @spec get_volume(volume_pair()) :: number()
  def get_volume({_, v}), do: v

  @spec to_milliliter(volume_pair()) :: volume_pair()
  def to_milliliter({unit, volume}), do: {:milliliter, volume * @ratio[unit]}

  @spec from_milliliter(volume_pair(), unit()) :: volume_pair()
  def from_milliliter({_, volume}, unit), do: {unit, volume / @ratio[unit]}

  @spec convert(volume_pair(), unit()) :: volume_pair()
  def convert(volume_pair, unit), do: volume_pair |> to_milliliter |> from_milliliter(unit)
end
