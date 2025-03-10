import pytest
from models import Role, Audition

def test_role_creation():
    role = Role(character_name="Lead Role")
    assert role.character_name == "Lead Role"

def test_audition_creation():
    audition = Audition(actor="John Doe", location="Theater A", phone=1234567890, hired=False)
    assert audition.actor == "John Doe"
    assert audition.location == "Theater A"
    assert audition.phone == 1234567890
    assert audition.hired is False

def test_role_auditions():
    role = Role(character_name="Supporting Role")
    audition1 = Audition(actor="Jane Doe", location="Theater B", phone=9876543210)
    audition2 = Audition(actor="Jim Beam", location="Theater C", phone=1231231234)
    role.auditions.append(audition1)
    role.auditions.append(audition2)
    
    assert len(role.auditions) == 2
    assert role.actors() == ["Jane Doe", "Jim Beam"]
    assert role.locations() == ["Theater B", "Theater C"]

def test_role_lead():
    role = Role(character_name="Lead Role")
    audition1 = Audition(actor="John Doe", location="Theater A", phone=1234567890, hired=True)
    audition2 = Audition(actor="Jane Doe", location="Theater B", phone=9876543210, hired=False)
    role.auditions.append(audition1)
    role.auditions.append(audition2)
    
    assert role.lead() == audition1
    assert role.understudy() == 'no actor has been hired for understudy for this role'

def test_audition_callback():
    audition = Audition(actor="John Doe", location="Theater A", phone=1234567890)
    audition.call_back()
    assert audition.hired is True
