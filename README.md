# Steam Hook

> Announce your Steam achievements to a Slack channel

## Development instructions

We use Python and `uv` because we're cool like that. Make sure you have those things installed, and then

```bash
uv sync # Create the venv, be sure to update the interpreter path in VSCode
uv run main.py
```

## Roadmap

### v1

- [ ] Achievement tracking
- [ ] Slack integration (webhooks)
- [ ] Some way to configure it (web UI probably)

### Later (perhaps)

- [ ] Configuration from within Slack (Slack app)
- [ ] Discord support
- [ ] Playtime tracking
  - "MMK21 has been playing Terraria for 1 hour!" kind of thing?

## Acknowledgements

- Uses the [Steam Web API](https://developer.valvesoftware.com/wiki/Steam_Web_API) and its [official Python library](https://steam.readthedocs.io/en/latest/user_guide.html#webapi)
- Thank you to babelshift for making the [better Steam Web API documentation](https://steamwebapi.azurewebsites.net/)
