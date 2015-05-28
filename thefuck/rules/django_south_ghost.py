def match(command, settings):
    return 'manage.py' in command.script and \
           'migrate' in command.script \
           and 'or pass --delete-ghost-migrations' in command.stderr


def get_new_command(command, settings):
    return u'{} --delete-ghost-migrations'.format(command.script)