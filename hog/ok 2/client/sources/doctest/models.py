from client import exceptions as ex
from client.sources.common import core
from client.sources.common import models
from client.sources.common import doctest_case
from client.sources.common import importing
from client.utils import format
from client.utils import output
import re
import textwrap

##########
# Models #
##########

class Doctest(models.Test):
    docstring = core.String()

    PS1 = '>>> '
    PS2 = '... '

    SETUP = PS1 + 'from {} import *'
    prompt_re = re.compile(r'(\s*)({}|{})'.format(PS1, '\.\.\. '))

    def __init__(self, file, verbose, interactive, timeout=None, **fields):
        super().__init__(**fields)
        self.file = file
        self.verbose = verbose
        self.interactive = interactive
        self.timeout = timeout

        self.console = doctest_case.PythonConsole(self.verbose, self.interactive,
                                                  self.timeout)

    def post_instantiation(self):
        # TODO(albert): rewrite test validation. Inconsistent leading space is
        # currently not validated correctly (see tests).
        self.docstring = textwrap.dedent(self.docstring)
        code = []
        prompt_on = False
        leading_space = ''
        for line in self.docstring.split('\n'):
            prompt_match = self.prompt_re.match(line)
            if prompt_match:
                if prompt_on and not line.startswith(leading_space):
                    raise ex.SerializeException('Inconsistent tabs for doctest')
                elif not prompt_on:
                    prompt_on = True
                    leading_space = prompt_match.group(1)
                code.append(line.lstrip())
            elif not line.strip():
                prompt_on = False
                leading_space = ''
            elif prompt_on:
                if not line.startswith(leading_space):
                    raise ex.SerializeException('Inconsistent tabs for doctest')
                code.append(line.lstrip())
        module = self.SETUP.format(importing.path_to_module_string(self.file))
        self.case = doctest_case.DoctestCase(self.console, module,
                                             code='\n'.join(code))

    def run(self):
        """Runs the suites associated with this doctest.

        RETURNS:
        bool; True if the doctest completely passes, False otherwise.
        """
        output.off()
        log_id = output.new_log()

        format.print_line('-')
        print('Doctests for {}'.format(self.name))
        print()

        success = self.case.run()
        if success:
            print('-- OK! --')

        output.on()
        output_log = output.get_log(log_id)
        output.remove_log(log_id)

        if not success or self.verbose:
            print(''.join(output_log))

        if not success and self.interactive:
            self.console.interact()

        if success:
            return {'passed': 1, 'failed': 0, 'locked': 0}
        else:
            return {'passed': 0, 'failed': 1, 'locked': 0}

    def score(self):
        format.print_line('-')
        print('Doctests for {}'.format(self.name))
        print()
        success = self.case.run()
        score = 1.0 if success else 0.0

        print('Score: {}/1'.format(score))
        print()
        return score

    def unlock(self, interact):
        """Doctests cannot be unlocked."""

    def lock(self, hash_fn):
        """Doctests cannot be locked."""

    def dump(self, file):
        """Doctests do not need to be dumped, since no state changes."""
