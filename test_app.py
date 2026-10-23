def test_message():
    message = "Hello from Jenkins CI Pipeline!"
    assert message == "Hello from Jenkins CI Pipeline!"
    print("Test passed!")


if __name__ == "__main__":
    test_message()