defmodule TopSecret do
  def to_ast(string) do
    Code.string_to_quoted(string)

    case Code.string_to_quoted(string) do
      {:ok, quoted} ->
        quoted

      {:error, reason} ->
        reason
    end
  end

  defp get_arity({_a, _b, c}) when is_list(c), do: c |> length()
  defp get_arity(_), do: 0

  defp get_fname([{a, _b, c}, action]) when a == :when, do: get_fname([List.first(c), action])
  defp get_fname([{a, b, c}, _action]) do
    a
    |> Atom.to_string()
    |> String.slice(0, get_arity({a, b, c}))
  end

  def decode_secret_message_part({:def, b, c}, acc) do
    {{:def, b, c}, [get_fname(c) | acc]}
  end
  def decode_secret_message_part({:defp, b, c}, acc) do
    {{:defp, b, c}, [get_fname(c) | acc]}
  end
  def decode_secret_message_part(ast, acc) do
    {ast, acc}
  end


  defp process_ast(ast, acc) when is_list(ast) do
    Enum.reduce(ast, acc, fn element, current_acc ->
      process_ast(element, current_acc)
    end)
  end

  defp process_ast(ast, acc) when is_tuple(ast) do
    case ast do
      {:do, function_def} ->
        process_ast(function_def, acc)

      {_atom, _metadata, children} when is_list(children) ->
        new_acc = process_ast(children, acc)
        case decode_secret_message_part(ast, []) do
          {_ast, [part | _]} when part != "" ->
            [part | new_acc]
          _ -> new_acc
        end

      _ ->
        case decode_secret_message_part(ast, []) do
          {_ast, [part | _]} when part != "" ->
            [part | acc]
          _ -> acc
        end
    end
  end

  defp process_ast(ast, acc) do
    case decode_secret_message_part(ast, []) do
      {_ast, [part | _]} when part != "" ->
        [part | acc]
      _ -> acc
    end
  end


  def decode_secret_message(string) do
    to_ast(string) |> process_ast([]) |> Enum.reverse() |> Enum.join("")
  end
end
