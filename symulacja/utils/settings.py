class Settings :
    def __init__(self, filename):
        self.width = None
        self.height = None
        self.type = 'square'
        self._read_file(filename)

    def _read_file(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                key, value = line.strip().split(':')
                key = key.strip().lower()
                value = value.strip().lower()

                if key == 'width':
                    self.width = int(value)
                elif key in 'height':  # typo handling
                    self.height = int(value)
                elif key == 'map':
                    if value in ['square', 'hex']:
                        self.map_type = value
                    else:
                        raise ValueError(f"Invalid map type: {value}")

    def set_map_sqr(self):
        self.type = 'square'

    def set_map_hex(self):
        self.type= 'hex'