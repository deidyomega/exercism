defmodule RPG.CharacterSheet do
  def welcome(), do: IO.puts("Welcome! Let's fill out your character sheet together.")

  defp ask(thing), do: IO.gets("What is your character's #{thing}?\n") |> String.trim
  def ask_name(), do: ask("name")
  def ask_class(), do: ask("class")
  def ask_level(), do: ask("level") |> String.to_integer
  
  def run() do
    welcome()
    IO.inspect(%{
      name: ask_name(),
      class: ask_class(),
      level: ask_level()
    }, label: "Your character")
  end
end
