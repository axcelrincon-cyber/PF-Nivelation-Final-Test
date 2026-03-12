from main import invasive_species

# Test 1
def test_trivia_fetch_returns_dict():
    result = invasive_species(1)
    assert isinstance(result, dict)


# Test 2
def test_trivia_fetch_has_required_fields():
    result = invasive_species(1)
    assert "id" in result
    assert "name" in result


# Test 3
def test_trivia_fetch_correct_id():
    result = invasive_species(5)
    assert result["id"] == 5

# Test 4
def test_trivia_fetch_name_not_empty():
    result = invasive_species(1)
    assert result["name"]
    assert isinstance(result["name"], str)

# Test 5
def test_trivia_fetch_accepts_numbers():
    result = invasive_species(15)
    assert result is not None