import pytest
from test_ohce_builder import OHCEBuilder
from src.langues import FR

@pytest.mark.parametrize("période, salutation", [
    ("matin", "bonjour_am"),
    ("après-midi", "bonjour_pm"),
    ("soirée", "bonjour_soir"),
    ("nuit", "bonjour_nuit"),
])
def test_salutation_selon_période(période, salutation):
    ohce = OHCEBuilder().parlant(FR).à_la_période(période).build()
    result = ohce.Palindrome("test")
    assert result.startswith(salutation)


@pytest.mark.parametrize("période, au_revoir", [
    ("matin", "auRevoir_am"),
    ("après-midi", "auRevoir_pm"),
    ("soirée", "auRevoir_soir"),
    ("nuit", "auRevoir_nuit"),
])
def test_adieu_selon_période(période, au_revoir):
    ohce = OHCEBuilder().parlant(FR).à_la_période(période).build()
    result = ohce.Palindrome("test")
    assert result.endswith(au_revoir)
