import unittest
import sqlite3
import os

class TestDatabaseConnection(unittest.TestCase):

    def setUp(self):
        # Path to the database file
        self.db_path = 'FireGuard_DB.sql'

    def test_db_connection(self):
        """Test if we can establish a connection to the database."""
        try:
            conn = sqlite3.connect(self.db_path)
            conn.close()
            connected = True
        except sqlite3.Error as e:
            connected = False
        self.assertTrue(connected, f"Failed to connect to the database: {self.db_path}")

if __name__ == '__main__':
    unittest.main()
