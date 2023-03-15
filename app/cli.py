import sys

import click
from addon_cmds import commands as addon
from operator_cmds import commands as operator


@click.group()
def entry_point():
    # Entrypoint for all click groups (Addons and Operators)
    pass


if __name__ == "__main__":
    entry_point.add_command(addon.addon)
    entry_point.add_command(operator.operator)
    click.echo(f"Click Version: {click.__version__}")
    click.echo(f"Python Version: {sys.version}")
    _commands = {
        "addon": {
            "install": addon.install,
            "uninstall": addon.uninstall,
        },
        "operator": {
            "install": operator.install,
            "uninstall": operator.uninstall,
        },
    }
    _type = sys.argv[1]
    _type_commands = _commands.get(_type)
    if not _type_commands:
        click.echo(f"Available commands are: {'/'.join(_commands.keys())}\n")
        raise click.Abort()

    user_help_command = [ar.strip() for ar in sys.argv[-2:]]
    sub_command = _type_commands.get(user_help_command[0])
    if user_help_command[-1] == "--help" and sub_command:
        with click.Context(sub_command) as ctx:
            click.echo(sub_command.get_help(ctx))

    else:
        entry_point(obj={})
