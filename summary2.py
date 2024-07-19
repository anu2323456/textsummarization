import click
import ollama

@click.command()
@click.option('--file', type=click.Path(exists=True), help='Path to the text file to summarize.')
@click.option('--text', type=str, help='Text to summarize.')
def main(file, text):
    if not file and not text:
        click.echo("You must provide either a text file or text input.")
        return
    
    if file:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                text = f.read()
        except Exception as e:
            click.echo(f"Error reading file '{file}': {e}")
            return
    
    try:
        response = ollama.generate(model='qwen2', prompt=text)
        summary = response['response']
        click.echo("Summary:")
        click.echo(summary)
    except Exception as e:
        click.echo(f"Error with Ollama: {e}")

if __name__ == "__main__":
    main()
