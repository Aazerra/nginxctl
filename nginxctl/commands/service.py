import click
import os


@click.group()
def execute():
    pass


@execute.command("restart")
def create():
    os.system("systemctl restart nginx")
    click.echo("Restarting...")


@execute.command("stop")
def create():
    os.system("systemctl stop nginx")
    click.echo("Stoping...")


@execute.command("start")
def create():
    os.system("systemctl start nginx")
    click.echo("Starting...")


@execute.command("enable")
def create():
    os.system("systemctl enable nginx")
    click.echo("Enabling...")


@execute.command("disable")
def create():
    os.system("systemctl disable nginx")
    click.echo("Disabling...")
