# -*- coding: utf-8 -*-
def test_delete_group(app):
    app.session.login(user_name="admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()
