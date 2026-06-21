import pytest
from logic_utils import check_guess, parse_guess, get_range_for_difficulty, update_score


# ---------------------------------------------------------------------------
# check_guess
# ---------------------------------------------------------------------------

class TestCheckGuess:
    def test_exact_match_is_win(self):
        outcome, _ = check_guess(50, 50)
        assert outcome == "Win"

    def test_win_message(self):
        _, message = check_guess(50, 50)
        assert message == "🎉 Correct!"

    def test_guess_too_high_outcome(self):
        outcome, _ = check_guess(60, 50)
        assert outcome == "Too High"

    def test_guess_too_high_hint_says_lower(self):
        _, message = check_guess(60, 50)
        assert "LOWER" in message

    def test_guess_too_low_outcome(self):
        outcome, _ = check_guess(40, 50)
        assert outcome == "Too Low"

    def test_guess_too_low_hint_says_higher(self):
        _, message = check_guess(40, 50)
        assert "HIGHER" in message

    def test_boundary_low_exact(self):
        outcome, _ = check_guess(1, 1)
        assert outcome == "Win"

    def test_boundary_high_exact(self):
        outcome, _ = check_guess(100, 100)
        assert outcome == "Win"

    def test_one_below_secret(self):
        outcome, _ = check_guess(49, 50)
        assert outcome == "Too Low"

    def test_one_above_secret(self):
        outcome, _ = check_guess(51, 50)
        assert outcome == "Too High"


# ---------------------------------------------------------------------------
# parse_guess
# ---------------------------------------------------------------------------

class TestParseGuess:
    def test_valid_integer(self):
        ok, value, err = parse_guess("42")
        assert ok is True
        assert value == 42
        assert err is None

    def test_valid_float_truncated(self):
        ok, value, err = parse_guess("7.9")
        assert ok is True
        assert value == 7
        assert err is None

    def test_empty_string(self):
        ok, value, err = parse_guess("")
        assert ok is False
        assert value is None
        assert err is not None

    def test_none_input(self):
        ok, value, err = parse_guess(None)
        assert ok is False
        assert value is None
        assert err is not None

    def test_non_numeric_string(self):
        ok, value, err = parse_guess("abc")
        assert ok is False
        assert value is None
        assert err is not None

    def test_negative_number_parses(self):
        ok, value, err = parse_guess("-5")
        assert ok is True
        assert value == -5

    def test_whitespace_only(self):
        ok, value, err = parse_guess("   ")
        assert ok is False

    def test_number_with_spaces(self):
        # "50 " or " 50" — int() strips whitespace, so this should parse
        ok, value, err = parse_guess(" 50 ")
        assert ok is True
        assert value == 50

    def test_zero(self):
        ok, value, err = parse_guess("0")
        assert ok is True
        assert value == 0


# ---------------------------------------------------------------------------
# get_range_for_difficulty
# ---------------------------------------------------------------------------

class TestGetRangeForDifficulty:
    def test_easy(self):
        assert get_range_for_difficulty("Easy") == (1, 20)

    def test_normal(self):
        assert get_range_for_difficulty("Normal") == (1, 100)

    def test_hard(self):
        assert get_range_for_difficulty("Hard") == (1, 50)

    def test_unknown_defaults_to_normal(self):
        low, high = get_range_for_difficulty("Unknown")
        assert low == 1
        assert high == 100


# ---------------------------------------------------------------------------
# update_score
# ---------------------------------------------------------------------------

class TestUpdateScore:
    def test_win_on_first_attempt(self):
        # attempt_number=1: 100 - 10*1 = 90
        score = update_score(0, "Win", 1)
        assert score == 90

    def test_win_on_second_attempt(self):
        score = update_score(0, "Win", 2)
        assert score == 80

    def test_win_score_floor_is_10(self):
        # attempt_number=10: 100 - 100 = 0, floored to 10
        score = update_score(0, "Win", 10)
        assert score == 10

    def test_win_score_floor_enforced_beyond_10(self):
        score = update_score(0, "Win", 15)
        assert score == 10

    def test_win_adds_to_existing_score(self):
        score = update_score(50, "Win", 1)
        assert score == 140

    def test_too_low_subtracts_5(self):
        score = update_score(100, "Too Low", 1)
        assert score == 95

    def test_too_low_always_subtracts_regardless_of_attempt(self):
        assert update_score(100, "Too Low", 2) == 95
        assert update_score(100, "Too Low", 3) == 95

    def test_too_high_even_attempt_adds_5(self):
        score = update_score(100, "Too High", 2)
        assert score == 105

    def test_too_high_odd_attempt_subtracts_5(self):
        score = update_score(100, "Too High", 1)
        assert score == 95

    def test_unknown_outcome_no_change(self):
        score = update_score(100, "SomeOtherOutcome", 1)
        assert score == 100

    def test_score_can_go_negative(self):
        score = update_score(3, "Too Low", 1)
        assert score == -2
