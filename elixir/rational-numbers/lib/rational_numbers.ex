defmodule RationalNumbers do
  def add({a1, b1}, {a2, b2}), do: { a1 * b2 + a2 * b1, b1 * b2 } |> reduce
  def subtract({a1, b1}, {a2, b2}), do: {(a1 * b2) - (a2 * b1), b1 * b2} |> reduce
  def multiply({a1, b1}, {a2, b2}), do: {a1 * a2, b1 * b2} |> reduce
  def divide_by({a1, b1}, {a2, b2}), do: {a1 * b2, a2 * b1} |> reduce
  def abs({a, b}), do: {Kernel.abs(a), Kernel.abs(b)} |> reduce
  def pow_rational({a1, b1}, n) when n < 0, do: {b1 ** Kernel.abs(n), a1 ** Kernel.abs(n)} |> reduce
  def pow_rational({a1, b1}, n), do: {a1 ** n, b1 ** n} |> reduce
  def pow_real(x, {a1, b1}), do: :math.pow(x, a1/b1)
  def reduce({a, b}) when b < 0, do: {-a, -b} |> reduce
  def reduce({a, b}), do: {div(a, Integer.gcd(a, b)), div(b, Integer.gcd(a, b))}
end