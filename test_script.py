import sys

def test_data_file():
    try:
        import common
        data = common.load_data()
        assert isinstance(data, dict)
        assert "students" in data
        print("✅ common.load_data() test passed")
    except Exception as e:
        print("❌ Test failed:", e)
        sys.exit(1)

if __name__ == "__main__":
    test_data_file()
