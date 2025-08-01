defmodule RemoteControlCar do
  @enforce_keys [:nickname]
  defstruct [:nickname, battery_percentage: 100,  distance_driven_in_meters: 0]


  def new(), do: new("none")
  def new(nickname), do: %RemoteControlCar{nickname: nickname}

  def display_distance(%RemoteControlCar{distance_driven_in_meters: distance}), do: "#{distance} meters"

  def display_battery(%RemoteControlCar{battery_percentage: bat}) do
    if bat == 0 do
      "Battery empty"
    else
      "Battery at #{bat}%"
    end
  end
  def drive(%RemoteControlCar{} = remote_car) do
    if remote_car.battery_percentage == 0 do
      remote_car
    else
      %RemoteControlCar{
        nickname: remote_car.nickname,
        battery_percentage: remote_car.battery_percentage - 1,
        distance_driven_in_meters: remote_car.distance_driven_in_meters + 20
      }
    end
  end
end
