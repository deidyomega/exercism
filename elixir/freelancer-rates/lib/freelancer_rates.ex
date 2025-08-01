defmodule FreelancerRates do
  @daily_rate 8.0
  @monthly_billable_days 22

  @spec daily_rate(number()) :: float()
  def daily_rate(hourly_rate), do: hourly_rate * @daily_rate

  @spec apply_discount(number(), number()) :: float()
  def apply_discount(before_discount, discount), do: before_discount * (1 - discount / 100)

  @spec daily_discounted_rate(number(), number()) :: float()
  defp daily_discounted_rate(hourly_rate, discount) do
    hourly_rate
    |> daily_rate
    |> apply_discount(discount)
  end

  @spec monthly_rate(number(), number()) :: integer()
  def monthly_rate(hourly_rate, discount) do
    daily_discounted_rate(hourly_rate, discount) * @monthly_billable_days
    |> ceil
  end

  @spec days_in_budget(number(), number(), number()) :: float()
  def days_in_budget(budget, hourly_rate, discount) do
    budget / daily_discounted_rate(hourly_rate, discount)
    |> Float.floor(1)
  end
end
