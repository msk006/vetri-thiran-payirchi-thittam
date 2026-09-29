from utils import clean_json_block, parse_json


def test_clean_json_block():
    assert clean_json_block('```json\n{"a": 1}\n```') == '{"a": 1}'


def test_parse_json():
    assert parse_json('prefix [1, 2, 3] suffix') == [1, 2, 3]
