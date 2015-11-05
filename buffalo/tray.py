from buffalo import utils

class Tray(object):

    FEATHER = 10
    # FEATHER is the number of pixels away from the edges of a tray
    # that the "resize region" goes

    DEFAULT_MIN_WIDTH = 150
    DEFAULT_MAX_WIDTH = 1000
    DEFAULT_MIN_HEIGHT = 150
    DEFAULT_MAX_HEIGHT = 1000
    DEFAULT_COLOR = (0, 0, 100, 150)

    def __init__(self, pos, size,
                 min_width=None, max_width=None,
                 min_height=None, max_height=None,
                 color=None):
        self.pos = pos
        self.size = size
        self.min_width = min_width if min_width is not None else Tray.DEFAULT_MIN_WIDTH
        self.max_width = max_width if max_width is not None else Tray.DEFAULT_MAX_WIDTH
        self.min_height = min_height if min_height is not None else Tray.DEFAULT_MIN_HEIGHT
        self.max_height = max_height if max_height is not None else Tray.DEFAULT_MAX_HEIGHT
        self.color = color if color is not None else Tray.DEFAULT_COLOR
        self.elems = set()
        self.should_resize = False
        self.edge = 0b0000
        self.render()

    def render(self):
        self.surface = utils.empty_surface(self.size)
        self.surface.fill(self.color)
        for elem in self.elems:
            elem.blit(self.surface)
        
    def update(self):
        rerender = False
        for elem in self.elems:
            if elem.update():
                rerender = True

    def move(self, diff):
        self.pos = self.pos[0] + diff[0], self.pos[1] + diff[1]

    def resize(self, mouse_pos):
        x, y = mouse_pos
        original_pos = self.pos
        original_size = self.size
        if self.edge & 0b0001: # left
            r = self.x + self.width
            self.pos = x, self.y
            self.size = self.width + (r - (self.x + self.width)), self.height
        if self.edge & 0b0010: # top
            b = self.y + self.height
            self.pos = self.x, y
            self.size = self.width, self.height + (b - (self.y + self.height))
        if self.edge & 0b0100: # right
            self.size = self.width + (x - (self.x + self.width)), self.height
        if self.edge & 0b1000: # bottom
            self.size = self.width, self.height + (y - (self.y + self.height))
        if self.size[0] < self.min_width or self.size[0] > self.max_width:
            self.size = original_size[0], self.size[1]
            self.pos = original_pos[0], self.pos[1]
        if self.size[1] < self.min_height or self.size[1] > self.max_height:
            self.size = self.size[0], original_size[1]
            self.pos = self.pos[0], original_pos[1]
        self.render()

    def handle(self, mouse_pos, mouse_rel):
        self.update() # see if anything must be rerendered
        assert(type(mouse_pos) == tuple and len(mouse_pos) == 2)
        assert(type(mouse_pos[0]) == int and type(mouse_pos[1]) == int)
        x, y = mouse_pos
        # Edges:
        # Left:   0b0001
        # Top:    0b0010
        # Right:  0b0100
        # Bottom: 0b1000
        within_x = x >= self.x and x <= self.x + self.width
        within_y = y >= self.y and y <= self.y + self.height
        if within_x:
            if abs(y - (self.y + self.height)) <= Tray.FEATHER:
                self.should_resize = True
                self.edge |= 0b1000
            if abs(y - self.y) <= Tray.FEATHER:
                self.should_resize = True
                self.edge |= 0b0010
        if within_y:
            if abs(x - self.x) <= Tray.FEATHER:
                self.should_resize = True
                self.edge |= 0b0001
            if abs(x - (self.x + self.width)) <= Tray.FEATHER:
                self.should_resize = True
                self.edge |= 0b0100
        if x > self.x + Tray.FEATHER * 5 and x < self.x + self.width - Tray.FEATHER * 5:
            if y > self.y + Tray.FEATHER * 5 and y < self.y + self.height - Tray.FEATHER * 5:
                self.should_move = True
                for elem in self.elems:
                    if elem.get_rect().collidepoint(mouse_pos):
                        self.should_move = False
                        break
        if self.should_move:
            self.move(mouse_rel)
        if self.should_resize:
            self.resize(mouse_pos)

    def blit(self, dest):
        dest.blit(self.surface, self.pos)

    @property
    def pos(self):
        return (self.x, self.y)

    @property
    def size(self):
        return (self.width, self.height)

    @property
    def color(self):
        return (self.r, self.g, self.b, self.a)

    @pos.setter
    def pos(self, value):
        assert(type(value) == tuple and len(value) == 2)
        assert(type(value[0]) == int)
        assert(type(value[1]) == int)
        self.x, self.y = value

    @size.setter
    def size(self, value):
        assert(type(value) == tuple and len(value) == 2)
        assert(type(value[0]) == int)
        assert(type(value[1]) == int)
        self.width, self.height = value

    @color.setter
    def color(self, value):
        assert(type(value) == tuple and len(value) == 4)
        assert(type(value[0]) == int and value[0] >= 0 and value[0] <= 255)
        assert(type(value[1]) == int and value[1] >= 0 and value[1] <= 255)
        assert(type(value[2]) == int and value[2] >= 0 and value[2] <= 255)
        assert(type(value[3]) == int and value[3] >= 0 and value[3] <= 255)
        self.r, self.g, self.b, self.a = value
