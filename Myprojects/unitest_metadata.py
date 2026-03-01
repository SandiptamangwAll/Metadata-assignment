import unittest
from metadata import MetadataTag

class TestMetadata(unittest.TestCase):
    def test_sensitive_tag(self):
        tag = MetadataTag("gps_latitude", "27.7", "GPSInfo")
        self.assertTrue(tag.is_sensitive())

if __name__ == "__main__":
    unittest.main()