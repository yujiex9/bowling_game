class Game:
    def __init__(self) -> None:
        self._throws = []
        self._current_frame = 0
        self._is_first_throw_in_frame = True

    def add(self, pins: int):
        if self._is_first_throw_in_frame:
            self._current_frame = min(10, self._current_frame + 1)
            if pins != 10:
                self._is_first_throw_in_frame = False
        else:
            self._is_first_throw_in_frame = True
        self._throws.append(pins)

    def score_for_frame(self, frame: int) -> int:
        if len(self._throws) < 2:
            return sum(self._throws)
        score = 0
        _throw = 0
        for _ in range(frame):
            first_throw_in_frame = self._throws[_throw]
            if first_throw_in_frame == 10:
                score += 10 + self._throws[_throw + 1] + self._throws[_throw + 2]
                _throw += 1
            else:
                second_throw_in_frame = self._throws[_throw + 1]
                if first_throw_in_frame + second_throw_in_frame == 10:
                    score += 10 + self._throws[_throw + 2]
                else:
                    score += self._throws[_throw] + self._throws[_throw + 1]
                _throw += 2
        return score

    @property
    def current_frame(self) -> int:
        return self._current_frame

    @property
    def score(self) -> int:
        return self.score_for_frame(self.current_frame)
