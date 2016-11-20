from subprocess import Popen, PIPE


class JarWrapper:
    """Wraps a call to a .jar file"""

    def __init__(self, jar_filepath):
        self.jar_filepath = jar_filepath

    def execute(self, *args):
        process = Popen(['java', '-jar', self.jar_filepath] + list(args), stdout=PIPE, stderr=PIPE)

        ret = []
        while process.poll() is None:
            line = process.stdout.readline()
            if line != '' and line.endswith(b'\n'):
                ret.append(line[:-1])

        stdout, stderr = process.communicate()
        ret += stdout.split(b'\n')
        if stderr != '':
            ret += stderr.split(b'\n')
        ret.remove(b'')

        return ret
