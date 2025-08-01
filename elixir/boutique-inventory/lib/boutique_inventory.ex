defmodule BoutiqueInventory do

  def sort_by_price(inventory), do: inventory |> Enum.sort_by &(&1.price)

  def with_missing_price(inventory), do: inventory |> Enum.filter &(&1.price == nil)

  def update_names(inventory, old_word, new_word) do
    inventory |> Enum.map &( %{ &1 | name: String.replace(&1.name, old_word, new_word) } )
  end

  def increase_quantity(item, count) do
    qbs = Map.new(item.quantity_by_size, fn {key, val} -> {key, val + count} end)
    %{item | quantity_by_size: qbs }
  end

  def total_quantity(item) do
    item.quantity_by_size
    |> Enum.reduce(0, fn {_key, val}, acc -> acc + val end)
  end
end
