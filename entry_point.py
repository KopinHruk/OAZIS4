import typer

from synthesize import fast_run


def main(
    mode: str = typer.Option(
        ...,
        help='Chose either `recognition` or `generation`.'
    ),
    text_input: str = typer.Option(
        None,
        help='Write text for speech synthesis'
    ),
):

    if mode.lower() == 'recognition':
        print(mode, text_input)
    elif mode.lower() == 'generation':
        if text_input is None:
            typer.echo("Error: Missing option '--text_input'", err=True)

        fast_run(text_input)

    else:
        return

if __name__ == '__main__':
    typer.run(main)