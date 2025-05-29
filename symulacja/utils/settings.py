class Settings :
    def __init__(self, filename):
        self.label = None
        self.width = None
        self.height = None
        self.map_type = 'square'
        self.current_lvl = ''
        self._read_file(filename)

    def _read_file(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                key, value = line.strip().split(':')
                key = key.strip().lower()
                value = value.strip().lower()

                if key == 'width':
                    self.width = int(value)
                elif key in 'height':
                    self.height = int(value)
                elif key == 'map':
                    if value in ['square', 'hex']:
                        self.map_type = value
                    else:
                        raise ValueError(f"Invalid map type: {value}")

    def set_map_sqr(self):
        self.map_type = 'square'
        self.update_label()

    def set_map_hex(self):
        self.map_type= 'hex'
        self.update_label()

    def update_label(self):
        if self.label:
            self.label.config(text=f"Selected map type: {self.map_type}")

    def bind_label(self, label_widget):
        self.label = label_widget

    def set_lvl(self,name):
        self.current_lvl = f"files/lvl/{name}.txt"