__author__ = 'wdolowicz'

from model.group import Group


def test_add_group(app):
    old_list = app.group.get_group_list(app.main_window)
    group = Group(name='test')
    app.group.add_new_group(app.main_window, group)
    new_list = app.group.get_group_list(app.main_window)
    old_list.append(group.name)
    assert sorted(old_list) == sorted(new_list)
