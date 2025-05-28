class Settings :
    def __init__(self, filename):
        self.width = None
        self.height = None
        self._read_file(filename)

    def _read_file(self,filename):
        with open(filename, 'r') as f:
            for line in f:
                key, value = line.strip().split(':')
                key = key.strip().lower()
                value = int(value.strip())

                if key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value


