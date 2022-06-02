# Exercise 1

Crate a `Track` class which will model a _"musical track"_ object (song):

* The class will need to have at least 4 attributes:
  * 1st one should be the `name` of the track
  * 2nd one should be the `starred` attribute, which will be a `bool` (i.e., the track can be marked as favorite or not)
  * 3rd attribute will be the track length. This could be either an `int`, `float` or even a `time` object
  * 4th attribute is optional
  * It should also have at least 2 functions apart of the common setters/getters functions of the attributes (the behavior is optional for each function)

Create a `MusicPlayer` class (it could also be called `MusicApp` or any related synonym). The goal of this class is to model a real-life _"CD"_ object, and must have at least **3** attributes, 1 of them must be some data structure that handles the storage for `1 or more` tracks. The functions that this class will have are described below:

* A function that let us add `tracks` objects to a class instance
* Another function that can return all of the `starred tracks` within the music player/app instance
* Finally, the last function which will return all of the `track` instances sorted by its length in ascendant mode
