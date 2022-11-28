AirBnB clone - The console
Group project

This is the first step towards building your first full web application: the AirBnB clone. 
This is first step and is to be used during building following projects
All other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help yo to:

put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
create the first abstracted storage engine of the project: File storage.
create all unittests to validate all our classes and storage engine

Execution

All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash
