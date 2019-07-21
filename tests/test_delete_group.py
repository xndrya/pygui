def test_delete_group(app):
    if len(app.groups.get_group_list()) == 0:
        app.groups.add_new_group("Test")
    old_list = app.groups.get_group_list()
    app.groups.delete_first_group()
    new_list = app.groups.get_group_list()
    assert len(old_list)-1 == len(new_list)