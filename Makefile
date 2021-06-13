EXT_NAME:=ulauncher-variety
EXT_DIR:=$(shell pwd)

attach:
	@ln -s ${EXT_DIR} ~/.local/share/ulauncher/extensions/${EXT_NAME}

detach:
	@rm -r ~/.local/share/ulauncher/extensions/${EXT_NAME}
