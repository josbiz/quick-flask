from click import command, option, argument

@command()
@option('--name', help='Name of the person to greet.', required=True, prompt="What is your name?")
@argument('number')
def cli(name, number):
    for _ in range(int(number)):
        print(f"Hello {name}!")