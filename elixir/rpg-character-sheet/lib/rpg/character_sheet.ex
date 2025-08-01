defmodule RPG.CharacterSheet do
  def welcome() do
    IO.puts("Welcome! Let's fill out your character sheet together.")
  end

  defp ask(thing), do: IO.gets(thing) |> String.trim

  def ask_name(), do: ask("What is your character's name?\n")
  def ask_class(), do: ask("What is your character's class?\n")
  def ask_level(), do: ask("What is your character's level?\n") |> String.to_integer
  
  def run() do
    welcome()
    IO.inspect(%{
      name: ask_name(),
      class: ask_class(),
      level: ask_level()
    }, label: "Your character")
  end
end
