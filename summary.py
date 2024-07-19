import click
import requests

# Assuming Ollama is running on localhost and port 11434
OLLAMA_API_URL = "http://localhost:11434/v1/summarize"

def summarize_text(text):
    try:
        headers = {
            "Content-Type": "application/json"
        }
        payload = {
            "model": "qwen2",
            "text": text
        }
        response = requests.post(OLLAMA_API_URL, json=payload, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
        summary = response.json().get("summary", "")
        return summary
    except requests.exceptions.RequestException as e:
        return f"Error connecting to Ollama API: {e}"
    except Exception as e:
        return f"Error: {e}"

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
    
    summary = summarize_text(text)
    click.echo("Summary:")
    click.echo(summary)

if __name__ == "__main__":
    main()
