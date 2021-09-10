"""Example to demonstrate typechecking."""
from typing import NewType

# Use Typed strings and add type annotations

Country = NewType('Country', str)
City = NewType('City', str)

# Case 1: Assigning values that match expected types
valid_country: Country = Country('United States')             # noqa
valid_city: City = City('New York')                           # noqa

# Case 2: Assigning values that DO NOT match expected types
invalid_country: Country = City('United States')              # noqa
invalid_city: City = Country('New York')                      # noqa















