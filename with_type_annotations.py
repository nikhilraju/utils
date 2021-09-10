"""Example to demonstrate typechecking."""
from typing import NewType

# Use Typed strings and add type annotations

Country = NewType('Country', str)
City = NewType('City', str)

# Case 1: Assigning values that match expected types
valid_country: Country = Country('United States') # noqa
valid_city: City = City('New York') # noqa

# Case 2: Assigning values that DO NOT match expected types -> Will throw error
invalid_country: Country = City('United States') # noqa
invalid_city: City = Country('New York') # noqa

# Case 3: Assigning regular strings -> Will throw error
another_valid_country: Country = 'France' # noqa
another_valid_city: City = 'Paris' # noqa

# Case 4: Define types but don't use them -> Won't throw error
another_invalid_country: str = 'Paris' # noqa
another_invalid_city: str = 'France' # noqa
