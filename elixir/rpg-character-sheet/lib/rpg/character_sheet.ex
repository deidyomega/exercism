defmodule RPG.CharacterSheet do
  def welcome() do
    IO.puts("Welcome! Let's fill out your character sheet together.")
    :ok
  end

  defp ask(thing), do: IO.gets(thing) |> String.trim

  def ask_name(), do: ask("What is your character's name?\n")
  def ask_class(), do: ask("What is your character's class?\n")
  def ask_level(), do: ask("What is your character's level?\n") |> String.to_integer
  
  def run() do
    welcome()
    char = %{
      name: ask_name(),
      class: ask_class(),
      level: ask_level()
    }
    IO.puts("Your character: #{inspect(char)}")
    char
  end
end
