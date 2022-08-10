import os
import click

plugin_folder = os.path.join(os.path.dirname(__file__), 'commands')


class App(click.MultiCommand):

    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(plugin_folder):
            if filename.startswith("_"):
                continue
            if filename.endswith('.py'):
                rv.append(filename[:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        ns = {}
        fn = os.path.join(plugin_folder, name + '.py')
        try:
            with open(fn) as f:
                code = compile(f.read(), fn, 'exec')
                eval(code, ns, ns)
            return ns['execute']
        except Exception as e:
            return


def run():
    cli = App(help='A tool for config and handle nginx')
    cli()
