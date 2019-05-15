# -*- coding: utf-8 -*-
from model.entry import Entry


def test_add_entry(app):
    app.session.login(user_name="admin", password="secret")
    app.entry.create(Entry(firstname="Test",
                           nickname="NS",
                           middlename="FOS",
                           email="test.fos@mail.mu"))
    app.session.logout()

