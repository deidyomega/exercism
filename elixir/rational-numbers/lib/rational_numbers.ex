defmodule RationalNumbers do
  @type rational :: {integer, integer}

  @doc """
  Add two rational numbers
  """
  @spec add(a :: rational, b :: rational) :: rational
  def add({a1, b1}, {a2, b2}), do: { a1 * b2 + a2 * b1, b1 * b2 } |> reduce

  @doc """
  Subtract two rational numbers
  """
  @spec subtract(a :: rational, b :: rational) :: rational
  def subtract({a1, b1}, {a2, b2}), do: {(a1 * b2) - (a2 * b1), b1 * b2} |> reduce

  
  @doc """
  Multiply two rational numbers
  """
  @spec multiply(a :: rational, b :: rational) :: rational
  def multiply({a1, b1}, {a2, b2}), do: {a1 * a2, b1 * b2} |> reduce

  @doc """
  Divide two rational numbers
  """
  @spec divide_by(num :: rational, den :: rational) :: rational
  def divide_by({a1, b1}, {a2, b2}), do: {a1 * b2, a2 * b1} |> reduce

  @doc """
  Absolute value of a rational number
  """
  @spec abs(a :: rational) :: rational
  def abs({a, b}), do: {Kernel.abs(a), Kernel.abs(b)} |> reduce

  @doc """
  Exponentiation of a rational number by an integer
  """
  @spec pow_rational(a :: rational, n :: integer) :: rational
  def pow_rational({a1, b1}, n) when n < 0 do
    na = Kernel.abs(n)
    {Integer.pow(b1, na), Integer.pow(a1, na)} |> reduce
  end
  def pow_rational({a1, b1}, n), do: {Integer.pow(a1, n), Integer.pow(b1,n)} |> reduce

  @doc """
  Exponentiation of a real number by a rational number
  """
  @spec pow_real(x :: integer, n :: rational) :: float
  def pow_real(x, {a1, b1}), do: :math.pow(x, a1/b1)

  defp gcd(a, 0) when is_integer(a), do: a
  defp gcd(a, b), do: gcd(b, rem(a, b))

  @doc """
  Reduce a rational number to its lowest terms
  """
  @spec reduce(a :: rational) :: rational
  def reduce({a, b}) when b < 0, do: {-a, -b} |> reduce
  def reduce({a, b}) do
    common_divisor = gcd(Kernel.abs(a), Kernel.abs(b))
    {div(a, common_divisor), div(b, common_divisor)}
  end
end
