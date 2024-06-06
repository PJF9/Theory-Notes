"""
In software `enterprises` each class, function and method has to be `documentated`
precisely, meaning that we have written some `comments` that `highlights` the behaviour
that we have achived.

Next, after we've written the documentation, we `pass` the program through some `modules`
that generates `automaticly` in nice formats the documentation, of each compenent of the
program.

We documentate our programusing the """ """ (docstrings) and we place them in `specific`
places:
1) After the name of the class to give info about the class members (attributes).
2) After the name of a function or a method to give info about about  the arguments,
    condition, raises and the returned value.
"""


# An example that demonstrates documentation:
class Animal:
    """
    A class used to represent an Animal

    ...

    Attributes
    ----------
    name: str
        The name of the animal
    sound: str
        The sound that the animal is making
    mun_legs: int
        The number of the legs that the animal is having ( default 4 )

    Methods
    -------
    says(sound=None):
        Prints the animals name and the sound that is making
    """
    
    def __init__(self, name, sound, num_legs=4):
        """
        Parameters
        ----------
        name: str
            The name of the animal
        sound: str
            The sound that the animal is making
        num_legs: int, optional
            The number of legs that the animal is having
        """

        self.name = name
        self.sound = sound
        self.num_legs = num_legs

    def says(self, sound=None):
        """
        Print the animals name and what sound is making

        ...


        Parameters
        ----------
        sound: str, optional
            The sound that the animal makes


        Raises
        ------
        NotImplementedError
            If not sound is passed as an argument or set at the initialisation
        """

        if (self.sound is None) and (sound is None):
            raise NotImplementedError("Silent animals are not supported!")

        outputed_sound = self.sound if sound is None else sound
        
        print(f"{self.name} says {outputed_sound}")
