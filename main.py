from cli_fragments import CliFragments


def validator_function(value: str):
    if value == "wrong":
        raise ValueError("The value is wrong.")


io = CliFragments()

io.debug("This is a debug message.")
io.notice("This is a notice message.")
io.warning("This is a warning message.")
io.error("This is an error message.")
io.success("This is a success message.")
io.text("This is padded raw text message.")

io.ask("This is a user question", None, None)

io.ask("This is a validated user question", "default", validator_function)
