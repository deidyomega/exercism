defmodule NameBadge do
  defp dept(department) do
    if department do
      String.upcase(department)
    else
      "OWNER"
    end
  end

  def print(id, name, department) do
    if id do
      "[#{id}] - #{name} - #{dept(department)}"
    else
      "#{name} - #{dept(department)}"
    end
    
  end
end
