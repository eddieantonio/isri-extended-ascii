extended_ascii.1: README.md
	pandoc -s -t man $< -o $@
