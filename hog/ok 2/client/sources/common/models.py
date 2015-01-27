"""Models for serialization of tests."""

from client.sources.common import core

class Test(core.Serializable):
    name = core.String()
    points = core.Float()
    partner = core.Int(optional=True)

    def run(self):
        """Subclasses should override this method to run tests."""
        raise NotImplementedError

    def score(self):
        """Subclasses should override this method to score the test."""
        raise NotImplementedError

    def unlock(self, interact):
        """Subclasses should override this method to lock the test."""
        raise NotImplementedError

    def lock(self, hash_fn):
        """Subclasses should override this method to lock the test."""
        raise NotImplementedError

    def dump(self, file):
        """Subclasses should override this method for serialization."""
        raise NotImplementedError

class Case(core.Serializable):
    """Abstract case class."""

    hidden = core.Boolean(default=False)
    locked = core.Boolean(optional=True)

    def run(self):
        """Subclasses should override this method for running a test case.

        RETURNS:
        bool; True if the test case passes, False otherwise.
        """
        raise NotImplementedError

    def lock(self, hash_fn):
        """Subclasses should override this method for locking a test case.

        This method should mutate the object into a locked state.

        PARAMETERS:
        hash_fn -- function; computes the hash code of a given string.
        """
        raise NotImplementedError

    def unlock(self, interact):
        """Subclasses should override this method for unlocking a test case.

        It is the responsibility of the the subclass to make any changes to the
        test case, including setting its locked field to False.

        PARAMETERS:
        interact -- function; handles user interaction during the unlocking
                    phase.
        """
        raise NotImplementedError

