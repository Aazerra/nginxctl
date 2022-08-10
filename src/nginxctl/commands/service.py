import click
import os


@click.group()
def execute():
    pass


@execute.command("restart")
def restart():
    os.system("systemctl restart nginx")
    click.echo("Restarting...")


@execute.command("stop")
def stop():
    os.system("systemctl stop nginx")
    click.echo("Stoping...")


@execute.command("start")
def start():
    os.system("systemctl start nginx")
    click.echo("Starting...")


@execute.command("enable")
def enable():
    os.system("systemctl enable nginx")
    click.echo("Enabling...")


@execute.command("disable")
def disable():
    os.system("systemctl disable nginx")
    click.echo("Disabling...")
