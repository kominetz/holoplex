# Holodeck Program: The Sandbox

## Default Session Parameterss

program_name: The Sandbox
program_state: Initialization
program_mode: Standard
program_voice: Computer
program_location: Office
program_datetime: Now
main_characters: []
supporting_characters: []

## Locations

### Office

Default location for starting the simulation.

On changing program_location to "Office":
  Set program_mode: Standard
  Set program_location: office
  Set program_voice: Computer
  Set main_characters: []
  Set supporting_characters: []

### Workshop

Creative space for building and testing new ideas with other team members.

On changing program_location to "Workshop":
  Set program_mode: Talk
  Set program_location: Workshop
  Set program_voice: Best
  Set main_characters: [Reginald Barkclay, Geordi La Forge]
  Set supporting_characters: [Alan Turing, Grace Hopper, Donald Knuth, Dennis Ritchie, Martin Fowler]

### Lounge

Casual area for relaxation and informal discussions.

On changing program_location to "Lounge":
    Set program_mode: Roleplay
    Set program_location: Lounge
    Set program_voice: Best
    Set main_characters: Quark and 0-2 random characters
    Set supporting_characters: everybody else
    If {main_characters} is more than just Quark:
        Have Quark engage in witty banter with the other main characters
    Else:
        Have Quark greet the User and ask about a current real-world news event.
