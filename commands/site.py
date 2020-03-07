import click
import os

config_path = "/etc/nginx/sites-available"
enabled_path = "/etc/nginx/sites-enabled"


@click.group()
def execute():
    pass


@execute.command("+")
@click.argument("name", required=True)
def enconf(name):
    file_path = os.path.join(config_path, name)
    dist_path = os.path.join(enabled_path, name)
    if not os.path.exists(file_path):
        return click.echo("-> Config File NotFound")
    if os.path.exists(dist_path):
        return click.echo("-> Config Already Enabled")
    os.link(file_path, dist_path)
    return click.echo(f"-> Config {name} Has Been Enabled")


@execute.command("-")
@click.argument("name", required=True)
def disconf(name):
    file_path = os.path.join(enabled_path, name)
    if not os.path.exists(file_path):
        return click.echo("-> Config Already Disabled Or Not Found")
    os.unlink(file_path)
    return click.echo(f"-> Config {name} Has Been Disabled")
