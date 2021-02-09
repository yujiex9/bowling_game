class Game:
    def __init__(self) -> None:
        self._scorer = Scorer()
        self._current_frame = 0
        self._is_first_throw_in_frame = True

    def add(self, pins: int):
        self._update_current_frame()
        self._reset_is_first_throw_flag(pins)
        self._scorer.add_pins(pins)

    def _update_current_frame(self) -> bool:
        def _advance_frame():
            self._current_frame = min(10, self._current_frame + 1)

        if self._is_first_throw_in_frame:
            _advance_frame()

    def _reset_is_first_throw_flag(self, pins: int):
        def _is_a_strike_frame() -> bool:
            return pins == 10

        if self._is_first_throw_in_frame:
            if not _is_a_strike_frame():
                self._is_first_throw_in_frame = False
        else:
            self._is_first_throw_in_frame = True

    def score_for_frame(self, frame: int) -> int:
        return self._scorer.score_for_frame(frame)

    @property
    def current_frame(self) -> int:
        return self._current_frame

    @property
    def score(self) -> int:
        return self._scorer.score_for_frame(self.current_frame)


class Scorer:
    def __init__(self) -> None:
        self._throws = []

        # internal state
        self.__throw = 0

    def add_pins(self, pins: int):
        self._throws.append(pins)

    def score_for_frame(self, frame: int) -> int:
        if len(self._throws) < 2:
            return sum(self._throws)
        score = 0
        self.__throw = 0
        for _ in range(frame):
            if self._is_strike():
                score += 10 + self._next_two_throws_for_strike()
                self.__throw  += 1
            elif self._is_spare():
                score += 10 + self._next_throw_for_spare()
                self.__throw += 2
            else:
                score += self._two_neighbouring_throws()
                self.__throw += 2
        return score

    def _is_strike(self) -> bool:
        return self._throws[self.__throw ] == 10

    def _next_two_throws_for_strike(self) -> int:
        return self._throws[self.__throw + 1] + self._throws[self.__throw + 2]

    def _is_spare(self) -> bool:
        return self._throws[self.__throw] + self._throws[self.__throw + 1] == 10

    def _next_throw_for_spare(self) -> int:
        return self._throws[self.__throw + 2]

    def _two_neighbouring_throws(self) -> int:
        return self._throws[self.__throw] + self._throws[self.__throw + 1]
