defmodule LogLevel do
  @log_labels [:trace, :debug, :info, :warning, :error, :fatal]

  @spec to_label(integer(), boolean()) :: :trace | :debug | :info | :warning | :error | :fatal | :unknown
  def to_label(level, false) when level in 0..5, do: Enum.at(@log_labels, level)
  def to_label(level, true) when level in 1..4, do: Enum.at(@log_labels, level)
  def to_label(_, _), do: :unknown


  @spec alert_recipient(integer(), boolean()) :: :dev1 | :dev2 | false | :ops
  def alert_recipient(level, legacy?) do
    case to_label(level, legacy?) do
      label when label in [:error, :fatal] -> :ops
      :unknown -> if legacy?, do: :dev1, else: :dev2
      _ -> false
    end
  end
end
