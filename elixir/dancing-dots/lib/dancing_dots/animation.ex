defmodule DancingDots.Animation do
  @type dot :: DancingDots.Dot.t()
  @type opts :: keyword
  @type error :: any
  @type frame_number :: pos_integer

  @callback init(opts()) :: {:ok, opts()} | {:error, error()}
  @callback handle_frame(dot(), frame_number(), opts()) :: dot()

  defmacro __using__(_opts) do
    quote do
      @behaviour DancingDots.Animation
      def init(opts), do: {:ok, opts}
      defoverridable [init: 1]
    end
  end
end

defmodule DancingDots.Flicker do
  use DancingDots.Animation

  @impl DancingDots.Animation
  def handle_frame(dot, frame_number, _opts) do
    case rem(frame_number, 4) do
      0 ->
        %{dot | opacity: dot.opacity * 0.5}
      _ ->
        dot
    end
  end
end

defmodule DancingDots.Zoom do
  use DancingDots.Animation

  @impl DancingDots.Animation
  def init([velocity: velocity]) when is_number(velocity), do: {:ok, [velocity: velocity]}
  def init(opts), do: {:error,  "The :velocity option is required, and its value must be a number. Got: #{inspect(Keyword.get(opts, :velocity))}"}

  @impl DancingDots.Animation
  def handle_frame(dot, frame_number, opts) do
    frame_number = frame_number - 1
    case frame_number do
      0 ->
        dot
      _ ->
        %{ dot | radius: dot.radius + opts[:velocity] * frame_number }
    end
  end

end
