import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import threading
import unittest
from http.server import HTTPServer
from urllib.error import HTTPError
from urllib.request import urlopen

from app import FrontendHandler


class FrontendTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = HTTPServer(("127.0.0.1", 0), FrontendHandler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base_url = f"http://127.0.0.1:{cls.server.server_port}"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def test_health(self):
        with urlopen(f"{self.base_url}/health") as response:
            self.assertEqual(response.status, 200)
            self.assertEqual(response.read(), b"OK")

    def test_info(self):
        with urlopen(f"{self.base_url}/info") as response:
            self.assertEqual(response.status, 200)
            self.assertEqual(
                json.loads(response.read()),
                {"service": "frontend", "version": "1.0.0"},
            )

    def test_unknown_path(self):
        with self.assertRaises(HTTPError) as error:
            urlopen(f"{self.base_url}/unknown")
        error.exception.close()
        self.assertEqual(error.exception.code, 404)


if __name__ == "__main__":
    unittest.main()


