# navAirport.py
class NavAirport:
    def __init__(self, name_airport, sid_str, star_str): # Renamed for clarity in this example
        self.Name_airport = name_airport
        self.SID = sid_str.split()  # Store as a list of strings
        self.STAR = star_str.split() # Store as a list of strings
        self.associated_navpoint_number = None # To store the number of its first SID
        self.associated_navpoint_name = None # To store the name of its first SID


