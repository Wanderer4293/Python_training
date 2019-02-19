# -*- coding: utf-8 -*-
def test_delete_group(app):
    app.session.login(user_name="admin", password="secret")
    app.entry.delete_first_entry()
    app.session.logout()
