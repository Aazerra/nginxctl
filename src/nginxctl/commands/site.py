import click
import os

config_path = os.getenv("NGINX_CONFIG_PATH") or "/etc/nginx/sites-available"
enabled_path = os.getenv("NGINX_ENABLED_PATH") or "/etc/nginx/sites-enabled"


@click.group()
def execute():
    pass


@execute.command("+")
@click.argument("name", required=True)
def enconf(name):
    file_path = os.path.join(config_path, name)
    dist_path = os.path.join(enabled_path, name)

    if not os.path.exists(file_path):
        return click.echo(f"[#] {name} file notfound")
    if os.path.exists(dist_path):
        return click.echo(f"[x] {name} already enabled")
    os.link(file_path, dist_path)
    return click.echo(f"[.] {name} has been enabled")


@execute.command("-")
@click.argument("name", required=True)
def disconf(name):
    file_path = os.path.join(enabled_path, name)
    if not os.path.exists(file_path):
        return click.echo(f"[#] {name} is already disabled or notfound")
    os.unlink(file_path)
    return click.echo(f"[.] {name} has been disabled")
