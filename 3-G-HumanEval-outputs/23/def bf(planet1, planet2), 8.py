
def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    
    if planet1 not in planets or planet2 not in planets:
        return ()
    
    start_idx = planets.index(planet1)
    end_idx = planets.index(planet2)
    
    if start_idx < end_idx:
        return tuple(sorted(planets[start_idx+1:end_idx], key=lambda x: planets.index(x)))
    else:
        return tuple(sorted(planets[end_idx+1:start_idx], key=lambda x: planets.index(x)))

# Test cases
print(bf("Jupiter", "Neptune"))  # Output: ('Saturn', 'Uranus')
print(bf("Earth", "Mercury"))     # Output: ('Venus')
print(bf("Mercury", "Uranus"))    # Output: ('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn')
