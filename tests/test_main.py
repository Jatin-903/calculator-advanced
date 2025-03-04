# tests/test_main.py

from plugins.menu import show_menu
import pytest

# Add your test functions here
def test_show_menu():
    result = show_menu()
    assert result is not None  # Adjust this test based on the actual return of show_menu
