defmodule TopSecret do
  def to_ast(string) do
    Code.string_to_quoted!(string)
  end

  def decode_secret_message_part({op, _, args} = ast, acc) when op in [:def, :defp] do
    {name, args} = name_and_args(args)
    name_slice = String.slice(to_string(name), 0, length(args))
    {ast, [name_slice | acc]}
  end

  def decode_secret_message_part(ast, acc) do
    {ast, acc}
  end

  defp name_and_args([{:when, _, args} | _]) do
    name_and_args(args)
  end

  defp name_and_args([{name, _, args} | _]) when is_list(args) do
    {name, args}
  end

  defp name_and_args([{name, _, args} | _]) when is_atom(args) do
    {name, []}
  end

  def decode_secret_message(string) do
    ast = to_ast(string)
    {_, acc} = Macro.prewalk(ast, [], &decode_secret_message_part/2)

    acc
    |> Enum.reverse()
    |> Enum.join("")
  end
end
