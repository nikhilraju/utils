from typing import NewType

Country = NewType('Country', str)

c1: Country = Country('United States')
c2: Country = 'New York'
c3: str = Country('United States')










